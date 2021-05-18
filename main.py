import random

# caesar encryption method
def encrypt(message, shift):
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    encrypted_message = ""
    shift = int(shift)
    for char in message:
        if(char.lower() in chars):
            # calculate current index and target shifted index
            current_index = chars.index(char.lower())
            shifted_index = current_index + shift
            if(shifted_index > 25):
                shifted_index = shifted_index - 26 # make sure program doesn't throw an error if target index is > 25
            if(char.isupper()): # handle case
                encrypted_message = encrypted_message + chars[shifted_index].upper()
            else:
                encrypted_message = encrypted_message + chars[shifted_index]
        else:
            encrypted_message = encrypted_message + char
    return encrypted_message

# handle encryption
def encryption_handler():
    # get the unencrypted message
    input_valid = False
    while(input_valid != True):
        print('\nPlease enter the message you wish to encrypt:')
        message = input()
        print("Enter'Y' to confirm and 'N' to re-enter your message")
        confirm = input()
        if(confirm == 'Y'):
            input_valid = True

    # get the number of shifts
    input_valid = False
    while(input_valid != True):
        print("\nPlease enter the number of shifts (enter 'R' for random)")
        shift = input()
        print("Enter'Y' to confirm and 'N' to re-enter the number")
        confirm = input()
        if(confirm == 'Y'):
            input_valid = True
            if(shift.lower() == 'r'):
                shift = random.randint(1, 25)
    print("Encrypted Message:\n" + encrypt(message, shift) + "\n")

# handle decryption
def decryption_handler():
    # get the decrypted message
    input_valid = False
    while(input_valid != True):
        print('\nPlease enter the message you wish to decrypt:')
        message = input()
        print("Enter'Y' to confirm and 'N' to re-enter your message")
        confirm = input()
        if(confirm == 'Y'):
            input_valid = True

    # get the number of shifts
    input_valid = False
    while(input_valid != True):
        print("\nPlease enter the number of shifts (enter 'A' to use brute force)")
        shift = input()
        print("Enter'Y' to confirm and 'N' to re-enter the number")
        confirm = input()
        if(confirm == 'Y'):
            input_valid = True
    print("Decrypted Message:\n" + decrypt(message, shift) + "\n")

# caesar decryption method
def decrypt(message, shift):
    chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    decrypted_message = ""
    if(shift.lower() != 'a'):
        # manual shift (assumes shift is known)
        shift = int(shift)
        for char in message:
            if(char.lower() in chars):
                # calculate current index and target shifted index
                current_index = chars.index(char.lower())
                shifted_index = current_index - shift
                if(shifted_index < 0):
                    shifted_index = 26 - shifted_index # make sure program doesn't throw an error if target index is > 25
                if(char.isupper()): # handle case
                    decrypted_message = decrypted_message + chars[shifted_index].upper()
                else:
                    decrypted_message = decrypted_message + chars[shifted_index]
            else:
                decrypted_message = decrypted_message + char
    else:
        # brute force shift (assumes shift is unknown)
        brute_shifts = [""] * 26
        attempted_shifts = 0
        while(attempted_shifts < 26):
            for char in message:
                if(char.lower() in chars):
                    # calculate current index and target shifted index
                    current_index = chars.index(char.lower())
                    shifted_index = current_index - attempted_shifts
                    if(shifted_index < 0):
                        shifted_index = 26 + shifted_index # make sure program doesn't throw an error if target index is > 25
                    if(char.isupper()): # handle case
                        brute_shifts[attempted_shifts] = brute_shifts[attempted_shifts] + chars[shifted_index].upper()
                    else:
                        brute_shifts[attempted_shifts] = brute_shifts[attempted_shifts] + chars[shifted_index]
                else:
                    brute_shifts[attempted_shifts] = brute_shifts[attempted_shifts] + char
            attempted_shifts += 1
        # check shift attempts
        relevance = [0] * 26 # keeps track of which brute force attempts are the most relevant
        keywords = ['this','at','in','for','to','the','that','you','me','from','on','we','they','them','us','with','and','or']
        index = 0
        for sentence in brute_shifts:
            for word in keywords:
                if(word in sentence):
                    relevance[index] += 1
            index += 1
        decrypted_message = brute_shifts[relevance.index(max(relevance))]
    return decrypted_message
        
# main loop
program_active = True
while(program_active):
    print('Press [0] to ENCRYPT A MESSAGE')
    print('Press [1] to DECRYPT A MESSAGE')
    print('Press [2] to EXIT PROGRAM')
    command = input()
    if(command == '0'):
        encryption_handler()
    elif(command == '1'):
        decryption_handler()
    elif(command == '2'):
        program_active = False
