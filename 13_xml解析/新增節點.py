import xml.etree.ElementTree as ET
tree=ET.ElementTree(file="index.html")
root=tree.getroot()
#先找指定的節點
table=tree.find("body/table")
#產生一個新的節點，並附於node之下
tr=ET.SubElement(table,"tr")
td=ET.SubElement(tr,"td")
td.set("colspan","4")
td.text="新增的點"
tree.write("test1.html")