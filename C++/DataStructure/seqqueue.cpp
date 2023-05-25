#include <iostream>
using namespace std;

template <class T>
class seq_queue {
private:
	int front, rear;
	T* array;
	int maxsize;
public:
	seq_queue(int max) {
		this->maxsize = max;
		this->front = 0;
		this->rear = 0;
		array = new T(maxsize);
		if (array == NULL) {
			exit(1);
		}
	}
	~seq_queue() {
		delete[]array;
	}
	seq_queue(seq_queue& L) {
		this->maxsize = L.maxsize;
		this->front = L.front;
		this->rear = L.rear;
		array = new T(maxsize);
		int Lmover = L.front;
		int Newmover = front;
		for (Lmover; Lmover <= L.rear; Lmover++) {
			array[Lmover] = L.array[Lmover];
		}
	}
	bool GetFront(T& x) {
		if (array == NULL) {
			return false;
		}
		x = array[front];
		return true;
	}
	bool IsEmpty() {
		return rear == front;
	}
	bool IsFull() {
		return ((rear + 1) % maxsize) == front;
	}
	bool enter(T& x) {
		if (IsFull()) {
			return false;
		}
		array[rear] = x;
		rear = (rear + 1) % maxsize;
		return true;
	}
	bool depart(T& x) {
		if (IsEmpty()) {
			return false;
		}
		x = array[front];
		front = (front + 1) % maxsize;
		return true;
	}
	void MakeEmpty() {
		front = 0;
		rear = 0;
	}
};