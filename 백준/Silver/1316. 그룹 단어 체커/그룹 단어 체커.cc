#include <stdio.h>
#include <string.h>

int main() {

  int n;
  char s[101];
  scanf("%d", &n);

  int flag;
  int ans = 0;
  while(n--) {
    scanf("%s", s);

    int isUsed[26] = { 0, };
    isUsed[s[0] - 'a'] = 1;
    flag = 1;

    for(int i = 1; i < strlen(s); i++) {
      if(s[i] == s[i - 1]) continue;

      if(isUsed[s[i] - 'a']) flag = 0;

      isUsed[s[i] - 'a'] = 1;
    }

    if(flag) ans++;
  }

  printf("%d", ans);  

  return 0;
}