import smtplib

content = 'Tmrw therikka vidrom'

mail = smtplib.SMTP('smtp.gmail.com',587)

mail.ehlo()

mail.starttls()

mail.login('baranitharan2020@gmail.com','baranitharan20@')

mail.sendmail('baranitharan2020@gmail.com','rviratnagasurya@gmail.com',content)

mail.close()
