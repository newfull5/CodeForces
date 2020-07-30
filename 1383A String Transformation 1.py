for _ in range(int(input())):
    n = int(input())
    a = [ord(c) - ord('a') for c in input()]
    b = [ord(c) - ord('a') for c in input()]
 
    imp = False
    for i in range(n):
        if b[i] < a[i]:
            print(-1)
            imp = True
            break
    if imp:
        continue
 
    cnt = 0
 
    for i in range(21):
        s = []
        for j in range(n):
            ac = a[j]
            bc = b[j]
            if ac == i and ac < bc:
                s.append(j)
        if s:
            cnt += 1
            mn = min(map(lambda o: b[o], s))
            for j in s:
                a[j] = mn
 
    print(cnt)
