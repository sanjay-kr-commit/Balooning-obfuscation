import sys
import hashlib

def get_keystream(password, position):
    data = f"{password}:{position}".encode()
    digest = hashlib.sha256(data).digest()

    return int.from_bytes(digest[:2], "big")

def decode_message(encoded, password):
    result = []

    for pos, index in enumerate(range(0, len(encoded), 5)):
        block = encoded[index:index + 5]

        encoded_num = int(block, 16)

        chaos = get_keystream(password, pos)

        transformed = encoded_num - chaos

        reversed_hex = f"{transformed:X}"

        original_hex = reversed_hex[::-1][:-1]

        result.append(chr(int(original_hex, 16)))

    return "".join(result)

if not sys.stdin.isatty():
    encoded = sys.stdin.read().rstrip("\n").rstrip("\r")
    password = sys.argv[1]
else:
    encoded = input("Encoded: ")
    password = input("Password: ")

print(decode_message(encoded, password), end="")