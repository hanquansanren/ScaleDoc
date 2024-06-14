import os
import subprocess



def process(images_dir, output_dir):
    # 如果不存在output_dir目录，则创建
    os.makedirs(output_dir, exist_ok=True)

    # 设置Tesseract执行文件所在的目录
    tesseract_dir = 'H:\\Tesseract'

    # 遍历images_dir目录下的所有文件
    for image_name in os.listdir(images_dir):
        # 构建完整的图片路径
        image_path = os.path.join(images_dir, image_name)
        # 构建输出基础名，不包含扩展名
        output_base = os.path.splitext(os.path.join(output_dir, image_name))[0]
        # 构建命令行命令
        command = f'tesseract.exe "{image_path}" "{output_base}" -l eng'
        # 执行命令，设置cwd参数为Tesseract的安装目录
        subprocess.run(command, shell=True, cwd=tesseract_dir)
        print(f'已处理图片：{image_name}')

    print('处理完成')

if __name__ == '__main__':
    # 设置图片所在的目录路径
    images_dir = 'H:\PythonBaseH\SURF23\\benchmarkDatasets_OCR'
    # 设置输出目录路径
    output_dir = 'H:\PythonBaseH\SURF23\\benchmarkDatasets_OCR_result'

    for dir in os.listdir(images_dir):
        print(f'正在处理目录：{dir}')
        process(os.path.join(images_dir, dir), os.path.join(output_dir, dir))