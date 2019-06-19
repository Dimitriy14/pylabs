# TODO: add more keys
dic = {
    "Kernighan": ["The C Programming Language", 1972, 352],
    "Eckel": ["Thinking in Java", 1998, 1150],
    "Maruch": ["Python for dummies", 2011, 411],
    "Kernigan": ["The Go Programming Language", 2015, 432],
    "Minnick,": ["Coding with JavaScript For Dummies", 2015, 320]
}


def main():
    try:
        print(dic[input("Enter key: ")])

    except KeyError:
        print("No such key")
        keys = list(dic.keys())
        keys.sort()
        for key in keys:
            print("dic[{0}] => {1}".format(key, dic[key]))

    except Exception as e:
        print("Unhandled exception: ", e)
        exit(127)


if __name__ == "__main__":
    main()
