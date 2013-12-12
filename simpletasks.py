#v0.1
import fileaccess

fa = fileaccess.FileAccess()
file = 'list.txt'

def openFile():
    try:
        fa.OpenFile(file,'r+')
    except:
        fa.OpenFile(file,'w')
        fa.CloseFile()
        fa.OpenFile(file,'r+')
        
    contents = fa.ToString()
    contents = contents.split('\n')
    return contents


def nextTask():
    print(contents[currenttask])
    currenttask += 1

def addTask():
    fa.CloseFile() #close the file
    fa.OpenFile(file, 'a') #open the file in append mode
    task = str(input()) #get task to be appended
    fa.AddLine('\n' + task) #add task to file
    fa.CloseFile() #close and save the file
    return task

contents = openFile()
for line in contents:
    if line == '':
        contents.remove(line)
currenttask = 0

def run(contents,currenttask):
    while True:
        print('==============================')
        print('CURRENT TASK: %s' % contents[currenttask])
        print('==============================')
        print('(g)et task list, (n)ext task, (a)dd a task, (q)uit')
        response = str(input('>>> ').lower())
        if response == 'g':
            print('----- CURRENT TASKS ------')
            print(contents)
            print('--------------------------')
        elif response == 'n':
            if currenttask < len(contents)-1:
                currenttask += 1
            else:
                currenttask = 0
        elif response == 'a':
            contents.append(addTask())
        elif response == 'q':
            quit()

run(contents, currenttask)
