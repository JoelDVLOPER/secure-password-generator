import random

def secure_password():
    characters = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '123456789', 
                  "!#$%&/()=?*[]_-.;,:"]
    pass_name = input('Insert your password key name.')
    pass_len = random.randint(8, 18)
    counter = 0
    password_chars = []
    while counter < pass_len:
        for c in characters:
            random_character = random.choice(c)
            password_chars.append(random_character)
            counter += 1
            if counter >= pass_len:
                break
    pw = "".join(password_chars)
    with open("passwords.txt", "a") as myfile:
        myfile.write(f'{pass_name}: {pw} \n')
    print('Password(s) saved at passwords.txt.')

secure_password()
