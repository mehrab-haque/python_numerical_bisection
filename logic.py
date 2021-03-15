from tabulate import tabulate

K=0.05
pt=3

lb=-0.5
ub=0.1
max_iter=20
maxErrorPercentage=0.5

prevRoot = (ub+lb)/2

table = []

def func(x):
    return (x/(1-x)*(2*pt/(2+x))**0.5)-K

def bisect(lowerBound,upperBound,iteration):
    global ub,lb,prevRoot
    if iteration==0:
        return prevRoot
    currentRoot=(upperBound+lowerBound)/2
    errorPercentage = abs(((currentRoot-prevRoot)*100/currentRoot))
    if iteration==max_iter :
        errorPercentage='-'
    table.append([max_iter-iteration+1,currentRoot,errorPercentage])
    if iteration<max_iter and errorPercentage<=maxErrorPercentage:
        prevRoot=currentRoot
        return currentRoot
    if func(currentRoot)==0:
        return currentRoot
    elif func(lowerBound)*func(currentRoot)<0:
        upperBound=currentRoot
    else:
        lowerBound=currentRoot
    prevRoot=currentRoot
    return bisect(lowerBound,upperBound,iteration-1)




