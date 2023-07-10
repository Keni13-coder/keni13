import os
from pathlib import Path
import shutil
# print(os.mkdir("D:\Codewars\it is prank\derik "))
# print(os.path.isdir("D:\Codewars\it is prank\derik\\test "))
# print(*os.walk('D:\Codewars\it is prank\Lesson_python'))
# Path("C:\it is prank\keni13\\tk\\tr\\pr").mkdir(parents=True)
# print(Path("C:\it is prank\keni13\iuui").is_dir())
# p = Path().cwd() /'C:\Program Files'
# print(p)
# print([x for (x,) in [[1],[2],[3]]])

def create_folders_from_list(folder_path, folder_names):
    for folder in folder_names:
        if not os.path.exists(f'{folder_path}\\{folder}'):
            os.mkdir(f'{folder_path}\\{folder}')
            
extensions = {

    'video': ['mp4', 'mov', 'avi', 'mkv', 'wmv', '3gp', '3g2', 'mpg', 'mpeg', 'm4v', 
              'h264', 'flv', 'rm', 'swf', 'vob'],

    'data': ['sql', 'sqlite', 'sqlite3', 'csv', 'dat', 'db', 'log', 'mdb', 'sav', 
             'tar', 'xml'],

    'audio': ['mp3', 'wav', 'ogg', 'flac', 'aif', 'mid', 'midi', 'mpa', 'wma', 'wpl',
              'cda'],

    'image': ['jpg', 'png', 'bmp', 'ai', 'psd', 'ico', 'jpeg', 'ps', 'svg', 'tif', 
              'tiff'],
    'text': ['pdf', 'txt', 'doc', 'docx', 'rtf', 'tex', 'wpd', 'odt'],
    
    'exe': ['exe'],
    }
            
# Path('Test_folder_file').mkdir()
# create_folders_from_list('Test_folder_file',extensions)
# for dir,folder,file in os.walk('D:\Codewars\it is prank\Test_folder_file'):
#     print(dir)
# shutil.rmtree('Test_folder_file')
# Path('Test_folder_file\\ainufierouvbrwwx.avi').rename('Test_folder_file\\лох.txt')
print('1'.zfill(2))