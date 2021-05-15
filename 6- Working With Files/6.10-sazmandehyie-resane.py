import sys
import os 
from time import ctime

def copyfile(source_file:str, dest:str):
    with open(source_file, 'rb') as file:
        data = file.read()
        new_file_path = os.path.join(dest, os.path.basename(file.name))
        # open(new_file_path, 'x').close()
        with open(new_file_path, 'xb') as new_file:
            new_file.write(data)

def filetype(file:str, lower= True):
    # bname = os.path.basename(file)
    splited = file.split('.', 1)       
    
    if len(splited) == 1:
        return None
    else:
        if lower:
            splited[1] = splited[1].lower()
        return splited[1]


inputs = sys.argv
source_path, dest_path = inputs[1], inputs[2]
# source_path, dest_path = "E:\\New folder\\Algorithms and Data Structures Course", "E:\\New folder\\new"

pictures = ('jpg', 'jpeg', 'png')
videos = ('mp4', 'avi', '3gp', 'mpeg', 'mkv', 'wmv', 'mov')

if not os.path.exists(dest_path):
    os.mkdir(dest_path)
    
all_data = list(os.walk(source_path))

years = set()
for tup in all_data:
    for file in tup[2]:
        file_path = os.path.join(tup[0], file)
        file_year = ctime(os.path.getmtime(file_path))[-4:]
        year_path = os.path.join(dest_path, file_year)
        # if the year path doesn't exist in the destination path, then create it
        

        file_t = filetype(file)
        if file_t == None:
            continue
        
        if file_t in pictures:
            folder_type = 'photos'
        elif file_t in videos:
            folder_type = 'videos'
        else:
            continue
        
        if not file_year in years:
            os.mkdir(year_path)
            years.add(file_year)
        dest = os.path.join(year_path, folder_type)
        if not os.path.exists(dest):
            os.mkdir(dest)
        copyfile(file_path, dest)
        
        
            
        
        
# print('s;lgkaja.h'.split('.'))

# open('E:\\New folder\\new\\2021\\videos\\24-goli_land.txt', 'xb').close()