"""
Script for Sending Emails With Attachments
"""
import os
from dotenv import find_dotenv, load_dotenv
import smtplib
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import certificates_lib.constants as cons
import certificates_lib.helper as helper
import arabic_reshaper
from bidi.algorithm import get_display


# Setup port number and server name
smtp_port = 587                 # Standard secure SMTP port
smtp_server = "smtp.gmail.com"  # Google SMTP Server


# Define the email function
def send_emails(participates):

    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    pswd = os.getenv("GMAIL_APP_PASS")

    for index, person in enumerate(participates):

        file_name = p_name = person['name']
        p_email = person['email']

        if(person['lang'] == cons.ENG):
            DES = cons.ENG
            line_1 = 'Hey there'
            line_2 =  'Your certificate from Flutter Community arrived'
            dear = 'Flutter Programmer:'
            

        elif(person['lang'] == cons.ARA):
            DES = cons.ARA
            line_1 = 'أهلًا وسهلًا'
            line_2 = 'Flutter وصلت شهادتك من مجتمع'
            dear = 'مطور/ة Flutter'
            p_name = arabic_reshaper.reshape(p_name)
            p_name = get_display(p_name)  
            
        else:
            helper.unsported_language(person)
            continue   

    
        # Make the body of the email
        body = f"""
        {line_1}
        {dear} {p_name}
        {line_2}
        """

        # make a MIME object to define parts of the email
        msg = MIMEMultipart()
        msg['From'] = cons.EMAIL_FROM
        msg['To'] = p_email
        msg['BCC'] = cons.EMAIL_BCC
        msg['Subject'] = cons.SUBJECT

        # Attach the body of the message
        msg.attach(MIMEText(body, 'plain'))

        # Define the file to attach
        file_path = f'certificates_lib/generated_certificates/{DES}/{file_name}.jpg'
        
        # Open the file in python as a binary
        image = open(file_path, 'rb').read()  # r for read and b for binary

        image_package = MIMEImage(image, 'jpg', name = 'flutter_dart_bootcamp_certificate.jpg')
        
        msg.attach(image_package)

        # Cast as string
        text = msg.as_string()

        # Connect with the server
        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        TIE_server.login(cons.EMAIL_FROM, pswd)
        print("Succesfully connected to server")
        print()

        # Send emails to "person" as list is iterated
        print(f"Sending email to: {p_name}...")
        TIE_server.sendmail(cons.EMAIL_FROM, p_email, text)
        print('Email sent to: {}/{}'.format(index + 1, len(participates)))

    # Close the port
    TIE_server.quit()