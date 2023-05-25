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
	cout << "\t\tѧ�ţ� ";
    cin >> number;
	cout << "\t\t������ ";
    cin >> name;
    cout << "\t\t���֤�� ";
    cin >> ID;
    cout << "\t\t�绰�� ";
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
        cerr << "û�и��ļ����򿪴��󣬼����˳�����" << endl;
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
	cout << "����..." << endl;
	getch();
}

void Message::Remove(){
	char ne[8];
	cout << "������ɾ���������� ";
	cin >> ne;
	Student* p = first;
	while(p != last){
		if(!(strcmp(p->link->name,ne))){
			Student* temp = p->link;
			cout << "��ѧ����Ϣ" << endl;
			temp->show();
			if(temp != last){
				p->link = temp->link;
				break;
			}
			else if(temp == last){
				last = p;
				cout << "����..." << endl;
				getch();
				return;
			}
		}
		else{
			p= p->link;
		}
	}
	if(p == last){
		cout << "û�и�ѧ����Ϣ��ɾ��ʧ�ܣ�" << endl;
	}
	cout << "����..." << endl;
	getch();
}

void Message::Search(){
	cout << "���������ѧ�������� ";
	char ne[8];
	cin >> ne;
	Student* p = first;
	while(p->link != last){
		if(!strcmp(p->name,ne)){
			cout << "�����ɹ���" << endl;
			p->show();
			cout << "����..." << endl;
			break;
		}
		else{
			p = p->link;
		}
	}
	p = p->link;
	if(p == last && !strcmp(p->name,ne)){
		cout << "�����ɹ���" << endl;
		p->show();
		cout << "����..." << endl;
		getch();
	}
	else if(p == last && strcmp(p->name,ne)){
		cout << "û�и�ѧ��������ʧ�ܣ�" << endl;
	}
	getch();
}

void Message::Display(){
	cout << endl << endl;
	cout << "ȫԱ��Ϣ" << endl;
	Student* p = first->link;
	while(p != last){
		p->show();
		p = p->link;
	}
	last->show();
	cout << "����..." << endl;
	getch();
}

void Message::Modify(){
    char ne[8];
    cout << "������ѧ�������� ";
    cin >> ne;
    Student* p = first->link;
    while(p != last){
        if(!strcmp(p->name,ne)){
            p->show();
            cout << endl << endl;
            cout << "���޸ĸ�ѧ���绰�� ";
            cin >> p->phone;
            cout << "����..." << endl;
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
        cout << "���޸ĸ�ѧ���绰�� ";
        cin >> p->phone;
        cout << "����..." << endl;
        getch();
    }
    else if(p == last && strcmp(p->name,ne)){
        cout << "û�и�ѧ����" << endl;
        cout << "����..." << endl;
        getch();
    }
}

void Menu(){
	cout << endl;
	cout << "\t0.�˳�ϵͳ" << endl;
	cout << "\t1.�����Ϣ" << endl;
	cout << "\t2.ɾ����Ϣ" << endl;
	cout << "\t3.������Ϣ" << endl;
	cout << "\t4.��ʾ��Ϣ" << endl;
    cout << "\t5.�޸���Ϣ" << endl;
	cout << endl;
	cout << "\t\t�����룺 ";
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
	cout << "\t\t\t\t\t\t��ӭʹ��ѧ������ϵͳ" << endl;
	cout << endl;
	cout << "\t���û�� originalData.txt �ļ�������ͬ���ļ����ﴴ��ͬ�� ANSI ��ʽ�ļ��±�" << endl;
	cout << endl;
	cout << "\t������..." << endl;
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
