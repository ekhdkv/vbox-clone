# vbox-clone
This is an external tool to clone VirtualBox virtual machines. I don't like using the native vbox clone mechanism, and currently my host machine is FreeBSD with ZFS. So I use zfs-snapshots for VMs. This brings problems making a clone of VM from a snapshot, because the machine and media UUIDs are not regenerated. So I've written this tool to perform this operation.

The code is pretty ugly currently:) I've just started learning python, and that's the reason. But I'm going to make it more pretty.
