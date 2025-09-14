DIGITS = "abcdefghijklmnopqrstuvwxyz"
BASE = 26

def to_base26(n: int) -> str:
    if n == 0:
        return DIGITS[0]
    result = []
    while n > 0:
        n, remainder = divmod(n, BASE)
        result.append(DIGITS[remainder])
    return ''.join(reversed(result))

def from_base26(s: str) -> int:
    n = 0
    for ch in s:
        n = n * BASE + DIGITS.index(ch)
    return n


def encryptor(text, key):
    cleaned = text.lower().replace(" ", "")
    encrypted_rows = []
    for i in range(0, len(cleaned), 8):
        row = cleaned[i:i+8]
        if len(row) < 8:
            row += 'a' * (8 - len(row))
        encrypted_rows.append(row)
    
    final_encrypted = ""
    for block in encrypted_rows:
        block_num = from_base26(block)
        block_num += key
        block_encrypted = to_base26(block_num)
        if len(block_encrypted) < 8:
            block_encrypted = 'a' * (8 - len(block_encrypted)) + block_encrypted
        final_encrypted += block_encrypted
    print(f"Encrypted String :{final_encrypted}")
    return final_encrypted
    


def decryptor(final_encrypted, key):
    encrypted_rows = []
    for i in range(0, len(final_encrypted), 8):
        row = final_encrypted[i:i+8]
        if len(row) < 8:
            row += 'a' * (8 - len(row))
        encrypted_rows.append(row)
    
    decrypted_text = ""
    for block in encrypted_rows:
        block_num = from_base26(block)
        block_num -= key
        block_decrypted = to_base26(block_num)
        if len(block_decrypted) < 8:
            block_decrypted = 'a' * (8 - len(block_decrypted)) + block_decrypted
        decrypted_text += block_decrypted
    
    return decrypted_text







text = "Through the flames of war Through the wire Through the living through the wall for the chance to be with you ill gladly risk it all"
final_len = len(text.replace(" ", ""))
space_arr = [i for i, ch in enumerate(text) if ch == " "]

encrypted = encryptor(text, 2313424)
decrypted = decryptor(encrypted, 2313424)

decrypted = decrypted[:final_len]
decrypted_list = list(decrypted)
for space in space_arr:
    decrypted_list.insert(space, " ")

decrypted_with_spaces = "".join(decrypted_list)
print(decrypted_with_spaces)

