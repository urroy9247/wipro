import xml.etree.ElementTree as ET
 
# Read and parse the XML file
tree = ET.parse("data.xml")
root = tree.getroot()
print(root)
# Extract data
for child in root:
    print(f"{child.tag}: {child.text}")