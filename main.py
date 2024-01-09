def encrypt(msg, n):
    encrypted_msg = ""
    for ch in msg:
        if ch.isalpha():
            val = ord(ch)
            val = val - n
            val = ((val - ord("A")) % 26) + ord("A")
            val = chr(val)
        else:
            val = ch
        encrypted_msg = encrypted_msg + val
    return encrypted_msg

print(encrypt("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 3))
#Should return QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD

def decrypt(encrypted_msg, n):
    clear_msg = ""
    for ch in encrypted_msg:
        if ch.isalpha():
            val = ord(ch)
            val = val + n
            val = ((val - ord("A")) % 26) + ord("A")
            val = chr(val)
        else:
            val = ch
        clear_msg = clear_msg + val
    return clear_msg

print(decrypt("QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD", 3))
#Should return THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG

def decrypt_and_encrypt_textfile():
    f1 = open("clearText.txt", "r")
    f2 = open("encryptedText.txt", "a")
    lines = f1.readlines()
    for l in lines:
        l = l.upper()
        l = encrypt(l.upper(), 3)
        f2.write(l)

decrypt_and_encrypt_textfile()

def frequency_analysis():
    fre_map = {}
    file = open("encryptedText.txt", "r")
    lines = file.readlines()
    for line in lines:
        for ch in line:
            if ch.isalpha():
                if ch not in fre_map.keys():
                    fre_map[ch] = 1
                else:
                    fre_map[ch] = fre_map[ch] + 1

    for k in sorted(fre_map.keys()):
        print(f"{k} occours {fre_map[k]} times in the encrypted text.")

frequency_analysis()