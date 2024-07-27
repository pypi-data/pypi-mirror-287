# `environparse`

Environment variable parsing library, inspired by stdlib `argparse`.

## Features:

- Handles both optional and required environment variable.
- Automatically multi-language support.
    - Currently supported 5 languages: en, zh_CN, zh_SG, zh_HK, zh_TW.
- ~~And more features that have not yet been implemented.~~

## Install

Available on [PyPI](https://pypi.org/project/environparse).

The release page also provided wheel package to download.

## Example

Consider the following demo script, it will start an HTTP server with specified options from environment variables:

```python
import contextlib
import http.server
import socket
from pathlib import Path
from pprint import pprint

import environparse

parser = environparse.EnvironmentVariableParser(
    description='An script to start a http server, but use `envparse` to demonstrate the option parsing.',
    epilog='This is the epilog.'
)
parser.defineOption(
    'BIND_ADDRESS',
    action=environparse.Action.STRING,
    description='Bind to a specified address. Leave empty to bind all interfaces.'
)
parser.defineOption(
    'BIND_PORT',
    action=environparse.Action.INTEGER,
    description='Bind to a specified port.',
    default=1425
)
parser.defineOption(
    'ROOTDIR',
    dest='rootdir',
    action=environparse.Action.PATH,
    description='Serve a specified directory.',
    default=Path.cwd()
)

if __name__ == '__main__':
    consumed_env_names, options = parser.parseOptions()

    print('Consumed names of environment variables:', consumed_env_names)
    print('Parsed options:')
    pprint(options)


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
```

After install `environparse`, run the script with environment variable `HELP` to get more information:

```sh-session
$ > pwd
/tmp
$ > LANGUAGE=en_GB.UTF-8 HELP= python /tmp/scratch.py
Usage: [ENVS]... scratch.py [ARGS]...

An script to start a http server, but use `envparse` to demonstrate the option parsing.

The following environment variables will be preemptively parsed and exit after performing the operation:
    HELP=[...]    Show this help message and exit.

Unless otherwise stated, all options are optional by default.
List of available environment variables [ENVS]:
    BIND_ADDRESS=[STRING]    Bind to a specified address. Leave empty to bind all interfaces.
                             [Default: <Empty>]                                              
    BIND_PORT=[INTEGER]      Bind to a specified port.                                       
                             [Default: 1425]                                                 
    ROOTDIR=[PATH]           Serve a specified directory.                                    
                             [Default: /tmp]                                                 
This is the epilog.
$ >
```

`environparse` even support localization:

```sh-session
$ > LANGUAGE=zh_CN.UTF-8 HELP= python /tmp/scratch.py
用法：[环境变量]... scratch.py [参数]...

An script to start a http server, but use `envparse` to demonstrate the option parsing.

以下环境变量将被抢先解析，并在运行操作后退出：
    HELP=[...]    显示此帮助信息并退出。

除非另有说明，所有选项默认都是可选的。
可用的 [环境变量] 列表：
    BIND_ADDRESS=[字符串]    Bind to a specified address. Leave empty to bind all interfaces.
                             [默认值：<空>]                                                  
    BIND_PORT=[整数]         Bind to a specified port.                                       
                             [默认值：1425]                                                  
    ROOTDIR=[PATH]           Serve a specified directory.                                    
                             [默认值：/tmp]                                                  
This is the epilog.
$ >
```

Now, try to test the HTTP server:

```sh-session
$ > ROOTDIR="$HOME" BIND_ADDRESS='127.127.127.127' python /tmp/scratch.py
Consumed names of environment variables:
['BIND_ADDRESS', 'ROOTDIR']
Parsed options:
{'BIND_ADDRESS': '127.127.127.127', 'BIND_PORT': 1425, 'rootdir': PosixPath('/home/user')}
Starting the HTTP server...
Serving HTTP on 127.127.127.127 port 1425 (http://127.127.127.127:1425/) ...
127.0.0.1 - - [27/Jul/2024 01:35:59] "GET /Music/EXEC_HYMME_SEAMLESSECHO%3DH_D_.%20-%20stellatram.flac HTTP/1.1" 200 -
127.0.0.1 - - [27/Jul/2024 01:36:45] "GET /Music/%E3%82%B3%E3%83%BC%E3%83%89%E3%83%BB%E3%82%A8%E3%83%86%E3%82%B9%E3%82%A6%E3%82%A7%E3%82%A4%28Class__ETHES_WEI%3D_extends.COMMUNI_SAT_.%29%20-%20%E9%9C%9C%E6%9C%88%E3%81%AF%E3%82%8B%E3%81%8B.flac HTTP/1.1" 200 -
127.0.0.1 - - [27/Jul/2024 01:57:04] "GET /Music/%E7%A5%AD%E6%9E%9C%E3%81%A6%E3%81%AE%E8%8A%B1%20-%20%E4%B8%AD%E6%81%B5%E5%85%89%E5%9F%8E%E3%80%81%E9%9C%9C%E6%9C%88%E3%81%AF%E3%82%8B%E3%81%8B.flac HTTP/1.1" 200 -
^C
Keyboard interrupt received, exiting.
$ >
```
