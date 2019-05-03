import smtplib
import socket
import sys


message_template = """To: {}
From: {}
Subject: Test message

Hello,

thy is a test message 
"""


def main():
    if len(sys.argv) < 4:
        name = sys.argv[0]
        print("usage {} server fromaddr to [toaddr...]".format(name))
        sys.exit(2)

    server, fromaddr, toaddrs = sys.argv[1], sys.argv[2], sys.argv[3:]
    message = message_template.format(', '.join(toaddrs), fromaddr)
    try:
        connection = smtplib.SMTP(server)
        report_on_msg_size(connection, fromaddr, toaddrs, message)
    except (socket.gaierror, socket.error, socket.herror,
            smtplib.SMTPException) as e:
        print("your message may haven't been sent!")
        print(e)
        sys.exit(1)
    else:
        s = '' if len(toaddrs) == 1 else 's'
        print("Message sent to {} recipient{}".format(len(toaddrs), s))
        connection.quit()


def report_on_msg_size(conn, faddr, taddr, msg):
    code = conn.ehlo()[0]
    uses_esmtp = (200 <= code <= 299)
    if not uses_esmtp:
        code = conn.ehlo()[0]
        if not (200 <= code <= 299):
            print("Remote server refused Helo code, code:", code)
            sys.exit(1)
    if uses_esmtp and conn.has_extn('size'):
        print(f'Maximum message size is {conn.esmtp_features["size"]}')
        if len(msg) > int(conn.esmtp_features["size"]):
            print("Message too large; aborting.")
            sys.exit(1)

    conn.sendmail(faddr, taddr, msg)


if __name__ == '__main__':
    main()