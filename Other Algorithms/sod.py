def sod(n):
    if n == 0:
        return 0 
    return   n%10+sod(n//10)

if __name__ == "__main__":
    n = 5463
    print(sod(n))