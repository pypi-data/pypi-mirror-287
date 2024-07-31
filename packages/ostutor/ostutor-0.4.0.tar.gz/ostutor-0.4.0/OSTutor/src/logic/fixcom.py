from ..dao import InstDao
import subprocess
import re
from .getlastcommand import GetCommand
from .kimi import Kimi_fixcom
class CommandFixer:
    def __init__(self) -> None:
        pass

    def fixcom(self):
        fixer = GetCommand() 
        command, result = fixer.get_command()
        print(command)
        if command is not None:
            self.exact_search(command, result)
            return
        else:
            print("Command execution succeeded!")
            return

    def exact_search(self, command, result):
        # 精确搜索命令
        command_name, options, arguments = self.parse_complex_command(command)
        print(result)
        print(command_name, options, arguments)
        inst = InstDao()
        data = inst.SelectExistByName(command_name)
        print(data)
        if data and data.exist == 1:
            # 如果存在，则传递给Kimi大模型进行错误修复
            fixed_command = self.repair_command(command, result)
            if fixed_command:
                print(f"Fixed command: {fixed_command}")
            else:
                print("No fix available.")
        elif data and data.exist == 0:
            # 如果不存在，则询问用户是否下载RPM包
            self.ask_user_to_download(data.rpm)
        else:
            print(f"Command '{command_name}' not found in the database.")

    def parse_complex_command(self, command):
        parts = re.findall(r"[\w-]+(?:=[\w-]+)?|\"[^\"]*\"|\'[^\']*\'", command)

        command_name = parts[0]
        options = []
        arguments = []

        i = 1
        while i < len(parts):
            part = parts[i]

            if part.startswith('-'):
                # 处理短选项和长选项
                if '=' in part:
                    option, value = part.split('=', 1)
                    options.append(option)
                    arguments.append(value)
                else:
                    options.append(part)

                    # 如果下一个部分不是选项，则视为当前选项的参数
                    if i + 1 < len(parts) and not parts[i+1].startswith('-'):
                        arguments.append(parts[i+1])
                        i += 1
            else:
                arguments.append(part)

            i += 1

        return command_name, options, arguments

    def repair_command(self, command, result):
        # 这里是使用Kimi大模型进行修复的逻辑
        # 实际的修复逻辑应该在这里实现
        # 调用Kimi大模型
        fixed_command = self.call_kimi_model(command, result)
        print("kimi返回结果:",fixed_command)
        return
        if fixed_command:
            print("Error repaired successfully.")
        return fixed_command

    def call_kimi_model(self, command, result):
        # 假设这是调用Kimi大模型的函数
        # 这里仅作模拟，实际应用中需要替换为真实的调用逻辑
        # 模拟返回一个修复后的命令
        user_input="指令为"+command+"报错为"+result 
        Kimi_fixcom(user_input)
        return
        if command.startswith('gcc'):
            return f"gcc -v {command}"
        elif command.startswith('ls'):
            return f"ls -la {command}"
        # 如果无法修复，返回None
        return None

    def ask_user_to_download(self, rpm):
        # 询问用户是否下载RPM包
        response = input(f"The rpm '{rpm}' is not installed. Download it? [yes/no]: ")
        if response.lower() == 'yes':
            self.download_rpm_package(rpm)
        elif response.lower() == 'no':
            print("Operation cancelled.")
        else:
            print("Invalid input. Operation cancelled.")

    def download_rpm_package(self, rpm):
        # 实际下载RPM包的过程
        try:
            # 使用yum或dnf下载RPM包
            # 这里假设使用dnf作为包管理器
            subprocess.run(['sudo', 'dnf', 'install', '-y', rpm], check=True)
            print(f"{rpm} has been installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Failed to install {rpm}: {e}")
        except Exception as e:
            print(f"An error occurred: {e}")
