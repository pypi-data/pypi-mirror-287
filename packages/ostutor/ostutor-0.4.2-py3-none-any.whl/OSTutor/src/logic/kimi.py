from openai import OpenAI
from .config import cfg
from colorama import Fore, Style

prompt = """
你是openeuler系统上的应用助手，你的任务是帮助用户在openEuler操作系统上实现特定的需求。
当用户提出一个需求时，你需要生成一系列的命令行指令，这些指令将帮助用户在openEuler系统上完成所需的任务。
请确保你的指令准确无误，并且完全兼容openEuler操作系统。不要输出除指令外的内容。不同指令用换行符分隔开。
请使用尽可能少，尽可能常见的指令来实现用户需求，并确保所有指令都是openeuler系统上标准可用的。
现在，请准备接收用户需求并输出相应的指令集。当用户需要写入内容时，请使用echo指令。不要生成任何注释。

示例需求：用户想要在openEuler系统上创建一个名为ostutor的文件，并向其中写入数字666。

你返回的指令可能是：
    touch ostutor
    echo "666" > ostutor
你返回的指令不可能是
    # 首先创建一个文件
    touch ostutor 
    # 然后向文件中写入内容
    echo "666" > ostutor
"""

def Kimi(user_input):
    if user_input == "":
        return ""
    kimi_api_key = cfg.get("kimi_api_key")
    if not kimi_api_key:
        set_kimi_api_key()
        kimi_api_key = cfg.get("kimi_api_key")
    try:
        client = OpenAI(
            api_key = kimi_api_key,
            base_url = "https://api.moonshot.cn/v1",
        )
        
        completion = client.chat.completions.create(
            model = "moonshot-v1-8k",
            messages = [
                {"role": "system", "content": prompt, "partial": True},
                {"role": "user", "content": user_input}
            ],
            temperature = 0.3,
        )
        # 去除注释, 获取指令信息
        isnts = completion.choices[0].message.content.split('\n')
        isnts = [i for i in isnts if not i.startswith('```') and not i.startswith('#')]
        return isnts
    
    except Exception as e:
        print(Fore.RED + 'Please enter the correct path.' + Style.RESET_ALL)
    return ""

def Kimi_fixcom(user_input):
    if user_input == "":
        return ""
    prompt = """
    
    你是一个指令修复助手，需要根据用户输入的指令和指令执行后的报错来修改用户的指令，并返回正确指令给用户。
    要求返回的格式是原来的格式加上一些可能得修复后的指令。当接受一个错误时，你需要修复生成一系列的命令行指令，
    这些指令将帮助用户在openEuler系统上完成所需的任务。
    请确保你的指令准确无误，并且完全兼容openEuler操作系统。不要输出除指令外的内容。不同指令用换行符分隔开。
    请使用尽可能少，尽可能常见的指令来实现用户需求，并确保所有指令都是openeuler系统上标准可用的。
    现在，请准备接收用户需求并输出相应的指令集。
    """
    # 示例：用户传入了指令“gcc”和报错“gcc: \u81f4\u547d\u9519\u8bef\uff1a\u6ca1\u6709\u8f93\u5165\u6587\u4ef6\n\u7f16\u8bd1\u4e2d\u65ad\u3002”
    
    # # 你返回的指令可能是：
    # # gcc -c
    # # gcc -i 

    
    
    kimi_api_key = cfg.get("kimi_api_key")
    if not kimi_api_key:
        set_kimi_api_key()
        kimi_api_key = cfg.get("kimi_api_key")
    try:
        client = OpenAI(
            api_key = kimi_api_key,
            base_url = "https://api.moonshot.cn/v1",
        )
        
        completion = client.chat.completions.create(
            model = "moonshot-v1-8k",
            messages = [
                {"role": "system", "content": prompt, "partial": True},
                {"role": "user", "content": user_input}
            ],
            temperature = 0.3,
        )
        print(completion)
        # # 去除注释, 获取指令信息
        # isnts = completion.choices[0].message.content.split('\n')
        # isnts = [i for i in isnts if not i.startswith('```') and not i.startswith('#')]
        # return isnts
        return ""
    except Exception as e:
        print(Fore.RED + 'Please enter the correct path.' + Style.RESET_ALL)
    return ""


def set_kimi_api_key(api_key=None):
    if not api_key:
        import click
        print("No api key? You can get it at https://platform.moonshot.cn/console/api-keys")
        api_key = click.prompt("Please enter kimi api key")
    cfg.add("kimi_api_key", api_key)