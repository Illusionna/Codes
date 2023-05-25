#include <iostream>
using namespace std;

int KMP(const string& target, const string& pattern){
	int lenT = target.length();
	int lenP = pattern.length();
	int next[lenP];
	int j = 0;
	int k = -1;
	next[0] = -1;
	while(j < lenP){
		if(k == -1 || pattern[j] == pattern[k]){
			j++;
			k++;
			next[j] = k;
		}
		else{
			k = next[k];
		}
	}
	cout << "next[]: ";
	for(int t=0; t<lenP; t++)
	cout << next[t] << " ";
	cout << endl;
	cout << "KMP result: ";;
	int pi = 0;
	int pj = 0;
	while(pj < lenP && pi < lenT){
		if(pj == -1 || pattern[pj] == target[pi]){
			pi++;
			pj++;
		}
		else{
			pj = next[pj];
		}
	}
	if(pj < lenP){
		return -1;
	}
	else{
		return pi-pj;
	}
}

int main(){
	string target = "abdababaabcaabcadadaabaafbcfa";
	string pattern = "abaabc";
	cout << KMP(target, pattern);
	return 0;
}
