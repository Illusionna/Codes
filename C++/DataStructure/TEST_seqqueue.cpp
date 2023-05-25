#include <iostream>
using namespace std;
#include "seqqueue.cpp"

int main() {
	seq_queue<int> seqline(3);
	cout << seqline.IsEmpty() << endl;
	int x = 100;
	seqline.enter(x);
	x = 200;
	seqline.enter(x);
	x = 300;
	seqline.enter(x);
	cout << seqline.IsEmpty() << endl;
	cout << seqline.IsFull() << endl;
	int y;
	seqline.GetFront(y);
	cout << y << endl;
	seqline.depart(y);
	seqline.GetFront(y);
	cout << y << endl;
	cout << "******************************" << endl;
	seq_queue<int> s(seqline);
	s.GetFront(y);
	cout << y << endl;
	s.GetFront(y);
	cout << y << endl;
	s.MakeEmpty();
	cout << s.IsEmpty() << endl;
	cout << seqline.IsEmpty() << endl;
	return 0;
}