# -*- encoding: utf-8 -*-
# Copyright (c) 2024 53572814+nukemiko@users.noreply.github.com
# environparse is licensed under Mulan PSL v2.
# You can use this software according to the terms and conditions of the Mulan PSL v2.
# You may obtain a copy of Mulan PSL v2 at:
#          http://license.coscl.org.cn/MulanPSL2
# THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
# EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
# MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
# See the Mulan PSL v2 for more details.

"""Environment variable parsing library.

As an argparse-inspired environment variable parsing library, this module can:

- Handles both optional and required environment variable.
- Automatically multi-language support.
    - Currently supported 5 languages: en, zh_CN, zh_SG, zh_HK, zh_TW.
- And more features that have not yet been implemented.

Signatures in this module that meet the following conditions are public:

- Listed in the constant `__all__`.
- Not start with underscore (`_`).

Signatures that do not satisfy the above conditions are considered implementation details.
"""
__version__ = '0.1.0'

import abc as _abc
import enum as _enum
import errno as _errno
import functools as _functools
import gettext as _gettext
import math as _math
import operator as _operator
import os as _os
import re as _re
import shlex as _shlex
import sys as _sys
import typing as _typing
import warnings as _warnings
from pathlib import Path as _Path
from pathlib import PosixPath as _PosixPath
from pathlib import WindowsPath as _WindowsPath

import attrs as _attrs
from rich import console as _console
from rich import table as _table

__all__ = (
    'EnvironmentVariableParseError',
    'RunActionError',
    'CreateActionError',
    'FileOpenActionError',
    'AbstractAction',
    'StringAction',
    'NumberAction',
    'BooleanAction',
    'PathAction',
    'FileOpenAction',
    'Action',
    'DefinedOptionType',
    'EnvironmentVariableParser'
)

_ = _gettext.translation(__name__, _Path(__file__).parent / 'locale', fallback=True).gettext
_c = _gettext.translation('libc', fallback=True).gettext

_T = _typing.TypeVar('_T')
_P = _typing.ParamSpec('_P')


class _Never(BaseException):
    """Play the same role as ``typing.assert_never()``."""


class EnvironmentVariableParseError(Exception):
    def __init__(self, message: str = '', exitcode: int = 1) -> None:
        self.message = message
        self.exitcode = exitcode
        super().__init__('[Exitcode {!r}] {!s}'.format(self.exitcode, self.message))


class RunActionError(EnvironmentVariableParseError):
    pass


class CreateActionError(EnvironmentVariableParseError):
    pass


class AbstractAction(metaclass=_abc.ABCMeta):
    __slots__ = ()

    @property
    def metavar(self) -> str:
        return _('VALUE')

    @property
    def early(self) -> bool:
        return False

    @_abc.abstractmethod
    def __call__(self, parser: 'EnvironmentVariableParser', option: '_DefinedOption', actual_name: str, value: str, /) -> _typing.Any:
        raise NotImplementedError


@_attrs.frozen(kw_only=True, slots=False)
class HelpAction(AbstractAction):
    @property
    def early(self) -> bool:
        return True

    def __call__(self, parser: 'EnvironmentVariableParser', option: '_DefinedOption', actual_name: str, value: str, /) -> _typing.NoReturn:
        parser.printHelp(show_default=True)
        raise EnvironmentVariableParseError(exitcode=0)


@_attrs.frozen(kw_only=True, slots=False)
class StringAction(AbstractAction):
    allow_empty: bool = _attrs.field(default=False, converter=bool)
    lstrip: bool = _attrs.field(default=False, converter=bool)
    rstrip: bool = _attrs.field(default=False, converter=bool)

    @property
    def metavar(self) -> str:
        return _('STRING')

    def __call__(self, parser: 'EnvironmentVariableParser', option: '_DefinedOption', actual_name: str, value: str, /) -> str:
        if not (value or self.allow_empty):
            raise RunActionError(_('The value of option {!s} cannot be empty').format(actual_name))

        if self.lstrip:
            value = value.lstrip()
        if self.rstrip:
            value = value.rstrip()

        return value


@_attrs.frozen(kw_only=True, slots=False)
class NumberAction(AbstractAction):
    base: int = _attrs.field(
        default=10,
        validator=_attrs.validators.and_(  # type:ignore
            _attrs.validators.instance_of(int),
            _attrs.validators.ge(2),
            _attrs.validators.le(36)
        )
    )
    is_float: bool = _attrs.field(default=False, converter=bool)
    finite_only: bool = _attrs.field(default=True, converter=bool)

    @property
    def metavar(self) -> str:
        if self.is_float:
            return _('FLOAT')
        return _('INTEGER')

    def __call__(self, parser: 'EnvironmentVariableParser', option: '_DefinedOption', actual_name: str, value: str, /) -> int | float:
        if self.is_float:
            try:
                result = float(value)
            except ValueError as exc:
                raise RunActionError(
                    _(
                        'The value of option {!s} ({!r}) cannot be interpreted as float'
                    ).format(actual_name, value)
                ) from exc
            else:
                if not _math.isfinite(result) and self.finite_only:
                    raise RunActionError(
                        _(
                            'The value of option {!s} cannot be float {!s}'
                        ).format(actual_name, 'infinity' if _math.isinf(result) else 'NaN (Not a Number)')
                    )
        else:
            try:
                result = int(value, base=self.base)
            except ValueError as exc:
                if str(exc).startswith('Exceeds the limit'):
                    # To recognize the ValueError caused by integer string conversion length limitation
                    raise RunActionError(
                        _('The value of option {!s} has exceeded the limit ({!r} digits) for integer string conversion').format(
                            actual_name, _sys.get_int_max_str_digits()
                        )
                    ) from exc
                if self.base != 10:
                    raise RunActionError(
                        _('The value of option {!s} ({!r}) cannot be interpreted as integer with base {!r}').format(
                            actual_name, value, self.base
                        )
                    ) from exc
                raise RunActionError(
                    _('The value of option {!s} ({!r}) cannot be interpreted as integer').format(
                        actual_name, value
                    )
                ) from exc

        return result


@_attrs.frozen(kw_only=True, slots=False)
class BooleanAction(AbstractAction):
    class UnrecognizedValueHandler(_enum.Enum):
        STRICT = _enum.auto()
        DEFAULT = _enum.auto()
        AS_TRUE = _enum.auto()
        AS_FALSE = _enum.auto()

    reversed: bool = _attrs.field(default=False, converter=bool)
    literal_true: tuple[str, ...] = _attrs.field(
        default=('true', 'yes', 'y', 'ok', 'on'),
        validator=_attrs.validators.deep_iterable(
            member_validator=_attrs.validators.instance_of(str),
            iterable_validator=_attrs.validators.and_(
                _attrs.validators.instance_of(tuple),
                _attrs.validators.min_len(1)
            )
        )
    )
    literal_false: tuple[str, ...] = _attrs.field(
        default=('false', 'no', 'n', 'off'),
        validator=_attrs.validators.deep_iterable(
            member_validator=_attrs.validators.instance_of(str),
            iterable_validator=_attrs.validators.and_(
                _attrs.validators.instance_of(tuple),
                _attrs.validators.min_len(1)
            )
        )
    )
    unrecognized: UnrecognizedValueHandler = _attrs.field(
        default=UnrecognizedValueHandler.STRICT,
        validator=_attrs.validators.instance_of(UnrecognizedValueHandler)  # type:ignore
    )

    @property
    def metavar(self) -> str:
        return _('BOOLEAN')

    def __call__(self, parser: 'EnvironmentVariableParser', option: '_DefinedOption', actual_name: str, value: str, /) -> bool:
        if self.reversed:
            beforeReturn = _operator.not_
        else:
            beforeReturn = bool
        try:
            integer = _typing.cast(int, NumberAction()(parser, option, actual_name, value))
        except RunActionError:
            value = value.lower()
            literal_true = [__.lower() for __ in self.literal_true]
            literal_false = [__.lower() for __ in self.literal_false]
            if value in literal_true:
                return beforeReturn(True)
            if value in literal_false:
                return beforeReturn(False)
            match self.unrecognized:
                case self.UnrecognizedValueHandler.STRICT:
                    raise RunActionError(_('The value of option {!s} ({!r}) cannot be converted to boolean')) from None
                case self.UnrecognizedValueHandler.DEFAULT:
                    return option.default
                case self.UnrecognizedValueHandler.AS_TRUE:
                    return beforeReturn(True)
                case self.UnrecognizedValueHandler.AS_FALSE:
                    return beforeReturn(False)
                case _:
                    raise _Never
        else:
            return beforeReturn(integer > 0)


@_attrs.frozen(kw_only=True, slots=False)
class PathAction(AbstractAction):
    path_cls: type[_Path] | type[_PosixPath] | type[_WindowsPath] = _attrs.field(
        default=_Path,
        validator=_attrs.validators.in_(
            (_Path, _PosixPath, _WindowsPath)
        )
    )
    resolve: bool = _attrs.field(default=False, converter=bool)

    @property
    def metavar(self) -> str:
        return 'PATH'

    def __call__(self, parser: 'EnvironmentVariableParser', option: '_DefinedOption', actual_name: str, value: str, /) -> _Path:
        p = self.path_cls(value)

        if self.resolve:
            try:
                p = p.resolve()
            except RuntimeError as exc:
                # An infinite loop is encountered along the resolution path
                raise RunActionError(
                    _('Failed to interpret the value of option {!s} ({!r}) as path: {!s}').format(
                        actual_name,
                        value,
                        OSError(_errno.ELOOP, _c(_os.strerror(_errno.ELOOP)), value)
                    )
                ) from exc

        return p


class FileOpenActionError(CreateActionError):
    pass


@_attrs.frozen(kw_only=True, slots=False)
class FileOpenAction(AbstractAction):
    mode: str = _attrs.field(default='r', validator=_attrs.validators.instance_of(str))  # type:ignore
    buffering: int = _attrs.field(default=-1, validator=_attrs.validators.instance_of(int))  # type:ignore
    encoding: str | None = _attrs.field(
        default=None,
        validator=_attrs.validators.optional(  # type:ignore
            _attrs.validators.instance_of(str)
        )
    )
    errors: str | None = _attrs.field(
        default=None,
        validator=_attrs.validators.optional(  # type:ignore
            _attrs.validators.instance_of(str)
        )
    )
    newline: str | None = _attrs.field(
        default=None,
        validator=_attrs.validators.optional(  # type:ignore
            _attrs.validators.instance_of(str)
        )
    )
    closefd: bool = _attrs.field(default=True, converter=bool)

    def __attrs_post_init__(self) -> None:
        try:
            with open(
                    file=_os.devnull,
                    mode=self.mode,
                    buffering=self.buffering,
                    encoding=self.encoding,
                    errors=self.errors,
                    newline=self.newline,
                    closefd=self.closefd
            ):
                pass
        except Exception as exc:
            raise FileOpenActionError('Cannot create the action {!s}: {!s}'.format(type(self).__name__, exc)) from exc

    @property
    def metavar(self) -> str:
        return _('FILE')

    def __call__(self, parser: 'EnvironmentVariableParser', option: '_DefinedOption', actual_name: str, value: str, /) -> _typing.IO:
        try:
            return open(file=value,
                        mode=self.mode,
                        buffering=self.buffering,
                        encoding=self.encoding,
                        errors=self.errors,
                        newline=self.newline,
                        closefd=self.closefd
                        )
        except ValueError as exc:
            if '\x00' in value:
                raise RunActionError(_('The value of option {!s} ({!r}) is contained null bytes').format(actual_name, value)) from exc
            raise
        except OSError as exc:
            raise RunActionError(
                _(
                    'Failed to open the value of option {!s} as file: {!s}'
                ).format(actual_name, OSError(exc.errno, _c(exc.strerror), exc.filename))
            ) from exc


class Action(_enum.Enum):
    HELP = HelpAction()
    STRING = StringAction()
    INTEGER = NumberAction()
    FLOAT = NumberAction(is_float=True)
    BOOLEAN = BooleanAction()
    BOOLEAN_REVERSED = BooleanAction(reversed=True)
    PATH = PathAction()
    READ_TEXTFILE = FileOpenAction(mode='rt')
    READ_BINARYFILE = FileOpenAction(mode='rb')
    WRITE_TEXTFILE = FileOpenAction(mode='wt')
    WRITE_BINARYFILE = FileOpenAction(mode='wb')


@_attrs.frozen(kw_only=True, slots=False)
class _DefinedOption:
    names: tuple[str, ...] = _attrs.field(
        validator=_attrs.validators.deep_iterable(
            member_validator=_attrs.validators.instance_of(str),
            iterable_validator=_attrs.validators.and_(
                _attrs.validators.instance_of(tuple),
                _attrs.validators.min_len(1)
            )
        )
    )
    description: str | None = _attrs.field(validator=_attrs.validators.optional(_attrs.validators.instance_of(str)))
    action: AbstractAction = _attrs.field(validator=_attrs.validators.instance_of(AbstractAction))
    required: bool = _attrs.field(converter=bool)
    dest: str = _attrs.field(validator=_attrs.validators.instance_of(str))
    metavar: str | None = _attrs.field(validator=_attrs.validators.optional(_attrs.validators.instance_of(str)))
    default: _typing.Any = _attrs.field()
    choices: tuple | None = _attrs.field(
        validator=_attrs.validators.optional(
            _attrs.validators.deep_iterable(
                _attrs.validators.instance_of(str),
                _attrs.validators.instance_of(tuple)
            )
        )
    )
    annotation: _typing.Any = _attrs.field()


class DefinedOptionType(_typing.Protocol):
    @property
    def name(self) -> tuple[str, ...]:
        raise NotImplementedError

    @property
    def description(self) -> str | None:
        raise NotImplementedError

    @property
    def action(self) -> AbstractAction:
        raise NotImplementedError

    @property
    def required(self) -> bool:
        raise NotImplementedError

    @property
    def dest(self) -> str:
        raise NotImplementedError

    @property
    def metavar(self) -> str | None:
        raise NotImplementedError

    @property
    def default(self) -> _typing.Any:
        raise NotImplementedError

    @property
    def choices(self) -> tuple | None:
        raise NotImplementedError

    @property
    def annotation(self) -> _typing.Any:
        raise NotImplementedError


class _RegexPatterns(_enum.Enum):
    if _sys.platform == 'win32':
        DISALLOWED_OPTION_NAME = _re.compile(r'[\x00-\x1f%<>^&|=:]')
    else:
        DISALLOWED_OPTION_NAME = _re.compile(r'[\x00=]')  # type:ignore
    IEEE_STD_OPTION_NAME = _re.compile(r'^[A-Z_][0-9A-Z_]*$')  # Used by IEEE Std 1003.1-2001


class EnvironmentVariableParser:
    """Object for parsing environment variables into Python objects.

    Note: Command line parsing does not support. Please use argparse.ArgumentParser instead.
    """
    __slots__ = (
        '__defined_options', '__defined_early_options',
        '__defined_option_names', '__defined_option_dest_names', '__console',
        '__prefix', 'prog', 'cmdline_usage', 'description', 'epilog', 'exit_on_error'
    )

    def __init__(self,
                 *, prefix: str = '',
                 prog: str | None = None,
                 cmdline_usage: str | None = None,
                 description: str | None = None,
                 epilog: str | None = None,
                 console: _console.Console | None = None,
                 add_help: bool = True,
                 exit_on_error: bool = True
                 ) -> None:
        """Initialize the EnvironmentVariableParser object with optional parameters.

        ``exit_on_error`` will determine whether EnvironmentVariableParser
        exits with error info when an error occurs.
        If you want to handle errors manually, disable it and catch
        ``EnvironmentVariableParseError`` during ``parseOptions()``.

        Args:
            prefix (str): The prefix for option names.
            prog (str, optional): The program name. Set to ``None`` (default) to use ``sys.argv[0]`` instead.
            cmdline_usage (str, optional): The command-line usage information. Defaults to ``None``.
            description (str, optional): The description of the program. Defaults to ``None``.
            epilog (str, optional): The epilog of the program. Defaults to ``None``.
            console (rich.console.Console, optional): An object has implemented Rich Console API. Defaults to ``None``.
            add_help (bool): Add an option before finishing the instantiation to show the help message. Defaults to ``False``.
            exit_on_error (bool): Determines whether EnvironmentVariableParser exits with error info when an error occurs.
        """
        self.__defined_options: list[_DefinedOption] = []
        self.__defined_early_options: list[_DefinedOption] = []
        self.__defined_option_names: list[str] = []
        self.__defined_option_dest_names: list[str] = []
        if console is None:
            self.__console = _console.Console(markup=True, highlight=False)
        elif isinstance(console, _console.Console):
            self.__console = console
        else:
            raise TypeError('Console must be a rich.console.Console object, not {!r}'.format(type(console).__name__))

        self.__prefix = ''
        self.prefix = prefix
        self.prog = prog
        self.cmdline_usage = cmdline_usage
        self.description = description
        self.epilog = epilog
        self.exit_on_error = exit_on_error

        if add_help:
            self.defineOption('HELP', action=Action.HELP, description=_('Show this help message and exit.'))

    @property
    def console(self) -> _console.Console:
        return self.__console

    def _validateOptionNameOrPrefix(self, name_or_prefix: _typing.Any, is_prefix: bool = False) -> None:
        if not isinstance(name_or_prefix, str):
            raise TypeError('The option name{!s} must be str, not {!r}'.format(' prefix' if is_prefix else '', type(name_or_prefix).__name__))

        if not is_prefix:
            if not name_or_prefix:
                raise ValueError('Option name cannot be an empty string')
            if name_or_prefix in self.__defined_option_names:
                raise ValueError('Conflicted option name: {!r}'.format(name_or_prefix))

        if _RegexPatterns.DISALLOWED_OPTION_NAME.value.search(name_or_prefix):
            raise ValueError('Option name{!s} {!r} is invalid on your platform'.format(' prefix' if is_prefix else '', name_or_prefix))

        if not _RegexPatterns.IEEE_STD_OPTION_NAME.value.fullmatch(name_or_prefix):
            if is_prefix:
                if name_or_prefix:
                    _warnings.warn(
                        SyntaxWarning(
                            _(
                                'The option name prefix {!r} is not compatible with IEEE Std 1003.1-2001. '
                                'Other shells and utilities may not support reading or assigning environment variables starts with this prefix.'
                            ).format(name_or_prefix)
                        )
                    )
            else:
                _warnings.warn(
                    SyntaxWarning(
                        _(
                            'The option name {!r} is not compatible with IEEE Std 1003.1-2001. '
                            'Other shells and utilities may not support reading or assigning environment variables with this name.'
                        ).format(name_or_prefix)
                    )
                )

    @property
    def prefix(self) -> str:
        return self.__prefix

    @prefix.setter
    def prefix(self, value: str | None, /) -> None:
        if value:
            prefix = str(value)
        else:
            prefix = ''

        self._validateOptionNameOrPrefix(prefix, is_prefix=True)

        self.__prefix = prefix

    def printUsage(self) -> None:
        usage_prompt = _('Usage: ')
        prog = self.prog or _shlex.quote(_os.path.basename(_sys.argv[0]))
        cmdline_usage = _('[ENVS]... {!s} {!s}').format(prog, self.cmdline_usage or _('[ARGS]...'))
        self.__console.print(f'{usage_prompt!s}{cmdline_usage!s}')

    def printOptionsAndDescriptions(self, *, show_default: bool = False) -> None:
        option_names_conj = _('or')
        renderables = []

        if self.__defined_early_options:
            early_options_table = _table.Table.grid(padding=(0, 4, 0, 4), expand=False)
            early_options_table.add_column(justify='left')
            early_options_table.add_column(justify='left')

            for option in self.__defined_early_options:
                row_column1_lines = []
                for name in option.names:
                    metavar = '[...]'
                    row_column1_lines.append(f'    {name!s}={metavar!s}')

                row_column2_lines = []
                if option.description:
                    row_column2_lines.extend(option.description.splitlines())

                early_options_table.add_row(
                    f'{_os.linesep!s}{option_names_conj!s} '.join(row_column1_lines),
                    _os.linesep.join(row_column2_lines)
                )
            renderables.extend(
                [
                    _(
                        'The following environment variables will be preemptively parsed '
                        'and exit after performing the operation:'
                    ),
                    early_options_table,
                    ''
                ]
            )

        if self.__defined_options:
            options_table = _table.Table.grid(padding=(0, 4, 0, 4), expand=False)
            options_table.add_column(justify='left')
            options_table.add_column(justify='left')

            for option in self.__defined_options:
                row_column1_lines = []
                for name in option.names:
                    metavar = str(option.action.metavar) if option.metavar is None else str(option.action.metavar)
                    if option.required:
                        metavar = f'<{metavar!s}>'
                    else:
                        metavar = f'[{metavar!s}]'
                    row_column1_lines.append(f'    {name!s}={metavar!s}')

                row_column2_lines = []
                if option.description:
                    row_column2_lines.extend(option.description.splitlines())
                if option.required:
                    row_column2_lines.append(_('[Required Option]'))
                elif show_default:
                    row_column2_lines.append(
                        _('[Default: {!s}]').format(
                            _('<Empty>') if option.default is None else option.default
                        )
                    )

                options_table.add_row(
                    f'{_os.linesep!s}{option_names_conj!s} '.join(row_column1_lines),
                    _os.linesep.join(row_column2_lines)
                )
            renderables.extend(
                [
                    _('Unless otherwise stated, all options are optional by default.'),
                    _('List of available environment variables [ENVS]:'),
                    options_table
                ]
            )

        for renderable in renderables:
            self.__console.print(renderable)

    def printHelp(self, *, show_default: bool = False) -> None:
        self.printUsage()
        if self.description and self.description.strip():
            self.__console.print()
            self.__console.print(self.description)
        self.__console.print()
        self.printOptionsAndDescriptions(show_default=show_default)
        if self.epilog and self.epilog.strip():
            self.__console.print(self.epilog)

    def defineOption(self,
                     *names: str,
                     action: str | Action | AbstractAction | None = None,
                     dest: str | None = None,
                     metavar: str | None = None,
                     required: bool = False,
                     choices: _typing.Iterable[_typing.Any] | None = None,
                     default: _typing.Any = None,
                     description: str | None = None,
                     annotation: _typing.Any = _typing.Any
                     ) -> _DefinedOption:
        """Define how a single environment variable should be parsed.

        ``action`` is played an essential role in the option value conversion. It can be:

            - A string represented to name of an internal action.
              The uppercase form of the name must be equal to attribute
              ``name`` of any member in the enum class ``Action``.
            - A member in the enum class ``Action``.
            - An instance of a class that is inherited from ``AbstractAction``.

        To use your customized action, you need to inherit from ``AbstractAction``
        and implement the ``__call__()`` method: put your logic into this method,
        and ensure it can handle the option value conversion.

        Args:
            *names (str): Names of the option.
            action (str | Action | AbstractAction, optional): Action to be performed for the option.
            dest (str, optional): Destination name for the option.
            metavar (str, optional): A placeholder to refer to each expected option.
            required (bool, optional): Indicates if the option is required. Defaults to ``False``.
            choices (Iterable[Any], optional): List of choices for the option. Defaults to ``None``.
            default (Any, optional): Default value for the option. Defaults to ``None``.
            description (str, optional): Description text for the option. Defaults to ``None``.
            annotation (Any, optional): Typing annotation for the value of option. Defaults to ``typing.Any``.

        Returns:
            The option definition, in an ``attrs``-powered dataclass object.
        """
        if not names:
            raise TypeError('At least one name required by option definition')
        for name in names:
            self._validateOptionNameOrPrefix(name, is_prefix=False)

        if isinstance(action, str):
            action_name = action.upper().replace('-', '_')
            for item in Action:
                if item.name == action_name:
                    selected_action = item.value
                    break
            else:
                raise ValueError('Unknown name of action: {!r}'.format(action))
        elif isinstance(action, Action):
            selected_action = action.value
        elif isinstance(action, AbstractAction):
            selected_action = action
        elif action is None:
            selected_action = Action.STRING.value
        else:
            raise TypeError(
                "'action' must be a name of the action, "
                "a member from {!r} or an instance of the class inherited from {!r}, "
                "not {!r}".format(Action, AbstractAction, action)
            )

        if not dest:
            dest = names[0]
        if dest in self.__defined_option_dest_names:
            raise ValueError('Conflicted option destination name: {!r}'.format(dest))

        if choices is not None:
            choices = tuple(choices)
            if not choices:
                raise ValueError('Choice sequence is empty')

        defined_option = _DefinedOption(names=names,
                                        description=description,
                                        action=selected_action,
                                        required=required,
                                        dest=dest,
                                        metavar=metavar,
                                        default=default,
                                        choices=choices,
                                        annotation=annotation
                                        )
        if defined_option.action.early:
            self.__defined_early_options.append(defined_option)
        else:
            self.__defined_options.append(defined_option)
        self.__defined_option_names.extend(names)
        self.__defined_option_dest_names.append(dest)

        return defined_option

    def printOptionValueTypes(self) -> None:
        self.__console.print(
            repr({__.dest: __.annotation for __ in self.__defined_options}),
            highlight=True
        )

    def beforeExit(self, message: str) -> None:
        self.__console.print('{!s}: {!s}'.format(self.prog or _shlex.quote(_os.path.basename(_sys.argv[0])), message))

    @staticmethod
    def _exitGracefully(method: _typing.Callable[_P, _T]) -> _typing.Callable[_P, _T]:
        @_functools.wraps(method)
        def gracefullyExitWrapper(*args, **kwargs):
            self: EnvironmentVariableParser = args[0]
            if self.exit_on_error:
                try:
                    return method(*args, **kwargs)
                except EnvironmentVariableParseError as exc:
                    if exc.exitcode != 0:
                        if exc.message:
                            self.beforeExit(_('Environment variable parse error: {!s}').format(exc.message))
                    elif exc.message:
                        self.beforeExit(exc.message)
                    _sys.exit(exc.exitcode)
            else:
                return method(*args, **kwargs)

        return _typing.cast(_typing.Callable[_P, _T], gracefullyExitWrapper)

    @_exitGracefully
    def parseOptions(self, env: _typing.Mapping[str, str] | None = None) -> tuple[list[str], dict[str, _typing.Any]]:
        """Collect all defined options from a mapping of environment variables.

        Args:
            env (Mapping[str, str], optional): A mapping of specified environment variables.
                Set to None (default) to use os.environ instead.

        Returns:
            A 2-tuple, which is contained a list of consumed environment variable names
            and a populated dict.
        """
        if env is None:
            environ = dict(_os.environ)
        else:
            environ = dict(env)

        consumed_environ_names: list[str] = []
        result: dict[str, _typing.Any] = {}

        for early_option in self.__defined_early_options:
            for name in early_option.names:
                final_name = f'{self.prefix!s}{name}'
                if final_name in environ:
                    early_option.action(self, early_option, final_name, environ.pop(final_name))
                    raise _Never

        for option in self.__defined_options:
            value: str | None = None
            for name in option.names:
                final_name = f'{self.prefix!s}{name}'
                if final_name in environ:
                    value = environ.pop(final_name)
                    consumed_environ_names.append(final_name)
                    break
            if value is None:
                if option.required:
                    raise EnvironmentVariableParseError(_('Missing the required environment variable: {!s}').format(option.names[0]))
                else:
                    result[option.dest] = option.default
                    continue

            if option.choices and value not in option.choices:
                raise EnvironmentVariableParseError(
                    _(
                        'The value of option {!s} ({!r}) is not in the following choices: {!r}'
                    ).format(consumed_environ_names[-1], value, option.choices)
                )

            result[option.dest] = option.action(self, option, consumed_environ_names[-1], value)

        return consumed_environ_names, result
