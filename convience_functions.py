import os


# func to get lists inside of directory lists. -> maybe change to list items
def getTasks():
    Tasks = []
    dirs = os.listdir('./lists')

    if dirs != []:
        for dir in dirs:
            Tasks.append(dir)

    return Tasks


# func that takes in a taskname and status and creates a task based on those
def addTaskToList(taskName, taskStatus):
    if taskName and taskStatus:
        with open(f'./lists/{taskName}.txt', 'w') as f:
            f.write(f'Task: {taskName} - Status: {taskStatus}')
    else:
        if taskName == '':
            print('Taskname is not supplied')
        if taskStatus == '':
            print('Task Status is not supplied')

        # func that takes in a taskName and deletes them.


def permDeleteTask(taskName):
    if taskName:
        os.delete(f'./lists/{taskName}.txt')


# func to get details of a specefied task. Takes in the taskname and returns the contents.
def getTaskDetails(taskName):
    details = []
    with open(f'./lists/{taskName}') as lines:
        for line in lines:
            details.append(line)

    return details
