# `environparse`

Environment variable parsing library, inspired by stdlib `argparse`.

## Features:

- Handles both optional and required environment variable.
- Built-in various actions to handle the value parsing, such as:
    - String
    - Number (integer or float)
    - Boolean
    - Path (with optional validations)
    - File opener
- Localization support. Currently, supports the following languages:
    - `en`
    - `zh-CN`
    - `zh-SG`
    - `zh-HK`
    - `zh-TW`
- And more features that have not yet been implemented...

## Install

Available on [PyPI](https://pypi.org/project/environparse).

The release page also provided wheel package to download.

## Example

`environparse` has a built-in HTTP server startup script to demonstrate the basic usage of `environparse`. To access it, run the following command to see help messages:

```sh-session
$ > pwd
/tmp
$ > LANGUAGE=en_SG.UTF-8 HELP= python -m environparse.examples.httpserver
Usage: [ENVS]... httpserver.py [ARGS]...

An script to start a http server, but use `environparse` to demonstrate the option parsing.

The following environment variables will be preemptively parsed and exit after performing the operation:
    HELP=[...]    Show this help message and exit.

Unless otherwise stated, all options are optional by default.
List of available environment variables [ENVS]:
    BIND_ADDRESS=[STRING]    Bind to a specified address. Leave empty to bind all interfaces.
    BIND_PORT=[INTEGER]      Bind to a specified port.                                       
                             [Default: 6282]                                                 
    ROOTDIR=[PATH]           Serve a specified directory.                                    
                             [Default: /tmp]                                                 

Do not forget the warning from `http.server` documentation:
http.server is not recommended for production. It only implements basic security checks.
$ >
```

`environparse` even support localization:

```sh-session
用法：[环境变量]... httpserver.py [参数]...

An script to start a http server, but use `environparse` to demonstrate the option parsing.

以下环境变量将被抢先解析，并在运行操作后退出：
    HELP=[...]    显示此帮助信息并退出。

除非另有说明，所有选项默认都是可选的。
可用的 [环境变量] 列表：
    BIND_ADDRESS=[字符串]    Bind to a specified address. Leave empty to bind all interfaces.
    BIND_PORT=[整数]         Bind to a specified port.                                       
                             [默认值：6282]                                                  
    ROOTDIR=[PATH]           Serve a specified directory.                                    
                             [默认值：/tmp]                                                  

Do not forget the warning from `http.server` documentation:
http.server is not recommended for production. It only implements basic security checks.
$ >
```

Now, try to test the HTTP server:

```sh-session
$ > ROOTDIR="$HOME/Music" BIND_ADDRESS='127.127.127.127' python /tmp/scratch.py
Consumed names of environment variables:
['BIND_ADDRESS', 'ROOTDIR']
Parsed options:
{'BIND_ADDRESS': '127.127.127.127', 'BIND_PORT': 6282, 'rootdir': PosixPath('/home/user/Music')}
Starting the HTTP server...
Serving HTTP on 127.127.127.127 port 6282 (http://127.127.127.127:6282/) ...
127.0.0.1 - - [27/Jul/2024 01:35:59] "GET /Music/EXEC_HYMME_SEAMLESSECHO%3DH_D_.%20-%20stellatram.flac HTTP/1.1" 200 -
127.0.0.1 - - [27/Jul/2024 01:36:45] "GET /Music/%E3%82%B3%E3%83%BC%E3%83%89%E3%83%BB%E3%82%A8%E3%83%86%E3%82%B9%E3%82%A6%E3%82%A7%E3%82%A4%28Class__ETHES_WEI%3D_extends.COMMUNI_SAT_.%29%20-%20%E9%9C%9C%E6%9C%88%E3%81%AF%E3%82%8B%E3%81%8B.flac HTTP/1.1" 200 -
127.0.0.1 - - [27/Jul/2024 01:57:04] "GET /Music/%E7%A5%AD%E6%9E%9C%E3%81%A6%E3%81%AE%E8%8A%B1%20-%20%E4%B8%AD%E6%81%B5%E5%85%89%E5%9F%8E%E3%80%81%E9%9C%9C%E6%9C%88%E3%81%AF%E3%82%8B%E3%81%8B.flac HTTP/1.1" 200 -
^C
Keyboard interrupt received, exiting.
$ >
```
