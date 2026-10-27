from panos.objects import  AddressObject, AddressGroup
from panos.firewall import  Firewall
import stdiomask


def parse_file(file_path):
    objects = []
    with open(file_path,"r") as file:
        lines=file.readlines()
        for a,b in zip(lines[0::2],lines[1::2]):
            objects.append((a.strip(),b.strip()))
    return objects


def push_address_objects(address_list,firewall):
    for entry in address_list:
        addr = AddressObject(entry[0],entry[1])
        firewall.add(addr)
        addr.create()


def main():
    file_path = input("Enter the file path: ")
    username = input("Enter the username: ")
    password = stdiomask.getpass(prompt="Enter the password: ",mask="*")
    Firewall_IP = input("Enter the Firewall IP or hostname: ")

    #Create a firewall object
    fw = Firewall(Firewall_IP, username, password, vsys="shared")
    #parse file data
    addresses = parse_file(file_path)

    push_address_objects(addresses,fw)

    group = input("Do you wish to bundle objects into an address group? (y/n)")
    if group == "y" or group == "Y":
        name = input("Enter the group name: ")
        object_names = [address[0] for address in addresses]
        address_group = AddressGroup(name, static_value=object_names)
        fw.add(address_group)
        address_group.create()
    fw.commit()

if __name__ == "__main__":
    main()
