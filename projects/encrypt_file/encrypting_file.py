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

    """ 使用公钥加密文件,混合加密方法，即 PKCS#1 OAEP"""

    with open(result_file, 'wb') as out_file:
        # 导入公钥
        recipient_key = RSA.import_key(open(public_rsa_key).read())

        print('recipient_key', recipient_key)

        session_key = get_random_bytes(16)

        # 使用公钥匙产生 PKCS1_OAEP 对象，对随机数进行加密，写入文件
        cipher_rsa = PKCS1_OAEP.new(recipient_key)
        out_file.write(cipher_rsa.encrypt(session_key))

        # 使用随机数产生 AES 对象，对文件内容进行加密，写入文件
        cipher_aes = AES.new(session_key, AES.MODE_EAX)
        with open(target_file, 'rb') as f:
            data = f.read()

        # 对内容进行加密和摘要
        ciphertext, tag = cipher_aes.encrypt_and_digest(data)
        out_file.write(cipher_aes.nonce)

        # 写入 二进制标签
        out_file.write(tag)

        # 已经加密对内容
        out_file.write(ciphertext)


def decryption_file(result_file, code):
    """ 使用私钥解密文件 """

    with open(result_file, 'rb') as fobj:
        private_key = RSA.import_key(
            open(private_rsa_key).read(),
            passphrase=code)
        # 会话密钥,16字节随机数,16字节消息认证码, 加密的数据
        enc_session_key, nonce, tag, ciphertext = [fobj.read(x) for x in (private_key.size_in_bytes(), 16, 16, -1)]

        # PKCS1_OAEP 使用私钥创建对象，解密出加密时对 16 位随机数
        cipher_rsa = PKCS1_OAEP.new(private_key)
        session_key = cipher_rsa.decrypt(enc_session_key)

        # 再使用 AES 根据 session_key 解密文本
        cipher_aes = AES.new(session_key, AES.MODE_EAX, nonce)
        data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    print('解密输出：', data.decode('utf-8'))


create_key(code)
encrypting_file(result_file, target_file)
decryption_file(result_file, code)
