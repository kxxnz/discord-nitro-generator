# discord-nitro-generator

This is a Python script that generates Discord Nitro codes and checks if they are valid. It uses the requests library to make HTTP requests to Discord's API and the threading library to generate multiple codes simultaneously.

The script first defines a function generate_code that generates a single code and checks if it is valid. If it is valid, it adds it to a list of codes. If it is not valid, it retries a certain number of times before giving up.

The generate_codes function creates a list of threads, each of which calls the generate_code function. Once all the threads have been started, it waits for them to finish before returning the list of generated codes.

The validate_codes function takes a list of codes and checks if they are valid by making an HTTP request to Discord's API. It groups the codes into batches of 100 to avoid making too many requests at once. It then checks the response for each code and determines whether it is valid or not.

Finally, the generate_nitro_codes function calls the generate_codes function to generate a specified number of codes, saves them to a file, and then calls the validate_codes function to check which codes are valid. It then saves the valid codes to a separate file and prints some statistics about the results.

Note that this script should only be used for educational purposes and generating codes without permission is against Discord's terms of service.
