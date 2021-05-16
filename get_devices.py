import lib.dna_lib

response = lib.dna_lib.list_network_devices()
print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
    format("hostname","mgmt IP","serial",
    "platformId","SW Version","role","Uptime"))
for device in response['response']:
    #print(i['hostname'],'\t', i['inventoryStatusDetail'], '\n')
    if device['hostname'] != 'cat_9k_1':
    #    print("yes")
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        print("{0:42}{1:17}{2:12}{3:18}{4:12}{5:16}{6:15}".
            format(device['hostname'],
                    device['managementIpAddress'],
                    device['serialNumber'],
                    device['platformId'],
                    device['softwareVersion'],
                    device['role'],uptime))
