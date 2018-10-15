# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

list = os.listdir('.')
#print (list)
newPath = os.path + list[0]

FichList = [ f for f in list if newPath.isfile(newPath.join('.',f)) ]
print (FichList)