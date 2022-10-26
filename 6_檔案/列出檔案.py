import os
# path="D:\\3- 遊戲"
# file=os.listdir(path)
# for file in file:
#     print(file)
#列出子目錄
path = "D:\\3- 遊戲"
tree =os.walk(path)
# print(type(tree)) -> generator
# dirs格式[當前目錄絕對路徑，[當前目錄下的子目錄]，[當前目錄下的檔案]]
#for dirs in tree:
#    print(dirs)

#把所有的目錄印出
#for root,subdirs,files in tree:
#    print(root)
#把所有檔案列出
count = 0
for root,subdirs,files in tree:
    for file in files:
        file_lower=file.lower()
        if file_lower.endswith(".jpg") or file_lower.endswith("png"):
            count+=1
            # print(os.path.join(root,file))
            abs = os.path.join(root,file)
            #print(abs)
            #print(os.path.dirname(abs), os.path.basename(abs))
            print(os.path.basename(abs))
print(f'總共有{count:,d}張圖片)')