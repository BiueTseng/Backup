'''
DOM(Document Object Model) : 將XML解析成一顆樹, 效能差
SAX(Simple API for XML) : 使用事件驅動模型, 效能好, 佔用記憶体少. 但不方便使用
ElementTree(元素樹) : 為上面二個的綜合体, 方便使用, 且效能跟SAX一樣, 且不佔太多的記憶体.
'''

import xml.etree.ElementTree as ET
tree=ET.ElementTree(file="index.html")
root=tree.getroot()
# print(root.tag,root.attrib)
# #<html> , <table> 標籤, tag "<>Diamond"
# #root 包含自己之外，還包含下一層的tag
# for i  in range(len(root)):
#     print(root[i].tag,root[i].attrib)
# for node in root.iter():
#     print(node.tag,node.attrib)
#xpath :使用絕對路徑，由根開始指定要走的節點 body/table
node=tree.find('body/table/tr') #tree.find -> 找第一個tr，傳回的是單一節點
print(node.tag,node.attrib)
#print(type(node))
#若要找量個以上咧
#tree.iterfind-> 搜尋table下所有的tr，並以list傳回
for node in tree.iterfind('body/table/tr'): 
    print(node.tag,node.attrib)