# -*- coding: utf-8 -*-

from sgo.config import BaseConfig

from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
from cryptography.hazmat.backends import default_backend
import time

from sgo.extensions import token_auth

BaseCipher = Cipher(algorithm=algorithms.AES(BaseConfig.SECRET_KEY),
                    mode=modes.CBC(BaseConfig.AES_IV),
                    backend=default_backend())


def encrypt(plaintext):
    """

    :param plaintext: bytes
    :return: bytes
    """
    encryptor = BaseCipher.encryptor()
    cipher = encryptor.update(plaintext) + encryptor.finalize()
    return cipher


def decrypt(cipher):
    """

    :param cipher: bytes
    :return: bytes
    """
    decryptor = BaseCipher.decryptor()
    plaintext = decryptor.update(cipher) + decryptor.finalize()
    return plaintext


def timestamp():
    """
    generate timestamp
    do not define which time standard or zone is being used

    :return: int, seconds since epoch
    """
    return time.time()

