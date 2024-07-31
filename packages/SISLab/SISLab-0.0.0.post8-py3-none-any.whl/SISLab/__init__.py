__version__ = '0.0.0-8'

import os
from cryptography.fernet import Fernet

def load_key_checker():
    encryption_key = os.environ.get('SISLAB_ENCRYPTION_KEY')
    if not encryption_key:
        raise ValueError("Encryption key not found in environment variables.")

    current_dir = os.path.dirname(os.path.abspath(__file__))
    encrypted_file = os.path.join(current_dir, 'key_checker.py.enc')

    f = Fernet(encryption_key.encode())
    with open(encrypted_file, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)

    exec(decrypted_data)
    return locals()['check_key']

try:
    check_key = load_key_checker()
    check_key()
    # 키 검증이 성공하면 나머지 모듈을 import합니다
    from .utils.loader import *
    from .utils.proccessor.image import *
    # 기타 필요한 import 문들...
except ValueError as e:
    print(f"SISLab activation failed: {e}")
    # 키 검증 실패 시 제한된 기능만 제공하거나 에러를 발생시킬 수 있습니다
