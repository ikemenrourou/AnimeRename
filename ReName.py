import os
import sys
import re

def load_prefixes(file_path):
    prefixes = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 去除行末的换行符，并拆分为前缀和替换内容
            parts = line.strip().split('，')
            if len(parts) == 2:
                prefix, replacement = parts
                prefixes[prefix] = replacement
    return prefixes

def rename_files_in_directory(directory, prefixes_to_remove):
    # 遍历指定目录下的所有文件
    for filename in os.listdir(directory):
        # 文件的完整路径
        file_path = os.path.join(directory, filename)
        
        # 检查文件是否是普通文件
        if os.path.isfile(file_path):
            # 初始新文件名为原文件名
            new_filename = filename
            
            # 对每个前缀进行检查和处理
            for prefix, replacement in prefixes_to_remove.items():
                new_filename = re.sub(re.escape(prefix), replacement, new_filename)
            
            # 使用正则表达式查找和替换集数格式
            new_filename = re.sub(r'\[(\d+)\]', r' - \1', new_filename)
            
            # 新文件的完整路径
            new_file_path = os.path.join(directory, new_filename)
            
            # 打印信息，确认重命名操作
            if new_file_path != file_path:
                print(f'Renaming {filename} to {new_filename}')
                
                # 重命名文件
                os.rename(file_path, new_file_path)

# 获取命令行参数，即qbittorrent传递的目录路径
if len(sys.argv) < 2:
    print("Usage: python rename_script.py <directory_path>")
    sys.exit(1)

directory_path = sys.argv[1]

# 从指定路径加载前缀替换规则
prefixes_file_path = "P:\\QB重命名代码\\成品\\prefixes.txt"
prefixes_to_remove = load_prefixes(prefixes_file_path)

# 调用函数并指定要处理的目录路径
rename_files_in_directory(directory_path, prefixes_to_remove)
