import os

def cle_logs():
    # 指定要删除的文件
    log_files = ['output.log', 'version.log']

    # 遍历文件列表并删除每个文件
    for log_file in log_files:
        if os.path.exists(log_file):
            os.remove(log_file)


