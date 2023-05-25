#include <bits/stdc++.h>
using namespace std;
#include "seqstack.cpp"

int main(){
	seqstack<int> vector(5);
	cout << vector.IsEmpty() << " " << "The stack is empty" << endl;
	for(int i=0,x=100; i<5; i++,x=x+100){
		vector.push(x);
	}
	cout << vector.IsFull() << " " << "Now, the stack is full" << endl;
	int y;
	vector.pop(y);
	cout << y << endl;
	vector.pop(y);
	cout << "After twice pops, the top element is: ";
	vector.gettop(y);
	cout << y << endl;
	cout << vector.IsFull() << " " << "The stack isn't full" <<endl;
	cout << "***************************************" << endl;
	seqstack<int> v(vector);
	cout << "Deep copy the vector to create a new stack, then get the top element" << endl;
	v.gettop(y);
	cout << y << endl;
	v.pop(y);
	v.pop(y);
	cout << y << endl;
	v.MakeEmpty();
	cout << v.IsEmpty() << endl;
	cout << vector.IsEmpty() << endl;
	return 0;
}