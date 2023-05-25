#include <iostream>
using namespace std;
#include "seqlist.cpp"

int main()
{
	SeqList <int> seq(5);
	if (seq.isEmpty())cout << "顺序表为空" << endl;
	else cout << "顺序表不为空" << endl;
	if (seq.isFull())cout << "顺序表已满" << endl;
	else cout << "顺序表未满" << endl;

	for (int i = 0; i < 5; i++)
	{
		seq.insert(i, i);
	}
	cout << "顺序表当前内容如下：" << endl;
	seq.output();
	if (seq.isEmpty())cout << "顺序表为空" << endl;
	else cout << "顺序表不为空" << endl;
	if (seq.isFull())cout << "顺序表已满" << endl;
	else cout << "顺序表未满" << endl;
	int x;
	seq.remove(1, x);
	cout << "顺序表当前内容如下：" << endl;
	seq.output();
	if (seq.isEmpty())cout << "顺序表为空" << endl;
	else cout << "顺序表不为空" << endl;
	if (seq.isFull())cout << "顺序表已满" << endl;
	else cout << "顺序表未满" << endl;
	cout << "顺序表内当前元素个数：" << seq.length() << endl;
	cout << "顺序表内最大存放元素个数：" << seq.size() << endl;
	x = 3;
	cout << "数据" << x << "在顺序表中的索引位置为：" << seq.search(x) << endl;
	seq.getData(1, x);
	cout << "顺序表中1号索引位置的数据值为：" << x << endl;
	x = 100;
	seq.setData(2, x);
	cout << "顺序表当前内容如下：" << endl;
	seq.output();
	seq.makeEmpty();
	if (seq.isEmpty())cout << "顺序表为空" << endl;
	else cout << "顺序表不为空" << endl;
	return 0; 
}
