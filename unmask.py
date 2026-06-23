import sys

def decode_message(encoded_output):
    # Extract the salt prefix length
    salt_length = int(encoded_output[0])
    
    # Extract the actual random salt
    salt_hex = encoded_output[1 : 1 + salt_length]
    salt = int(salt_hex, 16)

    index = 1 + salt_length
    decoded_message = ""

    A, B, C = 37, 59, 101
    M = 0xFFF
    i = 0

    while index < len(encoded_output):
        segment_length = int(encoded_output[index])
        index += 1

        current_hex = encoded_output[index : index + segment_length]
        index += segment_length

        salted_num = int(current_hex, 16)
        chaos_step = (A * (i ** 2) + B * i + C) % M
        
        num_val = salted_num - salt - chaos_step
        i += 1

        reversed_hex = f"{num_val:X}"
        hex_val = reversed_hex[::-1][:-1]
        decoded_message += chr(int(hex_val, 16))

    return decoded_message

if not sys.stdin.isatty():
    input_string = sys.stdin.read().removesuffix("\n").removesuffix("\r")
else:
    input_string = input("Enter encoded message: ")

decoded_string = decode_message(input_string)
print(decoded_string, end="")