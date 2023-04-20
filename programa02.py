import random
import string
import os
import requests
import threading

def generate_code(max_attempts=1000, attempts=1, codes=[]):
    prefix = ['https://discord.gift/', 'https://discord.com/gift/']
    letters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    code = ''.join(random.choice(letters) for i in range(16))
    gift_code = random.choice(prefix) + code
    response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes/{gift_code}?with_application=false&with_subscription_plan=true')
    if response.status_code == 200:
        codes.append(gift_code)
    elif attempts < max_attempts:
        print(f"Tentativa {attempts} falhou. Tentando novamente...")
        generate_code(max_attempts, attempts + 1, codes)
    else:
        print(f"Não foi possível gerar um código válido após {attempts} tentativas.")

def generate_codes(num_codes, max_attempts=1000):
    codes = []
    threads = []
    for i in range(num_codes):
        thread = threading.Thread(target=generate_code, args=(max_attempts, 1, codes))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    return codes

def validate_codes(codes):
    valid_codes = []
    invalid_codes = []
    code_batches = [codes[i:i + 100] for i in range(0, len(codes), 100)]
    for batch in code_batches:
        codes_str = ','.join(batch)
        response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes?codes={codes_str}&with_application=false&with_subscription_plan=true')
        if response.status_code == 200:
            data = response.json()
            for i, result in enumerate(data):
                if result['code'] in batch and result['uses'] is None:
                    valid_codes.append(result['code'])
                else:
                    invalid_codes.append(result['code'])
        else:
            print(f"Não foi possível verificar os códigos {batch}. Status code: {response.status_code}")
    return valid_codes, invalid_codes

def generate_nitro_codes(num_codes, max_attempts):
    codes = generate_codes(num_codes, max_attempts)

    folder_name = "Nitro Codes"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = f"{folder_name}/nitro_codes.txt"
    with open(file_name, "w") as f:
        for code in codes:
            f.write(f"{code}\n")

    print(f"{num_codes} códigos gerados e salvos em {file_name}!")

    valid_codes, invalid_codes = validate_codes(codes)

    valid_folder_name = "Valid Nitro Codes"
    if not os.path.exists(valid_folder_name):
        os.makedirs(valid_folder_name)

    valid_file_name = f"{valid_folder_name}/valid_nitro_codes.txt"
    with open(valid_file_name, "w") as f:
        for code in valid_codes:
            f.write(f"{code}\n")

    print(f"{len(valid_codes)} códigos válidos salvos em {valid_file_name}!")
    print(f"{len(invalid_codes)} códigos inválidos encontrados.")

if __name__ == "__main__":
    num_codes = int(input("Digite o número de códigos Nitro a serem gerados: "))
    max_attempts = int(input("Digite o número máximo de tentativas para gerar cada código: "))

def generate_codes(num_codes, max_attempts=1000):
    codes = []
    threads = []
    for i in range(num_codes):
        thread = threading.Thread(target=generate_code, args=(max_attempts, 1, codes))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

    return codes

def validate_codes(codes):
    valid_codes = []
    invalid_codes = []
    code_batches = [codes[i:i + 100] for i in range(0, len(codes), 100)]
    for batch in code_batches:
        codes_str = ','.join(batch)
        response = requests.get(f'https://discordapp.com/api/v6/entitlements/gift-codes?codes={codes_str}&with_application=false&with_subscription_plan=true')
        if response.status_code == 200:
            data = response.json()
            for i, result in enumerate(data):
                if result['code'] in batch and result['uses'] is None:
                    valid_codes.append(result['code'])
                else:
                    invalid_codes.append(result['code'])
        else:
            print(f"Não foi possível verificar os códigos {batch}. Status code: {response.status_code}")
    return valid_codes, invalid_codes

def generate_nitro_codes(num_codes, max_attempts):
    codes = generate_codes(num_codes, max_attempts)

    folder_name = "Nitro Codes"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    file_name = f"{folder_name}/nitro_codes.txt"
    with open(file_name, "w") as f:
        for code in codes:
            f.write(f"{code}\n")

    print(f"{num_codes} códigos gerados e salvos em {file_name}!")

    valid_codes, invalid_codes = validate_codes(codes)

    valid_folder_name = "Valid Nitro Codes"
    if not os.path.exists(valid_folder_name):
        os.makedirs(valid_folder_name)

    valid_file_name = f"{valid_folder_name}/valid_nitro_codes.txt"
    with open(valid_file_name, "w") as f:
        for code in valid_codes:
            f.write(f"{code}\n")

    print(f"{len(valid_codes)} códigos válidos salvos em {valid_file_name}!")
    print(f"{len(invalid_codes)} códigos inválidos encontrados.")

if __name__ == "__main__":
    num_codes = int(input("Digite o número de códigos Nitro a serem gerados: "))
    max_attempts = int(input("Digite o número máximo de tentativas para gerar cada código: "))
    generate_nitro_codes(num_codes, max_attempts)
