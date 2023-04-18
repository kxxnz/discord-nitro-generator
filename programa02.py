import random
import string
import os
import requests

def generate_code(attempts=1):
    prefix = ['https://discord.gift/', 'https://discord.com/gift/']
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    code = ''.join(random.choice(letters) for i in range(16))
    gift_code = random.choice(prefix) + code
    response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{gift_code}?with_application=false&with_subscription_plan=true')
    if response.status_code == 200:
        return gift_code
    elif attempts < 1000:  # aumentando para 20 tentativas
        print(f"Tentativa {attempts} falhou. Tentando novamente...")
        return generate_code(attempts + 1)
    else:
        raise Exception(f"Não foi possível gerar um código válido após {attempts} tentativas.")

def generate_codes(num_codes):
    codes = []
    for i in range(num_codes):
        try:
            code = generate_code()
            codes.append(code)
        except Exception as e:
            print(e)
            print(f"Não foi possível gerar o código {i+1}.")
    return codes

def validate_codes(codes):
    valid_codes = []
    for code in codes:
        response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{code}?with_application=false&with_subscription_plan=true')
        if response.status_code == 200:
            valid_codes.append(code)
    return valid_codes

if __name__ == '__main__':
    num_codes = 10
    codes = generate_codes(num_codes)
    
    folder_name = "Nitro Codes"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = f"{folder_name}/nitro_codes.txt"
    with open(file_name, "w") as f:
        for code in codes:
            f.write(f"{code}\n")
    
    print(f"{num_codes} códigos gerados e salvos em {file_name}!")
    
    valid_codes = validate_codes(codes)
    
    valid_folder_name = "Valid Nitro Codes"
    if not os.path.exists(valid_folder_name):
        os.makedirs(valid_folder_name)

    valid_file_name = f"{valid_folder_name}/valid_nitro_codes.txt"
    with open(valid_file_name, "w") as f:
        for code in valid_codes:
            f.write(f"{code}\n")
    
    print(f"{len(valid_codes)} códigos válidos salvos em {valid_file_name}!")