import threading
import time
import json
import requests


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




def check_vpn(incoming_msg):
    """Check if VPN address has changed
    """
    
    
    #response = Response()
    #response.text = "Gathering  Information...\n\n"

    mon = MonitorVPNint()
    status = mon.setup('testbed/routers.yml')
    if status != "":
        response.text += status
        return response


    status = mon.learn_interface()
    if status == "":
        response.text += "The interface has not changed."
        
    else:#add function(possibly a netmiko chellenege 3 like one) that allows me to send commands to CSR1. Ask Nam
        print("Different IP detected")
        ip = status
        print(ip)
        response.text += status
        
    return response

check_vpn(check_vpn)