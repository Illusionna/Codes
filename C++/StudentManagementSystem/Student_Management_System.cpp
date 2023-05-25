#include <iostream>
#include <string.h>
#include <stdlib.h>
#include <iomanip>
#include <fstream>
#include <conio.h>
#include <windows.h>
using namespace std;

struct Student{
    Student* link;
    int number;
    char name[8];
    string ID;
    char phone[11];
    void input();
    void show();
};

void Student::input(){
	cout << "\t\t学号： ";
    cin >> number;
	cout << "\t\t姓名： ";
    cin >> name;
    cout << "\t\t身份证： ";
    cin >> ID;
    cout << "\t\t电话： ";
    cin >> phone;
}

void Student::show(){
    cout << "	|  " << number << "  |" << setw(8) << name << "  |  " << ID << "  |  " << phone << "  |" << endl; 
	cout << "	|-------------|----------|----------------------|---------------|\n";
}

class Message{
    private:
        Student* first;
        Student* last;
    public:
        Message();
		~Message();
		void Insert();
		void Remove();
		void Search();
		void Display();
        void Modify();
		friend void Menu();
    protected:
		void Save();
};

Message::Message(){
    first = new Student;
    last = first;
    ifstream I;
    I.open("originalData.txt",ios::in);
    if(!I.is_open()){
        cout << endl;
        cerr << "没有该文件，打开错误，即将退出程序！" << endl;
        Sleep(3000);
        exit(1);
    }
	while(!I.eof()){
		Student* p = new Student;
		I >> p->number >> p->name >> p->ID >> p->phone;
		last->link = p;
        last = p;
	}
}

Message::~Message(){
	Save();
	delete first;
	delete last;
}

void Message::Insert(){
	Student* p = new Student;
	p->input();
	p->show();
	last->link = p;
	last = p;
	cout << "继续..." << endl;
	getch();
}

void Message::Remove(){
	char ne[8];
	cout << "请输入删除的姓名： ";
	cin >> ne;
	Student* p = first;
	while(p != last){
		if(!(strcmp(p->link->name,ne))){
			Student* temp = p->link;
			cout << "该学生信息" << endl;
			temp->show();
			if(temp != last){
				p->link = temp->link;
				break;
			}
			else if(temp == last){
				last = p;
				cout << "继续..." << endl;
				getch();
				return;
			}
		}
		else{
			p= p->link;
		}
	}
	if(p == last){
		cout << "没有该学生信息，删除失败！" << endl;
	}
	cout << "继续..." << endl;
	getch();
}

void Message::Search(){
	cout << "请输入查找学生姓名： ";
	char ne[8];
	cin >> ne;
	Student* p = first;
	while(p->link != last){
		if(!strcmp(p->name,ne)){
			cout << "搜索成功！" << endl;
			p->show();
			cout << "继续..." << endl;
			break;
		}
		else{
			p = p->link;
		}
	}
	p = p->link;
	if(p == last && !strcmp(p->name,ne)){
		cout << "搜索成功！" << endl;
		p->show();
		cout << "继续..." << endl;
		getch();
	}
	else if(p == last && strcmp(p->name,ne)){
		cout << "没有该学生，搜素失败！" << endl;
	}
	getch();
}

void Message::Display(){
	cout << endl << endl;
	cout << "全员信息" << endl;
	Student* p = first->link;
	while(p != last){
		p->show();
		p = p->link;
	}
	last->show();
	cout << "继续..." << endl;
	getch();
}

void Message::Modify(){
    char ne[8];
    cout << "请输入学生姓名： ";
    cin >> ne;
    Student* p = first->link;
    while(p != last){
        if(!strcmp(p->name,ne)){
            p->show();
            cout << endl << endl;
            cout << "请修改该学生电话： ";
            cin >> p->phone;
            cout << "继续..." << endl;
            getch();
            break;
        }
        else{
            p = p->link;
        }
    }
    if(p == last && !strcmp(p->name,ne)){
        p->show();
        cout << endl << endl;
        cout << "请修改该学生电话： ";
        cin >> p->phone;
        cout << "继续..." << endl;
        getch();
    }
    else if(p == last && strcmp(p->name,ne)){
        cout << "没有该学生！" << endl;
        cout << "继续..." << endl;
        getch();
    }
}

void Menu(){
	cout << endl;
	cout << "\t0.退出系统" << endl;
	cout << "\t1.添加信息" << endl;
	cout << "\t2.删除信息" << endl;
	cout << "\t3.搜素信息" << endl;
	cout << "\t4.显示信息" << endl;
    cout << "\t5.修改信息" << endl;
	cout << endl;
	cout << "\t\t请输入： ";
}

void Message::Save(){
	Student* p = first->link;
	ofstream O;
	O.open("originalData.txt",ios::out);
	while(p != last){
		O << p->number << "	" << p->name << "	" << p->ID << "	" << p->phone << '\n';
		p = p->link;
	}
	O << last->number << "	" << last->name << "	" << last->ID << "	" << last->phone;
	O.close();
}

int main(){
    cout << endl << endl;
	cout << "\t\t\t\t\t\t欢迎使用学生管理系统" << endl;
	cout << endl;
	cout << "\t如果没有 originalData.txt 文件，请在同级文件夹里创建同名 ANSI 格式的记事本" << endl;
	cout << endl;
	cout << "\t加载中..." << endl;
	int number;
	Message G;
	bool judge = true;
	Sleep(3000);
	while(judge){
		system("cls");
		Menu();
		cin >> number;
		switch(number){
			case 0:
				judge = false;
				break;
			case 1:
				G.Insert();
				break;
			case 2:
				G.Remove();
				break;
			case 3:
				G.Search();
				break;
			case 4:
				G.Display();
				break;
            case 5:
                G.Modify();
                break;
		}
	}
	return 0;
}
