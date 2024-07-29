"""
Entry point for asrch

Main file for asrch which handles all modules
CLI argument and command handling
"""

import logging
import sys
from typing import Optional
from datetime import datetime
import os

import click
import typer
import typer.core
from typing_extensions import Annotated
import toml
from pathlib import Path

import asrch.webdriver.webdriver_manager as webdriver_manager
from asrch.commands._find import find_elements
from asrch.commands._open import get_page, get_html, get_image, get_js, get_screenshot
from asrch.commands._send import search_engines
from asrch.commands.no_driver._nd_open import get_page, inspect, get_js
from asrch.modules._formatting import Bar as Sep
from asrch.modules.logging_formatter import ColorFormatter
from asrch.utils.constants import Colors, OpenModes  # , ConfigDefaults

from ascli.modules._output import Output


form = Sep()
colors = Colors()

app = typer.Typer()

config_path = Path(__file__).parent
config = toml.load(Path(f"{config_path}/config/undetected.toml"))
ws_config = toml.load(Path(f"{config_path}/config/current_ws.toml"))
workspace_path = Path(f"{config_path}/config/config/workspaces.txt")
cworkspace_path = Path(f"{config_path}/config//current_ws.txt")

config_path = Path(__file__).parent.parent.parent
path_with_config = config_path / '.cache'


current_dir = os.path.dirname(os.path.realpath(__file__))

resolved_path = f"{Path(__file__).parent.parent.parent}/workspaces/"

current_datetime = datetime.now()

c_log = logging.getLogger(__name__)
c_log.setLevel(logging.DEBUG)


sh = logging.StreamHandler()

c_form = ColorFormatter("%(asctime)s|%(levelname)8s|%(message)s")


sh.setFormatter(c_form)

c_log.addHandler(sh)

def ensure_ws_doesnt_exist(ws_name: str) -> bool:
    file_path = Path("src/asrch/config/workspaces.txt")
    with open(file_path, 'r') as f:
        for line in f:
            if f"name:{ws_name}" in line.strip():
                return False  
    return True 

def create_workspace(name: str, current_datetime: str, config: str):
    if ensure_ws_doesnt_exist(name):
        with open(Path("src/asrch/config/workspaces.txt"), 'a') as f:
            f.write(f"""\n\n
            --------------
            WORKSPACE {name}
            --------------
            name:{name}
            config: {config} 
            created:{current_datetime}
            --------------
            END WORKSPACE {name}
            --------------""".replace("                ", ""))
            os.mkdir(f"{resolved_path}/{name}/")
        typer.echo(f"Workspace '{name}' created successfully.")
    else:
        c_log.error(f"Workspace '{name}' already exists.")
        
def get_ws():
    with open("src/asrch/config/current_ws.txt", 'r') as f:
        for line in f:
            return

@app.command(name="open")
def open_(
    mode: OpenModes = typer.Argument(help="Mode for command"),
    url: str = typer.Argument(help="URL to retrieve"),
    proxy: str = typer.Option(
        None, "--proxy", "-p", help="Proxy to send request <ip:port> [optional]"
    ),
    header: bool = typer.Option(False, "--header", "-H", help="Show browser header"),
    browse: bool = typer.Option(
        False,
        "--browse",
        "-b",
        help="Enable browsing (using keyboard inputs to open urls)",
    ),
    pager: bool = typer.Option(False, "--pager", "-P", help="Output [JS] in pager"),
    download: bool = typer.Option(
        False, "--download", "-d", help="Download all scraped images"
    ),
    log: bool = typer.Option(
        False, "--log", "-l", help="Suppress all logs (for emacs mode)"
    ),
    nodriver: bool = typer.Option(
        False,
        "--nodriver",
        "-n",
        help="Use requests and BS4 instead of selenium (faster but more detectable)",
    ),
    parser: str = typer.Option(
        "html.parser",
        "--parser",
        help="HTML parser to use for nodriver. Choices: html.parser, lxml",
    ),
    silent: bool = typer.Option(
        False,
        "--silent",
        "-s",
        help="Output to text file instead of terminal (defaults to workspace folder)",
    ),
    inspect_mode: str = typer.Option(
        "html",
        "-iM",
        help = "What part of the page you would like to inspect. :Note: -M js can have a LONG ASS output (~5k line history rec)",
    ),
        
):
    """Open a URL and perform various operations.

    :param mode: Mode for the command.
    :type mode: OpenModes

    :param url: URL to retrieve.
    :type url: str

    :param proxy: Proxy to send request <ip:port> [optional].
    :type proxy: str, optional

    :param header: Show browser header.
    :type header: bool, optional

    :param browse: Enable browsing (using keyboard inputs to open URLs).
    :type browse: bool, optional

    :param pager: Output [JS] in pager.
    :type pager: bool, optional

    :param download: Download all scraped images.
    :type download: bool, optional

    :param log: Suppress all logs (for emacs mode).
    :type log: bool, optional

    :param nodriver: Use requests and BS4 instead of selenium (faster but more detectable).
    :type nodriver: bool, optional

    :param parser: HTML parser to use for nodriver. Choices: html.parser, lxml.
    :type parser: str, optional

    :param silent: Output to text file instead of terminal (defaults to workspace folder).
    :type silent: bool, optional

    :param inspect_mode: What part of the page you would like to inspect.
    :type inspect_mode: str, optional

    :Note:
        - For `log`, this option is intended for emacs mode and should be ignored in normal CLI mode, but can be used if needed.
        - `inspect_mode` with `-M js` can produce a large output (~5k line history record).
    """
    if not nodriver:
        with webdriver_manager.format_alerts(
            2,
            f"[{get_ws()}] Begin {mode.value} | {'-b' if browse else ''} | {'-h' if header else ''} | {url}",
        ):
            if mode.value == "text":
                if browse:
                    returned_url = url
                    while returned_url not in ["q", "<"]:
                        returned_url = get_page(
                            url=returned_url,
                            proxy=proxy,
                            header=header,
                            log=log,
                            browse=browse,
                        )

                elif browse is False:
                    if silent: 
                        with open(f"{resolved_path}/{get_ws()}/output.txt", "w") as f:
                            f.write(f"{datetime} \n")
                            f.write((get_page(url=url, proxy=proxy, header=header, log=log)))
                    else:
                        print(get_page(url=url, proxy=proxy, header=header, log=log))

            elif mode.value == "body":
                print(get_page(url=url, proxy=proxy, header=header))
            elif mode.value == "html":
                print(get_html(url=url, proxy=proxy, header=header))
            elif mode.value == "js":
                js_srcs = get_js(url=url, proxy=proxy, header=header)
                if log:
                    for js_src in js_srcs:
                        print(js_src)
                elif pager:
                    click.echo_via_pager(js_srcs)
                else:
                    for js_src in js_srcs:
                        print(js_src)
            elif mode.value == "img":
                for images in get_image(url, proxy, header, download=download, workspace=get_ws()):
                    print(images)
            elif mode.value == "ss":
                get_screenshot(url, proxy, header)
                click.echo("SCREENSHOTTED")
    else:  # nodriver
        with webdriver_manager.format_alerts(
            2,
            f"Begin {mode.value} | {'-b' if browse else ''} | {'-h' if header else ''} | {url}",
        ):           
            if mode.value == "html":
                print(get_html(url, parser=parser))
            elif mode.value in ["ins", "inspect"]:
                if pager:
                    click.echo_via_pager(inspect(url=url,proxy=proxy, header=header,mode=inspect_mode))
                else:
                    inspect(url=url,proxy=proxy, header=header,mode=inspect_mode)
            elif mode.value == "text":
                if browse:
                    returned_url = url
                    while returned_url not in ["q", "<"]:
                                returned_url = get_page(
                                    url=returned_url,
                                    proxy=proxy,
                                    header=header,
                                    log=log,
                                    browse=browse,
                                )

            elif mode.value == "js":
                print(get_js(
                    url=url,
                    proxy=proxy,
                    header=header,
                    log=log,
                    ))
@app.command()
def browse(
    url = "https://asrch.bitbucket.io",
    proxy: str = typer.Option(
        None, "--proxy", "-p", help="Proxy to send request <ip:port> [optional]"
    ),

    log: bool = typer.Option(
        False, "--log", "-l", help="Suppress all logs (for emacs mode)"
    ),
    nodriver: bool = typer.Option(
        False,
        "--nodriver",
        "-n",
        help="Use requests and BS4 instead of selenium (faster but more detectable)",
    ),
    parser: str = typer.Option(
        "html.parser",
        "--parser",
        help="HTML parser to use for nodriver. Choices: html.parser, lxml",
    ),        
):
    """Browse the web.

    :param url: The URL to start browsing from (default is "https://asrch.bitbucket.io").
    :type url: str

    :param proxy: Proxy to send requests (<ip:port>) [optional].
    :type proxy: str, optional

    :param log: Suppress all logs (for emacs mode).
    :type log: bool, optional

    :param nodriver: Use requests and BS4 instead of selenium (faster but more detectable).
    :type nodriver: bool, optional

    :param parser: HTML parser to use for nodriver. Choices: html.parser, lxml (default is html.parser).
    :type parser: str, optional

    :return: None
    :rtype: None

    :raises ValueError: If invalid parser option is provided.

    :Example:

        To browse using default settings:

        >>> browse()

        To browse using a proxy and suppress logs:

        >>> browse(proxy="127.0.0.1:8080", log=True)

        To browse without using a webdriver and specify a parser:

        >>> browse(nodriver=True, parser="lxml")
    """
    browse = True
    if browse:
        returned_url = url
        
        while returned_url not in ["q", "<"] and returned_url:
            returned_url = get_page(
                   url=returned_url,
                   proxy=proxy,
                   log=log,
                   browse=browse,
               )


@app.command()
def ccache():
    """
    Clear browser cache
    
    """
    for file in path_with_config.iterdir():
        if file.is_file() and file.suffix == '.txt':
            c_log.debug(f"del: {file}")
            file.unlink()

            print(f"{Colors.GREEN}Cache cleared")
@app.command()
def search(
    query: str = typer.Argument(help="Search query"),
    proxy: str = typer.Option(
        "", "--proxy", "-p", help="Proxy to send request <IP:port> [optional]"
    ),
    browse: bool = typer.Option(False, "--browse", "-b", help="Enable browse mode"),
    header: bool = typer.Option(False, "--header", "-H", help="Show browser header"),
    log: bool = typer.Option(
        False, "--log", "-l", help="Suppress all logs (for emacs mode, ignored in CLI)"
    ),
):
    """Search function to perform a search operation.

    :param header: Show browser header. Annotated with bool.
    :type header: Annotated[bool, typer.Option(help="show browser header")]

    :param proxy: Proxy to send request <IP:port> [optional]. Annotated with str.
    :type proxy: Annotated[str, typer.Option(help="proxy to send request <IP:port> [optional]")]

    :param log: toggle logging message visibility
    :type log: bool
    :default: false
    : This flag is intended for the emacs plugin and is not made to
      be used within the normal CLI mode however you can use it if
      you like.
    """

    with webdriver_manager.format_alerts(
        2,
        f"Begin | {query}",
    ):        

        returned_url: str | int = search_engines(query, header, proxy, log, browse)
        if browse:
            while returned_url:
                returned_url = get_page(
                    url = returned_url,
                    proxy=proxy,
                    header=header,
                    log=log,
                    browse=browse,
                )
        else:
            print(search_engines(query, header, proxy, log, browse))

            

@app.command()
def find(
    url: Annotated[str, typer.Option(help="URL to retrieve")],
    element: Annotated[str, typer.Option(help="Element to return")],
    proxy: Annotated[
        Optional[str], typer.Option(help="proxy to send request <ip:port> [optional]")
    ] = "",
    header: Annotated[bool, typer.Option(help="show browser header")] = False,
    log: Annotated[
        bool,
        typer.Option(
            help="supress all logs (this option is for emacs mode and should be ignore in the CLI)"
        ),
    ] = False,
    locator: Annotated[str, typer.Option(help="Locator to find element")] = "tag_name",
):
    """Find an element on a web page.

    :param url: URL to retrieve.
    :type url: str

    :param element: Element to return.
    :type element: str

    :param proxy: Proxy to send request (<ip:port>) [optional].
    :type proxy: Optional[str]
    :default proxy: ""

    :param header: Show browser header.
    :type header: bool
    :default header: False

    :param log: Suppress all logs.
    :type log: bool
    :default log: False

    :param locator: Locator to find the element.
    :type locator: str
    :default locator: "tag_name"

    :return: None
    :rtype: None
    """
    with webdriver_manager.format_alerts(
        2,
        f"Begin | {url}"):
        print((find_elements(url, locator, element, header, proxy, log)))


@app.command()
def workspace(
    initialize: bool = typer.Option(False, "--initialize", help="Initialize workspace"),
    create: bool = typer.Option(False, "--create", help="Create workspace"),
    config: str = typer.Option(None, "-c" ,"--conf", help="The name of the workspace to act on"),
    name: str = typer.Option(None,"-n", "--name", help="The name of the workspace to act on"),
    delete: bool = typer.Option(False, "--delete", help="Delete workspace")
):
    """Perform operations related to workspaces.
    Depending on the options provided, this function can initialize, create, delete,
    or perform other actions related to workspaces.

    :param initialize: Flag to initialize workspace.
    :type initialize: bool
    
    :param create: Flag to create workspace.
    :type create: bool
    
    :param config: The name of the workspace to act on.
    :type config: str
    
    :param name: The name of the workspace to act on.
    :type name: str
    
    :param delete: Flag to delete workspace.
    :type delete: bool
    """
    if initialize:
        if not ensure_ws_doesnt_exist(name):
            with open("src/asrch/config/current_ws.txt", 'w') as f:
                f.write(name)
            typer.echo(f"{Colors.MINT}Initialized workspace: {name} and {config}")
            sys.ps1 = name

        else:
            typer.echo("Error: Please provide an existing workspace name with --name option.")

    if create:
        if name:
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
            create_workspace(name, current_datetime, config)
        else:
            typer.echo("Error: Please provide a workspace name with --name option.")

@app.command()
def conf():
    """Output current config
    """
    print(f"{Colors.MINT}{Colors.BOLD}\n[Workspace]{Colors.NC}")
    with open("src/asrch/config/current_ws.txt", 'r') as f:
        for line in f:
            print(line)
        
    print(f"{Colors.PASTEL_PINK}{Colors.BOLD}[basic]{Colors.NC}")
    print(f"url = {config['basic']['url']}\n")

    print(f"{Colors.BOLD}{Colors.PASTEL_PINK}[privacy]{Colors.NC}")
    print(f"proxy = {config['privacy']['proxy']}\n")

    print(f"{Colors.PASTEL_PINK}{Colors.BOLD}[commands]{Colors.NC}\n")

    commands = config['commands']
    for command, settings in commands.items():
        print(f"  {Colors.PASTEL_ORANGE}[commands.{command}]{Colors.NC}")
        for setting, value in settings.items():
            print(f"{setting} = {value}")
        print() 


if __name__ == "__main__":
    app()

