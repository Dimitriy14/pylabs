import re


def get_int_vlan_map(file):
    trunk = {}
    access = {}
    matched_lines = re.findall("interface((.*\n){2})", file.read())
    for line in matched_lines:
        interface = re.findall(".*", line[0])[0].strip()

        if "trunk" in line[1]:
            ports = re.findall("vlan(.*)", line[1])[0].strip().split(",")
            trunk[interface] = [int(port) for port in ports]

        if "access vlan" in line[1]:
            access[interface] = int(re.findall("vlan(.*)", line[1])[0])

    return trunk, access


def main():
    with open("config_sw.txt") as file:
        trunk, access = get_int_vlan_map(file)
        print("Trunk: ", trunk)
        print("Access: ", access)


if __name__ == "__main__":
    main()
