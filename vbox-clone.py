#!/usr/local/bin/python

import xml.etree.ElementTree as ET
import uuid
import sys
import os.path
import subprocess
import re

if len(sys.argv) < 2:
	sys.exit('usage: vbox-clone.py [machine_file]')

vboxname = sys.argv[1]
if not(os.path.isfile(vboxname)):
	sys.exit("Wrong filename")


namespace = 'http://www.innotek.de/VirtualBox-settings'
tree = ET.parse(vboxname)
root = tree.getroot()
machine = root[0]

# machine uuid
print machine.get('uuid'), "\n"
new_uuid = uuid.uuid1()

new_uuid_str = str(new_uuid)
print new_uuid_str, "\n"
machine.set('uuid', '{' + str(new_uuid) + '}')

# media uuid
uuid_mapping = {};
for hdd in root.iter('{' + namespace + '}HardDisk'):
	print hdd.tag, hdd.attrib

	hdd_uuid = hdd.get('uuid')
	hdd_path = hdd.get('location')
	print hdd_uuid
	print hdd_path

	new_uid_vbox_str = subprocess.check_output(['VBoxManage', 'internalcommands', 'sethduuid', hdd_path])
	print new_uid_vbox_str
	matchObj = re.match( r'^UUID changed to: (.*)$', new_uid_vbox_str)
	new_uid_vbox = ''
	if matchObj:
		print matchObj.group(1)
		new_uid_vbox = matchObj.group(1)
	else:
		raise Exception("Wrong hdd uuid")

	uuid_mapping[hdd_uuid] = '{' + new_uid_vbox + '}'
	hdd.set('uuid', '{' + new_uid_vbox + '}')

for elem in root.iter():
	if elem.tag == '{' + namespace + '}Image':
		print 'Found attached'
		att_uuid = elem.get('uuid')
		print 'uuid: ', att_uuid
		if att_uuid in uuid_mapping:
			print 'Changing ', att_uuid, ' to ', uuid_mapping[att_uuid]
			elem.set('uuid', uuid_mapping[att_uuid])

ET.register_namespace('', namespace)
tree.write(vboxname)
