import smtplib
import random
from pwinput import pwinput

#random module used to generate 6 digit otp.
otp=''.join([str(random.randint(0,9)) for i in range(6)])

#smtp has vaious classes and methods to login the particular gmail and to send the mail to the given mailId.
server=smtplib.SMTP('smtp.gmail.com',587)

server.starttls()

MailId_user=input("Please enter the User's mail: ")
MailId_pass=pwinput("Plese Enter the password: ","*")
MailId_rec=input("Please Enter the Receiver's Mail: ")

server.login(MailId_user,MailId_pass)


msg="Hello,Your OTP is"+str(otp)

server.sendmail(MailId_user,MailId_rec,msg)

print("OTP Sent to mail")

server.quit()

#This is used for the OTP Verification which is sent to the Receiver.
#In this User has 3 turns to enter a correct otp
for i in range(3):
    OTP=int(input("Enter the Received OTP:"))

    if(OTP==int(otp)):
        print("OTP(One Time Password) Verified")
        break

    else:
        print("Wrong OTP")

