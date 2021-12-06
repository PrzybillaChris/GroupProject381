import threading
import time
import json
import requests



#python
import os
import logging
import re
from ipaddress import IPv4Network, IPv4Address

# Genie
from genie.utils.config import Config
from genie.libs.parser.utils.common import Common
from genie.libs.sdk.libs.utils.normalize import GroupKeys
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# libs
from genie.libs.sdk.apis.utils import (
    int_to_mask,
    get_config_dict,
    question_mark_retrieve,
    get_delta_time_from_outputs,
)

from genie.libs.sdk.apis.iosxe.running_config.get import (
    get_running_config_section_dict,
)

# for XML
import xml.dom.minidom as p
import xmltodict



from ansible import context
from ansible.cli import CLI
from ansible.module_utils.common.collections import ImmutableDict
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.parsing.dataloader import DataLoader
from ansible.inventory.manager import InventoryManager
from ansible.vars.manager import VariableManager
#from ansible.playbook import PlayBook



# To build the table at the end
from tabulate import tabulate

### teams Bot ###
from webexteamsbot import TeamsBot
from webexteamsbot.models import Response

### Utilities Libraries
import routers
import useless_skills as useless
import useful_skills as useful
from BGP_Neighbors_Established import BGP_Neighbors_Established
from Monitor_Interfaces import MonitorInterfaces
from Monitor_VPN_int import MonitorVPNint
from initial_ip import VPNintialIP

#For netmiko/paramiko
from netmiko import ConnectHandler
import myParamiko as m
from ncclient import manager

router = {'device_type': 'cisco_ios', 'host': '192.168.56.101', 'username': 'cisco','password': 'cisco123!','port': 22,
        		'secret': 'cisco123!', 'verbose': True}

# Create  thread list
threads = list()
# Exit flag for threads
exit_flag = False
vpn_flag = False
vpn_ip = '172.16.0.2'

# Router Info 
device_address = routers.router['host']
device_username = routers.router['username']
device_password = routers.router['password']

# RESTCONF Setup
port = '443'
url_base = "https://{h}/restconf".format(h=device_address)
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'} 


# Bot Details
bot_email = '' #bot address
teams_token = '' #your teams token
bot_url = '' #Ngrok session link
bot_app_name = 'CNIT-381 Network Auto Chat Bot'

# Create a Bot Object
#   Note: debug mode prints out more details about processing to terminal
bot = TeamsBot(
    bot_app_name,
    teams_bot_token=teams_token,
    teams_bot_url=bot_url,
    teams_bot_email=bot_email,
    debug=True,
    webhook_resource_event=[
        {"resource": "messages", "event": "created"},
        {"resource": "attachmentActions", "event": "created"},],
)

# Create a function to respond to messages that lack any specific command
# The greeting will be friendly and suggest how folks can get started.
def greeting(incoming_msg):
    # Loopkup details about sender
    sender = bot.teams.people.get(incoming_msg.personId)

    # Create a Response object and craft a reply in Markdown.
    response = Response()
    response.markdown = "Hello {}, I'm a friendly CSR1100v assistant .  ".format(
        sender.firstName
    )
    response.markdown += "\n\nSee what I can do by asking for **/help**."
    return response




import paramiko








def show_run (incoming_msg):
    """Show the running-config of device
    """
    #response = Response()
    # creating an ssh client object
    #ssh_client = paramiko.SSHClient()
    #ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    router1 = {'hostname': '192.168.56.101', 'port': '22', 'username': 'cisco', 'password': 'cisco123!'}
    router2 = {'hostname': '192.168.56.102', 'port': '22', 'username': 'cisco', 'password': 'cisco123!'}


    if incoming_msg.text == "show run router1":
        
        #return "router1"
        response = Response()
        # creating an ssh client object
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(**router1, look_for_keys=False, allow_agent=False)
        # creating a shell object
        shell = ssh_client.invoke_shell()

        # sending commands to the remote device to execute them
        # each command ends in \n (new line, the enter key)
        shell.send('terminal length 0\n')
        shell.send('en\n')
        shell.send('cisco123!\n')
        shell.send ('show run\n')
        time.sleep(2) # waiting for the remove device to finish executing thew commands (mandatory)

        # reading from the shell's output buffer
        output = shell.recv(7439)
        # print(type(output))
        response.text = output.decode('utf-8') # decoding from bytes to string
    

        # closing the connection if it's active
        if ssh_client.get_transport().is_active() == True:
            print('Closing connection')
            ssh_client.close()
        return response

    elif incoming_msg.text == "show run router2":
        response = Response()
        # creating an ssh client object
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(**router2, look_for_keys=False, allow_agent=False)
        # creating a shell object
        shell = ssh_client.invoke_shell()

        # sending commands to the remote device to execute them
        # each command ends in \n (new line, the enter key)
        shell.send('terminal length 0\n')
        shell.send('en\n')
        shell.send('cisco123!\n')
        shell.send ('show run\n')
        time.sleep(2) # waiting for the remove device to finish executing thew commands (mandatory)

        # reading from the shell's output buffer
        output = shell.recv(7439)
        # print(type(output))
        response.text = output.decode('utf-8') # decoding from bytes to string
    

        # closing the connection if it's active
        if ssh_client.get_transport().is_active() == True:
            print('Closing connection')
            ssh_client.close()
        return response
        















m = manager.connect(host="192.168.56.101", port=830, username="cisco", password="cisco123!", hostkey_verify=False)
r = manager.connect(host="192.168.56.102", port=830, username="cisco", password="cisco123!", hostkey_verify=False)





def change_interface(incoming_msg):
    #Here is the config that is sent to the respective router. By default, it will set GigabitEthernet2 to up.
    config = ''' 
        <config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
              <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                    <name>GigabitEthernet2</name>
                    <enabled>true</enabled>
                </interface>
              </interfaces>
          </config>
        ''' 
    config_dict = xmltodict.parse(config)

    # Determines if the user wants router 1 or 2 enabled or disabled here.
    # Disable commands utilize a dictionary command that will change the "enabled" part
    # of the XML config file to false.
    # This will turn GigabitEthernet2 off.
    if incoming_msg.text == "changeint enable 1":
        netconf_reply = m.edit_config(target='running', config=config)
        return "Int G2 was successfully enabled."
    elif incoming_msg.text == "changeint disable 1":
        config_dict["config"]["interfaces"]["interface"]["enabled"] = "false"
        config = xmltodict.unparse(config_dict)
        netconf_reply = m.edit_config(target='running', config=config)
        return "Int G2 was successfully disabled."
    elif incoming_msg.text == "changeint enable 2":
        netconf_reply = r.edit_config(target='running', config=config)
        return "Int G2 was successfully enabled."
    elif incoming_msg.text == "changeint disable 2":
        config_dict["config"]["interfaces"]["interface"]["enabled"] = "false"
        config = xmltodict.unparse(config_dict)
        netconf_reply = r.edit_config(target='running', config=config)
        return "Int G2 was successfully disabled."
    else:
        return "Wrong command, please try again."










def monitor_vpn(incoming_msg):
    """Monitor interfaces in a thread
    """
    response = Response()
    response.text = "Monitoring interfaces...\n\n"
    monitor_vpn_job(incoming_msg)


    return response






def monitor_vpn_job(incoming_msg):
    response = Response()
    ip_old = check_inital_IP(incoming_msg)
    

    global vpn_flag
    while vpn_flag == False:
        newIP = check_vpn(incoming_msg, ip_old)
        if ip_old != newIP:

            VPN_reconfig(ip_old, newIP)
            finalmessage(incoming_msg)

            works = "New IP Detected - Reconfigure Complete - IP is now " + newIP
            works = str(works)
            useless.create_message(incoming_msg.roomId, works)
        ip_old = newIP
        time.sleep(20)

    vpn_flag = False

    return response


def finalmessage(incoming_msg):
    response = Response()
    response.text = "It worked\n\n"
    print("working?")
    return "Backup Complete - {}".format(incoming_msg.text)




def stop_vpn_monitor(incoming_msg):
    """end Monitoring the vpn
    """
    response = Response()
    response.text = "Stopping all Monitors...\n\n"
    global vpn_flag
    vpn_flag = True
    time.sleep(5)
    response.text += "Done!..\n\n"

    return response





def check_vpn(incoming_msg, old_ip):
    """Check if VPN address has changed
    """
    
    
    response = Response()
    response.text = "Gathering  Information...\n\n"

    mon = MonitorVPNint()
    status = mon.setup('testbed/routers.yml')
    if status != "":
        response.text += status
        return response


    status = mon.find_ip(old_ip)
    if status == old_ip:
        print('no change')
        response.text += "The interface has not changed.\n\n"
        
    if status != old_ip:
        print("Different IP detected")
        response.text += "The IP has changed, reconfiguring VPN now\n\n"
        ip = status
        print(ip)
        print("change")
        response.text += status
        
        
    return status



def check_inital_IP(incoming_msg):
    """Check if VPN address has changed
    """
    ip = ""
    
    response = Response()
    response.text = "Gathering  Information...\n\n"

    mon = VPNintialIP()
    status = mon.setup('testbed/routers.yml')
    if status != "":
        response.text += status
        return response


    status = mon.find_ip()
    response.text += status
    

        
    return status



def VPN_reconfig(old_ip, new_ip):
    connection = ConnectHandler(**router)

    prompt = connection.find_prompt()

    if '>' in prompt:
        connection.enable()

    connection.config_mode()
    output = connection.send_command('crypto isakmp key cisco address '+ new_ip)
    print("Complete")
    output = connection.send_command('no crypto isakmp key cisco address '+ old_ip)
    print("Complete")
    if not connection.check_config_mode():
        connection.config.mode()
    str = 'crypto map Crypt 10 ipsec-isakmp\n'
    str = str + 'no set peer ' + old_ip + '\n'
    str = str + 'set peer ' + new_ip + '\n'
    str = str + 'exit\n'     
    output = connection.send_config_set(str.split('\n'))
    print("Complete1")
    connection.exit_config_mode()
    print("Complete")
    print(output)

    print('Closing Connection')
    connection.disconnect()
    print('#'*40)




def backup(incoming_msg):

    loader = DataLoader()

    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                    module_path=None, forks=100, remote_user='xxx', private_key_file=None,
                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)

    inventory = InventoryManager(loader=loader, sources=('/home/devasc/labs/devnet-src/Group_Project/hosts',))

    variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))

    pbex = PlaybookExecutor(playbooks=['/home/devasc/labs/devnet-src/Group_Project/backup_cisco_router_playbook.yaml'], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})

    pbex.run()
    
    return "Backup Complete - {}".format(incoming_msg.text)

def backup2(incoming_msg):

    loader = DataLoader()

    context.CLIARGS = ImmutableDict(tags={}, listtags=False, listtasks=False, listhosts=False, syntax=False, connection='ssh',
                    module_path=None, forks=100, remote_user='xxx', private_key_file=None,
                    ssh_common_args=None, ssh_extra_args=None, sftp_extra_args=None, scp_extra_args=None, become=True,
                    become_method='sudo', become_user='root', verbosity=True, check=False, start_at_task=None)

    inventory = InventoryManager(loader=loader, sources=('/home/devasc/labs/devnet-src/Group_Project/hosts2',))

    variable_manager = VariableManager(loader=loader, inventory=inventory, version_info=CLI.version_info(gitinfo=False))

    pbex = PlaybookExecutor(playbooks=['/home/devasc/labs/devnet-src/Group_Project/backup_cisco_router_playbook2.yaml'], inventory=inventory, variable_manager=variable_manager, loader=loader, passwords={})

    pbex.run()
    
    return "Backup Complete - {}".format(incoming_msg.text)


def arp_list(incoming_msg):
    """Return the arp table from device
    """
    response = Response()
    arps = useful.get_arp(url_base, headers,device_username,device_password)

    if len(arps) == 0:
        response.markdown = "I don't have any entries in my ARP table."
    else:
        response.markdown = "Here is the ARP information I know. \n\n"
        for arp in arps:
            response.markdown += "* A device with IP {} and MAC {} are available on interface {}.\n".format(
               arp['address'], arp["hardware"], arp["interface"]
            )

    return response

def sys_info(incoming_msg):
    """Return the system info
    """
    response = Response()
    info = useful.get_sys_info(url_base, headers,device_username,device_password)

    if len(info) == 0:
        response.markdown = "I don't have any information of this device"
    else:
        response.markdown = "Here is the device system information I know. \n\n"
        response.markdown += "Device type: {}.\nSerial-number: {}.\nCPU Type:{}\n\nSoftware Version:{}\n" .format(
            info['device-inventory'][0]['hw-description'], info['device-inventory'][0]["serial-number"], 
            info['device-inventory'][4]["hw-description"],info['device-system-data']['software-version'])

    return response

def get_int_ips(incoming_msg):
    """Return Interface IPs
    """
    response = Response()
    intf_list = useful.get_configured_interfaces(url_base, headers,device_username,device_password)

    if len(intf_list) == 0:
        response.markdown = "I don't have any information of this device"
    else:
        response.markdown = "Here is the list of interfaces with IPs I know. \n\n"
    for intf in intf_list:
        response.markdown +="*Name:{}\n" .format(intf["name"])
        try:
            response.markdown +="IP Address:{}\{}\n".format(intf["ietf-ip:ipv4"]["address"][0]["ip"],
                                intf["ietf-ip:ipv4"]["address"][0]["netmask"])
        except KeyError:
            response.markdown +="IP Address: UNCONFIGURED\n"
            
    return response

def check_bgp(incoming_msg):
    """Return BGP Status
    """
    response = Response()
    response.text = "Gathering BGP Information from BGP peers...\n\n"

    bgp = BGP_Neighbors_Established()
    status = bgp.setup('testbed/routers.yml')
    if status != "":
        response.text += status
        return response

    status = bgp.learn_bgp()
    if status != "":
        response.text += status

    response.text += bgp.check_bgp()

    return response

def check_int(incoming_msg):
    """Find down interfaces
    """
    response = Response()
    response.text = "Gathering  Information...\n\n"

    mon = MonitorInterfaces()
    status = mon.setup('testbed/routers.yml')
    if status != "":
        response.text += status
        return response

    status = mon.learn_interface()
    if status == "":
        response.text += "All Interfaces are OK!"
    else:
        response.text += status

    return response

def monitor_int(incoming_msg):
    """Monitor interfaces in a thread
    """
    response = Response()
    response.text = "Monitoring interfaces...\n\n"
    monitor_int_job(incoming_msg)
    th = threading.Thread(target=monitor_int_job, args=(incoming_msg,))
    threads.append(th)  # appending the thread to the list

    # starting the threads
    for th in threads:
        th.start()

    # waiting for the threads to finish
    for th in threads:
        th.join()

    return response

def monitor_int_job(incoming_msg):
    response = Response()
    msgtxt_old=""
    global exit_flag
    while exit_flag == False:
        msgtxt = check_int(incoming_msg)
        if msgtxt_old != msgtxt:
            print(msgtxt.text)
            useless.create_message(incoming_msg.roomId, msgtxt.text)
        msgtxt_old = msgtxt
        time.sleep(20)

    print("exited thread")
    exit_flag = False

    return response

def stop_monitor(incoming_msg):
    """Monitor interfaces in a thread
    """
    response = Response()
    response.text = "Stopping all Monitors...\n\n"
    global exit_flag
    exit_flag = True
    time.sleep(5)
    response.text += "Done!..\n\n"

    return response

# Set the bot greeting.
bot.set_greeting(greeting)

# Add Bot's Commmands

bot.add_command("show run", "displays the show run command for either router 1 or 2. ie. show run router1 or show run router2", show_run)

bot.add_command("changeint", "Enable/Disable Gigabit2 on either CSR1 or 2.\n Example: changeint enable 1 will change CSR1 G2 to up, or changeint disable 2 will disable G2 on CSR2.", change_interface)

bot.add_command(
    "arp list", "See what ARP entries I have in my table.", arp_list)
bot.add_command(
    "monitor-vpn", "Monitor the vpn", monitor_vpn)
bot.add_command(
    "stop-vpn-monitor", "Monitor the vpn", stop_vpn_monitor)
bot.add_command(
    "backup", "Create or update a backup of the CSR1kv router", backup)
bot.add_command(
    "router2", "Create or update a backup of the CSR2kv router", backup2)
bot.add_command(
    "system info", "Checkout the device system info.", sys_info)
bot.add_command(
    "show interfaces", "List all interfaces and their IP addresses", get_int_ips)
bot.add_command("attachmentActions", "*", useless.handle_cards)
bot.add_command("showcard", "show an adaptive card", useless.show_card)
bot.add_command("donothing", "Tell me the bot to do nothing something", useless.do_nothing)
bot.add_command("dosomething", "help for do something", useless.do_something)
bot.add_command("time", "Look up the current time", useless.current_time)
bot.add_command("check bgp", "This job checks that all BGP neighbors are in Established state", check_bgp)
bot.add_command("check interface", "This job will look down interfaces", check_int)
bot.add_command("monitor interfaces", "This job will monitor interface status in back ground", monitor_int)
bot.add_command("stop monitoring", "This job will stop all monitor job", stop_monitor)
# Every bot includes a default "/echo" command.  You can remove it, or any
bot.remove_command("/echo")

if __name__ == "__main__":
    # Run Bot
    bot.run(host="0.0.0.0", port=5000)
