#include <iostream>
using namespace std;

int searchmax(int list[],int len){
	int max = list[0];
	for(int i=1; i<len; i++){
		if(max<=list[i]){
			max = list[i];
		}
	}
	return max;
}
void Arraysetting(int list[], int len){
	int temp[searchmax(list,len)+1]={0};
	for(int i=0; i<len; i++){
		temp[list[i]]++;
		if(temp[list[i]] == 1){
			cout << list[i] << " ";
		}
	}
}

// ���鼯�ϻ���ȥ���ظ�Ԫ��. 
int main(){
	int list[9] = {5,4,4,7,1,1,10,3,2};
	int len=9;
	Arraysetting(list,len);
	return 0;
}
