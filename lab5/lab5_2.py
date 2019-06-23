import re

def find_nmu_one(f):
    regex = re.compile(r"(\w+\.\w+){2}@nmu\.one$")
    return [ regex.search(l).group() for l in f if regex.search(l) ]

def find_zero_or_dot(f):
    regex = re.compile(r"^.*[\.|0].*@.+$")
    return [ regex.search(l).group() for l in f if regex.search(l) ]

def main():
    with open("sample_2.txt", 'r') as file:
        nmu_one     = find_nmu_one(file)
        file.seek(0)
        zero_or_dot = find_zero_or_dot(file)
    print("First filter:\t", nmu_one)
    print("Second filter:\t",zero_or_dot)

    return None

if __name__ == "__main__":
    main()