#! usr/bin/env python3

import os

def getLists():

    lists = []
    dirs = os.listdir('./lists')

    if dirs != []:
        for dir in dirs:
            with open(f'./lists/{dir}', 'r') as l:
                for task in l:
                    lists.append(task)

    return lists
            
        


def main():
    lists = getLists()
    print(lists)


if __name__ == '__main__':
    main()