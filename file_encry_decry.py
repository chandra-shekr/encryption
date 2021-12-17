""" 
    Encrypts your file with a custom key phrase
"""

import base64
from Crypto.Cipher import AES
import getpass
import sys
import pdb

def salt_gen():
    """
        You enter you key phrase and it'll be converted to base64 string
    """
    salt = getpass.getpass("Enter salt: ")

    try:
        salt = base64.b64encode(salt.encode())
        return salt
    except Exception as ex:
        pdb.set_trace()
        return None

def key_gen():
    """Generate AES obj to encode or decode.
        This function calls salt_gen to get the key_phrase
    """
    try:

        key = AES.new(salt_gen(), AES.MODE_CFB, 'This is an IV456')
        print("key Generated")
        return key
    except Exception as ex1:
        print(ex1)
        return None

def encry(file_path):

    key_gen_obj = key_gen()
    if key_gen_obj is None:
        print("Sorry, cannot continue the process. Exiting now......")
    with open(str(file_path), 'rb') as f:
        data = f.read()
    encry_data = key_gen_obj.encrypt(data)
    encry_data = base64.b64encode(encry_data)
    with open(file_path, 'wb') as f:
        f.write(encry_data)
    print("File successfully encrypted")

def decry(file_path):

    key_gen_obj = key_gen()
    if key_gen_obj is None:
        print("Sorry, cannot continue the process. Exiting now......")
    with open(str(file_path), 'rb') as f:
        data = f.read()
    data = base64.b64decode(data)
    decry_data = key_gen_obj.decrypt(data)
    with open(file_path, 'wb') as f:
        f.write(decry_data)
    print("File successfully decrypted")


if __name__ == '__main__':

    file_path = str(sys.argv[1])
    choice = input("Do you want to Encrypt (E) or Decrypt (D). Press 'q' to quit: ").lower()
    if(choice =='e' and len(file_path) > 2):
        encry(file_path)
    elif (choice=='d' and len(file_path) > 2):
        decry(file_path)
    else:
        print("Invalid choice.Exiting now.... ")
