def main():
    while True:
        import http.client
        import socket
        test_con_url = "www.google.com"  # For connection testing
        test_con_resouce = "/intl/en/policies/privacy/"  # may change in future
        test_con = http.client.HTTPConnection(test_con_url)  # create a connection

        try:
            test_con.request("GET", test_con_resouce)  # do a GET request
            response = test_con.getresponse()
        except http.client.ResponseNotReady as e:
            print ("Improper connection state")
        except socket.gaierror as e:
            print ("Not connected")
        else:
            print ("Connected")
            break;

        test_con.close()
    import pyautogui

    # Take screenshot
    pic = pyautogui.screenshot()

    # Save the image
    pic.save('screenshot.jpg')
    import cv2
    # initialize the camera
    # cam = VideoCapture(0)   # 0 -> index of camera
    # s, img = cam.read()
    # if s:    # frame captured without any errors
    # namedWindow("cam-test",CV_WINDOW_AUTOSIZE)
    # imshow("cam-test",img)
    # waitKey(0)
    # destroyWindow("cam-test")
    # imwrite("filename.jpg",img) #save image
    # cv2.namedWindow("survelliance")
    cap = cv2.VideoCapture(0)
    if (cap.isOpened()):
        s, img = cap.read()
        # cv2.imshow("survelliance",img)
        cv2.imwrite(r"filename.jpg", img)
        # k = cv2.waitKey(10)
        # if k == 27:
        # break

    from urllib.request import urlopen
    data = urlopen("http://myip.dnsdynamic.org/").read()
    data = str(data, 'utf-8')
    print (data)

    # from here i need to focus

    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders

    email_user = 'keclite2078@gmail.com'
    email_password = #put password your
    fh = open("data2.txt", "r")
    email_send = fh.read()
    fh.close()

    subject = 'IP Address'

    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_send
    msg['Subject'] = subject

    body = 'Recent IP Addres ' + str(data)
    msg.attach(MIMEText(body, 'plain'))

    filename = 'filename.jpg'
    attachment = open(filename, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename)

    msg.attach(part)

    filename2 = 'screenshot.jpg'
    attachment2 = open(filename2, 'rb')
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment2).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= " + filename2)
    msg.attach(part)

    text = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_user, email_password)

    server.sendmail(email_user, email_send, text)
    server.quit()

main()
# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
def get_mostnew_email(messages):
    """
    Getting in most recent emails using IMAP and Python
    :param messages:
    :return:
    """
    ids = messages[0]  # data is a list.
    id_list = ids.split()  # ids is a space separated string
    # latest_ten_email_id = id_list  # get all
    latest_ten_email_id = id_list[-1:]  # get the latest 10
    keys = map(int, latest_ten_email_id)
    news_keys = sorted(keys, reverse=True)
    str_keys = [str(e) for e in news_keys]
    return str_keys
def control():
    import sys#for input output and string split
    import imaplib
    import email
    import re
    import pyautogui#for keyboard
    import subprocess#for sysytem off on
    import os#for batch file opening
    import imaplib
    from email.parser import HeaderParser

    M = imaplib.IMAP4_SSL('imap.gmail.com')
    M.login('keclite2078@gmail.com', 'urllib2078')
    M.list()
    M.select("inbox")# connect to inbox.

    (retcode, messages) = M.search(None, 'ALL')
    news_mail = get_mostnew_email(messages)
    n = 0
    (retcode, messages) = M.search(None, '(UNSEEN)')
    if retcode == 'OK':

        for num in messages[0].split():
            print ('Processing ')
            n = n + 1
            typ, data = M.fetch(num, '(RFC822)')
            for response_part in data:
                if isinstance(response_part, tuple):
                    original = email.message_from_string(str(response_part[1],'utf-8'))

                    print (original['From'])
                    print (original['Subject'])
                    typ, data = M.store(num, '+FLAGS', '\\Seen')
                    l = 'signoff'
                    c = 'cancel'
                    ip = 'ip'
                    subj = original['Subject']
                    s = 'shutdown'
                    #print(subj)
                    word=subj.split(',')
                    if subj=='destroyxxx':
                        p= subprocess.Popen("kill.bat",creationflags=subprocess.CREATE_NEW_CONSOLE)

                    if word[0]=='key':
                        i=1
                        while i<len(word):
                            print(word[i])
                            pyautogui.press(word[i])
                            i=i+1
                    if subj == ip:
                        main()
                    if subj == l:
                        print(subj)
                        subprocess.call(["shutdown", "-f", "-l"])
                    if subj == s:
                        subprocess.call(["shutdown", "-f", "-s", "-t", "120"])
                    if subj == c:
                        subprocess.call(["shutdown","-a"])

    print (n)

while True:
    import time
    control()
    time.sleep(2)