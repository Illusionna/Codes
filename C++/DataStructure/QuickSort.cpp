#include <iostream>
using namespace std;

int findmiddle(int array[], int start, int end){
	while(start < end){
		while(array[start] <= array[end] && start < end){
			end--;
		}
		if(start < end){
			int t = array[start];
			array[start] = array[end];
			array[end] = t;
		}
		while(array[start] <= array[end] && start < end){
			start++;
		}
		if(start < end){
			int t = array[start];
			array[start] = array[end];
			array[end] = t;
		}
	}
	return start;
}

void fastsort(int array[], int start, int end){
	int middle;
	if(!(start < end))
		return;
	else{
		middle = findmiddle(array, start, end);
		fastsort(array, start, middle-1);
		fastsort(array, middle+1, end);
	}
}

void show(int array[], int size){
	for(int i=0; i<size; i++)
		cout << array[i] << " ";
}

int main(){
	int array[]={90,100,86,77,52,83,75,98,67,81,83,92,86,1,24,70};
	int size = (sizeof(array))/(sizeof(int));
	findmiddle(array, 0, size-1);
	fastsort(array, 0, size-1);
	show(array,size);
	return 0;
}