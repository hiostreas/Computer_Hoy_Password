#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
if you are using the console or the terminal you should save the result in a variable
and then print, because if you do dont do that, and 
you type it directly in the console letters like the accents or the ñ could
appear encoded.

for example:
m = dice_pass.getpassword()
print m


"""

import random
import csv
def getpassword():

	n_digits = random.randrange(6,9) # put the number of digits
	
	tmp_password =""; # save temporary variable for the password
	for n in range(1, (n_digits+1)):
		tmp_char = str(random.randrange(1,9))
		tmp_password  = tmp_char + tmp_password
		
	char_diccionary = random.randrange(0,58008)# get the random position of the words in the diccionary
	final_password = tmp_password # in case of dont finding any position in the diccionary database 
	
	i=0
	with open('palabras.csv', 'rU') as csvfile: # read the csv database
	    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
	    for row in spamreader:
	    	if(i == char_diccionary):
	    		print "char_diccionary es: "+ str(char_diccionary)
	    		print row[1]
	    		final_password = tmp_password + row[1]  		
	    	i = i + 1
    		
	return final_password;