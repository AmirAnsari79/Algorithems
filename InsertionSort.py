def insertionSort(Array):
	length=len(Array)
	for i in range(1,length):
		key=Array[i]
		j=i-1
	
		while(j>-1 and Array[j]>key):
			Array[j+1]=Array[j]
			j-=1
	Array[j+1]=key

Array=list(map(int,input('enter a numbers').split()))
insertionSort(Array)
print(Array)
