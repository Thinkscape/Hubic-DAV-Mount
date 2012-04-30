# Hubic DAV Mount

## Overview

A small script to mount your Hubic account using davfs2

Based on a pythons script by Nicolas P  
Based on a perl script written by GR  
>	(thanks to GR for having found the ws authentification trick)   

Usage:  
>	sudo hubic.py username password mount_point

Node: This is NOT a DropBox-like setup!  
Davfs accesses are remote only, making them very slow on regular usage.

My setup:  
>	hubic.py launched in initd. at startup, mounted on /mnt/hubic  
>	Using lsync.d to sync locally to ~/hubic   




# Licence
 Copyright © 2012 Benoît Vidis

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

The Software is provided "as is", without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose and noninfringement. In no event shall the authors or copyright holders be liable for any claim, damages or other liability, whether in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or other dealings in the Software.
