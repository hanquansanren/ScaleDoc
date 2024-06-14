import os
import re

def preprocess_text(text):
    """
    预处理文本：去除空格、换行、标点符号，并转换为小写。
    """
    # 去除空格和换行符
    text = text.replace(" ", "").replace("\n", "")
    # 去除标点符号
    text = re.sub(r'[^\w\s]', '', text)
    # 转换为小写
    text = text.lower()
    return text

def preprocess_files_in_directory(directory):
    """
    遍历指定目录及其子目录下的所有txt文件，并进行预处理。
    """
    for root, dirs, files in os.walk(directory):
        print(f"Processing files in {root}")

        for file in files:
            print(f"Processing {dirs}")
            print(f"Processing {file}")
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                # 预处理文本内容
                processed_content = preprocess_text(content)
                # 重写文件
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(processed_content)
                print(f"Processed {file_path}")

# 设置OCR结果目录路径
ocr_results_dir = 'H:\PythonBaseH\SURF23\OCR_result'
# 对指定目录下的文件进行预处理
preprocess_files_in_directory(ocr_results_dir)

print("所有文件预处理完成。")
