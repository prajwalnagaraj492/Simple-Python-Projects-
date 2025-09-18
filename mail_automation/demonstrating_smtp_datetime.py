import datetime as dt
import smtplib

mymail = "" #add mail
password = "#####" #setup in mail

now = dt.datetime.now()
current_hour = now.hour
wishtime = 00 #12AM in 24 hours


def wish_p(text):
    with smtplib.SMTP("smtp.gmail.com") as connection: #we created a connection with gmail smpt server
        connection.starttls() #establishing secure connection
        connection.login(user=mymail,password=password) #login to verify
        connection.sendmail(from_addr=mymail,to_addrs="prajwaln8109@gmail.com",msg=text)
        print("mail sent")


''''A BDAY WISHER'''
# if current_hour == wishtime:
#     wish_p("happy birthday")

'''a mail spammer'''
# level = 5
# for i in range(level):
#     wish_p("subject: SPAM ALERT\n\n  QWERTYUIOPASDFGHJKL;ZXCVBNM,QWERTYUIOPASDFGHJKXCVBNMQWERTYUIOSDFGHJKXCVBNM")




