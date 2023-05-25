#include <iostream>
using namespace std;
#include "linkqueue.cpp"

int main() {
	link_queue<int> linkline;
	cout << linkline.IsEmpty() << endl;
	int x = 100;
	linkline.enter(x);
	x = 200;
	linkline.enter(x);
	x = 300;
	linkline.enter(x);
	cout << linkline.IsEmpty() << endl;
	int y;
	linkline.GetFront(y);
	cout << y << endl;
	linkline.depart(y);
	linkline.GetFront(y);
	cout << y << endl;
	cout << "**********************************" << endl;
	link_queue<int> l(linkline);
	l.depart(y);
	cout << y << endl;
	l.GetFront(y);
	cout << y << endl;
	l.MakeEmpty();
	cout << l.IsEmpty() << endl;
	cout << linkline.IsEmpty() << endl;
	return 0;
}