
def unsported_language(person):
    print('unsported langeuage name', person)
    f = open("unsent_certificates.txt", "a")
    f.write(f'\nname: {person[0]}, email: {person[1]}\n')
    f.close()