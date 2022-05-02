
'''
This is just an example of what can be grabbed from the cat files.
'''
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring

import os
cwd = os.getcwd()
targetDirectory = cwd + '\\Data\\Unzipped_Data\\Aeldari - Craftworlds.cat'
tree = ET.parse(targetDirectory)
root = tree.getroot()

for item in root:
    #print(item.tag)
    '''
        {http://www.battlescribe.net/schema/catalogueSchema}publications
        {http://www.battlescribe.net/schema/catalogueSchema}profileTypes
        {http://www.battlescribe.net/schema/catalogueSchema}categoryEntries
    '''
    for child in item:
        print(child)
        '''<Element '{http://www.battlescribe.net/schema/catalogueSchema}publication' at 0x0000020B529572E0>
        <Element '{http://www.battlescribe.net/schema/catalogueSchema}profileType' at 0x0000020B529573D0>
        '''
#
        for attribute in child:
            #print(attribute.tag)
            ''' {http://www.battlescribe.net/schema/catalogueSchema}characteristicTypes
            {'id': 'fb5a-2f35-6253-b891', 'name': 'Faction: <Craftworld>', 'hidden': 'false'}
            {'id': '05e9-e880-b1fb-ce90', 'name': 'Faction: Aeldari', 'hidden': 'false'}
            '''
        #print(child.get('id'))      # 30b2-6f64-pubN137513
        #print(child.get('name'))    # Codex: Craftworlds
