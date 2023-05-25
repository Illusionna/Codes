#include <iostream>
using namespace std;
#include "linkstack.cpp"

int main() {
	int x;
	cout << "输入一个正整数： " << endl;
	cin >> x;
	linkstack<int> vector;
	cout << "**********************************" << endl;
	cout << "中间计算过程如下： " << endl;
	cout << "**********************************" << endl;
	int y;
	int count = 0; 
	do{
		y = x/2;
		int z = x%2;
		x = y;
		cout << y << " " << z << endl;
		vector.push(z);
		count++;
	}while(y!=0);
	cout << "**********************************" << endl;
	cout << "数学意义下二进制所对应的结果： " << endl;
	cout << "**********************************" << endl;
	for(int i=0; i<count; i++){
		int t;
		vector.pop(t);
		cout << t;
	}
	return 0;
}