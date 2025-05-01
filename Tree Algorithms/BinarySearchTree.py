class Node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    
    def __init__(self):
        self.root = None

    def insert(self ,root, value):
        # If the root is None, create a new node with the given value and return it
        if root is None:
            return Node(value)
        else:
            # If the value is greater than the current node's data, insert it into the right subtree
            if root.data  < value:
                root.right = self.insert(root.right , value)
            # Otherwise, insert it into the left subtree
            else:
                root.left = self.insert(root.left , value)
        # Return the root node after insertion
        return root
    
    # deleting a node
    def delete(self, node , value):  
        if node is None:
            return None
        
        if node.data < value: 
            node.right = self.delete(node.right , value )
        elif node.data > value:
            node.left = self.delete(node.left , value)
        else:
            # CASE 1 
            # if the node has no left or right child
            if node.left is None and node.right is None:
                return None

            # CASE 2 
            # if the node has one child either right or left
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # CASE 3 
            # if the node has both (left & right) child
            temp = self.minimum(node.right) # this takes the inorder successor (smallest in the right subtree)
            node.data = temp.data # Replacing the node data with the minimum data of the right child
            node.right = self.delete(node.right , temp.data)
    
        return node
    
     # left ->  root -> right
    def inorder(self , node):
        if node:
            # starts from the left
            self.inorder(node.left)
            print(node.data , end=' ')
            # ends at the right
            self.inorder(node.right)
    
    # root -> left -> right
    def preorder(self , node):
        if node: 
            print(node.data , end=' ')
            # first left
            self.preorder(node.left)
            # then right
            self.preorder(node.right)

    # left -> right -> root
    def postorder(self , node):
        if node:
            # checks all the left
            self.postorder(node.left)
            # then to the right
            self.postorder(node.right)
            print(node.data , end=' ')

    def search(self ,node , value):
        if node is None:
            return False

        # Check if the current node's data matches the value being searched
        if node.data == value:
            return True
        # If the value is greater than the current node's data, search in the right subtree
        if node.data < value:
            return self.search(node.right , value)
        # Otherwise, search in the left subtree
        else:
            return self.search(node.left , value)
        
    # for finding the minimum
    def minimum(self , node):
        if node is  None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    # for finding the maximum
    def maximum(self, node):
        if node is None:
            return None
        current = node
        while current.right is not None:
            current = current.right
        return current.data
    
def display_menu():
    print("\n==== Binary Search Tree Operations ====")
    print("1. Insert a value")
    print("2. Delete a value")
    print("3. Display Inorder Traversal")
    print("4. Display Preorder Traversal")
    print("5. Display Postorder Traversal")
    print("6. Search for a value")
    print("7. Find Minimum Value")
    print("8. Find Maximum Value")
    print("9. Exit")
    print("=====================================")
    return int(input("Enter your choice (1-9): "))

def main():
    bst = BinarySearchTree()
    
    while True:
        choice = display_menu()
        
        if choice == 1:
            try:
                value = int(input("Enter value to insert: "))
                bst.root = bst.insert(bst.root, value)
                print(f"Value {value} inserted successfully!")
            except ValueError:
                print("Please enter a valid integer!")
        
        elif choice == 2:

            tar = int(input('Enter the value to delete : '))
            bst.delete(bst.root , tar)

        elif choice == 3:
            print("\nInorder Traversal (Left -> Root -> Right):")
            if bst.root:
                bst.inorder(bst.root)
            else:
                print("Tree is empty!")
        
        elif choice == 4:
            print("\nPreorder Traversal (Root -> Left -> Right):")
            if bst.root:
                bst.preorder(bst.root)
            else:
                print("Tree is empty!")
        
        elif choice == 5:
            print("\nPostorder Traversal (Left -> Right -> Root):")
            if bst.root:
                bst.postorder(bst.root)
            else:
                print("Tree is empty!")
        
        elif choice == 6:
            try:
                value = int(input("Enter value to search: "))
                result = bst.search(bst.root, value)
                if result:
                    print(f"Value {value} found in the tree!")
                else:
                    print(f"Value {value} not found in the tree!")
            except ValueError:
                print("Please enter a valid integer!")
        
        elif choice == 7:
            minimum_value = bst.minimum(bst.root)
            if minimum_value:
                print(f'The minimum number in the tree is {minimum_value}')
            else:
                print('The tree is empty!')

        elif choice == 8:
            maximum_value = bst.maximum(bst.root)
            if maximum_value:
                print(f'The maximum number in the tree is {maximum_value}')
            else:
                print('The tree is empty!')

        elif choice == 9:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 9.")

if __name__ == "__main__":
    main()