"""
Date: 07/16/2020
Name: Rio Weil
Title: Getcourseinfo.py
Description: Checks the SSC at a specified frequency to see if a course has any open seats, and sends an email when (general) seats are available to the specified address. 
Inputs: From within the program, specify time between checks, time randomization, number of checks to be done before program termination, sender and receiver email addresses. 
Inputs 2: From terminal, specify the course subject, code, and section. 
Output: An email from and to the specified address notifying you when a seat in the course opens up. 
"""

import requests
import re
from bs4 import BeautifulSoup
import time
import smtplib
import sys
import numpy as np

#PARAMETERS (these can be changed)
delay = 60 # Checks the site every x seconds
sigma = 20 # The time in between checks varies by this amount (time between checks is randomized slightly). Make sure this is less than delay.
numcycles = 86400 # How many cycles you want this to run (the program will run for this number * delay seconds). Valid to make this as long as the period from now to the course add/drop deadline.
global fromaddr, toaddr, password, subject, course, section  # Declares global variables so these can be accessed inside functions. 
fromaddr = 'YOURADDRESS@gmail.com'  # Email will be sent from this address, e.g. 
toaddr = 'RECIPIENT_EMAIL_ADDRESS_HERE'  # Email will be sent to this address (could be same as address above)
password = 'YOUR_PASSWORD_HERE'  # Password for the fromaddr address. 
subject = sys.argv[1] # Subject course code, e.g. MATH. Set from terminal.
course = sys.argv[2] # 3-digit course number, e.g. 320. Set from terminal.
section = sys.argv[3]  # 3-character section code, e.g. 101. Set from terminal. 

def getseats_email(soup, title):
	find_string = soup.find(string = re.compile(str(title)))  # Finds the part of the html source code with the seat heading
	if str(type(find_string)) == "<class 'NoneType'>":  # Checks to see if find_string is NoneType, implying that the text could not be found due to the section being STT restricted.
		#print(title + ' = STT') # Prints this to console (commented out)
		return  # Returns nothing
	seatline = str(find_string.next_element)  # Goes to the next line, which contains the number of seats. 
	splitstr = seatline.split('>')[2]
	seatnumber = splitstr.split('<')[0]  # Splits the string to isolate the number of seats left
	#print(title + ' = ' + seatnumber) # Prints the number of seats left in that category (commented out)
	if title == "General Seats Remaining" and seatnumber != str(0):  # Runs this part if there are a nonzero amount of General seats found
		global msg
		msg = 'Seats have been found in ' + subject + ' ' + course + ' ' + section + '!'  # Message that a seat has opened up
		server = smtplib.SMTP('smtp.gmail.com',587)  # Sets up parameters for gmail server
		server.starttls()  # Starts the server
		server.login(fromaddr,password)  # Logs in with your address and password
		server.sendmail(fromaddr,toaddr,msg)  # Sends the email that seats are available in the course
		server.quit()  # Disconnects from server
		global seatfound
		seatfound = True # Declares global variable so main loop can be stopped
	return  # Returns nothing

for k in range(numcycles): # Repeats for the specified number of cycles
	url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=' + subject + '&course=' + course  + '&section=' + section  # url for course/section webpage on ssc
	r = requests.get(url)  # Fetches the html source code
	soup = BeautifulSoup(r.text,'html.parser')  # Creates beautiful soup object of the html source code
	for i in np.array(["Total Seats Remaining", "Currently Registered", "General Seats Remaining", "Restricted Seats Remaining"]):  # Iterates over the differnet course categories
		getseats_email(soup, i)  # Checks the number of seats in each course category, prints them, and sends an email (and ends loop) if general seats are available
	if 'seatfound' in globals():
		print(msg)
		break  # If seats are found, prints this to console and ends the loop
	time.sleep(np.random.uniform(delay+sigma,delay-sigma))  # Time delay for specified time +/- the uncertainty specified before checking again. 


