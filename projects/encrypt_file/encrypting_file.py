# 使用 RSA  加密解密文件
import os
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from conf import BASE_DIR

private_rsa_key = os.path.join(BASE_DIR, 'projects', 'encrypt_file', 'private_rsa_key.pem')
public_rsa_key = os.path.join(BASE_DIR, 'projects', 'encrypt_file', 'public_rsa_key.pem')

target_file = os.path.join(BASE_DIR, 'projects', 'encrypt_file', 'comm_data.text')

result_file = os.path.join(BASE_DIR, 'projects', 'encrypt_file', 'result.text')

code = 'this_is_password'


def create_key(code):
    """ 创建密钥"""

    key = RSA.generate(2048)
    encrypted_key = key.exportKey(passphrase=code, pkcs=8,
                                  protection="scryptAndAES128-CBC")

    with open(private_rsa_key, 'wb') as f:
        f.write(encrypted_key)
    with open(public_rsa_key, 'wb') as f:
        f.write(key.publickey().exportKey())


def encrypting_file(result_file, target_file):
    """ 使用公钥加密文件 """

    with open(result_file, 'wb') as out_file:
        # 导入公钥
        recipient_key = RSA.import_key(open(public_rsa_key).read())

        session_key = get_random_bytes(16)
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))
        cipher_aes = AES.new(session_key, AES.MODE_EAX)

        with open(target_file, 'rb') as f:
            data = f.read()

        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        out_file.write(cipher_aes.nonce)
        out_file.write(tag)
        out_file.write(ciphertext)


def decryption_file(filename, code):
    """ 使用私钥解密文件 """

    with open(filename, 'rb') as fobj:
        private_key = RSA.import_key(
            open(private_rsa_key).read(),
            passphrase=code)
        enc_session_key, nonce, tag, ciphertext = [fobj.read(x)
                                                   for x in (private_key.size_in_bytes(),
                                                             16, 16, -1)]
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    print('解密输出：', data.decode('utf-8'))


create_key(code)
encrypting_file(result_file, target_file)
decryption_file(result_file, code)
