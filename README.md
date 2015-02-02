# vbox-clone

vbox-clone.py is a simple script that helps in cloning VirtualBox VMs. It is useful in cases when you copy the VMs manually, rather than using VirtualBox 'Clone VM' mechanism. As an example, when you use ZFS as a filesystem and would like to use ZFS's snapshot/clone to copy the VMs. 

### What the script does
The script accepts the VirtualBox VM machine file (typically it has .vbox extension), which in fact is an XML file. The entities, that make each machine and its media (like virtual hdd's) unique to VirtualBox, are called UUIDs. The script parses the the machine file and changes the UUIDs of machine and media. Since the media UUIDs are stored in media files too, the script launches VBoxManage tool to change this UUIDs and modifies the machine file accordingly.

### Installation
No special installation is needed for the script. You are able to run it from any path, supplying the Vbox machine path.

### Requirements
1. Python 2.7.9
2. VirtualBox (actually, just **vboxmanage** tool from VirtualBox package is needed)

### Usage
```sh
$ python vbox-clone.py [-h] [-n NAME] [-f] machine
```
Typically, vbox-clone.py will save the original VM file adding the .orig extension to it in the machine directory. You can skip saving the backup with the **-f** key.

vbox-clone.py is able to change the machine name too, it could be done with **-n** key.

### Author
[Eugene Khudiakov](https://github.com/khudyakoff)



