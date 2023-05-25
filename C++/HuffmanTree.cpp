#include <iostream>
using namespace std;

template <class T>
struct TreeNode {
	T data;
	TreeNode* leftChild;
	TreeNode* rightChild;
	TreeNode* parent;
	TreeNode() {
		leftChild = NULL;
		rightChild = NULL;
		parent = NULL;
	}
	TreeNode(T element, TreeNode<T>* l = NULL, TreeNode<T>* r = NULL, TreeNode<T>* p = NULL) {
		this->data = element;
		this->leftChild = l;
		this->rightChild = r;
		this->parent = p;
	}
};
template <class T>
class MinHeap {
	private:
		TreeNode<T>** heap;
		int maxsize;
		int scale;
	public:
		MinHeap(T array[], int n);
		~MinHeap();
		void Show();
		bool Insert(TreeNode<T>*& node);
		bool Remove(TreeNode<T>*& removal);
		bool IsEmpty();
	protected:
		void SiftDown(int start, int end);
		void SiftUp(int terminal);
};
template <class T>
class HuffmanTree {
	private:
		TreeNode<T>* root;
	public:
		HuffmanTree(T array[], int n);
		~HuffmanTree();
		void PostOrder(void (*function)(TreeNode<T>* node));
	protected:
		void DeleteTree(TreeNode<T>* t);
		void MergeTree(TreeNode<T>* h1, TreeNode<T>* h2, TreeNode<T>*& pr);
		void PostOrder(TreeNode<T>* node, void (*function)(TreeNode<T>* node));
};

template <class T>
MinHeap<T>::MinHeap(T array[], int n) {
	maxsize = (10 < n) ? n : 10;
	heap = new TreeNode<T>*[maxsize];
	if (heap == NULL) {
		cerr << "Allocation Error" << endl;
		exit(1);
	}
	for (int i = 0; i < n; i++) {
		TreeNode<T>* p = new TreeNode<T>(array[i]);
		heap[i] = p;
	}
	scale = n;
	int start = (scale - 1) / 2;
	while (start >= 0) {
		SiftDown(start, scale - 1);
		start--;
	}
}
template <class T>
MinHeap<T>::~MinHeap() {
	delete[]heap;
}
template <class T>
void MinHeap<T>::Show() {
	for (int i = 0; i < scale; i++) {
		cout << heap[i] << " ";
	}
	cout << endl;
}
template <class T>
bool MinHeap<T>::Insert(TreeNode<T>*& node) {
	if (scale == maxsize) {
		cout << "Heap is Full" << endl;
		return false;
	}
	heap[scale] = node;
	SiftUp(scale);
	scale++;
	return true;
}
template <class T>
bool MinHeap<T>::Remove(TreeNode<T>*& removal) {
	if (scale <= 0) {
		cout << "Heap is Empty" << endl;
		return false;
	}
	removal = heap[0];
	heap[0] = heap[--scale];
	SiftDown(0, scale - 1);
	return true;
}
template <class T>
bool MinHeap<T>::IsEmpty() {
	return scale == 0;
}
template <class T>
void MinHeap<T>::SiftDown(int start, int end) {
	int i = start;
	int j = 2 * start + 1;
	TreeNode<T>* temp = heap[i];
	while (j <= end) {
		if (j == end) {

		}
		if (j < end && heap[j]->data > heap[j + 1]->data) {
			j++;
		}
		if (temp->data <= heap[j]->data) {
			break;
		}
		else {
			heap[i] = heap[j];
			i = j;
			j = 2 * j + 1;
		}
	}
	heap[i] = temp;
}
template <class T>
void MinHeap<T>::SiftUp(int terminal) {
	int i = terminal;
	int j = (terminal - 1) / 2;
	TreeNode<T>* temp = heap[terminal];
	while (i > 0) {
		if (heap[j]->data <= temp->data) {
			break;
		}
		else {
			heap[i] = heap[j];
			i = j;
			j = (j - 1) / 2;
		}
	}
	heap[i] = temp;
}
void display(TreeNode<float>* node) {
	while (node != 0) {
		cout << node->data << " ";
		node = node->parent;
	}
	cout << endl;
}
template <class T>
HuffmanTree<T>::HuffmanTree(T array[], int n) {
	MinHeap<T> object_heap(array, n);
	TreeNode<T>* removal_x;
	TreeNode<T>* removal_y;
	if (object_heap.IsEmpty()) {
		this->root = new TreeNode<T>;
	}
	else {
		int count = n;
		do {
			this->root = new TreeNode<T>;
			object_heap.Remove(removal_x);
			object_heap.Remove(removal_y);
			MergeTree(removal_x, removal_y, root);
			object_heap.Insert(root);
			n--;
		} while (n > 1);
	}
}
template <class T>
HuffmanTree<T>::~HuffmanTree() {
	DeleteTree(root);
}
template <class T>
void HuffmanTree<T>::PostOrder(void (*function)(TreeNode<T>* node)) {
	PostOrder(root, display);
}
template <class T>
void HuffmanTree<T>::DeleteTree(TreeNode<T>* t) {
	if (t == NULL) {
		return;
	}
	DeleteTree(t->leftChild);
	DeleteTree(t->rightChild);
	if (t->parent != NULL) {
		if (t == t->parent->leftChild) {
			t->parent->leftChild = NULL;
		}
		else if (t == t->parent->rightChild) {
			t->parent->rightChild = NULL;
		}
	}
	delete t;
}
template <class T>
void HuffmanTree<T>::MergeTree(TreeNode<T>* h1, TreeNode<T>* h2, TreeNode<T>*& pr) {
	pr->data = h1->data + h2->data;
	pr->leftChild = h1;
	pr->rightChild = h2;
	h1->parent = pr;
	h2->parent = pr;
}
template <class T>
void HuffmanTree<T>::PostOrder(TreeNode<T>* node, void (*function)(TreeNode<T>* node)) {
	if (node == NULL) {
		return;
	}
	function(node);
	PostOrder(node->leftChild, function);
	PostOrder(node->rightChild, function);
}

int main() {
	float a[] = { 7, 5, 2, 4 };
	HuffmanTree<float> ht(a, 4);
	ht.PostOrder(display);
	return 0;
}