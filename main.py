"""
Main Script for Generating Certificates and Sending them
"""

import certificates_lib.generate_certificates as gc
import send_emails as se
import certificates_lib.constants as cons
import certificates_lib.read_files as read_files

# Load the names from xlsx file
file_path = 'data/participants.xlsx'


participants = read_files.read_excel_file(file_path)


print(participants)

while cons.IS_SENDING:
    gc.generate_certificates(participants)
    se.send_emails(participants)
