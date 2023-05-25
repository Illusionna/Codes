#include <iostream>
#include <fstream>
using namespace std;

template <class T>
struct BinaryTreeVertex {
	T data;
	BinaryTreeVertex<T>* LeftSubtree;
	BinaryTreeVertex<T>* RightSubtree;
	BinaryTreeVertex() {
		this->LeftSubtree = NULL;
		this->RightSubtree = NULL;
	}
	BinaryTreeVertex(T x, BinaryTreeVertex<T>* L, BinaryTreeVertex<T>* R) {
		this->data = x;
		this->LeftSubtree = L;
		this->RightSubtree = R;
	}
};
template <class T>
class BinaryTree {
private:
	BinaryTreeVertex<T>* root;
	T EndTag;
protected:
	BinaryTreeVertex<T>* Copy(BinaryTreeVertex<T>* root);
	void CreateBinaryTree(ifstream& in, BinaryTreeVertex<T>*& subtree);
	void Destroy(BinaryTreeVertex<T>* subroot);
	void PreOrder(BinaryTreeVertex<T>* subroot);
	void InOrder(BinaryTreeVertex<T>* subroot);
	void PostOrder(BinaryTreeVertex<T>* subroot);
	int Height(BinaryTreeVertex<T>* subroot);
	int Size(BinaryTreeVertex<T>* subroot);
public:
	BinaryTree();
	BinaryTree(T value);
	~BinaryTree();
	BinaryTree(BinaryTree<T>& L);
	bool IsEmpty();
	int Height();
	int Size();
	void CreatePreOrder(ifstream& in);
	void PreOrder();
	void InOrder();
	void PostOrder();
	BinaryTreeVertex<T>* GetRoot();
};

template <class T>
BinaryTreeVertex<T>* BinaryTree<T>::Copy(BinaryTreeVertex<T>* Root) {
	if (Root == NULL) {
		return NULL;
	}
	BinaryTreeVertex<T>* t = new BinaryTreeVertex<T>;
	t->data = Root->data;
	t->LeftSubtree = Copy(Root->LeftSubtree);
	t->RightSubtree = Copy(Root->RightSubtree);
	return t;
}
template <class T>
void BinaryTree<T>::CreateBinaryTree(ifstream& in, BinaryTreeVertex<T>*& subtree) {
	T item;
	if (!in.eof()) {
		in >> item;
		if (item != EndTag) {
			subtree = new BinaryTreeVertex<T>(item, NULL, NULL);
			if (subtree == NULL) {
				cerr << "Allocation Error!" << endl;
				exit(1);
			}
			CreateBinaryTree(in, subtree->LeftSubtree);
			CreateBinaryTree(in, subtree->RightSubtree);
		}
		else {
			subtree = NULL;
		}
	}
}
template <class T>
void BinaryTree<T>::Destroy(BinaryTreeVertex<T>* subroot) {
	if (subroot != NULL) {
		Destroy(subroot->LeftSubtree);
		Destroy(subroot->RightSubtree);
		delete subroot;
		subroot = NULL;
	}
}
template <class T>
void BinaryTree<T>::PreOrder(BinaryTreeVertex<T>* subroot) {
	if (subroot != NULL) {
		cout << subroot->data << " ";
		PreOrder(subroot->LeftSubtree);
		PreOrder(subroot->RightSubtree);
	}
}
template <class T>
void BinaryTree<T>::InOrder(BinaryTreeVertex<T>* subroot) {
	if (subroot != NULL) {
		InOrder(subroot->LeftSubtree);
		cout << subroot->data << " ";
		InOrder(subroot->RightSubtree);
	}
}
template <class T>
void BinaryTree<T>::PostOrder(BinaryTreeVertex<T>* subroot) {
	if (subroot != NULL) {
		PostOrder(subroot->LeftSubtree);
		PostOrder(subroot->RightSubtree);
		cout << subroot->data << " ";
	}
}
template <class T>
int BinaryTree<T>::Height(BinaryTreeVertex<T>* subroot) {
	if (subroot == NULL) {
		return 0;
	}
	int NumberLeft = Height(subroot->LeftSubtree);
	int NumberRight = Height(subroot->RightSubtree);
	return NumberLeft > NumberRight ? (NumberLeft + 1) : (NumberRight + 1);
}
template <class T>
int BinaryTree<T>::Size(BinaryTreeVertex<T>* subroot) {
	if (subroot == NULL) {
		return 0;
	}
	int NumberLeft = Size(subroot->LeftSubtree);
	int NumberRight = Size(subroot->RightSubtree);
	return NumberLeft + NumberRight + 1;
}
template <class T>
BinaryTree<T>::BinaryTree() {
	root = NULL;
}
template <class T>
BinaryTree<T>::BinaryTree(T value) {
	EndTag = value;
	root = NULL;
}
template <class T>
BinaryTree<T>::~BinaryTree() {
	Destroy(root);
}
template <class T>
BinaryTree<T>::BinaryTree(BinaryTree<T>& L) {
	this->root = Copy(L.root);
}
template <class T>
bool BinaryTree<T>::IsEmpty() {
	return root == NULL;
}
template <class T>
int BinaryTree<T>::Height() {
	return Height(root);
}
template <class T>
int BinaryTree<T>::Size() {
	return Size(root);
}
template <class T>
void BinaryTree<T>::CreatePreOrder(ifstream& in) {
	CreateBinaryTree(in, root);
}
template <class T>
void BinaryTree<T>::PreOrder() {
	PreOrder(root);
}
template <class T>
void BinaryTree<T>::InOrder() {
	InOrder(root);
}
template <class T>
void BinaryTree<T>::PostOrder() {
	PostOrder(root);
}
template <class T>
BinaryTreeVertex<T>* BinaryTree<T>::GetRoot() {
	return root;
}

int main() {
	BinaryTree<char> Tree('@');
	if (Tree.IsEmpty()) {
		cout << "此时二叉树为空" << endl;
	}
	ifstream ifs("tree.txt");
	if (!ifs.is_open()) {
		cout << "> 找不到存放树结构的文件！" << endl;
		system("pause");
		return 0;
	}
	Tree.CreatePreOrder(ifs);
	ifs.close();
	cout << "********************************************" << endl;
	if (!Tree.IsEmpty()) {
		cout << "此时二叉树不为空" << endl;
	}
	cout << Tree.GetRoot()->data << endl;
	cout << Tree.GetRoot()->LeftSubtree->data << endl;
	cout << Tree.GetRoot()->RightSubtree->data << endl;
	cout << "前序遍历： ";
	Tree.PreOrder();
	cout << endl;
	cout << "中序遍历： ";
	Tree.InOrder();
	cout << endl;
	cout << "后序遍历： ";
	Tree.PostOrder();
	cout << endl;
	cout << "节点树： ";
	cout << Tree.Size() << endl;
	cout << "树的高： ";
	cout << Tree.Height() << endl;
	cout << "********************************************" << endl;
	BinaryTree<char> AnotherTree(Tree);
	cout << "Return: " << AnotherTree.IsEmpty() << " 此时新的二叉树不为空" << endl;
	cout << "Another New Tree 前序遍历： ";
	AnotherTree.PreOrder();
	cout << endl;
	system("pause");
	return 0;
}
