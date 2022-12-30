import shutil
import os
from pathlib import Path
from typing import List


# Ключи - названия папок. Значения - расширения файлов для каждой отдельной папки.
CATEGORIES = {
    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v',
              'h264', 'flv', 'rm', 'swf', 'vob'],
    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav',
             'tar', 'xml'],
    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
              'cda'],
    'images': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif',
              'tiff'],
    'archives': ['zip', 'rar', '7z', 'z', 'gz', 'rpm', 'arj', 'pkg', 'deb'],
    'documents': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],
    '3d': ['stl', 'obj', 'fbx', 'dae', '3ds', 'iges', 'step'],
    'presentation': ['pptx', 'ppt', 'pps', 'key', 'odp'],
    'spreadsheet': ['xlsx', 'xls', 'xlsm', 'ods'],
    'font': ['otf', 'ttf', 'fon', 'fnt'],
    'gif': ['gif'],
    'exe': ['exe'],
    'bat': ['bat'],
    'apk': ['apk']
}

path = input('Input folder path: ')

def main():
    create_folders_from_list(path, CATEGORIES)
    get_subfolder_paths(path)
    get_file_paths(path)
    sort_files(path)
    remove_empty_folders(path)


# Напишем функцию для создания папок из списка названий
def create_folders_from_list(folder_path, folder_names):
    os.mkdir(os.path.join(folder_path, 'unknowns'))
    for folder in folder_names:
        if not os.path.exists(os.path.join(folder_path, folder)):
            os.mkdir(os.path.join(folder_path, folder))

# для получения путей подпапок
def get_subfolder_paths(folder_path) -> list:
    subfolder_paths = [f.path for f in os.scandir(folder_path) if f.is_dir()]
    return subfolder_paths

# пути всех файлов в папке
def get_file_paths(folder_path) -> list:
    file_paths = [f.path for f in os.scandir(folder_path) if not f.is_dir()]
    return file_paths

# сортировка файлов
def sort_files(folder_path):
    file_paths = get_file_paths(folder_path)  # пути файлов
    file_path: os.path
    for file_path in Path(folder_path).glob('**/*'):
        if file_path.is_dir():
            continue
        moved = False
        file = Path(file_path)
        extension = file.suffix.replace('.', '').lower()
        file_name = file.name

        # распаковка архивов
        if extension in CATEGORIES['archives']:
            shutil.unpack_archive(file, os.path.join(folder_path, 'archives', file_name))
            continue

        # цикл внутри
        for category, extensions in CATEGORIES.items():
            if extension in extensions:
                print(f'Moving {file_path} in {category} folder\n')
                os.rename(file_path, os.path.join(path, category, file_name))
                moved = True
                break
        if not moved:
            file_destination = os.path.join(folder_path, 'unknowns')
            os.rename(file_path, os.path.join(file_destination, file_name))



# удаляем пустые папки
def remove_empty_folders(folder_path):
    subfolder_paths = get_subfolder_paths(folder_path)
    for p in subfolder_paths:
        if not os.listdir(p):
            print('Deleting empty folder:', p.split('\\')[-1], '\n')
            os.rmdir(p)


if __name__ == "__main__":
    main()

