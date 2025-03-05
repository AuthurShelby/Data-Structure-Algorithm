def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk {n} from rod {source} to rod {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, auxiliary)  # Move n-1 disks to auxiliary peg
    print(f"Move disk {n} from rod {source} to rod {destination}")  # Move nth disk to destination
    tower_of_hanoi(n - 1, auxiliary, source, destination)  # Move n-1 disks from auxiliary to destination

# Example usage
n = int(input('Enter the number of : '))  # Change this value for different number of disks
tower_of_hanoi(n, 'A', 'B', 'C')