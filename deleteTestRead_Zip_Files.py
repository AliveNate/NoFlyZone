
# First unzip the files in a new location so they arent compressed
# import zipfile
# with zipfile.ZipFile("D:\\Programming\\PythonProjects\\Battlescribe Replacement\\NoFlyZone\\Data\\Aeldari - Craftworlds.catz", 'r') as zip_ref:
#    zip_ref.extractall("D:\\Programming\\PythonProjects\\Battlescribe Replacement\\NoFlyZone\\Data\\Unzipped_Data")

# Then read the files in
# importing element tree
# under the alias of ET
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring

# Passing the path of the
# xml document to enable the
# parsing process
import os
cwd = os.getcwd()
targetDirectory = cwd + '\\Data\\Unzipped_Data\\Aeldari - Craftworlds.cat'
tree = ET.parse(targetDirectory)


# getting the parent tag of
# the xml document
root = tree.getroot()

for item in root:
    #print(item.get('id'))
    #print(item.text)
    '''
        {http://www.battlescribe.net/schema/catalogueSchema}catalogue
        {'id': '30b2-6f64-b85e-b4dc', 'name': 'Aeldari - Craftworlds', 'revision': '152', 'battleScribeVersion': '2.03', 'authorName': 'BSData Developers', 'authorContact': '@FarseerV @WindstormSCR', 'authorUrl': 'https://www.bsdata.net/contact', 'library': 'false', 'gameSystemId': '28ec-711c-d87f-3aeb', 'gameSystemRevision': '208'}
    '''
    #print(item.tag)
    '''
        {http://www.battlescribe.net/schema/catalogueSchema}publications
        {http://www.battlescribe.net/schema/catalogueSchema}profileTypes
        {http://www.battlescribe.net/schema/catalogueSchema}categoryEntries
    '''
    for child in item:
        #print(child)
        #print(child.attrib)
        #print(child.tag)
        print(child.attrib)
        for attribute in child:
            print(attribute.tag)
        #print(child.get('id'))
        #print(child.get('name'))
print("This is the tree:")
# print('---------------------------------------------------')

#print(root.tag)
#print(root.attrib)

'''
for thing in root:
    print(thing.tag, thing.attrib)
    for thing2 in thing:
        print(thing2.tag, thing2.attrib)
'''
