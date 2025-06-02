s = input()

a = s.replace("XXXX","AAAA")
b = a.replace("XX", "BB")

print(-1 if "X" in b else b)