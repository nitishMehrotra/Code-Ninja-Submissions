tempInput = raw_input().split()
M,K = int(tempInput[0]),int(tempInput[1])
SIZE = 24 * 60 + 1

_time_slots = [0 for i in range(SIZE)]
_time_slots[-1] = 1


def _reset():
	global _time_slots
	
	for i in range(0,SIZE):
		_time_slots[i] = 0
	_time_slots[-1] = 1
	return
	
def _set( start, end ):
	global _time_slots
	
	start = (start / 100 ) * 60 + (start % 100 )
	end = (end / 100 ) * 60 + (end % 100 )
	
	for i in range( start, end ):
		_time_slots[i] = 1
	
	return
	
def outputData():
	global _time_slots
	start = 0
	for j in range(0, SIZE):
		if ( _time_slots[j] == _time_slots[start] ):
			continue
		else:
			if( _time_slots[j] == 1 and _time_slots[start] == 0 ):
				if ( (j-start) >= K ):
					if ( j/60 == 24 ):
						print str(start/60).zfill(2) + " " + str(start%60).zfill(2) + " " +  str(0).zfill(2) + " " + str(j%60).zfill(2) 
					else:
						print str(start/60).zfill(2) + " " + str(start%60).zfill(2) + " " +  str(j/60).zfill(2) + " " + str(j%60).zfill(2) 
			start = j		
			
	return
	
def inputData():
	_reset()
	for _ in range(M):
		tempTime = raw_input().split()
		_start_time = int( tempTime[0] + tempTime[1] )
		_end_time = int( tempTime[2] + tempTime[3] )
		_set( _start_time, _end_time )
	
	outputData()
	

inputData()
