import nltk
nltk.download('words')
from nltk.corpus import words

def vigenere_decrypt(ciphertext, key):
    decrypted = ''
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index]) - ord('A')
            decrypted += chr((ord(char) - shift - ord('A')) % 26 + ord('A'))
            key_index = (key_index + 1) % len(key)
        else:
            decrypted += char
    return decrypted

word_list = words.words()
ciphertext = "OOGNVMTNTCLUOGZSZSHTXAZGMOMEPKWDDQM"

found_key = None
decrypted_text = None

for word in word_list:
    decrypted_attempt = vigenere_decrypt(ciphertext, word.upper())
    decrypted_words = decrypted_attempt.split()
    if all(w in word_list for w in decrypted_words):
        found_key = word.upper()
        decrypted_text = decrypted_attempt
        break

if found_key:
    print("Found Key:", found_key)
    print("Decrypted Message:", decrypted_text)
else:
    print("Key not found.")
