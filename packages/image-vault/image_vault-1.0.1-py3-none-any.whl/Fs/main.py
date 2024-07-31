import os
import shutil
import hashlib
from io import BytesIO
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import binascii
from PIL import Image
import click
def key_gen(seed):
    seed=bytes(seed,"utf-8")
    seed_hash=hashlib.sha256()
    seed_hash.update(seed)
    return seed_hash.hexdigest()

def decrypt_file(input_file, seed_token):
    # Generate a key from the seed token
    key = seed_token.ljust(32)[:32].encode('utf-8')  # Ensure key is 32 bytes long

    # Read the hex data from the input file
    hex_data =input_file 

    # Convert the hex data back to binary
    encrypted_data_with_iv = binascii.unhexlify(hex_data)

    # Extract the IV and the encrypted data
    iv = encrypted_data_with_iv[:16]
    encrypted_data = encrypted_data_with_iv[16:]

    # Create a cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()

    # Decrypt the data
    padded_data = decryptor.update(encrypted_data) + decryptor.finalize()

    # Unpad the data
    unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
    data = unpadder.update(padded_data) + unpadder.finalize()
    print(f"Decrypted data")
    return data    
    

def encrypt_file(f_name,file_number,input_file,seed_token):
    # Generate a key from the seed token
    key = seed_token.ljust(32)[:32].encode('utf-8')  # Ensure key is 32 bytes long
    iv = os.urandom(16)  # Initialization vector

    # Create a cipher object
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()

    # Read the binary file
    data = input_file

    # Pad the data to make it a multiple of the block size
    padder = padding.PKCS7(algorithms.AES.block_size).padder()
    padded_data = padder.update(data) + padder.finalize()

    # Encrypt the data
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    # Convert to hex
    hex_data = binascii.hexlify(iv + encrypted_data).decode('utf-8')
    
    # Write the hex data to the output file
    with open(f'{f_name}{file_number}', 'w') as output_file:
        output_file.write(hex_data)

    print(f"Encrypted data written to {f_name}{file_number}")



def divide_file(path:str,parts:int,key):
    f_name=path.split(".")[0].replace("/","")
    paths=[]
    os.mkdir(f'./{f_name}')
    chunk_size=int(int(os.path.getsize(path))/parts)
    CHUNK_SIZE = chunk_size  # in bytes
    file_number = 0
    key=str(key_gen(key))
    with open(path, 'rb') as f:  # open in binary read mode
        chunk = f.read(CHUNK_SIZE)
        while chunk:
            paths.append(f"./{f_name}{file_number}")
            encrypt_file(f_name,file_number,chunk,key)
            file_number += 1
            chunk = f.read(CHUNK_SIZE)
    for i in paths:
        shutil.move(i,f'./{f_name}')
    return f_name

def combine_file(files:list,f_name:str,key:str):
    file=b''
    key=str(key_gen(key))
    for i in files:
        with open(i) as f:
            data=f.read()
        print(data)
        data = decrypt_file(data,key)
        file=file+data
    img=Image.open(BytesIO(file))
    img.save(f"./{f_name}.jpg")
    #plt.imshow(img)
    #plt.show()

def encrypt_folder(path:str,op_path:str,parts:int,key:str):
    os.chdir(path)
    enc_img_dir=[]
    total_img=len(os.listdir("./"))
    done=0
    for i in os.listdir("./"):
        enc_img_dir.append(f'./{divide_file(i,parts,key)}')
        done +=1
        print(f'###################{done}/{total_img}#######################')
    os.mkdir(f"./{op_path}")
    for i in enc_img_dir:
        shutil.move(i,f"./{op_path}")
    print("********************done*********************")

def decrypt_folder(path:str,key:str):
    total_img=len(os.listdir(path))
    done=0
    os.chdir(path)
    for i in os.listdir("./"):
        img=[]
        for x in os.listdir(i):
            img.append(f"./{i}/{x}")
        combine_file(img,f'{i}',key)
        done +=1
        print(f'###################{done}/{total_img}#######################')

@click.command()
@click.option("--encrypt",is_flag=True,help="use for encryption")
@click.option("--decrypt",is_flag=True,help="use for decryption")
@click.option("--input_path",help="mention input path",default="./")
@click.option("--output_path",help="mention output path",default="./op")
@click.option("--key",help="mention enc/dec key",default="1234")
@click.option("--parts",help="mention file division number",default="1")

def main(encrypt,decrypt,input_path,output_path,key,parts):
    if encrypt:
        parts=int(parts)
        encrypt_folder(input_path,output_path,parts,key)
    elif decrypt:
        decrypt_folder(input_path,key)
if __name__=="__main__":
    main()

'''
if __name__=="__main__":
    #encrypt_folder("./test/","./op",4,"tanish")
    decrypt_folder("./op/","tanish")
    #test
    divide_file("./images.jpg",2,"tanish")
    file_lst=[]
    img=b""
    path="./images/"
    for i in os.listdir(path):
        file_lst.append(f'{path}{i}')
    combine_file(file_lst,"tanish")
'''
