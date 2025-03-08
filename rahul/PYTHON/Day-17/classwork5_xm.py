import xml.etree.ElementTree as ET
 
# Create the root element
root = ET.Element("person")
 
# Create child elements
name = ET.SubElement(root, "name")
name.text = "Alice"
 
age = ET.SubElement(root, "age")
age.text = "25"
 
city = ET.SubElement(root, "city")
city.text = "New York"
 
# Convert the tree to a string
tree = ET.ElementTree(root)
with open("data.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)