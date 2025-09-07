def is_palindrome(s):
    return s == s[::-1]

def main():
    S = input().strip()
    n = len(S)
 
    for i in range(n):
        if is_palindrome(S[i:]):
            print(n + i)
            return

if __name__ == "__main__":
    main()