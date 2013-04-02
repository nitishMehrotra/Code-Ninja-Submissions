import sys
sys.setrecursionlimit(50000)
T =  int (raw_input())
##Utility Functions
def _print(_array):
	for row in range(0,N):
		string = ""
		for column in range(0,N):
			string += " " + str(_array[row][column])
		print string

def _connectedSets(row,column):
	global _array,_iarray,N,outputfile
	##Left Neighbour
	_array[row][column] = 1
	if( (column - 1) >= 0 ):
		##Top
		if( (row - 1) >= 0 ):
			if(int(_iarray[row-1][column-1]) and (not _array[row-1][column-1])):
				_connectedSets (row-1,column-1)
		##Middle
		if(int(_iarray[row][column-1]) and (not _array[row][column-1])):
			_connectedSets (row,column-1)
		##Bottom	
		if( (row + 1) < N ):
			if(int(_iarray[row+1][column-1]) and not (_array[row+1][column-1])):
				_connectedSets (row+1,column-1)
	##Straight Neighbours
	if( (row - 1) >= 0 ):
		if(int(_iarray[row-1][column]) and (not _array[row-1][column])):
				_connectedSets (row-1,column)
	if( (row + 1) < N ):
		if(int(_iarray[row+1][column]) and (not _array[row+1][column])):
			_connectedSets (row+1,column)
	##Right Neighbours
	if( (column + 1) < N ):
		##Top
		if( (row - 1) >= 0 ):
			if(int(_iarray[row-1][column+1]) and (not _array[row-1][column+1])):
				_connectedSets (row-1,column+1)
		##Middle
		if(int(_iarray[row][column+1]) and (not _array[row][column+1])):
			_connectedSets (row,column+1)
		##Bottom	
		if( (row + 1) < N ):
			if(int(_iarray[row+1][column+1]) and not (_array[row+1][column+1])):
				_connectedSets (row+1,column+1)
			
##Inpu Function and calls the proccessing Function
def _inputData():
	for _ in range(0,N):
		_iarray.append( raw_input().split() )
	
	_processData()
	return

def _processData():
	label = 0;
	for row in range(0,N):
		for column in range(0,N):
			if(int(_iarray[row][column]) and (not _array[row][column])):
				label += 1
				_connectedSets(row,column)
	print label
	return

for _ in range(0,T):
	N = int (raw_input())
	_iarray = []
	_array = [[0 for i in range(0,N)] for i in range(0,N)]
	_inputData()
	
