# -------------------------------------------------------------------------------
# Name:			get_info
# Purpose:		This programms takes info from a .csv and return it
#
# Author:      _____     _____  ________   ____  ____ ____         ____           ________   ____  ____
#              \    \   /    / /        \  |  |  |  | |  |         |  |          /        \  |  |  |  |
#               \    \ /    / |   ____   | |  |  |  | |  |         |  |         |   ____   | |  |  |  |
#                \    V    /  |  /    \  | |  |  |  | |  |         |  |         |  /    \  | |  |  |  |
#                 \       /   |  |    |  | |  |  |  | |  |         |  |         |  |    |  | |  |  |  |
#                  \     /    |  |    |  | |  |  |  | |  |         |  |         |  |    |  | |  |  |  |
#                   |   |     |  |    |  | |  |  |  | |  |         |  |         |  |    |  | |  |  |  |
#                   |   |     |  \    /  | |  |  |  | |  |         |  |         |  \    /  | |  |  |  |
#                   |   |     |   ¯¯¯¯   | |  \__/  | |  |_______  |  |_______  |   ¯¯¯¯   | |  \__/  |
#                   |___|      \________/  \___  ___/ |__________| |__________|  \________/  \___  ___/
#                                              ¯¯                                                ¯¯
#
# Created:     20/11/2020
# Copyright:   (c) Youllou 2020
# Licence:     <your licence>
# -------------------------------------------------------------------------------

# global import
import os

cur_path = os.path.dirname(__file__)


def get(filepath: str, splitter: str) -> list:
    """
    :param filepath: path to the csv file where data needs to be retrieved
    :param splitter: splitter used in the csv
    :rtype: list
    :return data: a list of strings contained in the csv file
    """

    data = []
    f = open(filepath, "r", encoding="UTF-8")
    while 1:
        info = f.readline()
        if info == "":
            break
        else:
            data += [info.replace("\n", "").split(splitter)]
    f.close()
    if len(data) == 1:
        data = data.pop()
    return data


def write(filepath: str, splitter: str, data: list):
    """
    Write data to a csv file from a list
    :param filepath: path to the csv file where data needs to be written
    :param splitter: splitter used to split data in the csv
    :param data: list of objects
    :raise: Any exception if one encountered
    """

    # getting original, if file not found then it will be created
    try :
        f = open(filepath, "r", encoding="UTF-8")
        base = f.read()
        f.close()
    except FileNotFoundError as e:
        print("File wasn't existing so has been created")

    # writing (if exception catch rewrite original)
    f = open(filepath, "w", encoding="UTF-8")
    try:
        if type(data[0]) != list:
            f.write(str(data[0]))
            data.pop(0)
            for i in data:
                f.write(splitter + str(i))
        else:
            print(data)
            for i in data:
                f.write(str(i[0]))
                i.pop(0)
                for j in i:
                    f.write(splitter + str(j))
                f.write("\n")
        f.close()
    except Exception as e:
        f.write(base)
        f.close()
        raise e

def append(filepath: str, splitter: str, data: list):
    """
    Append data to a csv file from a list
    calls get() and write()
    :param filepath: path to the csv file where data needs to be written
    :param splitter: splitter used to split data in the csv
    :param data: list of objects
    :raise: Any exception if one encountered
    """

    # getting original
    base = get(filepath,splitter)
    print(len(base))
    if len(base) == 0 :
        write(filepath,splitter,data)
    else :
        print(data)
        if type(base[0]) == type(data[0]):
            new = base+data
        elif type(base[0]) == list:
            new = base + [data]
        else :
            new = [base]+data
        write(filepath,splitter,new)




if __name__ == '__main__':

    write("get_info_demo.csv",",",["this is a demonstration","here is some data to write"])
    out = None
    print("You should have a get_info_demo.csv file in your directory. Go check it out.\nEnter continue when you want to do so")
    while out != "continue":
        out = input()

    data = get("get_info_demo.csv",",")
    print("Now here is the same data but in a list\n",data)

    append("get_info_demo.csv",",",[["here is some more data to add to the csv file"],["By the way, now the csv has more than one line"]])
    out = None
    print("Added some more content.\nEnter continue when you want to do so")
    while out != "continue":
        out = input()

    data = get("get_info_demo.csv",",")
    print("And here is what I get from the file now\n",data)

    write("get_info_demo.csv",",",["Woopsie, the file's empty"])
    print("Now if I reuse the write method, the file will be overwritten.\nBye bye old data")
    out = None
    print("You can check how the file's going if you want to.\nElse, you can enter continue to do so")
    while out != "continue":
        out = input()

    print("That's it, thank you for having followed the demo.\nNow let me delete the file I just created")
    os.remove("get_info_demo.csv")