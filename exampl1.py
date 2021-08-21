import requests
import getpass

# Allow self signed certs
requests.packages.urllib3.disable_warnings()

print('Enter credentials. This is public knowledge for sandbox, but still a best practice')
USER = str(input('Enter the username developer: ',) or 'developer')
PASSWORD = getpass.getpass(prompt='Enter the password C1sco12345: ')

# URL for request
url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/ietf-interfaces:interfaces"
url1 = url + '/interface=Loopback656'


# Set data formats
headers = {'Content-Type': 'application/yang-data+json',
           'Accept': 'application/yang-data+json'}


# Run GET
#response = requests.get(url, auth=(USER, PASSWORD), headers=headers, verify=False)
#response = requests.request('POST', url, auth=(USER, PASSWORD), headers=headers, data = payload, verify=False)
#response = requests.request('DELETE', urldel, auth=(USER, PASSWORD), headers=headers, verify=False)
# print(response)

int_number = 5


for i in range(0, int_number + 1):
    ipaddr = '172.12.2.7' + str(i)
    url2 = url1 + str(i)
    payload = '\
{\
  "ietf-interfaces:interface": {\
    "name": "Loopback656' + str(i) + '",\
    "description": "Configured by Python3",\
    "type": "iana-if-type:softwareLoopback",\
    "enabled": true,\
    "ietf-ip:ipv4": {\
        "address": [\
            {\
                "ip": "172.12.2.7' + str(i) + '",\
                "netmask": "255.255.255.255"\
            }\
        ]\
    },\
    "ietf-ip:ipv6": {}\
  }\
}\
'
    print(f'Working loopback with {ipaddr} Named Loopback656{str(i)}')
    # response = requests.request('POST', url, auth=(USER, PASSWORD), headers=headers, data = payload, verify=False) # Create
    # response = requests.request('DELETE', url2, auth=(USER, PASSWORD), headers=headers, verify=False) # Delete
    # print('Status Code: ' + str(response.status_code))
    # print(response.text)


for i in range(0, (int_number + 1)):
    url2 = url1 + str(i)
    response = requests.get(url2, auth=(USER, PASSWORD),
                            headers=headers, verify=False)
    print(f'Getting ouput from {url2}')
    print('Status Code: ' + str(response.status_code))
    print(response.text)
