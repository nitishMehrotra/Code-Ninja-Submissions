# Enter your code here. Read input from STDIN. Print output to STDOUT
def inputData():
    T = input()
    inputNumbers = []
    for counter in range(T):
        inputNumbers.append(input())

    return inputNumbers

def scf(a,b):
    if(a%2==0 and b%2==0): return 2    
    for i in range(3 , b + 1 , 2):
        if( ( a%i == 0 ) and ( b%i == 0 ) ):
            return i
    return 1
def processData(numbers):
    outputData = []
    for value in numbers:
        prvs = 1
        F, D = 2, 1
        while( F <= value ):
            D = scf ( value , F )
            if( D > 1):
                outputData.append( (F , D ) )
                break;
            else:
                prvs,temp = F,prvs
                F = F + temp
        else:
            while(True):
                if ( F % value == 0):
                    outputData.append ( (F, value) )
                    break;
                else:
                    prvs,temp = F,prvs
                    F = F + temp

    printData(outputData)

def printData(numberTuple):
    for (F,D) in numberTuple:
        print F, D

processData(inputData())

