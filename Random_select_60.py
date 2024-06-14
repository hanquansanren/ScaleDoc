import os
import shutil
import random


def copy_selected_images(folder_A, folder_B, num_files=60):
    """
    从文件夹A中随机选择指定数量的图片并复制到文件夹B，同时记录选中的图片名称（无视后缀名）。
    """
    os.makedirs(folder_B, exist_ok=True)

    files_A = [f for f in os.listdir(folder_A) if os.path.isfile(os.path.join(folder_A, f))]
    selected_files = random.sample(files_A, num_files)

    for file_name in selected_files:
        shutil.copy2(os.path.join(folder_A, file_name), folder_B)
        # 仅记录文件名，不包括扩展名
        base_name = os.path.splitext(file_name)[0]
        with open('selected_images_benchmark.txt', 'a') as f:
            f.write(base_name + '\n')

    print('图片已经从A复制到B，并记录选中的图片基本名称。')


def find_file_by_name_without_extension(folder, base_name):
    """
    在给定的文件夹中寻找具有指定基本名称但可能具有任何扩展名的文件。
    """
    for file_name in os.listdir(folder):
        if base_name == os.path.splitext(file_name)[0]:
            return file_name
    return None


def copy_images_based_on_list(folder_C, folder_D, list_file='selected_images.txt'):
    """
    根据记录的图片基本名称，从文件夹C复制到D（无视后缀名）。
    """
    os.makedirs(folder_D, exist_ok=True)

    with open(list_file, 'r') as f:
        base_names = [line.strip() for line in f.readlines()]

    for base_name in base_names:
        file_name = find_file_by_name_without_extension(folder_C, base_name)
        if file_name:
            shutil.copy2(os.path.join(folder_C, file_name), folder_D)

    print('根据记录从C复制到D，无视文件后缀名。')

# 示例调用
folder_A = 'H:\PythonBaseH\SURF23\\benchmarkDatasets\ours_result'
folder_B = 'H:\PythonBaseH\SURF23\\benchmarkDatasets_OCR\ours_result'
folder_C = 'H:\PythonBaseH\SURF23\Datasets\\raw_DDCP_result'
folder_D = 'H:\PythonBaseH\SURF23\Datasets_OCR\\raw_DDCP_result_OCR'

# 第一步：复制图片并记录
# copy_selected_images(folder_A, folder_B)

# 第二步：根据记录复制图片，这一步可以多次调用
# copy_images_based_on_list(folder_C, folder_D)


# 根据selected_images.txt文件中的文件名，提取对应的gt文件，也将其复制到新的文件夹中
# 例如，selected_images.txt中有文件名为"16_1 copy"，则将"16.png"复制到新的文件夹中
def copy_gt_files(folder_E, folder_F, list_file='selected_images.txt'):
    """
    根据记录的图片基本名称，从文件夹E复制到F（无视后缀名）。
    """
    os.makedirs(folder_F, exist_ok=True)

    with open(list_file, 'r') as f:
        base_names = [line.strip() for line in f.readlines()]

    for base_name in base_names:
        ID = base_name.split('_')[0]
        print(ID)
        file_name = find_file_by_name_without_extension(folder_E, ID)
        if file_name:
            shutil.copy2(os.path.join(folder_E, file_name), folder_F)

    print('根据记录从E复制到F，无视文件后缀名。')


copy_gt_files('H:\PythonBaseH\SURF23\\benchmarkDatasets\gt', 'H:\PythonBaseH\SURF23\\benchmarkDatasets_OCR\gt')