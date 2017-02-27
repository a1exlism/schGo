# -*- coding: utf-8 -*-

import pytest

import os
from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)
from cryptography.hazmat.backends import default_backend

from sgo.auth.utils import encrypt, decrypt

def encrypt_temp(key, plaintext, associated_data):
    # Generate a random 96-bit IV.
    iv = os.urandom(12)

    # Construct an AES-GCM Cipher object with the given key and a
    # randomly generated IV.
    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    ).encryptor()

    # associated_data will be authenticated but not encrypted,
    # it must also be passed in on decryption.
    encryptor.authenticate_additional_data(associated_data)

    # Encrypt the plaintext and get the associated ciphertext.
    # GCM does not require padding.
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return (iv, ciphertext, encryptor.tag)


def decrypt_temp(key, associated_data, iv, ciphertext, tag):
    # Construct a Cipher object, with the key, iv, and additionally the
    # GCM tag used for authenticating the message.
    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
        backend=default_backend()
    ).decryptor()

    # We put associated_data back in or the tag will fail to verify
    # when we finalize the decryptor.
    decryptor.authenticate_additional_data(associated_data)

    # Decryption gets us the authenticated plaintext.
    # If the tag does not match an InvalidTag exception will be raised.
    return decryptor.update(ciphertext) + decryptor.finalize()


@pytest.mark.usefixtures('app')
@pytest.mark.usefixtures('db')
@pytest.mark.usefixtures('client')
class TestAuth(object):
    def test_aes(self):
        from sgo.config import BaseConfig
        key = BaseConfig.SECRET_KEY
        iv, ciphertext, tag = encrypt_temp(
            key,
            b"a secret message!",
            b"authenticated but not encrypted payload"
        )

        assert (decrypt_temp(
            key,
            b"authenticated but not encrypted payload",
            iv,
            ciphertext,
            tag
        ))

    def test_aes_me(self):
        msg = b'a secret message'
        assert msg == decrypt(encrypt(msg))

    def test_encrypt(self):
        msg = b'a secret message'
        "Take Cautions Here"
        "cipher in different client should be the same"
        assert encrypt(msg) == b'pz\x96\x13\xba(\re\xeb\x833\xf0;\xcd\x167'

