#include <iostream>
#include <cctype>

using namespace std;

int main() {
    string word;
    cin >> word;

    int max_count = 0;
    char max_char = '?';

    for (char ch = 'A'; ch <= 'Z'; ++ch) {
        int count = 0;
        for (char c : word) {
            if (toupper(c) == ch) count++;
        }

        if (count > max_count) {
            max_count = count;
            max_char = ch;
        } else if (count == max_count && count > 0) {
            max_char = '?';
        }
    }

    cout << max_char << endl;
    return 0;
}
