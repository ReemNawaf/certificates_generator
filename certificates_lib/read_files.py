import certificates_lib.constants as cons
import certificates_lib.helper as helper
import pandas as pd

def read_excel_file(file_path):
    ara_names = 0
    eng_names = 0
    participants = []
    data = pd.read_excel(file_path, header = None).values.tolist()

    for person in (data):
        name_letter = str(person[0])[1].lower().encode()
        LANG = ''
       
        if (b'a' <= name_letter <= b'z'):
            LANG = cons.ENG
            eng_names += 1
            
            
        elif (b'\xd8\xa7' <= name_letter <= b'\xd9\xa8'):
            LANG = cons.ARA
            ara_names += 1

        else:
            helper.unsported_language(person)
            continue

        participants.append({'name': person[0].rstrip(), 'email': person[1].rstrip(), 'lang': LANG})
    
    print(f'{eng_names=}')
    print(f'{ara_names=}')

    return participants