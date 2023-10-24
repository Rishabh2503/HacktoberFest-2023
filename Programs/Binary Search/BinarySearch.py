def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == x:
            return mid  # Element found, return its index
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Element not found

# Input
n = int(input("Enter the size of the list: "))
a = [float(input("Enter element {}: ".format(i+1)) for i in range(n)]
x = float(input("Enter the desired element: "))


a.sort()

# Search for the element
result = binary_search(a, x)

# Output
if result != -1:
    print("Search is successful, and the position of the element is", result + 1)
else:
    print("Search unsuccessful")
