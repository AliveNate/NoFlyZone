

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
#Element tree represents the while XML doc
#Element represents a single node on the tree per https://docs.python.org/3/library/xml.etree.elementtree.html

 
# getting the parent tag of
# the xml document
root = tree.getroot()
 
# printing the root (parent) tag
# of the xml document
p = tostring(root)
print("This is the tree:")
#print(p)


#for thing in root.findall('.//entryLink'):
#	print(thing.tag, thing.attrib)

#print('---------------------------------------------------')
#print('---------------------------------------------------')
#print('---------------------------------------------------')
#print('---------------------------------------------------')
#print('---------------------------------------------------')

#for thing in root.iter('entryLinks'):
#	print(thing.tag, thing.attrib)
	#for thing2 in thing.findall('entryLink'):
	#	print(thing2.tag, thing2.attrib)

for thing in root:
	print(thing.tag, thing.attrib)
	for thing2 in thing:
		print(thing2.tag, thing2.attrib)


#for thing in root.findall('Wave Serpent'):
#	print(thing.tag, thing.attrib)
#print('This is the root:')
#print(root)
 
# printing the attributes of the
# first tag from the parent
#Print("Root 0 attribute")
#print(root[0].attrib)
 
