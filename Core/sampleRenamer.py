

import os
import os.path as path
import DocManager.DocManager as dm


dir_path = '/home/yangzheng/testData/hand'
name_width=6
doc = dm.DocManager(_docFilter=['.jpg'])
files_list = doc.GetFileList(dir_path)
files_list.sort()
n_frame = 0
temp_file_name = 'temp_temp_temp.file'

for it in files_list:
    frame_name = str(n_frame)
    if len(frame_name) < name_width:
        frame_name = (name_width - len(frame_name)) * '0' + frame_name+'.jpg'
    os.rename(path.join(dir_path, it),path.join(dir_path, temp_file_name))
    os.rename(path.join(dir_path, temp_file_name), path.join(dir_path, frame_name))
    n_frame=n_frame+1
print 'tall number of frames is: ', n_frame