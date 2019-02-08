import random
import timeit

def linearSearch(array, target):
    for i in range(0,len(array)):
        if array[i] == target:
            return True
    return False

def AlgorithmA(array, targetArray):
    for i in targetArray:
        linearSearch(array, i)

def mergeSort(array):
    if len(array) > 1:
        middle = len(array)//2
        right = array[:middle]
        left = array[middle:]
        mergeSort(right)
        mergeSort(left)

        i=0
        j=0
        k=0

        while j < len(right) and k < len(left):
            if right[j] < left[k]:
                array[i] = right[j]
                j+=1
            else:
                array[i] = left[k]
                k+=1
            i+=1

        while j < len(right):
            array[i] = right[j]
            i+=1
            j+=1
        while k < len(left):
            array[i] = left[k]
            i+=1
            k+=1

def binSearch(array, target, lowIndex = 0, highIndex=None):
    if highIndex == None:
        highIndex = len(array)-1
    if lowIndex > highIndex:
        return False
    else:
        midIndex = (lowIndex+highIndex)//2
        if target == array[midIndex]:
            return True
        elif target < array[midIndex]:
            return binSearch (array, target, lowIndex, midIndex-1)
        else:
            return binSearch(array, target, midIndex+1, highIndex)

def AlgorithmB(array, targetArray):
    mergeSort(array)
    for i in targetArray:
        binSearch(array, i)

def generateList(n):
    array = []
    for i in range(0,n):
        nextNum =  (random.randint(1,n+1)//2)*2
        array.append(nextNum)
    return array

def generateTargetList(k, array):
    targetArray = []
    firstHalfSize = k//2
    secondHalfSize = k-firstHalfSize
    for i in range (0,firstHalfSize):
        nextNum = array[random.randint(0,len(array)-1)]
        targetArray.append(nextNum)
    for i in range(0,secondHalfSize):
        nextNum = ((random.randint(1,len(array)+1)//2)*2)+1
        targetArray.append(nextNum)
    return targetArray



def main():
    global k, n
    setupA = '''from __main__ import AlgorithmA, generateList, generateTargetList, k, n
array = generateList(n)
targetArray = generateTargetList(k, array)
'''
    setupB = '''from __main__ import AlgorithmB, generateList, generateTargetList, k, n
array = generateList(n)
targetArray = generateTargetList(k, array)
'''
    stmtA = '''AlgorithmA(array, targetArray)
'''
    stmtB = '''AlgorithmB(array, targetArray)
'''

    i = 1000

    n = 1000
    print("N = 1000:")
    print("")
    print ("%-5s%-25s%-25s" % ('k','Algorithm A Time (ms)','Algorithm B Time (ms)'))
    print("_____________________________________________________________")
    for k in range(150,170):
        timeA = (timeit.timeit(stmt = stmtA, setup = setupA, number = i))*1000
        timeB = (timeit.timeit(stmt = stmtB, setup = setupB, number = i))*1000
        print("%-7d%-25d%-25d" % (k,timeA,timeB))
    print("")

    n = 2000
    print("N = 2000:")
    print("")
    print ("%-5s%-25s%-25s" % ('k','Algorithm A Time (ms)','Algorithm B Time (ms)'))
    print("_____________________________________________________________")
    for k in range(150,170):
        timeA = (timeit.timeit(stmt = stmtA, setup = setupA, number = i))*1000
        timeB = (timeit.timeit(stmt = stmtB, setup = setupB, number = i))*1000
        print("%-7d%-25d%-25d" % (k,timeA,timeB))
    print("")

    n = 5000
    print("N = 5000:")
    print("")
    print ("%-5s%-25s%-25s" % ('k','Algorithm A Time (ms)','Algorithm B Time (ms)'))
    print("_____________________________________________________________")
    for k in range(150,170):
        timeA = (timeit.timeit(stmt = stmtA, setup = setupA, number = i))*1000
        timeB = (timeit.timeit(stmt = stmtB, setup = setupB, number = i))*1000
        print("%-7d%-25d%-25d" % (k,timeA,timeB))
    print("")

    n = 10000
    print("N = 10000:")
    print("")
    print ("%-5s%-25s%-25s" % ('k','Algorithm A Time (ms)','Algorithm B Time (ms)'))
    print("_____________________________________________________________")
    for k in range(150,170):
        timeA = (timeit.timeit(stmt = stmtA, setup = setupA, number = i))*1000
        timeB = (timeit.timeit(stmt = stmtB, setup = setupB, number = i))*1000
        print("%-7d%-25d%-25d" % (k,timeA,timeB))


main()
