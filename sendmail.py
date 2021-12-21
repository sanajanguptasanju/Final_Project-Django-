import smtplib
import re, getpass

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()


def emailinput():
    sender_email = input("Enter Sender Email :")
    print(sender_email)
    if re.findall('[\w.%+-]{2,20}@[\w.%+-]{2,20}\.[A-Za-z]{2,3}', sender_email):
        pass

    else:
        print("Email is not correct")
        exit()

    print("Enter password associated with this email")
    password = getpass.getpass(prompt="enter password :")
    # print(password)
    return sender_email, password


sender_email, password = emailinput()

try:
    conn.login(sender_email, password)
    print("login Successful")

except:
    print("Either user name or password is incorrect Please allow less secure apps")


def mail_details():
    to_email = input("Enter to Email :")
    print(to_email)
    if re.findall('[\w.%+-]{2,20}@[\w.%+-]{2,20}\.[A-Za-z]{2,3}', to_email):
        subject = input("Enter Subject of Message")
        msg = input("Enter Message")

    else:
        print("Email is not correct")
        exit()

    return to_email, subject, msg


to_email, subject, msg = mail_details()
conn.sendmail(sender_email, to_email, ("Subject:" + str(subject) + "\n\n" + str(msg)))
print("email send successfully")
conn.quit()
