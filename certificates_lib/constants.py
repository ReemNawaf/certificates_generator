from PIL import ImageFont

IS_SENDING = True

FONT_SIZE = 130

ENG_LOC = (1050, 700)
ARA_LOC = (1500, 540)

FONT_COLOR = (71, 145, 234)

ARA_FONT = ImageFont.truetype(font = 'fonts/ibm_plex_sans_arabic_medium.ttf',size = FONT_SIZE)
ENG_FONT = ImageFont.truetype(font = 'fonts/kaushan_script-regular.ttf', size = 90)

# Set up the email lists
EMAIL_FROM = "gdsckau@gmail.com"
EMAIL_BCC = "reem.naw@gmail.com" 

# name the email subject
SUBJECT = "Flutter & Dart Bootcamp Certificate "

ARA = 'ara'
ENG = 'eng'