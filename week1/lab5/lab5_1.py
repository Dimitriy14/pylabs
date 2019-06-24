import re

def get_time(f):
    regex = re.compile(r"\d+:\d+:\d+.\d+")
    return [ regex.search(l).group() for l in f if regex.search(l) ]

def get_mac(f):
    regex = re.compile(r"([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}")
    return [ regex.search(l).group() for l in f if regex.search(l) ]

def find_in_mac(mac_arr):
    sorted_macs = {}
    regex = re.compile(r"[^|\.][0-9A-Fa-f]*")
        
    for mac_addr in mac_arr:
        sorted_macs[mac_addr] = {
            "with_b": [ q for q in regex.findall(mac_addr) if 'b' in q ],
            "with_a": [ q for q in regex.findall(mac_addr) if 'a' in q ] }

    return sorted_macs

def main():
    with open("sample_1.txt", 'r') as file:
        time_arr = get_time(file)
        file.seek(0)
        mac_arr = get_mac(file)

    sorted_macs = find_in_mac(mac_arr)
    
    print("Time:\t", time_arr)
    print("MAC:\t", mac_arr)

    for mac, blocks in sorted_macs.items():
        print("{0} contains blocks:\n\twith a: {1}\n\twith b: {2}".format(mac, blocks["with_a"], blocks["with_b"]))

    return None

if __name__ == "__main__":
    main()