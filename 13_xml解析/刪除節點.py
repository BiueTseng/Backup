import xml.etree.ElementTree as ET
tree=ET.ElementTree(file="index.html")
root=tree.getroot()
#先找到老爸
table=tree.find('body/table')
#再找到要刪的點
tr=tree.find('body/table/tr[@name="tr2"]')
#由老爸刪除節點
table.remove(tr)
tree.write("text2.html")