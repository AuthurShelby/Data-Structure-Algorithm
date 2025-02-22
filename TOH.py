def toh(n , source , auxi , dest):
    if n == 1:
        print(f'Disk {n} moved from {source} to {dest}')
        return 1
    toh(n-1 , source , dest , auxi)
    print(f'Disk {n} moved from {source} to {dest}')
    toh(n-1 , auxi , source , dest)
if __name__ == '__main__':
    toh(5, 1 , 2 , 3)