import os
def makedir(path , dira):
    dir = os.getcwd()
    print(dir)
    dir = dir +'\\'+ path
    os.mkdir(dir)
    dir1 = '\\'+ dira + '.csv'
    dir2 = '\\' + dira + '博文.csv'
    dir3 = '\\cleaned.csv'
    dir_1 = dir+dir1
    dir_2 = dir+dir2
    dir_3 = dir+dir3
    return dir,dir_1,dir_2,dir_3


def getdir(dira, dirb, dirc):
    dir = os.getcwd()
    dir_1 = dir+dira
    dir_2 = dir+dirb
    dir_3 = dir+dirc
    return dir_1,dir_2,dir_3
