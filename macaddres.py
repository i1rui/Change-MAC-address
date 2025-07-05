import optparse
import subprocess
import re
print("[+] By N3cr0Sh3ll|Telegram:i1rui):")
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", dest="network_interface", help="This place is for the network interface")
    parser.add_option("-m", dest="new_mac", help="This place is for the MAC Address")
    options, arguments = parser.parse_args()

    if not options.network_interface:
        parser.error("[-] Specify an interface, please. Type -h for help.")

    if not options.new_mac:
        parser.error("[-] Specify a MAC Address, please. Type -h for help.")

    return options

def mac_changer(network_interface, new_mac):
    subprocess.call("ifconfig " + network_interface + " down", shell=True)
    subprocess.call("ifconfig " + network_interface + " hw ether " + new_mac, shell=True)
    subprocess.call("ifconfig " + network_interface + " up", shell=True)
    print("[+] Changing MAC Address for " + network_interface + " to " + new_mac)

def get_mac(network_interface):
    ifconfig_result = subprocess.check_output("ifconfig " + network_interface, shell=True).decode("UTF-8")
    mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address:
        return mac_address.group(0)
    else:
        print("[-] Could not read MAC address.")
        return None

options = get_arguments()
mac_changer(options.network_interface, options.new_mac)
mac_address = get_mac(options.network_interface)

if mac_address and mac_address == options.new_mac:
    print("[+] MAC address has changed successfully to " + options.new_mac)
    print("[+] By BlackSec|Telegram:i3xui):")
else:
    print("[-] Something went wrong...")

