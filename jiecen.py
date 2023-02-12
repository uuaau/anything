def jie(n):
    if n==1:
        return 1
    else:
        return jie(n-1)*n
def cen(n):
    if n==1:
        return 1
    else:
        return jie(n)+cen(n-1)

print(jie(5))
print(cen(5))












