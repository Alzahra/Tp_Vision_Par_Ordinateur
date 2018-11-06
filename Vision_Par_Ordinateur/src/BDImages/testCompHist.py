#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 04:41:18 2018

@author: alzou
"""
# import the necessary packages
from scipy.spatial import distance as dist
import matplotlib.pyplot as plt
import numpy as np
import argparse
import glob
import cv2
 

 # -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import cv2
import numpy as np

import PIL
from PIL import Image

from pathlib import Path
from matplotlib import pyplot as plt

#list = os.listdir('.')
#print (list)
#newPath = os.path + list[0]

#FichList = [ f for f in list if os.path.isfile(os.path.join('.',f)) ]
#print (FichList)


directoryPath = '.'
images = []
images_path = []

index = 0
min_width = -1
min_height = -1
unset = 0

def is_min(w, h):
    global min_height, min_width
    if w <= min_width:
#        if h < min_height:
         min_width = w
#         min_height = h
    if h <= min_height:
#       if w < min_width:
#            min_width = w
      min_height = h
    
        
def set_min(w,h):
    global min_height, min_width
    min_height = h
    min_width = w

def calc_histo(img):
    
    color = ('b','g','r')
    for i,col in enumerate(color):
        histr = cv2.calcHist([img],[i],None,[256],[0,256])
        plt.plot(histr,color = col)
        plt.xlim([0,256])
    plt.show()
    
    #hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #hist = cv2.calcHist([img], [0,1], None, [256, 256], [0, 256, 0, 256])
    #cv2.imshow('histo', hist)
    
def research_path():
    global unset
    for f in os.listdir(directoryPath):
        #print(directoryPath)
        if os.path.isdir(os.path.join(directoryPath, f)):
            newPath = os.path.join(directoryPath, f)
            print(newPath)
            for filename in os.listdir(newPath):
                #print(filename)
    #            content = open(os.path.join(newPath, filename), 'r')  
                img = cv2.imread(os.path.join(newPath,filename))
                images_path.append(os.path.join(newPath,filename))
                if img is not None:
                    
                    images.append(img) 
                    width, height, channels = img.shape
                    if unset == 0 :
                        set_min(width, height)
                        unset = 1
                    is_min(width, height)
                    
        """
        elif os.path.isfile(os.path.join(directoryPath, f)):
            #print(directoryPath)
            print(f)
    #        content = open(os.path.join(directoryPath, f), 'r')
            img = cv2.imread(os.path.join(directoryPath,f))
            if img is not None:
                images.append(img) 
        """
    
#    print(len(images))
    print(min_height)
    print(min_width)
    """
 #         matrice_distance[len(images)][len(images)] 
    for i in images:
        imgRe = cv2.resize(i, (min_width,min_height),interpolation = cv2.INTER_AREA)
        cv2.imshow('image',imgRe )
        #hist = cv2.calcHist([imgRe],[0],None,[256, 256],[0,256,0,256])
        #hist = cv2.calcHist([imgRe],[0],None,[256],[0,256])
        #calc_histo(imgRe)
        #cv2.imshow('histo', hist)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
    """

def html(function,image_path,val):
    global index
    my_file = Path(function+".html")
    
    if (my_file.is_file()) and (cv2.imread(image_path)) is None:
        """index += 1"""
        htmlfile = open(function+".html", "a")
        htmlfile.write("<h3> Classe '" +str(index) + "'</h3>")
    elif (my_file.is_file()) and (cv2.imread(image_path) is not None):
            htmlfile = open(function+".html", "a")
            if val > -1:
                htmlfile.write('<span>"' + str(val) + '" </span>')    
            htmlfile.write('<img src = "' + image_path + '"width="'+ str(min_width) + '" height="'+ str(min_height) +'" alt ="cfg">\n')
    elif (my_file.is_file() is False) and (cv2.imread(image_path)) is not None:
        htmlfile = open(function+".html", "w")
        htmlfile.write("<html>\n")
        htmlfile.write("<head><title>Test</title></head>")
        if val > -1:
                htmlfile.write('<span>"' + str(val) + '" </span>')
        htmlfile.write('<img src = "' + image_path + '"width="'+ str(min_width) + '" height="'+ str(min_height) +'" alt ="cfg">\n')
        htmlfile.write("</html>\n")
    else :
        """index += 1"""
        htmlfile = open(function+".html", "w")
        htmlfile.write("<html>\n")
        htmlfile.write("<head><title>'" + function + "' </title></head>")
        htmlfile.write("<h3> Classe '" +str(index) + "'</h3>")
        htmlfile.write("</html>\n")
        
    htmlfile.close()


def createhtmlfile():
    print("dans la fonction")
    for i in images_path :
        html("plop",i,-1)
    

research_path()
"""
createhtmlfile()
"""

# initialize the index dictionary to store the image name
# and corresponding histograms and the imagesTest dictionary
# to store the imagesTest themselves
index = {}
imagesTest = {}

from os import listdir
from os.path import isfile, join
paths = ["./Test/" + f for f in listdir("./Test/") if isfile(join("./Test/", f))]

pathes = paths[:6]
"""print(pathes)
"""
# loop over the image paths
for imagePath in paths:
	# extract the image filename (assumed to be unique) and
	# load the image, updating the imagesTest dictionary
	filename = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)
	imagesTest[filename] = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
	# extract a 3D RGB color histogram from the image,
	# using 8 bins per channel, normalize, and update
	# the index
	hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8],[0, 256, 0, 256, 0, 256])
	#hist = cv2.normalize(hist).flatten()
	index[filename] = hist
	#print(filename)
# METHOD #1: UTILIZING OPENCV
# initialize OpenCV methods for histogram comparison
"""OPENCV_METHODS = (
	("Correlation", cv2.HISTCMP_CORREL),
	("Chi-Squared", cv2.HISTCMP_CHISQR),
	("Intersection", cv2.HISTCMP_INTERSECT), 
	("Hellinger", cv2.HISTCMP_BHATTACHARYYA))

# loop over the comparison methods
for (methodName, method) in OPENCV_METHODS:
""" 
methodName = "Correlation"
method = cv2.HISTCMP_INTERSECT

image_deBase = "desert_01_001.jpg"
	# initialize the results dictionary and the sort
	# direction
results = {}
reverse = False
 
	# if we are using the correlation or intersection
	# method, then sort the results in reverse order
if methodName in ("Correlation", "Intersection"):
    reverse = True
  
# compute the distance between the two histograms
	# using the method and update the results dictionary
for (k, hist) in index.items():
    d = cv2.compareHist(index[image_deBase], hist, method)
    results[k] = d
 
	# sort the results
results = sorted([(v, k) for (k, v) in results.items()], reverse = reverse)

# show the query image
"""
fig = plt.figure("Query")
ax = fig.add_subplot(1, 1, 1)
ax.imshow(imagesTest[image_deBase])
plt.axis("off")

	# initialize the results figure
fig = plt.figure("Results: %s" % (methodName))
fig.suptitle(methodName, fontsize = 20)
"""
	# loop over the results
for (i, (v, k)) in enumerate(results):
	# show the result
    #ax = fig.add_subplot(1, len(imagesTest), i + 1)
    #ax.set_title("%.2f" % (v))
    html("testIntersect","./Test/"+k,v)
"""
    plt.imshow(imagesTest[k])
    plt.axis("off")
 
# show the OpenCV methods
plt.show()
"""