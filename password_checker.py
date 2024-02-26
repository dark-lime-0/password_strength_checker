import re

print('''
 _____                                              _____ 
( ___ )                                            ( ___ )
 |   |~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|   | 
 |   |  ____                                     _  |   | 
 |   | |  _ \ __ _ ___ _____      _____  _ __ __| | |   | 
 |   | | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | |   | 
 |   | |  __/ (_| \__ \__ \\\ V  V / (_) | | | (_| | |   | 
 |   | |_|__ \__,_|___/___/ \_/\_/ \___/|_|_ \__,_| |   | 
 |   | / ___|| |_ _ __ ___ _ __   __ _| |_| |__     |   | 
 |   | \___ \| __| '__/ _ \ '_ \ / _` | __| '_ \    |   | 
 |   |  ___) | |_| | |  __/ | | | (_| | |_| | | |   |   | 
 |   | |____/ \__|_|  \___|_| |_|\__, |\__|_| |_|   |   | 
 |   |  / ___| |__   ___  ___| | |___/ _ __         |   | 
 |   | | |   | '_ \ / _ \/ __| |/ / _ \ '__|        |   | 
 |   | | |___| | | |  __/ (__|   <  __/ |           |   | 
 |   |  \____|_| |_|\___|\___|_|\_\___|_|           |   | 
 |___|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|___| 
(_____)                                            (_____)
                  v0.01 by dark-lime-0
''')

print("Create a strong password by combining uppercase and lowercase letters, numbers, and special characters. \n"
      "Avoid using common words or patterns. Your security is important to us!\n"
      "======================================================================================================\n"
      "======================================================================================================")

def check(passwd):
    lenght = len(passwd)
    has_lower = re.search(r'[a-z]', passwd)
    has_upper = re.search(r'[A-Z]',passwd)
    has_digits = re.search(r'[0-9]', passwd)
    has_special = re.search(r'[ !@#$%^&*()_+{}|\[\]:;<>,.?/~`]', passwd)

    a=0
    with open('common_passwords.txt', 'r') as f:
        common_passwords = f.read().splitlines()
        if (passwd.lower() in common_passwords):
            a+=1


    if(lenght>=12 and has_lower and has_upper and has_digits and has_special and a==0):
        return 'Strong'
    elif(lenght>=8 and has_lower and has_upper and has_digits):
        return 'Medium'
    else:
        return 'Weak'


while True :
    print(f"Your Password Is a {check(input('enter your password :'))} Password !!")

