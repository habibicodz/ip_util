def sayHello():
    print("IP Util")
    print("Created by habibicodz")
    print("")


def findBroadcastIP(ip_address: str, subnet_mask: str):
    ip_octets = ip_address.split(".")
    subnet_octets = subnet_mask.split(".")

    networkPortion=[]
    hostPortion=[]

    for index, octet in enumerate(ip_octets):
        sub_oct=int(subnet_octets[index])
        if sub_oct == 255:
            networkPortion.append(octet)
        else:
            hostPortion.append("255")
            
    broadcast_ip=".".join(networkPortion + hostPortion)
    print(broadcast_ip)
    

def findNetworkIP(ip_address: str, subnet_mask: str):
    ip_octets = ip_address.split(".")
    subnet_octets = subnet_mask.split(".")

    networkPortion=[]
    hostPortion=[]

    for index, octet in enumerate(ip_octets):
        sub_oct=int(subnet_octets[index])
        if sub_oct == 255:
            networkPortion.append(octet)
        else:
            hostPortion.append("0")
            
    network_ip=".".join(networkPortion + hostPortion)
    print(network_ip)

def validateIPv4Address(ip_address: str):
    octets=ip_address.split(".")
    all_octet_valid=True

    for octet in octets:
        if int(octet) >= 0 and int(octet) <= 255:
            all_octet_valid=True
        else:
            all_octet_valid=False
            break
    return all_octet_valid and len(octets) == 4

def validateSubnetMast(subnet_mask: str):
    octets=subnet_mask.split(".")
    all_octet_valid=True

    for octet in octets:
        if int(octet) >= 0 and int(octet) <= 255:
            all_octet_valid=True
        else:
            all_octet_valid=False
            break
    return all_octet_valid and len(octets) == 4

sayHello()

print("Type your IP Address: ")
ip_addr = input()
if validateIPv4Address(ip_addr) == False:
    print("Invalid IP Address")
    exit()

print("")
print("Type your Subnet Mask: ")
subnet_mask = input()
if validateSubnetMast(subnet_mask) == False:
    print("Invalid Subnet Mask")
    exit()

print("")
print("Choose your option: ")
print("1. Find broadcast IP")
print("2. Find network IP")
option=input()

if option == "1":
    findBroadcastIP(ip_addr, subnet_mask)
elif option == "2":
    findNetworkIP(ip_addr, subnet_mask)
else:
    print("Wrong option selected")