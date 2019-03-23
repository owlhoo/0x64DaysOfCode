import yagmail
from datetime import datetime
import sys


def send():

    """
    ============================================================================================
    ||    usage:                                                                              ||
    ||        notify.py [sender_email] [password] [receiver_email] [custom_message]           ||
    ||                                                                                        ||
    ||    Sender email is an email to log into                                                ||
    ||    Password is the password for the email                                              ||
    ||    Receiver email is an email where you want notification to be delivered              ||
    ||    Custom message is, well, custom message that you want to add to default message     ||
    ||                                                                                        ||
    ||    If none of the above are given, input is entered on the runtime on all of three,    ||
    ||    similarly if only two arguments are given third one is entered on the runtime etc.  ||
    ============================================================================================
    """
    try:
        with open("url.txt", "r") as file:
            path = ''.join(file.readline())
    except OSError:
        path = ''

    message = ["Raspored se promenio,I attached it in the mail for you. ", './raspored.pdf',
               "You can check it out here: " + path + ""]

    arg_length = len(sys.argv)
    sender = (sys.argv[1] if arg_length > 1 else str(input('Enter your email: ')))
    password = (sys.argv[2] if arg_length > 2 else str(input('Enter your password: ')))
    receiver = (sys.argv[3] if arg_length > 3 else str(input('Enter the email to who you want to send email to: ')))
    message.append(' '.join(sys.argv[4:]))

    yag = yagmail.SMTP(sender, password)
    yag.send(receiver, 'RASPORED - PROMENA', message)


try:
    send()
    print("Successfully sent an email. See you soon! :D ")
except:
    print(send.__doc__)
    print("Could not send an email for some reason..", file=sys.stderr)
    print("Time info:\n" + str(datetime.now()) + "\n", file=sys.stderr)



