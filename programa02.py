import random
import string
import os

def generate_code():
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    code = ''.join(random.choice(letters) for i in range(16))
    return f"https://discord.gift/{code}"

def generate_codes(num_codes):
    codes = []
    for i in range(num_codes):
        code = generate_code()
        codes.append(code)
    return codes

if __name__ == '__main__':
    num_codes = 2
    codes = generate_codes(num_codes)
    
    folder_name = "Nitro Codes"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = f"{folder_name}/nitro_codes.txt"
    with open(file_name, "w") as f:
        for code in codes:
            f.write(f"{code}\n")
    
    print(f"{num_codes} Códigos gerados e salvos em {file_name}!")