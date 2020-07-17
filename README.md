# UBC-seatcheck
A python script that will check the UBC course calendar for available seats in a specified course, complete with instructions on how to use it!

1. Download the program UBC_seatcheck.py from this repository.
2. If you do not have a python distribution downloaded on your system, you may have to download Anaconda before being able to run this program. This can be done here: https://www.anaconda.com/products/individual. 
3. (Optional, but reccomended) Create a new gmail account from which the program can send emails to notify you about courses opening up. 
4. For the email adddress that you want the program to send emails from, you must turn on access for less secure apps. This can be done by following this link https://myaccount.google.com/lesssecureapps
5. Open the UBC_seatcheck.py program file. In the parameters section, specify the delay time in between checks the program will do by changing the value of the variable 'delay' (i.e. if you want the program to check every two minutes, change this to delay = 120). Do note that as outlined in the Terms of Service of accessing UBC servers (which can be found here: https://www.ubc.ca/site/legal.html?utm_campaign=UBC+CLF&utm_medium=CLF+Global+Footer&utm_source=), "In using the Site, you agree that you will not use any device, software or routine to interfere or attempt to interfere with the proper working of the Site. You agree that you will not use any robot, spider, other automatic device, or manual process to impose an "unreasonable or disproportionately large load" on UBC’s infrastructure. An "unreasonable or disproportionately large load" is one that prevents other members of the University community from gaining fair and equitable access to web-based systems and resources." To be on the safe side, don't make this value too small as to not place too large of a load on the servers (though a single check from a single device will likely not constitute as an unreasonable load).
6. If you want to vary the amount of randomization between two checks, you can change the value of the variable 'sigma' (make sure this is less than whatever you set delay to be). 
7. Set the number of cycles (of checks) that you want the program to run by changing the variable 'numcycles'. The total runtime of the program will (approximately) be 'numcycles' times 'delay', so determine how many cycles the program may need to run before the add/drop deadline and set it to that. This can effectively just be set to an arbitrarily large number.
8. Set the variable 'fromaddr' to be the email address that you will send an email from (that you have turned on access from less secure apps)
9. Set the variable 'toaddr' to the email address that will receive the notification email. This can be the same as 'fromaddr'.
10. Set the variable 'password' to the password of 'fromaddr' so the program can login to your email and send you a notification.
11. After finishing setting the parameters in the program, you're almost done! Now, to run the program, start a new instance of terminal/open a new window in terminal.
12. Into terminal, type in "python " (with the space). Then, drag in the "UBC_seatcheck.py" program into terminal (or you can manually type in the full path of the program). Then, leaving another space, type in the desired course subject, course code, and section number (with spaces in between). The final input into terminal should look something like like:
"python /Users/USERNAME/Downloads/UBC_seatcheck.py MATH 320 101". Finally, hit return to start the program.
13. The program will continue to check the course at the specified time interval automatically as long as your computer is turned on. When it sees that the course has a general seat open, the program will stop running, and send an email from and to the specified address. 
14. To terminate the program early, either close the terminal window or press control-C.
15. To check more than one course/section at the same time, simply open another terminal window, and start the program in the same way (just changing the course and section code to be the next course you want to check). 

Happy coursehunting!
