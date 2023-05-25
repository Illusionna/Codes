#include <iostream>
using namespace std;
#include "linkstack.cpp"

int main(){
	int x,n;
	cout << "输入一个整数，再输入进制： " << endl;
	cin >> x >> n;
	linkstack<int> vector;
	if(n == 1){
		cerr << "检测到n为1";
		exit(1);
	}
	cout << "**********************************" << endl;
	cout << "中间计算过程如下： " << endl;
	cout << "**********************************" << endl;
	int y;
	int count = 0; 
	do{
		y = x/n;
		int z = x%n;
		x = y;
		cout << y << " " << z << endl;
		vector.push(z);
		count++;
	}while(y!=0);
	cout << "**********************************" << endl;
	cout << n << "进制所对应的数学意义下结果： " << endl;
	cout << "**********************************" << endl;
	for(int i=0; i<count; i++){
		int t;
		vector.pop(t);
		cout << t;
	}
	return 0;
}