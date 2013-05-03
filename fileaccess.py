#Class for reading and writing text files               
class FileAccess:
    def __init__(self):
        self.string = ''
        self.filename = ''
        self.mode = ''
    #open a file to have operation performed on it
    def OpenFile(self, filename, mode):
        #create a variable to hold the name of the last file opened
        self.filename = filename
        #create a variable to hold the last mode
        self.mode = mode
        #open the user-specified file in the user-specified mode
        self.file = open(filename, mode)
    #end operations on a file
    def CloseFile(self):
        self.file.close()
    #read all lines of a file
    #FILE MUST BE IN A READABLE MODE
    def ReadFile(self):
        self.file.seek(0)
        string = ''
        for line in self.file.readlines():
            string+=line
        print(string)
    #similar to ReadFile, but returns a string
    def ToString(self):
        for line in self.file:
            self.string+=line
        return self.string
    #adds text to the end of a text file if in append/'a' mode. Otherwise, overwrites data
    def AddLine(self, new):
        self.file.write(new)
    #deletes the last line of a file
    def DeleteLine(self,lastline=True):
        if lastline == True:
            self.file.seek(0)
            #create a blank list to hold each line of the file
            linelist = []
            #get each line from the file and add it to a list
            for line in self.file.readlines():
                linelist.append(line)
            #delete last item in the list
            linelist = linelist[0:-1]
            #create a new string to hold all the lines
            string = ''
            #convert the list back into a string
            for line in linelist:
                string += line
            self.file.seek(0)
            #write to the file by closing current mode, opening write mode, closing write mode, then opening read mode
            self.CloseFile()
            self.OpenFile(self.filename,'w')
            self.file.write(string)
            self.CloseFile()
            self.OpenFile(self.filename,'r+')

'''
fa = FileAccess()
fa.OpenFile('list.txt','r+')
fa.ReadFile()
'''

