import os
import sys
import re

# 定义媒体文件扩展名
MEDIA_EXTENSIONS = {
    '.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm',
    '.mp3', '.wav', '.flac', '.m4a', '.aac',
    '.srt', '.ass', '.ssa'
}

def load_prefixes(file_path):
    prefixes = {}
    if not os.path.exists(file_path):
        print(f"Error: Prefixes file not found at {file_path}")
        sys.exit(1)

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split('，')
            if len(parts) == 2:
                prefix, replacement = parts
                prefixes[prefix] = replacement
    return prefixes

def is_media_file(filename):
    return os.path.splitext(filename)[1].lower() in MEDIA_EXTENSIONS

def rename_files_in_directory(directory, prefixes_to_remove):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path) and is_media_file(filename):
            new_filename = filename
            for prefix, replacement in prefixes_to_remove.items():
                new_filename = re.sub(re.escape(prefix), replacement, new_filename)
            new_filename = re.sub(r'\[(\d+)\]', r' - \1', new_filename)
            new_file_path = os.path.join(directory, new_filename)
            if new_file_path != file_path:
                print(f'Renaming {filename} to {new_filename}')
                try:
                    os.rename(file_path, new_file_path)
                except OSError as e:
                    print(f"Error renaming {file_path} to {new_file_path}: {e}")

# 获取脚本所在目录的路径
script_dir = os.path.dirname(os.path.abspath(__file__))
prefixes_file_path = os.path.join(script_dir, "prefixes.txt")

# 获取命令行参数
if len(sys.argv) < 2:
    print("Usage: python rename_script.py <directory_path>")
    sys.exit(1)

directory_path = sys.argv[1]

# 加载前缀规则并处理目录
prefixes_to_remove = load_prefixes(prefixes_file_path)
rename_files_in_directory(directory_path, prefixes_to_remove)
