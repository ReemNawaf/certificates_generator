# Course Certificate Generator and Sender

Automate the generation and distribution of course certificates to participants' emails based on their names' language.

## Overview

This project is designed to streamline the process of generating and sending course certificates to participants. It takes an Excel file containing participant names and emails, detects the language of each participant's name, generates certificates in the corresponding language, and sends them to the respective email addresses.

## Features

- Automatically detects participant names' languages.
- Supports multiple languages for certificate generation.
- Generates certificates in PDF format.
- Sends certificates to participants' emails.

## Setup

1. Clone the repository:
    git clone git@github.com:ReemNawaf/certificates_generator.git

2. Install the required dependencies:
3. Prepare your Excel file:
   - Ensure the Excel file contains two columns: one for participant names and one for their email addresses.
   - Remove any headers or unnecessary data from the Excel file.

4. Run the script:
    python main.py --input_file your_input_file.xlsx


Replace `your_input_file.xlsx` with the name of your Excel file.

## Dependencies

- Python 3.x
- `pandas` - for reading Excel files
- `smtplib` and `email.mime` - for sending emails
- `PIL` - for placing styled text on image
- `bidi.algorithm` and `arabic_reshaper` - for fixing the display of Arabic characters
- `os` and `dotenv` - for env variables

## Usage

1. Provide an Excel file with participant names and emails, without a header row.
2. Run the `main.py` script.
3. Certificates will be generated and sent to participants' emails.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your proposed changes.

