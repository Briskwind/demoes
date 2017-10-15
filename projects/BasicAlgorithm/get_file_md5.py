import base64
import hashlib


def md5_from_file(file_name, block_size=64 * 1024):
    """对文件进行 md5 摘要"""

    with open(file_name, 'rb') as f:
        md5 = hashlib.md5()
        while True:
            data = f.read(block_size)
            if not data:
                break
            md5.update(data)
        retmd5 = base64.b64encode(md5.digest())
        return retmd5