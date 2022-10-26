import xml.etree.ElementTree as ET
html=ET.Element("html")
head=ET.Element("head")
#head=ET.SubElement(html, "head")
title=ET.SubElement( head,"title")
title.text="YO~~~~"
body=ET.Element("body")
p=ET.SubElement(body,"p")
p.set("align","center")
p.text="123哈哈哈"
html.extend((head,body))
#tree=ET.ElementTree(html)
#tree.write("test3.html")

from xml.dom import minidom
xmlstr=minidom.parseString(ET.tostring(html)).toprettyxml(indent="   ")
with open("test3_2.html" ,"w") as f:
    f.write(xmlstr)




