import subprocess
import sys

def execute_com():
    # 执行命令并将输出写入一个文件
    with open('output.log', 'w') as f:
        subprocess.check_call([sys.executable, "-c", "print('It is running')"], stdout=f, stderr=f)

    # 检查 Python 版本
    with open('version.log', 'w') as f:
        subprocess.check_call([sys.executable, "--version"], stdout=f, stderr=f)
