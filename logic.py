from tabulate import tabulate

K=0.05
pt=3

max_iter=20

prevRoot = 0

table = []

def func(x):
    return (x/(1-x)*(2*pt/(2+x))**0.5)-K

def bisect(lowerBound,upperBound,iteration,maxErrorPercentage):
    global prevRoot
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
    return bisect(lowerBound,upperBound,iteration-1,maxErrorPercentage)




