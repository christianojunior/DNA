import lib.dna_lib

response = lib.dna_lib.list_network_devices()
print("{0:20}{1:17}{2:12}{3:18}{4:15}{5:15}{6:25}{7}".
    format("hostname","mgmt IP","serial",
    "platformId","SW Version","role","Uptime","Is reachable?"))
for device in response['response']:
    if device['reachabilityStatus'] == 'Unreachable':
        print('{0:20}{1:17}{2:12}{3:18}{4:15}{5:15}{6:25}{7}'.
                    format("N/A",
                    device['managementIpAddress'],
                    "N/A",
                    "N/A",
                    "N/A",
                    "UNKNOWN",
                    "N/A",
                    "FALSE"   ))
    else:
        uptime = "N/A" if device['upTime'] is None else device['upTime']
        print("{0:20}{1:17}{2:12}{3:18}{4:15}{5:15}{6:25}{7}".
                    format(device['hostname'],
                    device['managementIpAddress'],
                    device['serialNumber'],
                    device['platformId'],
                    device['softwareVersion'],
                    device['role'],uptime,
                    "TRUE"))
