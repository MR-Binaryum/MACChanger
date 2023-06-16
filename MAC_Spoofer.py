import subprocess

def change_mac(interface, new_mac):
    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    

interface = input("interface > ")
new_mac = input("new MAC > ") 


subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether" , new_mac])
subprocess.call(["ifconfig", interface, "up"])
