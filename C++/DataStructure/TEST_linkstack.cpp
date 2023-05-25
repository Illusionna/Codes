#include <bits/stdc++.h>
using namespace std;
#include "linkstack.cpp"

int main(){
	linkstack<int> vector;
	cout << vector.IsEmpty() << " " << "The vector is empty" << endl;
	for(int i=0,x=100; i<5; i++,x=x+100){
		vector.push(x);
	}
	int y;
	vector.pop(y);
	cout << "The first pop element is: " << y << endl;
	vector.pop(y);
	cout << "After twice pops, the top element is: ";
	vector.GetTop(y);
	cout << y << endl;
	cout << "*****************************************" << endl;
	linkstack<int> v(vector);
	v.pop(y);
	v.pop(y);
	cout << y << endl;
	cout << "The top element of the new stack is: ";
	v.GetTop(y);
	cout << y << endl;
	v.MakeEmpty();
	cout << v.IsEmpty() << " " << "The new vector is empty" << endl;
	cout << vector.IsEmpty() << " " << "The old vector isn't' empty" << endl;
	return 0;
}