n = int(input())
for i in range(n):
    s = input()
    l = len(s)
    if(l>=1 and l<=100):
        if (l>10):
            for i in range(l):
                m = len(s[1:l-1])
                m = str(m)
            print(s[0]+m+s[-1])
        else:
            print(s)