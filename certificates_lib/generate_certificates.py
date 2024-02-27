"""
Script for Generating Flutter Bootcamp Certificates
"""

from PIL import Image, ImageDraw
import arabic_reshaper
from bidi.algorithm import get_display
import certificates_lib.constants as cons
import certificates_lib.helper as helper

def generate_certificates(participates):
    
    for index, person in enumerate(participates):
        print('--------', index, person)
        file_name = p_name = person['name']
        
        if(person['lang'] == cons.ENG):
            DES = cons.ARA
            FONT = cons.ENG_FONT
            LOC = cons.ENG_LOC
            IMG_PATH = 'certificate_templates/certificate-english.png'

        elif(person['lang'] == cons.ARA):
            DES = cons.ARA
            LOC = cons.ARA_LOC
            FONT = cons.ARA_FONT
            IMG_PATH = 'certificate_templates/certificate-arabic.png'
            p_name = arabic_reshaper.reshape(p_name)
            p_name = get_display(p_name)  
            
        else:
            helper.unsported_language(person)
            continue        

        certificate = Image.open(IMG_PATH)
        draw = ImageDraw.Draw(certificate)
        draw.text(LOC, p_name, font = FONT, fill = cons.FONT_COLOR)
        
        certificate.show()
        
        print('Processing Certificates {}/{}'.format(index + 1, len(participates)))
        certificate.save(f'certificates_lib/generated_certificates/{DES}/{file_name}.jpg')
