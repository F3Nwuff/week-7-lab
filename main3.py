class array:
    def __init__(self,arrlist=""):
        self.__arrlist = arrlist
    def get(self,i):
        return self.__arrlist[i]
    def append(self,i):
        return self.__arrlist.append(i)
    def pop(self):
        return self.__arrlist.pop()
    def extend(self,i):
        return self.__arrlist.extend(i)
    def insert(self,i,j):
        return self.__arrlist.insert(i,j)
    def index(self,i):
        return self.__arrlist.index(i)
    def length(self):
        return len(self.__arrlist)
