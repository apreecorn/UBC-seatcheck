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
delay = 21 # Checks the site every x seconds
sigma = 20 # The time in between checks varies by this amount (time between checks is randomized slightly). Make sure this is less than delay.
numcycles = 90000 # How many cycles you want this to run (the program will run for this number * delay seconds). Valid to make this as long as the period from now to the course add/drop deadline.
global fromaddr, toaddr, password, subject, course, section  # Declares global variables so these can be accessed inside functions. 
fromaddr = 'SENDERADDRESS@gmail.com'  # Email will be sent from this address, e.g. 
toaddr = 'RECIPIENT_EMAIL_ADDRESS_HERE'  # Email will be sent to this address (could be same as address above)
password = 'YOUR_PASSWORD_HERE'  # Password for the fromaddr address. 
subject = sys.argv[1] # Subject course code, e.g. MATH. Set from terminal.
course = sys.argv[2] # 3-digit course number, e.g. 320. Set from terminal.
section = sys.argv[3]  # 3-character section code, e.g. 101. Set from terminal. 


for k in range(numcycles): # Repeats for the specified number of cycles
	url = 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=' + subject + '&course=' + course  + '&section=' + section  # url for course/section webpage on ssc
	r = requests.get(url)  # Fetches the html source code of the course page on SSC
	soup = BeautifulSoup(r.text,'html.parser')  # Creates beautiful soup object of the html source code
	find_string = soup.find(string = re.compile(str("General Seats Remaining")))  # Searches the HTML source code for the "General Seats Remaining" string.
	if str(type(find_string)) != "<class 'NoneType'>":
		seatline = str(find_string.next_element)  # Goes to the next line, which contains the number of seats. 
		splitstr = seatline.split('>')[2]
		seatnumber = splitstr.split('<')[0]  # Splits the string to isolate the number of seats left
		if seatnumber != str(0):  # Checks to see if the number of seats is not 0, and if it is not, runs the next part of code that sends the email.
			msg = 'Seats have been found in ' + subject + ' ' + course + ' ' + section + '!'  # Message that a seat has opened up
			server = smtplib.SMTP('smtp.gmail.com',587)  # Sets up parameters for gmail server
			server.starttls()  # Starts the server
			server.login(fromaddr,password)  # Logs in with your address and password
			server.sendmail(fromaddr,toaddr,msg)  # Sends the email that seats are available in the course
			server.quit()  # Disconnects from server
			print(msg)  # Prints that seats have been found to terminal.
			break  # Breaks the for loop and ends the program. 
	time.sleep(np.random.uniform(delay+sigma,delay-sigma))  # Program "rests" for the amount of delay specified, with a little bit of randomization. 