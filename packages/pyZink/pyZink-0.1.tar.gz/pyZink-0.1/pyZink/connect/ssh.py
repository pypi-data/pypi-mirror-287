#   pyZink > connect > ssh.py
#   morten@znk.dk
#   Created April 2024
"""
    This document contains the 'SSH_Client'-class that has functionality to connect to- and send commands to a host through the SSH-interface
"""

import paramiko
import time

class SSH_Client:
    """
    Python SSH-client for Cisco IOS using Paramiko
    morten@znk.dk - September 2023 

    Inspiration from https://stackoverflow.com/a/34110037
    Documentation: https://dok-vand.znk.dk/books/physical-networking/page/remote-reconfiguration

    Short Example of use:
    > with SSH_Client(10.10.10.123, john, pass1234) as ssh:
    >    output = ssh.send_command("ip_a", return_output=True)
    >    print(output)

    :param ip_address: The IP-address of the remote SSH-server you are trying to connect to
    :param username:   The username to the user you are trying to log into on the SSH-server
    :param password:   The password to the user you are trying to log into on the SSH-server
    :param read_time:  The time in ms that is waited from sending a message to reading the data in the buffer (ie. how log to wait for data) If the wait too short, not all data will get through.
    """

    def __init__(self, ip_address:str, username:str, password:str, show_all = True, wait_for_response_ms:int = 800) -> None:
        self.default_response_wait = wait_for_response_ms
        self.remote_conn_pre=paramiko.SSHClient()
        self.remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.remote_conn_pre.connect(ip_address, 
                                port=22,
                                username=username,  
                                password=password,
                                look_for_keys=False,
                                allow_agent=False)
        self.ssh_client = self.remote_conn_pre.invoke_shell()
        if show_all:
            self.send_command("ter d")

    def __enter__(self):
        """
        This is called when the 'with SSH_Client'-scope is entered. Used by Python.
        """        
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        """
        This is called when the 'with SSH_Client'-scope is exited. Used to correctly disconnect from SSH-session
        """
        self.close_connection()
    
    def send_command(self, command:str, return_output:bool = True, print_output:bool = False, wait_for_response_ms:float|None = None) -> str | None:
        """
        Sends a single command formatted as a string.
        If the output is returned, it is formatted as a string

        :param command:         The command to send to the switch
        :param return_output:   (Optional, defaults to True) the output of the command is captured and returned by the method
        :param print_output:    (Optional, defaults to False) the output of the command is captured and printed to the terminal
        """
        if not wait_for_response_ms: wait_for_response_ms = self.default_response_wait
        try: 
            self.ssh_client.send(f"{command}\n")
            time.sleep(wait_for_response_ms / 1000)
            if return_output or print_output:
                output = self.ssh_client.recv(65535)
                if return_output:
                    return output.decode()
                if print_output:
                    print(output.decode())
        except Exception as e:
            print(f"Something went wrong in SSH_Client -- {e}")

    def send_commands_list(self, command_list:list, return_output:bool = False, print_output:bool = True, wait_for_response_ms:float|None = None) -> list | None:
        """
        Sends single commands formatted as a strings from a list sequentially.
        If the output is returned, it is formatted as strings in a list ordered in the same order as the commands

        :param command_list:    The list of commands to send to the switch
        :param return_output:   (Optional, defaults to True) the output of the command is captured and returned by the method
        :param print_output:    (Optional, defaults to False) the output of the command is captured and printed to the terminal
        """        
        if not wait_for_response_ms: wait_for_response_ms = self.default_response_wait
        if return_output: output_list = []
        for command in command_list:
            try:
                self.ssh_client.send(f"{command}\n")
                time.sleep(wait_for_response_ms / 1000)
                if return_output or print_output:
                    output = self.ssh_client.recv(65535)
                    if return_output:
                        output_list.append(output.decode())
                    if print_output:
                        print(output.decode())
            except Exception as e:
                print(f"Something went wrong in SSH_Client -- {e}")
                # <------------------------------------------------------------------ #TODO Noget med en log-fil?
        if return_output: return output_list

    def send_commands_multiline(self, commands:str, return_output:bool = False, print_output:bool = True) -> list | None:
        """
        Sends a multitude of commands formatted as a multi-line string(docstring). Commands are seperated by newlines
        This is useful for sending an entire configuration in one go.
        If the output is returned, it is formatted as a string

        :param command:         The command to send to the switch
        :param return_output:   (Optional, defaults to True) the output of the command is captured and returned by the method
        :param print_output:    (Optional, defaults to False) the output of the command is captured and printed to the terminal
        """        
        commands_lines = commands.split("\n")
        output = self.send_commands_list(commands_lines, return_output, print_output)
        if return_output:
            return output

    def close_connection(self) -> None:
        """
        Steps required to correctly disconnect from the SSH-session.
        """
        self.ssh_client.close()
        self.remote_conn_pre.close()