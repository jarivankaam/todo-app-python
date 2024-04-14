import os


# func to get lists inside of directory lists. -> maybe change to list items
def getTasks():
    Tasks = []
    dirs = os.listdir('./lists')

    if dirs:
        for dir in dirs:
            Tasks.append(dir)

    return Tasks


# func that takes in a taskname and status and creates a task based on those
def addTaskToList(taskName, taskStatus, taskDescription):
    if taskName and taskStatus:
        files = os.listdir('./lists')
        length = len(files)
        taskName = f'(#{length + 1})-{taskName}'

        with open(f'./lists/{taskName}.task', 'w') as f:
            f.write(f'Task: {taskName} - Status: {taskStatus} \n')
            if taskDescription:
                f.write(f'Description: {taskDescription}')
        print(f'Task {taskName} added.')
    else:
        if taskName == '':
            print('Taskname is not supplied')
        if taskStatus == '':
            print('Task Status is not supplied')

        # func that takes in a taskName and deletes them.


def permDeleteTask(taskName):
    if taskName:
        if os.path.exists(f'./lists/{taskName}.task'):
            os.remove(f'./lists/{taskName}.task')
            print(f'Task {taskName} deleted.')
        else:
            print('Task does not exist.')


# func to get details of a specefied task. Takes in the taskname and returns the contents.
def getTaskDetails(taskName):
    details = []
    with open(f'./lists/{taskName}.task') as lines:

        for line in lines:
            details.append(line.strip('\n'))

    return details
