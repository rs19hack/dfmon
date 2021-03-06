## dfmon

A GUI for managing hotplug storage devices (SATA, USB, SCSI, ...) in your 
Linux system with Truecrypt support.

### Screenshots

#### Successful Device Removal

![Successful Device Removal](https://github.com/ibressler/dfmon/raw/master/screenshots/scr01.png "Successful Device Removal")

#### Available Actions for a Device

![Available Actions for a Device](https://github.com/ibressler/dfmon/raw/master/screenshots/scr02.png "Available Actions for a Device")

#### Status Tooltip for Each Block Device

![Status Tooltip for Each Block Device](https://github.com/ibressler/dfmon/raw/master/screenshots/scr03.png "Status Tooltip for Each Block Device")

### About

Its creation was motivated by the need to hot-unplug (e)SATA hard disks from
the running system. Recent Linux distributions support this (via a GUI) for
USB devices but not for SATA devices directly, afaik (the author). Please
tell me, if I'm wrong, or if this is not supported by the kernel at all.

Device removal preparation follows [a guide from Redhat] [1]. Except for LVM,
md or multipath setups - to keep it simple for the beginning.

[1]: http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/5/html/Online_Storage_Reconfiguration_Guide/removing_devices.html

### Invokation

Clone the git repository somewhere on your disk:

	$ git clone https://github.com/ibressler/dfmon.git

The GUI is invoked like so (dots are important!):

	$ cd dfmon
	$ PYTHONPATH=. ./bin/dfmon

### Requirements

* Python
* Qt
* PyQt

Tested on Ubuntu 11, OpenSuse 12, Fedora 16

#### Ubuntu

	$ sudo apt-get install python-qt4

#### Fedora

	$ su
	# yum install PyQt4

#### OpenSuse

If you use the KDE Desktop, PyQt is already installed, but it won't hurt:

	$ su
	# zypper install python-qt4

### Personal Note

This tiny project serves also for getting familiar with python itself. Hence,
feel free to point me at problems, give suggestions or provide patches ;)

### Copying

Qt dependencies are restricted to dfmon.uiqt. dfmon.uicmd as well as
dfmon.backend are free of Qt. Therefore, it should be possible to write a
different GUI, if desired.

Copyright (c) 2010-2011, Ingo Breßler <dfmon@ingobressler.net>

This is Free Software distributed under the terms of the GPL license.
See the COPYING file for license rights and limitations.

