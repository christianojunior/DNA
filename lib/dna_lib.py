import requests
from requests.models import HTTPBasicAuth
from urllib3 import disable_warnings
disable_warnings()

def get_token( controller_url,port, username, password ):
    login_url = "https://{0}:{1}/dna/system/api/v1/auth/token".format(controller_url, port)
    result = requests.post(login_url, auth=HTTPBasicAuth(username, password), verify=False)
    result.raise_for_status()
    token = result.json()["Token"]
    return {
        "URL": controller_url,
        "token": token
            }
def create_url(controller_url, port, path):
    return "https://{0}:{1}/api/v1/{2}".format(controller_url, port, path)

def get_url(apipath):
    url = create_url("sandboxdnac.cisco.com", 443, apipath)
    token = get_token("sandboxdnac.cisco.com", 443, "devnetuser", "Cisco123!")
    headers = {"X-auth-token": token["token"]}
    try:
        response = requests.get(url, headers=headers, verify=False)
    except requests.exceptions.RequestException as cerror:
        print("error processing request", cerror)
        SystemExit(1)
    return response.json()
def list_network_devices():
    return get_url("network-device")


def ip_to_id(ip):
    return get_url("network-device/ip-address/%s" % ip)['response']['id']

def get_modules(id):
    return get_url("network-device/module?deviceId=%s" % id)

def print_info(modules):

    print("{0:30}{1:15}{2:25}{3:5}".format("Module Name","Serial Number","Part Number","Is Field Replaceable?"))
    for module in modules['response']:
        print("{moduleName:30}{serialNumber:15}{partNumber:25}{moduleType:5}".format(moduleName=module['name'],
        serialNumber=module['serialNumber'],
        partNumber=module['partNumber'],
        moduleType=module['isFieldReplaceable']))

