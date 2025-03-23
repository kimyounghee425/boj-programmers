#include <iostream>
#include <string>
#include <algorithm>
#include <utility>
using namespace std;

struct Student{
    int age;
    string name;
    int id;
};

bool compare_students (const Student &a, const Student &b){
    if (a.age != b.age){
        return a.age < b.age; // 나이 같으면 가입 순서(id) 대로 정렬
    }
    else{
        return a.id < b.id; // 아니면 큰게 뒤로 오게
    }
    
    
}




int main(){
    int N;
    cin >> N;

    Student students[N];

    for (int i = 0; i < N; i++){
        cin >> students[i].age >> students[i].name;
        students[i].id = i;
    }

    sort(students, students + N, compare_students);

    for (int i = 0; i < N; i++){
        cout << students[i].age << " " << students[i].name << "\n";
    }

    return 0;
}