import sys
import hashlib

def get_keystream(password, position):
    data = f"{password}:{position}".encode()
    digest = hashlib.sha256(data).digest()

    return int.from_bytes(digest[:2], "big")

def encode_message(message, password):
    encoded = []

    for i, char in enumerate(message):
        ascii_val = ord(char)

        hex_val = f"{ascii_val:02X}"
        transformed = int((hex_val + "1")[::-1], 16)

        chaos = get_keystream(password, i)

        encoded_num = transformed + chaos

        encoded.append(f"{encoded_num:05X}")

    return "".join(encoded)

if not sys.stdin.isatty():
    message = sys.stdin.read().rstrip("\n").rstrip("\r")
    password = sys.argv[1]
else:
    message = input("Message: ")
    password = input("Password: ")

print(encode_message(message, password), end="")