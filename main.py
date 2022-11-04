import subprocess
import optparse


# hi
# interface = input("interface > ")
# newMac = input("new MAC > ")

# interface = raw_input("interface > ")
# newMac = raw_input("new MAC > ")

# (options, arguments) options = -i, -m and argument = dest ="interface" or dest = "newMac" => eth0 or 00:11
def getArguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="newMac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify and interface, use --help for more information")
    elif not options.newMac:
        parser.error("[-] Please specify and Mac, use --help for more information")
    return options


def changeMac(interface, newMac):
    print("[+] Changing Mac address for" + interface + "to" + newMac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", newMac])
    subprocess.call(["ifconfig", interface, "up"])


# interface = options.interface
# newMac = options.newMac
options = getArguments()
changeMac(options.interface, options.newMac)
