#-------------------------------------------------------------------------------
# Name:			get_info
# Purpose:		This programms takes info from a .csv and return it
#
# Author:      _____     _____  ________   ____  ____ ____         ____           ________   ____  ____ 
#              \    \   /    / /        \  |  |  |  | |  |         |  |          /        \  |  |  |  | 
#               \    \ /    / |   ____   | |  |  |  | |  |         |  |         |   ____   | |  |  |  | 
#                \    V    /  |  /    \  | |  |  |  | |  |         |  |         |  /    \  | |  |  |  | 
#                 \       /   |  |    |  | |  |  |  | |  |         |  |         |  |    |  | |  |  |  | 
#                  \     /    |  |    |  | |  |  |  | |  |         |  |         |  |    |  | |  |  |  | 
#                   |   |     |  |    |  | |  |  |  | |  |         |  |         |  |    |  | |  |  |  | 
#                   |   |     |  \    /  | |  |  |  | |  |         |  |         |  \    /  | |  |  |  | 
#                   |   |     |   ¯¯¯¯   | |  \__/  | |  |_______  |  |_______  |   ¯¯¯¯   | |  \__/  | 
#                   |___|      \________/  \___  ___/ |__________| |__________|  \________/  \___  ___/   
#                                              ¯¯                                                ¯¯
#
# Created:     20/11/2020
# Copyright:   (c) Youllou 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#global import
import os

cur_path = os.path.dirname(__file__)

def get(filepath,splitter):
	"""
		gets all data from a .csv file
		filepath has to be a str
		the .csv must be encoded in UTF-8
		return -1 if the file isn't found
		return a list of data else
	"""

	allinfo= []
	try :
		f=open(os.path.relpath(filepath,cur_path),"r",encoding="UTF-8")
	except FileNotFoundError:
		return -1
	else :
		while 1:
			info = f.readline()
			if info =="":
				break
			else :
				allinfo+=[info.split(splitter)]
		f.close()

	return allinfo

def write(filepath,splitter,data):
	"""
		write in a csv from a list
		filepath must be a str
		data must be a list
	"""
	f = open(os.path.relpath(filepath,cur_path),"w",encoding="UTF-8")

	for i in range(len(data)):
		f.write(data[i][0])
		for j in range(1,len(data[i])):
			f.write(splitter+data[i][j])
	f.close()
