# Changelog

All notable changes to this project will be documented in this file.

This project adheres to [PyPI Version Specification](https://packaging.python.org/en/latest/specifications/version-specifiers).

## 0.2.0.post1 - 2024-07-28

- Fixed some typos in README.md.
- Added missing changelog of version 0.2.0.

## 0.2.0 - 2024-07-28

- Added an `environparse`-based HTTP server start script for example purpose.
    - To access/use this script, run:

      ```sh-session
      $ > [ENVIRONS]... python -m environparse.examples.httpserver
      ```

- Added some base path validators.
    - These validators are members of class `PathValidators`. For example, `PathValidators.HasPermission` can validate the path accessibility with specified `mode` argument.
    - To create a custom path validator, please inherit from `environparse.AbstractPathValidator` and implement the `__call__()` method.
- Now you can finer control over display of option defaults in help messages through keyword-only argument `show_default` in parser initialization and option definition.
- Protocol class `DefinedOptionType` is removed. Now `DefinedOption` (renamed from `_DefinedOption`) can use to annotate the return type of `EnvironmentVariableParser.defineOption()`.

## 0.1.0 - 2024-07-26

The initial release.
