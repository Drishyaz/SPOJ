def primes(n):
    c,i = 0,2
    while i <= n:
        if n%i==0:
            c += 1
        i *= i
        
    if c==0:
        return True
    else:
        return False
        
def main():
    for t in range(int(input())):
        l,u = map(int,input().split())
        for i in range(l,u+1):
            if i==1:
                continue
            if(primes(i)):
                print(i)

main()
