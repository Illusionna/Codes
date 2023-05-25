#include <bits/stdc++.h>
using namespace std;

template <class T>
class seqstack{
	private:
		T* array;
		int max;
		int last;
	public:
		seqstack(int max){
			this->max = max;
			last = -1;
			array = new T(max);
			assert(array != NULL);
		}
		~seqstack(){
			delete []array;
		}
		seqstack(seqstack& copy){
			this->max = copy.max;
			this->last = copy.last;
			this->array = new T(copy.max);
			for(int i=0; i<=last; i++){
				array[i] = copy.array[i];
			}
		}
		bool push(T& x){
			if(last == max-1){
				return false;
			}
			last++;
			array[last] = x;
			return true;
		}
		bool pop(T& x){
			if(last == -1){
				return false;
			}
			x = array[last];
			last--;
			return true;
		}
		bool gettop(T& x){
			if(last == -1){
				return false;
			}
			x = array[last];
			return true;
		}
		bool IsEmpty(){
			return last==-1;
		}
		bool IsFull(){
			return last==max-1;
		}
		void MakeEmpty(){
			last = -1;
		}
};