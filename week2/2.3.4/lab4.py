import json
import requests
from tabulate import *


def get_ticket():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Xj3BDqbU"
    }

    resp=requests.post(api_url,json.dumps(body_json),headers=headers,verify=False)

    print("Ticket request status: ", resp.status_code)

    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]
    print(serviceTicket)
    return serviceTicket

def print_devices(tiket):
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
    headers =  {
        "content-type": "application/json",
        "X-Auth-Token": tiket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    response_json = resp.json()
    devices_list = []
    i = 0
    for item in response_json["response"]:
        i+=1
        host = [
            i,
            item["type"],
            item["managementIpAddress"]
        ]
        devices_list.append(host)
        table_header = ["Number", "Type", "IP"]
    print(tabulate(devices_list, table_header))



def print_hosts(tiket):
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    headers =  {
        "content-type": "application/json",
        "X-Auth-Token": tiket
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    response_json = resp.json()
    host_list = []
    i = 0
    for item in response_json["response"]:
        i+=1
        host = [
            i,
            item["hostType"],
            item["hostIp"]
        ]
        host_list.append(host)
        table_header = ["Number", "Type", "IP"]
    print(tabulate(host_list, table_header))


def get_flowAnalysisId(url, tiket):
    s_ip = ""
    d_ip = ""

    while True:
        s_ip = input("Enter source ip: ")
        d_ip = input("Enter destination ip: ")
        if s_ip != "" and d_ip != "":
            break

        print("Ip address can`t be empty. Try again: ")

    headers =  {
        "content-type": "application/json",
        "X-Auth-Token": tiket
    }

    path_data = {"destIP": d_ip, "sourceIP": s_ip}

    path_json = json.dumps(path_data)

    resp = requests.post(url, path_json, headers=headers, verify=False)

    return resp.json()["response"]["flowAnalysisId"]





def main():
    requests.packages.urllib3.disable_warnings()
    tiket = get_ticket()
    print("List of hosts: ")
    print_hosts(tiket)

    print("List of devices: ")
    print_devices(tiket)

    url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"

    check_url = url + "/" + get_flowAnalysisId(url, tiket)

    check_resp = requests.get(check_url, headers={
        "content-type": "application/json",
        "X-Auth-Token": tiket
    }, verify=False)

    print("Status:", check_resp.json()["response"]["request"]["status"])
    print("Path source: ", check_resp.json()["response"]["request"]["sourceIP"])
    print("Path destination: ", check_resp.json()["response"]["request"]["destIP"])
    print("Network Elements Info: ", check_resp.json()["response"]["networkElementsInfo"])



if __name__ =="__main__":
    main()