import sys

def min_max_linear(arr):
    maxx = -sys.maxsize - 1
    minn = sys.maxsize
    for i in arr:
        if(i > maxx):
            maxx = i
        if(i < minn):
            minn = i
    return maxx, minn

print(min_max_linear([45, 23, 65, 100]))