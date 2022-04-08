

#First unzip the files in a new location so they arent compressed
#import zipfile
#with zipfile.ZipFile("D:\\Programming\\PythonProjects\\Battlescribe Replacement\\NoFlyZone\\Data\\Aeldari - Craftworlds.catz", 'r') as zip_ref:
#    zip_ref.extractall("D:\\Programming\\PythonProjects\\Battlescribe Replacement\\NoFlyZone\\Data\\Unzipped_Data")

#Then read the files in
# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring
 
# Passing the path of the
# xml document to enable the
# parsing process
tree = ET.parse('D:\\Programming\\PythonProjects\\Battlescribe Replacement\\NoFlyZone\\Data\\Unzipped_Data\\Aeldari - Craftworlds.cat')
#element = ET.xml(tree)
#ET.indent(element)
#print(ET.tostring(element, encoding='unicode'))
 
# getting the parent tag of
# the xml document
root = tree.getroot()
 
# printing the root (parent) tag
# of the xml document, along with
# its memory location

p = tostring(root)
print("This is the tree:")
print(p)
#print('This is the root:')
#print(root)
 
# printing the attributes of the
# first tag from the parent
#Print("Root 0 attribute")
#print(root[0].attrib)
 
