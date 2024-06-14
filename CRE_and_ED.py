import os
import difflib

def calculate_cer_and_ed(ocr_text, gt_text):
    edit_distance = difflib.ndiff(ocr_text, gt_text)
    ed = sum(1 for diff in edit_distance if diff.startswith('-') or diff.startswith('+'))
    cer = ed / max(len(gt_text), 1)
    return cer, ed

# 设置OCR结果和ground truth的目录路径
ocr_results_dir = 'H:\PythonBaseH\SURF23\\benchmarkDatasets_OCR_result'
gt_dir = 'H:\PythonBaseH\SURF23\\benchmarkDatasets_OCR_result\gt'

def process(ocr_results_dir, gt_dir):
    total_cer = 0
    total_ed = 0
    valid_file_count = 0  # 仅计算CER小于1的文件数

    # 遍历OCR结果文件
    for filename in os.listdir(ocr_results_dir):
        ocr_file_path = os.path.join(ocr_results_dir, filename)
        gt_filename = filename.split('_')[0] + '.txt'  # 假设GT文件名与OCR结果对应
        gt_file_path = os.path.join(gt_dir, gt_filename)

        if not os.path.exists(gt_file_path):
            print(f"Ground truth for {filename} not found.")
            continue

        with open(ocr_file_path, 'r', encoding='utf-8') as ocr_file, open(gt_file_path, 'r', encoding='utf-8') as gt_file:
            ocr_text = ocr_file.read()
            gt_text = gt_file.read()

        cer, ed = calculate_cer_and_ed(ocr_text, gt_text)

        if cer < 1:
            total_cer += cer
            total_ed += ed
            valid_file_count += 1

        print(f'File: {filename}, CER: {cer:.4f}, ED: {ed}')

    # 计算平均CER和ED，仅考虑CER小于1的情况
    average_cer = total_cer / valid_file_count if valid_file_count else 0
    average_ed = total_ed / valid_file_count if valid_file_count else 0

    # 准备写入文件的数据
    results_dir_part = os.path.basename(ocr_results_dir)
    results_text = f'{results_dir_part}\nAverage CER (valid cases only): {average_cer:.4f}, Average ED (valid cases only): {average_ed}\n'

    # 写入文件
    results_file_path = 'CER&ED_benchmark.txt'
    with open(results_file_path, 'a', encoding='utf-8') as results_file:
        results_file.write(results_text)

    print('平均CER和ED（仅考虑有效案例）已经保存到文件中。')

for folder in os.listdir(ocr_results_dir):
    if os.path.isdir(os.path.join(ocr_results_dir, folder)):  # 确保是目录
        ocr_results_subdir = os.path.join(ocr_results_dir, folder)
        process(ocr_results_subdir, gt_dir)
