#!/bin/env python3
# -*- encoding: utf-8 -*-
import contextlib
import http.server
import os
import socket
import sys
from pathlib import Path

import environparse

parser = environparse.EnvironmentVariableParser(
    description='An script to start a http server, but use `environparse` to demonstrate the option parsing.',
    epilog='Do not forget the warning from `http.server` documentation:\n'
           'http.server is not recommended for production. It only implements basic security checks.'
)
parser.defineOption(
    'BIND_ADDRESS',
    action=environparse.Action.STRING,
    description='Bind to a specified address. Leave empty to bind all interfaces.',
    show_default=False
)
parser.defineOption(
    'BIND_PORT',
    action=environparse.Action.INTEGER,
    description='Bind to a specified port.',
    default=6282
)
parser.defineOption(
    'ROOTDIR',
    dest='rootdir',
    action=environparse.PathAction(
        validators=[
            environparse.PathValidators.IsExists(),
            environparse.PathValidators.IsDir(),
            environparse.PathValidators.HasPermission(os.R_OK | os.X_OK)
        ]
    ),
    description='Serve a specified directory.',
    default=Path.cwd()
)

if __name__ == '__main__':
    consumed_env_names, options = parser.parseOptions()

    parser.console.print('Consumed names of environment variables:', consumed_env_names)
    parser.console.print('Parsed options:')
    parser.console.print(options, highlight=True)
    parser.console.print('[b]Starting the HTTP server...[/b]', markup=True)


    class DualStackHTTPServer(http.server.ThreadingHTTPServer):
        def server_bind(self) -> None:
            with contextlib.suppress(Exception):
                self.socket.setsockopt(
                    socket.IPPROTO_IPV6,
                    socket.IPV6_V6ONLY,
                    0
                )
            return super().server_bind()

        def finish_request(self, request, client_address) -> None:
            self.RequestHandlerClass(request, client_address, self, directory=options['rootdir'])


    http.server.test(
        HandlerClass=http.server.SimpleHTTPRequestHandler,
        ServerClass=DualStackHTTPServer,
        port=options['BIND_PORT'],
        bind=options['BIND_ADDRESS'],
        protocol='HTTP/1.0'
    )
else:
    parser.console.print('Please, start this HTTP server by:')
    parser.console.print(f'  [ENVIRONS]... {os.path.basename(sys.executable)!s} -m {__name__!s}')
