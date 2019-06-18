# TODO: add more keys
dic = {
    "Kernighan": ["The C Programming Language", 1972, 352],
    "Computer engineer": ["IT", 2016, 20],
    "iPhone": ["Apple", 1, 12345],
    "Dnipro": [2201, 15380],
    "Earth": [12756.2, 5.972, 149600000]
}

try:
    print(dic[input("Enter key: ")])
except:
    print("No such key")
    keys = list(dic.keys())
    keys.sort()
    for key in keys:
        print("dic[{0}] => {1}".format(key, dic[key]))
