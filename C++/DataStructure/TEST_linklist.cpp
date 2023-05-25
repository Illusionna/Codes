#include <iostream>
using namespace std;
#include "linklist.cpp"

int main(){
	LinkList <int> seq;
	if (seq.IsEmpty())cout << "链表为空" << endl;
	else cout << "链表不为空" << endl;
	for (int i = 0; i < 5; i++)
	{
		seq.insert(i, i);
	}
	cout << "链表当前内容如下：" << endl;
	seq.show();
	if (seq.IsEmpty())cout << "链表为空" << endl;
	else cout << "链表不为空" << endl;
	int x;
	seq.remove(1, x);
	cout << "链表当前内容如下：" << endl;
	seq.show();
	if (seq.IsEmpty())cout << "链表为空" << endl;
	else cout << "链表不为空" << endl;
	cout << "链表内当前元素个数：" << seq.length() << endl;
	x = 3;
	cout << "数据" << x << "在链表中的索引位置为：" << seq.search(x) << endl;
	seq.GetData(1, x);
	cout << "链表中1号索引位置的数据值为：" << x << endl;
	x = 100;
	seq.SetData(2, x);
	cout << "链表当前内容如下：" << endl;
	seq.show();
	seq.MakeEmpty();
	if (seq.IsEmpty())cout << "链表为空" << endl;
	else cout << "链表不为空" << endl;
	return 0;
}