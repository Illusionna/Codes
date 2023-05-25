#include <iostream>
using namespace std;

template <class T >
struct LinkNode {
	T data;
	LinkNode* link;
	LinkNode() {
		link = NULL;
	}
	LinkNode(T& number, LinkNode<T>* ptr = NULL) {
		data = number;
		link = ptr;
	}
};

template <class T>
class LinkList {
	private:
		LinkNode<T>* first;
	public:
		LinkList();
		LinkList(LinkList<T>& copy);
		~LinkList();
		int length();
		int search(T& x);
		bool GetData(int index, T& x);
		bool SetData(int index, T& x);
		bool insert(int index, T& x);
		bool remove(int index, T& x);
		bool IsEmpty();
		void MakeEmpty();
		void show();
};

template <class T>
LinkList<T>::LinkList() {
	first = new LinkNode<T>();
}
template <class T>
LinkList<T>::LinkList(LinkList<T>& copy) {
	T val;
	LinkNode<T>* head = copy.first;
	first = new LinkNode<T>();
	LinkNode<T>* table = first;
	while (head->link != NULL) {
		val = head->link->data;
		table->link = new LinkNode<T>(val, NULL);
	}
	table->link = NULL;
}
template <class T>
LinkList<T>::~LinkList() {
	LinkNode<T>* p = NULL;
	while (first != NULL) {
		p = first->link;
		delete first;
		first = p;
	}
	delete first;
}
template <class T>
int LinkList<T>::length() {
	LinkNode<T>* p = first->link;
	int count = 0;
	while (p != NULL) {
		count++;
		p = p->link;
	}
	return count;
}
template <class T>
int LinkList<T>::search(T& x) {
	LinkNode<T>* p = first->link;
	int index = 0;
	while (p != NULL) {
		if (p->data != x) {
			index++;
			p = p->link;
		}
		if (p->data == x) {
			return index;
		}
		if (p->link == NULL) {
			cout << "The Number is not belonging to the LinkList!" << endl;
			cout << "Return 0" << endl;
			return 0;
		}
	}
}
template <class T>
bool LinkList<T>::GetData(int index, T& x) {
	LinkNode<T>* p = first->link;
	while (index--) {
		p = p->link;
	}
	if (p != NULL) {
		x = p->data;
		return true;
	}
	else {
		return false;
	}
}
template <class T>
bool LinkList<T>::SetData(int index, T& x) {
	LinkNode<T>* p = first->link;
	while (index--) {
		p = p->link;
	}
	if (p->link != NULL) {
		p->data = x;
		return true;
	}
	else {
		return false;
	}
}
template <class T>
bool LinkList<T>::insert(int index, T& x) {
	LinkNode<T>* node = new LinkNode<T>(x, NULL);
	LinkNode<T>* current = first;
	while (index--) {
		current = current->link;
	}
	node->link = current->link;
	current->link = node;
	return true;
	if (current == NULL) {
		return false;
	}
}
template <class T>
bool LinkList<T>::remove(int index, T& x) {
	LinkNode<T>* current = first;
	while (index--) {
		current = current->link;
	}
	LinkNode<T>* temp;
	temp = current->link;
	x = temp->data;
	current->link = temp->link;
	delete temp;
	return true;
}
template <class T>
bool LinkList<T>::IsEmpty() {
	return first->link == NULL;
}
template <class T>
void LinkList<T>::MakeEmpty() {
	LinkNode<T>* p;
	while (first->link != NULL) {
		p = first->link;
		first->link = p->link;
		delete p;
	}
}
template <class T>
void LinkList<T>::show() {
	LinkNode<T>* p = first->link;
	while (p != NULL) {
		cout << p->data << " ";
		p = p->link;
	}
	cout << endl;
}