import click
from ..view import Cli, defuisearch as UI
from colorama import Fore, Style
from ..logic import GetCommand
@click.group()
def cmd():
    """OSTutor - OpenEuler Application Assistant."""
 
@cmd.command()

def getcom():
    gc = GetCommand()
    gc.get_command()

@cmd.command()

def fixcom():
    from ..logic import CommandFixer
    fixer = CommandFixer()
    fixer.fixcom()

# 查询指定指令信息，类型默认为user
@cmd.command()
@click.option('--admin', is_flag=True, help='Specify the query instruction type as admin, otherwise as user.')
@click.argument('instruction', nargs=1)
def query(admin, instruction):
    """Query detailed information about a specified instruction."""
    from ..logic import Query
    Query(admin, instruction)

# 查询指定指令信息，类型默认为user
@cmd.command()
@click.option('--web', is_flag=True, help='Search by the official networking model.')
@click.argument('keyword', nargs=-1)
def search(web, keyword):
    """Search by keyword."""
    if web:
        print(f"{'name':20}", "brief")
        from ..logic import HttpToolClient
        for i in HttpToolClient().model_search(' '.join(keyword)):
            print(f"{i['name']:20}", i["brief"])
    else:
        from ..logic import tfidf
        print(f"{'name':20}", "brief")
        for i in tfidf.search(' '.join(keyword))[:10]:
            print(f"{i[1]:20}", i[2])

@cmd.command()
def tui():
    """Start the user terminal ui."""
    UI()

@cmd.command()
def cli():
    """Command line retrieval."""
    Cli().Run()

## 终端开启指令
@cmd.command()
def terminal():
    """Open the terminal interface."""
    from ..view import Terminal
    Terminal().Run()

@cmd.command()
def rpmsexp():
    """Export the local RPM list to the current directory."""
    from ..data import Collection
    Collection().exportRpmList()


@cmd.command()
def install():
    """Do not differentially download the rpm package from the rpmsexport.txt file in the current directory."""
    from ..data import Collection
    Collection().downLoadRpmList()

@cmd.command()
def lrefresh():
    """Refresh the knowledge base locally."""
    from ..data import Collection
    Collection().collect()
    
@cmd.command()
@click.option('--user', is_flag=True, help='Query user instruction for which data does not exist')
@click.option('--admin', is_flag=True, help='Query administrator instruction for data that does not exist.')
@click.option('--all', is_flag=True, help='Query all instructions for non-existent data.')
def nodata(user, admin, all):
    """Search for local instructions without data."""
    from ..data import Collection
    nu, na = Collection().collectNoDataInsts()
    if user or all:
        print(Fore.MAGENTA + "user:")
        print(Fore.YELLOW + '\n'.join(nu), Style.RESET_ALL)
    if admin or all:
        print(Fore.MAGENTA + "admin:")
        print(Fore.YELLOW + '\n'.join(na)+ Style.RESET_ALL)

## 数据导入导出指令
@cmd.command()
@click.option('-e', is_flag=True, help='export data.')
@click.option('-i', is_flag=True, help='import data.')
@click.option('--local', is_flag=True, help='export or import locally.')
@click.option('--all', is_flag=True, help='export all data.')
@click.argument('arg', nargs=1, default='')
def data(e, i, local, all, arg):
    """Data export and import."""
    from ..logic import dataOptions
    dataOptions(e, i, local, all, arg)

## 知识库拉取
@cmd.command()
@click.option('--local', is_flag=True, help='import locally.')
@click.argument('arg', nargs=1, default='')
def pull(local, arg):
    """Data import."""
    from ..logic import dataOptions
    dataOptions(False, True, local, True, arg)

## 知识库推送
@cmd.command()
@click.option('--local', is_flag=True, help='exportlocally.')
@click.option('--all', is_flag=True, help='export all data.')
@click.argument('arg', nargs=1, default='')
def push(local, all, arg):
    """Data export."""
    from ..logic import dataOptions
    dataOptions(True, False, local, all, arg)

## 设置kimapikey
@cmd.command()
@click.argument('key', nargs=1)
def apikey(key):
    """Setting apikey."""
    from ..logic import cfg
    cfg.update('kimi_api_key', key)

## kimi 调用
@cmd.command()
@click.argument('args', nargs=-1)
def ask(args):
    from ..logic import Kimi
    if len(args) < 1:
        click.echo('Please enter requirements.')
        return
    insts = Kimi(' '.join(args))
    if len(insts) == 0:
        return
    # 询问用户是否执行这些命令
    if click.confirm(Fore.BLUE + 'Whether to run the following command?\n' + Fore.YELLOW + '\n'.join(insts) + Style.RESET_ALL):
        # 用户同意，执行命令
        import os
        print("********results********")
        for command in insts:
            # 使用 os.system 执行命令
            os.system(command)
        print(Fore.GREEN + "Complete! ✔" + Style.RESET_ALL)

@cmd.command()
def version():
    """Print the version of ostutor."""
    import subprocess
    try:
        result = subprocess.run(['pip', 'show', 'ostutor'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # 如果命令执行失败，打印错误信息
        print(f"Error: {e.stderr}")