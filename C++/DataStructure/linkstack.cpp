#include <bits/stdc++.h>
using namespace std;

template <class T>
struct linknode{
	T data;
	linknode* link;
	linknode(){
		link = NULL;
	}
	linknode(T& number, linknode<T>* p = NULL){
		data = number;
		link = p;
	}
}; 

template <class T>
class linkstack{
	private:
		linknode<T>* top;
	public:
		linkstack(){
			top = new linknode<T>();
		}
		linkstack(linkstack& copy){
			T val;
			linknode<T>* head = copy.top;
			top = new linknode<T>(copy.top->data);
			linknode<T>* p = top;
			while (head->link != NULL) {
				val = head->link->data;
				p->link = new linknode<T>(val, NULL);
				head = head->link;
				p = p->link;
			}
			p->link = NULL;
		}
		~linkstack(){
			MakeEmpty();
			delete top;
		}
		void push(T& x){
			linknode<T>* p = new linknode<T>(x, NULL);
			assert(p != NULL);
			p->link = top;
			top = p;
		}
		bool pop(T& x){
			if(top == NULL){
				return false;
			}
			linknode<T>* p = top;
			top = top->link;
			x = p->data;
			delete p;
			return true;
		}
		bool GetTop(T& x){
			if(top == NULL){
				return false;
			}
			x = top->data;
			return true;
		}
		bool IsEmpty(){
			return top==NULL;
		}
		void MakeEmpty(){
			linknode<T>* p;
			while(top != NULL){
				p = top;
				top = top->link;
				delete p;
			}
		}
};