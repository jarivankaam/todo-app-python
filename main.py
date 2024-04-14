import os
import sys
import argparse
from convience_functions import getTasks, addTaskToList, permDeleteTask, getTaskDetails


def main(arguments):
    # Check if any specific action is requested
    action_taken = False

    if arguments.list:
        tasks = getTasks()
        for item in tasks:
            print(f'Task: {item}')
        action_taken = True

    if arguments.all:
        print('Showing all tasks.')
        action_taken = True

    if arguments.mode:
        if arguments.mode == 'create':
            addTaskToList(arguments.name, arguments.status, arguments.desc)
            action_taken = True
        if arguments.mode == 'delete':
            permDeleteTask(arguments.name)
            action_taken = True
        if arguments.mode == 'details':
            details = getTaskDetails(arguments.name)
            print(details)
            action_taken = True

    # Failsafe: if no specific action is requested, default to listing tasks
    if not action_taken:
        print("No specific action requested. Defaulting to listing tasks.")
        tasks = getTasks()
        for item in tasks:
            print(f'Task: {item}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Task Manager")
    parser.add_argument('--list', action='store_true', help='List all tasks')
    parser.add_argument('--all', action='store_true', help='Process all tasks')
    parser.add_argument('--details', action='store_true', help='Show details of a task')
    parser.add_argument('--name', type=str, help='Name of the task to detail')
    parser.add_argument('--desc', type=str, help='desc of the task to detail')
    parser.add_argument('--status', type=str, help='status of the task to detail')
    parser.add_argument('--mode', help='create task')

    args = parser.parse_args()
    main(args)
