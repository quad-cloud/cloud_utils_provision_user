import sys
import os
import csv
import logging
def main():
    logging.basicConfig(
    filename="logfile.log",
    level=10,
    format="%(asctime)s:%(levelno)s:%(message)s"
    )

    f1=file("old_usernames.csv","r")
    list1 = f1.read().splitlines()

    f2=file("new_firstnames.csv","r")
    list2 = f2.read().splitlines()
    f3=file("new_lastnames.csv","r")
    list3 = f3.read().splitlines()

    list4=[]
    list5=[]
    list6=[]
    f1.close()
    f2.close()
    f3.close()
    for word in list3 :
        word.split()
        list4.append(word[:3])
        zip(list2,list4)
        list5 = [a + b for a, b in zip(list2, list4)]
    print(list5)
if __name__ == '__main__':
    main()
