# @Author: Yiyuan HE 
# @Date: 2023-12-09 16:01:43 
# @Last Modified by:   Yiyuan HE 
# @Last Modified time: 2023-12-09 16:01:43 
import threading
import subprocess
import time



# 定义 curl 命令
curl_command1 = 'curl -X POST "http://172.22.16.1:8000" -H \'Content-Type: application/json\' -d \'{"prompt": "你好", "history": []}\''
curl_command2 = 'curl -X POST "http://172.22.16.1:8001" -H \'Content-Type: application/json\' -d \'{"prompt": "hello", "history": []}\''


def run(curl_command,thread_name):
    
    print("thread_name:", thread_name,"start time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# 使用 subprocess.run 执行命令
    result = subprocess.run(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# 打印执行结果

    
    # print("Exit Code:", result.returncode)
    # print("STDOUT:")
    print(result.stdout)
    print("thread_name:", thread_name,"end time:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

thread1 = threading.Thread(target=run, args=(curl_command1, "thread1"))
thread2 = threading.Thread(target=run, args=(curl_command2, "thread2"))


thread1.start()
thread2.start()


