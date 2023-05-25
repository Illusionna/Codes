#include <iostream>
using namespace std;

template <class T>
struct linknode {
	T data;
	linknode* link;
	linknode() {
		link = NULL;
	}
	linknode(T& number, linknode<T>* p = NULL) {
		data = number;
		link = p;
	}
};

template <class T>
class link_queue {
	private:
		linknode<T>* front;
		linknode<T>* rear;
	public:
		link_queue() {
			front = NULL;
			rear = NULL;
		}
		~link_queue() {
			MakeEmpty();
		}
		link_queue(link_queue& L) {
			T val;
			linknode<T>* first = L.front;
			front = new linknode<T>(L.front->data);
			linknode<T>* p = front;
			while(first->link != NULL){
				val = first->link->data;
				p->link = new linknode<T>(val, NULL);
				first = first->link;
				p = p->link;
			}
			this->rear = p;
			delete p;
		}
		bool GetFront(T& x) {
			if (front == NULL) {
				return false;
			}
			x = front->data;
			return true;
		}
		bool depart(T& x) {
			if (front == NULL) {
				return false;
			}
			linknode<T>* p = front;
			x = front->data;
			front = front->link;
			delete p;
			return true;
		}
		bool IsEmpty() {
			return front == NULL;
		}
		void enter(T& x) {
			if (front == NULL) {
				front = new linknode<T>(x, NULL);
				rear = front;
				if (front == NULL) {
					exit(1);
				}
			}
			else {
				rear->link = new linknode<T>(x, NULL);
				if (rear->link == NULL) {
					exit(1);
				}
				rear = rear->link;
			}
		}
		void MakeEmpty() {
			linknode<T>* p;
			while (front != NULL) {
				p = front;
				front = front->link;
				delete p;
			}
		}
};