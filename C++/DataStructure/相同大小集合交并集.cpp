#include <iostream>
using namespace std;
#include "linklist.cpp"

void input(int* set, int len) {
	for (int i = 0; i < len; i++) {
		cin >> set[i];
	}
}

int main() {
	int set1[5], set2[5];
	int len1 = sizeof(set1) / 4;
	int len2 = sizeof(set2) / 4;
	cout << "依次往集合里添加元素： " << endl;
	input(set1, len1);
	input(set2, len2);

	LinkList<int> Union;
	int i = 0;
	for (i; i < len1; i++) {
		Union.insert(i, set1[i]);
	}
	for (int j = i; j < (len1 + len2); j++) {
		Union.insert(j, set2[j - i]);
	}
	cout << "************************************" << endl;
	cout << "已完成两集合的叠加......" << endl;
	Union.show();
	cout << "************************************" << endl;

	LinkList<int> Uni;
	LinkList<int> Int;
	for (int i = 0; i < len1; i++) {
		int t1 = set1[i];
		for (int j = 0; j < len2; j++) {
			int t2 = set2[j];
			if (t1 == t2) {
				Int.insert(Int.length(), t2);
			}
		}
	}
	cout << "交集为： ";
	Int.show();
	cout << "************************************" << endl;
	for (int i = 0; i < Int.length(); i++) {
		int k;
		Int.GetData(i, k);
		Union.remove(Union.search(k), k);
	}
	cout << "并集为： ";
	Union.show();
	return 0;
}