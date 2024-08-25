import random

def secure_password():
    pass_name = input('Insert your password key name.')
    characters = [{'alphabet': 'abcdefghijklmnñopqrstuvwxyz'},
                  {'uppercase alpha': 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'},
                  {'digits': '1234567890'},
                  {'symbols': '!"#$%&/()=?¡*[]_-.;,:'}]
    pass_len = random.randint(8, 18)
    counter = 0
    password = []
    while counter < pass_len:
        for c in characters:
            for g in c.values():
                h = random.choice(g)
                password.append(h)
                counter += 1
        if counter >= pass_len:
            break
    pw = "".join(password)
    with open("passwords.txt", "a") as myfile:
        myfile.write(f'{pass_name}: {pw} \n')

secure_password()
