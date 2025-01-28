#include <iostream>

using namespace std;

int main()
{
	long long int s;
	cin >> s;
	int i = 1;
	while (s >= i)
	{
		s -= i;
		i++;
	}
	cout << i - 1;
	return 0;
}