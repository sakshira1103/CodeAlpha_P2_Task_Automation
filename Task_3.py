from email.mime.text import MIMEText #to create simple text email
from email.mime.multipart import MIMEMultipart # to attach pdf,images,etc
import smtplib # for sending a email
import schedule #to automatic send email
import time 

smtp=smtplib.SMTP("smtp.gmail.com",587) # to build connection with smtp
smtp.ehlo() # to introduced 
smtp.starttls() # to encritped the data from normal to encrypted form
smtp.login('projecttask1103@gmail.com','dhexxfaoghscylgy')

msg=MIMEMultipart()

msg['From']='projecttask1103@gmail.com'
msg['To']='sakshiraut1103@gmail.com , sakshira7@gmail.com'
msg['Subject']='This is my third task.'

body=("Good Morning!\nThis is my task three about task automation report\nI used python languages to generate this task.\nBest regard\nSakshi Raut")

msg.attach(MIMEText(body,'plain'))

recipent_list=msg['To'].split(',')

smtp.sendmail(msg['From'],recipent_list,msg.as_string())

print("Email send successfully!")
smtp.quit()

