import sys
import random

def encode_message(user_input):
    # The salt is now a ghost, chosen by chance
    salt = random.randint(1, 0xFFF)
    salt_hex = f"{salt:X}"
    
    # Store the salt's length using our bucket logic
    salt_prefix_char = str(len(salt_hex))
    
    A, B, C = 37, 59, 101
    M = 0xFFF
    encoded_segments = ""
    
    for i, char in enumerate(user_input):
        ascii_val = ord(char)
        hex_val = f"{ascii_val:02X}"
        hex_with_suffix = hex_val + "1"
        reversed_hex = hex_with_suffix[::-1]
        num_val = int(reversed_hex, 16)
        
        chaos_step = (A * (i ** 2) + B * i + C) % M
        salted_num = num_val + salt + chaos_step
        final_hex = f"{salted_num:X}"

        prefix_char = str(len(final_hex))
        encoded_segments += prefix_char + final_hex

    # The prefix now holds the key to the salt, then the salt itself
    return f"{salt_prefix_char}{salt_hex}{encoded_segments}"

if not sys.stdin.isatty():
    input_string = sys.stdin.read().removesuffix("\r")
else:
    input_string = input("Enter your message: ")

result = encode_message(input_string)
print(result, end="")