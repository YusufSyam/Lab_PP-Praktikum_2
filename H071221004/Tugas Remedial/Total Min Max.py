n = list(map(int, input().split()))
m = list(n)

n.remove(max(n))
m.remove(min(m))
print(sum(n), sum(m))