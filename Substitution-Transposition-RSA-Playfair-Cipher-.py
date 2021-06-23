# Substitution Cipher
import itertools
import string
import random

# A list containing all characters
all_letters = string.ascii_letters

"""
create a dictionary to store the substitution
for the given alphabet in the plain text
based on the key
"""

dict1 = {}

dict2 = {}


# substitution


def substitution(stringg, key=4):
    # substitution
    for i in range(len(all_letters)):
        dict1[all_letters[i]] = all_letters[(i + key) % len(all_letters)]

    plain_txt = stringg
    cipher_txt = []
    # loop to generate ciphertext
    for char in plain_txt:
        if char in all_letters:
            temp = dict1[char]
            cipher_txt.append(temp)
        else:
            temp = char
            cipher_txt.append(temp)

    cipher_txt = "".join(cipher_txt)
    print("Cipher Text is: ", cipher_txt)
    """
    create a dictionary to store the substitution
    for the given alphabet in the cipher
    text based on the key
    """
    dict2 = {}
    for i in range(len(all_letters)):
        dict2[all_letters[i]] = all_letters[(i - key) % (len(all_letters))]

    # loop to recover plain text
    decrypt_txt = []

    for char in cipher_txt:
        if char in all_letters:
            temp = dict2[char]
            decrypt_txt.append(temp)
        else:
            temp = char
            decrypt_txt.append(temp)

    decrypt_txt = "".join(decrypt_txt)
    print("Recovered plain text :", decrypt_txt)

print("*****-substitution-****")

strin = input("Enter string -substitution -:")
ke = input("Enter key-substitution-:")

substitution(strin, int(ke))
########################################################################

def Transposition(text, encryption, key):
    rail = [['\n' for i in range(len(text))] for j in range(key)]

    # to find the direction

    dir_down = False
    (row, col) = (0, 0)

    if encryption == True:

        for i in range(len(text)):

            # check the direction of flow
            # reverse the direction if we've just
            # filled the top or bottom rail

            if row == 0 or row == key - 1:
                dir_down = not dir_down

            # fill the corresponding alphabet

            rail[row][col] = text[i]
            col += 1

            # find the next row using
            # direction flag

            if dir_down:
                row += 1
            else:
                row -= 1

        # now we can construct the cipher
        # using the rail matrix

        result = []
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] != '\n':
                    result.append(rail[i][j])
        return ''.join(result)

    # Decryption

    if encryption == False:

        for i in range(len(text)):

            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            # place the marker

            rail[row][col] = '*'
            col += 1

            # find the next row
            # using direction flag

            if dir_down:
                row += 1
            else:
                row -= 1

        # now we can construct the
        # fill the rail matrix

        index = 0
        for i in range(key):
            for j in range(len(text)):
                if rail[i][j] == '*' and index < len(text):
                    rail[i][j] = text[index]
                    index += 1

        # now read the matrix in
        # zig-zag manner to construct
        # the resultant text

        result = []
        (row, col) = (0, 0)
        for i in range(len(text)):

            # check the direction of flow

            if row == 0:
                dir_down = True
            if row == key - 1:
                dir_down = False

            # place the marker

            if rail[row][col] != '*':
                result.append(rail[row][col])
                col += 1

            # find the next row using
            # direction flag

            if dir_down:
                row += 1
            else:
                row -= 1
        return ''.join(result)
print("-************Transposition-********")
strr = input("Enter string -Transposition -:")
numm = int(input("Enter key-Transposition-:"))
Encrypted = Transposition(strr, True, numm)
print(Encrypted, '\n')
print(Transposition(Encrypted, False, numm))
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################

#RSA
print("***************-RSA-***********")
def is_prime(x):
    '''
    Takes an integer x and returns True if x is a prime number
    and Flase if x is not a prime number.
    '''
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    else:
        return True


def gcd(a, b):
    '''
    Computes the Greates Common Divisor (gcd) between integers a, b.
    '''
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def extended_gcd(x, y):
    '''
    Extended Euclidean algortihm between integers x, y to find
    the modular multiplicative inverse d of x under modulo y.
    '''
    if y == 0:
        return x, 1, 0

    d, a, b = extended_gcd(y, x % y)

    return d, b, a - (x // y) * b


def RSAencrypt(public_key, message):
    '''
    Encryptes a string message using a public_key as a tuple of (n, e).
    '''
    encrypted = []
    for character in message:
        int_message = ord(character)
        n, e = public_key
        c = pow(int_message, e) % n
        encrypted.append(c)
    return encrypted


def RSAdecrypt(private_key, encrypted):
    '''
    Decryptes a string message using a private_key as a tuple of (n, d).
    '''
    decrypted = []
    for character in encrypted:
        n, d = private_key
        int_message = pow(character, d) % n
        message = chr(int_message)
        decrypted.append(message)
    return decrypted


#############################RSA MAIN CODE########################################################
primes = [i for i in range(100, 500) if is_prime(i)]
p = random.choice(primes)
q = random.choice(primes)
message = input('Enter the text to be encrypted-RSA-: ')

n = p * q
k = (p - 1) * (q - 1)

for e in range(2, k):
    if gcd(e, k) == 1:
        break

public_key = (n, e)

_, b, _ = extended_gcd(e, k)
if b < 0:
    b = b + k
private_key = (n, b)

encrypted = RSAencrypt(public_key, message)
print(f'Encrypted message: {"".join(str(s) for s in encrypted)}')

decrypted = RSAdecrypt(private_key, encrypted)
print(f'Decrypted message: {"".join(str(s) for s in decrypted)}')
################################################################################################
################################################################################################
################################################################################################
################################################################################################
################################################################################################
print("*******************-playfair-************************")
def chunker(seq, size):
    it = iter(seq)
    while True:
        chunk = tuple(itertools.islice(it, size))
        if not chunk:
            return
        yield chunk


def prepare_input(dirty):
    # Prepare the plaintext by up-casing it
    # and separating repeated letters with X's

    dirty = "".join([c.upper() for c in dirty if c in string.ascii_letters])
    clean = ""

    if len(dirty) < 2:
        return dirty

    for i in range(len(dirty) - 1):
        clean += dirty[i]

        if dirty[i] == dirty[i + 1]:
            clean += "X"

    clean += dirty[-1]

    if len(clean) & 1:
        clean += "X"

    return clean


def generate_table(key):
    # I and J are used interchangeably to allow
    # us to use a 5x5 table (25 letters)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    # we're using a list instead of a '2d' array because it makes the math
    # for setting up the table and doing the actual encoding/decoding simpler
    table = []

    # copy key chars into the table if they are in `alphabet` ignoring duplicates
    for char in key.upper():
        if char not in table and char in alphabet:
            table.append(char)

    # fill the rest of the table in with the remaining alphabet chars
    for char in alphabet:
        if char not in table:
            table.append(char)

    return table


def encode(plaintext, key):
    table = generate_table(key)
    plaintext = prepare_input(plaintext)
    ciphertext = ""

    for char1, char2 in chunker(plaintext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            ciphertext += table[row1 * 5 + (col1 + 1) % 5]
            ciphertext += table[row2 * 5 + (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += table[((row1 + 1) % 5) * 5 + col1]
            ciphertext += table[((row2 + 1) % 5) * 5 + col2]
        else:  # rectangle
            ciphertext += table[row1 * 5 + col2]
            ciphertext += table[row2 * 5 + col1]
        ciphertext += " "
    return ciphertext


def decode(ciphertext, key):
    table = generate_table(key)
    ciphertext = prepare_input(ciphertext)
    plaintext = ""

    for char1, char2 in chunker(ciphertext, 2):
        row1, col1 = divmod(table.index(char1), 5)
        row2, col2 = divmod(table.index(char2), 5)

        if row1 == row2:
            plaintext += table[row1 * 5 + (col1 - 1) % 5]
            plaintext += table[row2 * 5 + (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += table[((row1 - 1) % 5) * 5 + col1]
            plaintext += table[((row2 - 1) % 5) * 5 + col2]
        else:  # rectangle
            plaintext += table[row1 * 5 + col2]
            plaintext += table[row2 * 5 + col1]
        plaintext += " "
    return plaintext


strin = input("Enter string-playfair-:")
ke = input("Enter key-playfair-:")
ciphertext = encode(strin, ke)
plaintext = decode(ciphertext, ke)
print("Cipher Text is: ", ciphertext)
print("Recovered plain text :", plaintext)


