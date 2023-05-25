#include <iostream>
using namespace std;

template <class T>
class SeqList
{
private:
	T* array;
	int max;
	int last;
public:
	SeqList(int max);
	SeqList(SeqList& L);
	~SeqList();
	void output();
	bool insert(T& num, int position);
	bool remove(int position, T& x);
	bool isEmpty();
	bool isFull();
	int length();
	int size();
	int search(const T&);
	bool getData(int index, T& x);
	bool setData(int index, T& x);
	void makeEmpty();
};

template <class T>
SeqList<T>::SeqList(int max)
{
	this->array = new T[max];
	if (array == NULL)
	{
		cerr << "存储分配错误！" << endl;
		exit(1);
	}
	this->max = max;
	this->last = -1;
}
template <class T>
SeqList<T>::SeqList(SeqList& L)
{
	this->max = L.max;
	this->last = L.last;
	this->array = new T[max];
	if (array == NULL)
	{
		cerr << "存储分配错误！" << endl;
		exit(1);
	}
	for (int i = 0; i <= last; i++)
	{
		this->array[i] = L.array[i];
	}
}
template <class T>
SeqList<T>::~SeqList()
{
	delete[] this->array;
}
template <class T>
void SeqList<T>::output()
{
	for (int i = 0; i <= last; i++)
	{
		cout << array[i] << " ";
	}
	cout << endl;
}
template <class T>
bool SeqList<T>::insert(T& num, int position)
{
	if (last == max - 1)return false;
	if (position < 0 || position > last + 1)return false;
	for (int i = last; i >= position; i--)
	{
		array[i + 1] = array[i];
	}
	array[position] = num;
	last++;
	return true;
}
template <class T>
bool SeqList<T>::remove(int position, T& x)
{
	if (last == -1)return false;
	if (position < 0 || position > last)return false;
	x = array[position];
	for (int i = position; i < last; i++)
	{
		array[i] = array[i + 1];
	}
	last--;
}
template <class T>
bool SeqList<T>::isEmpty() {
	if (last == -1) {
		return true;
	}
	else {
		return false;
	}
}
template <class T>
bool SeqList<T>::isFull() {
	if (last == max-1) {
		return true;
	}
	else {
		return false;
	}
}
template <class T>
int SeqList<T>::length() {
	return last + 1;
}
template <class T>
int SeqList<T>::size() {
	return max;
}
template <class T>
int SeqList<T>::search(const T& x) {
	int index;
	for (index = 0; index <= last; index++) {
		if (array[index] == x) {
			return index;
		}
	}
	if (index == last + 1) {
		cout << "The number is not belonging to the array!" << endl;
	}
}
template <class T>
bool SeqList<T>::getData(int index, T& x) {
	if (index > last || index < 0) {
		return false;
	}
	else {
		x = array[index];
		return true;
	}
}
template <class T>
bool SeqList<T>::setData(int index, T& x) {
	if (0 <= index && index <= last) {
		array[index] = x;
		return true;
	}
	else {
		return false;
	}
}
template <class T>
void SeqList<T>::makeEmpty() {
	last = -1;
}