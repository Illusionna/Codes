#include <iostream>
using namespace std;

int main(){
	int i,j;
	int count;
	for(int i=1; i<10; i++){
		count = i;
		for(int j=i; j<10; j++){
			if(i*j < 10){
				cout << " " << i*j << "    ";
			}
			else{
				cout << i*j << "    ";
			}
		}
		cout << endl;
		do{
			cout << "      ";
		}while((--count)>0);
	}
	return 0;
}