import argparse

def extract_line(filename):
    with open(filename, "r+") as thefile:
        lines = thefile.readlines()
        #print(lines)
        for each_line in lines:
            strip_line = each_line.strip('\n')
            if (strip_line != ''):
                for each_char_inline in strip_line:
                    #.....


def main():
    # print("hey, welcome to my version of Caesar cipher"+'\n')
    # parser = argparse.ArgumentParser()
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument("-d", "--decrypt", action="store_true")
    # group.add_argument("-e", "--encrypt", action="store_true")
    # parser.add_argument("-f", "--file")
    getFile = str(input("Please insert the name of your file : "))
    extract_line(getFile)

if __name__ == '__main__':
    main()
