#!/user/bin/python
import re


class kset:

    def __init__(self,maxsize):
        self.__kset = [i for i in range(maxsize)]
        self.__graph = {}
        self.__relation = []
        self.__sets = maxsize
        self.__result = {}
        self.__sum = 0

    def __get(self,key):
        reobj = re.compile('\d+')
        match = reobj.findall(key)
        return [int(i) for i in match]

    def __sort(self):
        self.__relation = sorted( self.__graph.iteritems(), key=lambda d:d[1], reverse = False)

    def __father(self,node):
        tmp = []
        while node != self.__kset[node]:
            tmp = tmp + [node]
            node = self.__kset[node]
        for i in tmp:
            self.__kset[i] = node
        return node

    def __union(self, X,Y):
        self.__kset[Y] = self.__kset[X]

    def push(self, X, Y, V):
        key = X + 'to' + Y
        self.__graph[key] = V

    def work(self):
        print self.__graph
        self.__sort()
        print self.__relation
        for key,v in self.__relation:
            nodes = self.__get(key)
            print nodes
            if self.__father(nodes[0]) != self.__father(nodes[1]):
                self.__sum = self.__sum + v
                self.__sets = self.__sets-1
                self.__result[key] = v
                if self.__sets == 1:
                    return self.__sum



if  __name__ == '__main__':
    f = open('test')
    line = f.readline()
    reobj = re.compile('^\d+')
    match = reobj.findall(line)
    ks = kset(int(match[0]))
    line = f.readline()
    reobj = re.compile('\d+')
    while line:
        match = reobj.findall(line)
        if len(match) != 3:
            line = f.readline()
            continue
        ks.push(match[0],match[1],int(match[2]))
        line = f.readline()

    print ks.work()

