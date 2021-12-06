import time

# Genie import
from genie.conf import Genie

# import the genie libs
from genie.libs import ops # noqa

# Parser import
from genie.libs.parser.iosxe.show_interface import ShowIpInterfaceBrief

# Import Genie Conf
from genie.libs.conf.interface import Interface
global vpn_ip
#ip = vpn_ip

class MonitorVPNint():


    def setup(self, testbed):
        genie_testbed = Genie.init(testbed)
        self.device_list = []
        str = ""
        for device in genie_testbed.devices.values():
            try:
                device.connect()
            except Exception as e:
                print("Failed to establish connection to '{}'".format(
                    device.name))
                str += "\nFailed to establish connection to "+ device.name

            self.device_list.append(device)

        return str

    def find_ip(self, old_ip):
        text=""
        #print(old_ip)
        #old_ip_string = str(old_ip)
        for dev in self.device_list:
            self.parser = ShowIpInterfaceBrief(dev)
            out = self.parser.parse()
            #print(out)
            self.intf1 = []
            # let's find  the interface
            for interface, value in out['interface'].items():
                #print(interface)
                if old_ip in value['ip_address']:
                    #text+="\n"+interface +" on " + dev.name + " has not changed"
                    text = value['ip_address']
                    #print(old_ip)
                    # Create a Genie conf object out of it
                    # This way, it will be OS/Cli/Yang Agnostic  
                    self.intf1.append(Interface(name=interface, device=dev))
                if interface == 'GigabitEthernet2':
                    if "172.16.0.1" != value['ip_address']:
                        if old_ip != value['ip_address']:
                            text+=value['ip_address']
                            #print("change")
                            #text+=old_ip_string
                            #print(value['ip_address'])


                #else:
                #    print(interface["GigabitEthernet2"], value["ip_address"])  
                

        return text
    

if __name__ == "__main__":
    # Test Functions
    mon = MonitorInterfaces()
    mon.setup('testbed/routers.yml')
    intfl = mon.learn_interface()
    print(intfl)
