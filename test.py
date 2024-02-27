"""
Main Script for Generating Certificates and Sending them
"""
"""
Main Script for Generating Certificates and Sending them
"""

import certificates_lib.generate_certificates as gc
import send_emails as se
import certificates_lib.constants as cons
import certificates_lib.read_files as read_files

# TODO: Fill this with test file that contains 2 columns names, emails without headers.
participant = read_files.read_excel_file('')
print(participant)

while cons.IS_SENDING:
    gc.generate_certificates(participant)
    se.send_emails(participant)

