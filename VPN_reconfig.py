from netmiko import ConnectHandler
import myParamiko as m

router = {'device_type': 'cisco_ios', 'host': '192.168.56.101', 'username': 'cisco','password': 'cisco123!','port': 22,
        		'secret': 'cisco123!', 'verbose': True}


def VPN_reconfig(ip):
    connection = ConnectHandler(**router)

    prompt = connection.find_prompt()

    if '>' in prompt:
        connection.enable()

    connection.config_mode()
    output = connection.send_command('crypto isakmp key cisco address 172.16.0.3')
    print("Complete")
    output = connection.send_command('no crypto isakmp key cisco address 172.16.0.2')
    print("Complete")
    if not connection.check_config_mode():
        connection.config.mode()
    str = 'crypto map Crypt 10 ipsec-isakmp\n'
    str = str + 'no set peer 172.16.0.2\n'
    str = str + 'set peer 172.16.0.3\n'
    str = str + 'exit\n'     
    output = connection.send_config_set(str.split('\n'))
    print("Complete1")
    # output = connection.send_config_set('set peer 172.16.0.3','exit')
    # print("Complete2")
    # output = connection.send_command('no set peer 172.16.0.2')
    connection.exit_config_mode()
    print("Complete")
    print(output)

    print('Closing Connection')
    connection.disconnect()
    print('#'*40)

VPN_reconfig('172.16.0.3')