import os
import shutil #copy的 package
from datetime import datetime
path='D:/生物/動物/人類'
target='e:/test'
files = os.listdir(path)
#tree =  os.walk(path)
for file in files:
    print(file)
    abs_path=os.path.join(path, file)
    abs_target=os.path.join(target, file)
    print(abs_path,abs_target)
    shutil.copyfile(abs_path, abs_target)

# for root,subdirs,files in tree:
#     #print(root)
#     shutil.copyfile(root,target)
