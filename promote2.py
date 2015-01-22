import xml.etree.ElementTree as ET
import uuid

namespace = 'http://www.innotek.de/VirtualBox-settings'
tree = ET.parse('403_templ.vbox')
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
	print hdd_uuid
	new_uid = uuid.uuid1()
	new_uid = str(new_uid)
	uuid_mapping[hdd_uuid] = '{' + new_uid + '}'
	hdd.set('uuid', '{' + new_uid + '}')

#for mapping in uuid_mapping.keys():
#	print mapping, " -> ", uuid_mapping[mapping]

for elem in root.iter():
	if elem.tag == '{' + namespace + '}Image':
		print 'Found attached'
		att_uuid = elem.get('uuid')
		print 'uuid: ', att_uuid
		if att_uuid in uuid_mapping:
			print 'Changing ', att_uuid, ' to ', uuid_mapping[att_uuid]
			elem.set('uuid', uuid_mapping[att_uuid])

ET.register_namespace('', namespace)
tree.write('403_templ.vbox')
