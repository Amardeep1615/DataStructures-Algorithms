"""
DSA COMPLETE STUDY PLAN
Run this file in VSCode with Python installed
Execute with: python dsa_complete.py
"""

def print_header(day, title):
    print(f"\n{'='*50}")
    print(f"DAY {day}: {title.upper()}")
    print(f"{'='*50}")

# ==============================================
# DAY 1: LOGIC BUILDING
# ==============================================
print_header(1, "Logic Building")

def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Is 17 prime?", is_prime(17))  # True
print("Is 15 prime?", is_prime(15))  # False

# ==============================================
# DAY 2: COMPLEXITIES
# ==============================================
print_header(2, "Complexities")

# O(1) - Constant Time
def get_first(arr):
    return arr[0]

# O(n) - Linear Time
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

print("First element:", get_first([1, 2, 3]))  # 1
print("Linear search:", linear_search([1, 2, 3], 2))  # 1

# ==============================================
# DAY 3: ARRAYS
# ==============================================
print_header(3, "Arrays")

arr = [1, 2, 3, 4]
print("Original array:", arr)
arr.append(5)  # Add to end
print("After append:", arr)
print("Element at index 2:", arr[2])  # O(1) access

# ==============================================
# DAY 4: SEARCHING ALGORITHMS
# ==============================================
print_header(4, "Searching Algorithms")

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

sorted_arr = [1, 2, 3, 4, 5, 6]
print("Binary search for 4:", binary_search(sorted_arr, 4))  # 3

# ==============================================
# DAY 5: SORTING ALGORITHMS
# ==============================================
print_header(5, "Sorting Algorithms")

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print("Bubble sort:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))

# ==============================================
# DAY 6: HASHING
# ==============================================
print_header(6, "Hashing")

from collections import defaultdict

word_freq = defaultdict(int)
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
for word in words:
    word_freq[word] += 1

print("Word frequencies:", dict(word_freq))

# ==============================================
# DAY 7: TWO POINTER TECHNIQUE
# ==============================================
print_header(7, "Two Pointer Technique")

def two_sum_sorted(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []

print("Two sum in sorted array:", two_sum_sorted([1, 2, 3, 4, 6], 6))  # [1, 3]

# ==============================================
# DAY 8: WINDOW SLIDING TECHNIQUE
# ==============================================
print_header(8, "Window Sliding Technique")

def max_subarray_sum(arr, k):
    max_sum = window_sum = sum(arr[:k])
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

print("Max subarray sum (k=3):", max_subarray_sum([2, 1, 5, 1, 3, 2], 3))  # 9

# ==============================================
# DAY 9: PREFIX SUM TECHNIQUE
# ==============================================
print_header(9, "Prefix Sum Technique")

def prefix_sum(arr):
    prefix = [0] * (len(arr) + 1)
    for i in range(1, len(arr) + 1):
        prefix[i] = prefix[i-1] + arr[i-1]
    return prefix

arr = [1, 2, 3, 4, 5]
print("Prefix sum array:", prefix_sum(arr))

# ==============================================
# DAY 10: STRINGS
# ==============================================
print_header(10, "Strings")

def reverse_string(s):
    return s[::-1]

print("Reversed string:", reverse_string("hello"))  # "olleh"

# ==============================================
# DAY 11: RECURSION
# ==============================================
print_header(11, "Recursion")

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial of 5:", factorial(5))  # 120

# ==============================================
# DAY 12: MATRIX/GRID
# ==============================================
print_header(12, "Matrix/Grid")

def print_matrix(matrix):
    for row in matrix:
        print(row)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("3x3 Matrix:")
print_matrix(matrix)

# ==============================================
# DAY 13: STACK
# ==============================================
print_header(13, "Stack")

stack = []
stack.append(1)  # push
stack.append(2)
stack.append(3)
print("Stack:", stack)
print("Popped:", stack.pop())  # 3 (LIFO)

# ==============================================
# DAY 14: QUEUE
# ==============================================
print_header(14, "Queue")

from collections import deque

queue = deque()
queue.append(1)  # enqueue
queue.append(2)
queue.append(3)
print("Queue:", queue)
print("Dequeued:", queue.popleft())  # 1 (FIFO)

# ==============================================
# DAY 15: DEQUE
# ==============================================
print_header(15, "Deque")

d = deque([1, 2, 3])
d.appendleft(0)  # add to front
d.append(4)      # add to end
print("Deque:", d)
print("Pop from end:", d.pop())       # 4
print("Pop from front:", d.popleft()) # 0

# ==============================================
# DAY 16: LINKED LIST
# ==============================================
print_header(16, "Linked List")

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Create a simple linked list: 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# Traverse the linked list
current = head
print("Linked List:")
while current:
    print(current.val, end=" -> ")
    current = current.next
print("None")

# ==============================================
# DAY 17: TREE
# ==============================================
print_header(17, "Tree")

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Create a simple binary tree
#       1
#      / \
#     2   3
#    /
#   4
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val, end=" ")
        inorder_traversal(node.right)

print("Inorder Traversal:")
inorder_traversal(root)  # 4 2 1 3

# ==============================================
# DAY 18: HEAP
# ==============================================
print_header(18, "Heap")

import heapq

min_heap = []
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 1)
heapq.heappush(min_heap, 2)

print("Min heap:")
while min_heap:
    print(heapq.heappop(min_heap), end=" ")  # 1 2 3

# ==============================================
# DAY 19: GRAPH
# ==============================================
print_header(19, "Graph")

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)
        
        print("BFS Traversal:")
        while queue:
            vertex = queue.pop(0)
            print(vertex, end=" ")
            
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.bfs(2)  # 2 0 3 1

# ==============================================
# DAY 20: GREEDY ALGORITHM
# ==============================================
print_header(20, "Greedy Algorithm")

def coin_change(coins, amount):
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            count += 1
    return count if amount == 0 else -1

print("Minimum coins needed:", coin_change([1, 5, 10], 18))  # 4 (10+5+1+1)

# ==============================================
# DAY 21: DYNAMIC PROGRAMMING
# ==============================================
print_header(21, "Dynamic Programming")

def fibonacci_dp(n):
    dp = [0, 1]
    for i in range(2, n+1):
        dp.append(dp[i-1] + dp[i-2])
    return dp[n]

print("Fibonacci(10):", fibonacci_dp(10))  # 55

# ==============================================
# DAY 22: OTHER ALGORITHMS
# ==============================================
print_header(22, "Other Algorithms")

# Dijkstra's, Kruskal's, etc. would go here
print("Advanced algorithms would be implemented here")

print("\nDSA STUDY PLAN COMPLETE!")