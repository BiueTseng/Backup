#修改節點時，當然是要找到指定的節點
import xml.etree.ElementTree as ET
tree=ET.ElementTree(file="index.html")
root=tree.getroot()

#先找指定的節點
node=tree.find('body/table/tr[@name="tr2"]/td')
#再修改->屬性
node.set("bgcolor","#ffff00")

#修改-> 標籤間的文字
node.text="中文測試"

tree.write('test.html')
'''
<tag 屬性1='值' 屬性2='值'> 本文Text </tag>
修改屬性 : node.set("屬姓名","值")
修改本文 : node.text("本文")
'''

