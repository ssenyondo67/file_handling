import string
import os
from trace import Trace

class file_manager:

    def __init__(self,file) -> None:
        self.__file=file
       
    
    def write_to(self):
        try:
            with open(self.__file,'w') as file:
                print('enter content to file if ')
                yes=True
                while yes:
                    line=input('enter stop any time to: ')
                    if line=='no' or line=='stop':
                        break
                    else:                             
                        file.write(line)
                        file.write("\n")
        except FileNotFoundError:
            print('file doesnot exist')
                
    def read_from(self):
        try:
            with open(self.__file,'r') as file:
                if os.stat(self.__file).st_size==0:
                    raise Exception('FileEmpty')
                else:
                    # lines=file.readlines()
                    for line in file:
                        print(line)
                        print()
        except FileNotFoundError:
            print('file doesnot exist')
      
    def delete(self):
        if os.path.exists(self.__file):
            os.remove(self.__file)
            return 'deleted'
        else:
            return 'failed'



class file_read:
    def __init__(self,file) -> None:
        self.__score={}
        self.__file=file
        

    def read(self):
        try:
            with open(self.__file,'r') as file:
                if os.stat(self.__file).st_size==0:
                    raise Exception('FileEmpty')
                else:
                    # lines=file.readlines()
                    for line in file:
                        print(line)
                        print()
        except FileNotFoundError:
            print('file doesnot exist')
        
    def sum(self):
        try:
            with open(self.__file,'r') as file: 
                if os.stat(self.__file).st_size==0:
                    raise Exception('FileEmpty')
                else:
                    # lines=file.readlines()
                    for line in file:
                        list=line.strip().split()
                        key = list[0]+" "+list[1]
                        if key in self.__score.keys():
                            self.__score[key] +=float(list[2])                                                      
                        else:
                            self.__score[key]=float(list[2])
            
        except FileNotFoundError:
            print('file doesnot exist')
        for key in self.__score.keys():
            print(key,self.__score[key],sep=':')

file=input('enter file name: ')
user=input('ENTER manage or use : ')
if user =='manage':
  
    manager=file_manager(file)
   
    n = input('do you want to enter content')
    if n != 'no':
        manager.write_to()
    
    r=input('do you want to read file: ')
    if r =='yes':
        manager.read_from()
    d =input('do you what to delete file: ')
    if d=='yes':
        manager.delete()
else:
    read_file=file_read(file)
    r=input('do you want to read file: ')
    if r =='yes':
        read_file.read()
    d =input('do you what to get sum file: ')
    if d=='yes':
        read_file.sum()