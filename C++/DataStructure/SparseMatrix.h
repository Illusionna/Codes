using namespace std;
#define dafaultsize 120

template <class T>
struct Trituple{
	int row;
	int column;
	T value;
	Trituple<T>& operator = (Trituple<T>& x){
		row = x.row;
		column = x.column;
		value = x.value;
		return * this;
	}
};

template <class T>
class SparseMatrix{
	private:
		int Rows;
		int Columns;
		int Terms;
		Trituple<T> * element;
		int maxTerms;
		friend ostream& operator << (ostream& out, SparseMatrix<T>& M);
		friend istream& operator >> (istream& in, SparseMatrix<T>& M);
	public:
		SparseMatrix(int maxSize = dafaultsize);
		~SparseMatrix();
		SparseMatrix<T>& operator = (SparseMatrix<T>& x);
		void add(SparseMatrix<T>& B, SparseMatrix<T>& C);
		void multiply(SparseMatrix<T>& B, SparseMatrix<T>& C);
		void Slow_transpose(SparseMatrix<T>& B);
		void Fast_transpose(SparseMatrix<T>& B);
};
template <class T>
ostream& operator << (ostream& out, SparseMatrix<T>& M){
	out << "rows = " << M.Rows << endl;
	out << "columns = " << M.Columns << endl;
	out << "Nonzero Terms = " << M.Terms << endl;
	for(int i=0; i<M.Terms; i++){
		out << "M[" << M.element[i].row << "][" << M.element[i].column << "]=" << M.element[i].value << endl;
	}
	return out;
}
template <class T>
istream& operator >> (istream& in, SparseMatrix<T>& M){
	cout << "Input the matrix's row and column: " << endl;
	in >> M.Rows >> M.Columns;
	Trituple<T> x;
	int End_Tag = -1;		// 行号 -1 控制输入结束 
	M.Terms = 0;
	cout << "Input the element's row, column and value: " << endl;
	in >> x.row >> x.column >> x.value;
	while(x.row != End_Tag){
		M.Insert(x);
		cout << "Input the element's row, column and value: " << endl;
		in >> x.row >> x.column >> x.value;
	}
	return in;
}
template <class T>
SparseMatrix<T>::SparseMatrix(int maxSize):maxTerms(maxSize){
	element = new Trituple<T>[maxSize];
	if(element == NULL){
		cerr << "Allocation Error!";
		exit(1);
	}
	Rows = Columns = Terms = 0;
}
template <class T>
SparseMatrix<T>::~SparseMatrix(){
	delete []element;
}
template <class T>
void SparseMatrix<T>::Slow_transpose(SparseMatrix<T>& B){
	B.Rows = Columns;
	B.Columns = Rows;
	B.Terms = Terms;
	if(Terms > 0){
		int k, i, CurrentB = 0;
		for(int k=0; k<Columns; k++){
			for(int i=0; i<Terms; i++){
				if(element[i].column == k){
					B.element[CurrentB].row = k;
					B.element[CurrentB].column = element[i].row;
					B.element[CurrentB].value = element[i].value;
					CurrentB++;
				}
			}
		}
	}
}
template <class T>
void SparseMatrix<T>::Fast_transpose(SparseMatrix<T>& B){
	int* rowsize = new int[Columns];
	int* rowstart = new int[Columns];
	B.Rows = Columns;
	B.Columns = Rows;
	B.Terms = Terms;
	if(Terms > 0){
		int i, j;
		for(i=0; i<Columns; i++){
			rowsize[i] = 0;
		}
		for(i=0; i<Terms; i++){
			rowsize[element[i].column]++;
		}
		rowstart[0] = 0;
		for(i=1; i<Columns; i++){
			rowstart[i] = rowstart[i-1] + rowsize[i-1];
		}
		for(i=0; i<Terms; i++){
			j = rowstart[element[i].column];
			B.element[j].row = element[i].column;
			B.element[j].column = element[i].row;
			B.element[j].value = element[i].value;
			rowstart[element[i].column]++;
		}
	}
	delete []rowsize;
	delete []rowstart;
}
template <class T>
void SparseMatrix<T>::add(SparseMatrix<T>& B, SparseMatrix<T>& C){
	if(Rows != B.Rows || Columns != B.Columns){
		cout << "The matrix has no consistent row and column!" << endl;
		exit(1);
	}
	int i, j = 0;
	int indexa, indexb;
	C.Terms = 0;
	while(i < Terms && j < B.Terms){
		indexa = Columns* element[i].row + element[i].column;
		indexb = Columns* B.element[j].row + B.element[j].column;
		if(indexa < indexb){
			C.element[C.Terms] = B.element[i];
			i++;
		}
		else if(indexa > indexb){
			C.element[C.Terms] = B.element[j];
			j++;
		}
		else{
			C.element[C.Terms] = element[i];
			C.element[C.Terms].value = element[i].value + B.element[i].value;
			i++;
			j++;
		}
		C.Terms++;
	}
	while(i < Terms){
		C.element[C.Terms] = element[i];
		C.Terms++;
		i++;
	}
	while(j < B.Terms){
		C.element[C.Terms] = B.element[i];
		C.Terms++;
		j++;
	}
}
template <class T>
void SparseMatrix<T>::multiply(SparseMatrix<T>& B, SparseMatrix<T>& C){
	if(Columns != B.Rows){
		cout << "The mutiplying has Error!";
		exit(1);
	}
	for(int i=0; i<Rows; i++){
		for(int j=0; j<B.Columns; j++){
			int sum = 0;
			int temp;
			for(int k=0; k<Columns; k++){
				temp = element[i][k].value * B.element[k][j].value;
				sum = sum + temp;
			}
			C.element[i][j] = sum;
			if(sum != 0){
				C.Terms++;
			}
		}
	}
}
