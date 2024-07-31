import os
import json
import subprocess


class GetCommand:
    def __init__(self):
        self.history_file = os.path.expanduser("~/.bash_history")
        self.log_file = "command_log.log"

    def get_last_command(self):
        """从历史记录中获取最后一条命令"""
        with open(self.history_file, 'r') as f:
            history = f.readlines()
            if history:
                return history[-2].strip()
            else:
                return None

    def execute_and_get_result(self, command):
        """执行命令并返回结果"""
        try:
            result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            status = "SUCCEED"
        except subprocess.CalledProcessError as e:
            result = e.output
            status = "FAILED"
        
        # 将结果转换为字符串
        result = result.decode().strip()
        return result, status

    def log_command(self, command, result, status):
        """将命令、结果和状态写入日志文件"""
        entry = {"Command": command, "Result": result, "Status": status}
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(entry) + '\n')

    def get_command(self):
        """获取最后一条命令，执行它并记录到日志"""
        os.system('history -a')
        last_command = self.get_last_command()
        if not last_command:
            print("No commands in history.")
            return

        result, status = self.execute_and_get_result(last_command)
        self.log_command(last_command, result, status)

        if status == "FAILED":
            return last_command,result
            print(f"Failed command: {last_command}")
        elif status == "SUCCEED":
            return None,''
            print(f"Command executed successfully: {last_command}")


