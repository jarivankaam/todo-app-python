import os
import sys
import argparse 
from convience_functions import getTasks, addTaskToList, permDeleteTask, getTaskDetails

# place for args. use parser. and add if statements in main func.


# call parser
parser = argparse.ArgumentParser()


# add url argument
parser.add_argument(
    "--name",
    "-name",
    default="test",
    help="name of the task",
    type=str,
    required=False,
)
# add password argument
parser.add_argument(
    "--status",
    "-s",
    default="pending",
    help="task status",
    type=str,
    nargs="?",
    const="hallo",
    required=False,
)
parser.add_argument(
    "--all",
    "-a",
    help="all tasks",
    nargs="?",
    required=False,
)
parser.add_argument(
    "--details",
    "-d",
    help="detail of task",
    nargs="?",
    required=False,
)




def main(args):
    if args == '':
        print('geen args')
    else: 
        lists = getTasks()
        for item in lists:
            print(f'Task: {item} \n')
    
    if args.all:
        print('all')

    if args.details and args.name:
        d = getTaskDetails(args.name)
        print(d)

if __name__ == '__main__':
    main(parser.parse_args())