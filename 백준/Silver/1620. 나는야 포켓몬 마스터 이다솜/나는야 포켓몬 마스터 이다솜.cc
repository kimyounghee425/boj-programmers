#include <iostream>
#include <map>
#include <string>
using namespace std;
 
int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    int N, M;
    cin >> N >> M;
 
    map<string, int> m;
    map<int, string> m2;
 
    string name;
    for(int i = 1; i <= N; i++)
    {
        cin >> name;
        m[name] = i;
        m2[i] = name;
    }
 
    string prb;
    for(int i = 1; i<= M; i++)
    {
        cin >> prb;
        if(prb[0] >= '0' && prb[0] <= '9'){
            cout << m2[stoi(prb)] << "\n";
        }
        else{
            cout << m[prb] << "\n";
        }
    }
}