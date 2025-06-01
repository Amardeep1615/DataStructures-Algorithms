"""
DSA COMPLETE GUIDE (GEEKSFORGEEKS DEFINITIONS + EXAMPLES)
"""

# ========================================================================
# 1. Logic Building (Day 1)
# ========================================================================
"""
Definition (GfG): The process of developing step-by-step procedures to solve computational problems.
Key Aspects:
- Problem decomposition
- Pattern recognition
- Algorithmic thinking
"""
# Example: Finding factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)  # Recursive logic building

# ========================================================================
# 2. Complexity Analysis (Day 2)
# ========================================================================
"""
Time Complexity (GfG): Amount of time taken by an algorithm to run as function of input size.
Space Complexity (GfG): Amount of memory used by algorithm as function of input size.
"""
# O(n) Time, O(1) Space example
def linear_search(arr, x):
    for i in range(len(arr)):  # O(n) time
        if arr[i] == x:
            return i
    return -1

# ========================================================================
# 3. Arrays (Day 3)
# ========================================================================
"""
Definition (GfG): Collection of items stored at contiguous memory locations.
Characteristics:
- Fixed size (static arrays)
- Random access O(1)
- Homogeneous elements
"""
arr = [10, 20, 30]
print(arr[1])  # Output: 20 (O(1) access)

# ========================================================================
# 4. Searching Algorithms (Day 4)
# ========================================================================
"""
Binary Search (GfG): Search algorithm that finds position of target value within sorted array.
- Works by repeatedly dividing search interval in half
- Time: O(log n)
"""
def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# ========================================================================
# 5. Sorting Algorithms (Day 5)
# ========================================================================
"""
QuickSort (GfG): Divide-and-conquer algorithm that picks element as pivot and partitions array.
- Average: O(n log n)
- Worst: O(n²) (rare)
"""
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

# ========================================================================
# 6. Hashing (Day 6)
# ========================================================================
"""
Definition (GfG): Technique that maps data to fixed-size values using hash functions.
Applications:
- Hash tables
- Cryptography
- Data fingerprinting
"""
hash_table = {}
hash_table['apple'] = 1  # Insert O(1)
print(hash_table.get('apple'))  # Lookup O(1)

# ========================================================================
# 7. Two Pointer Technique (Day 7)
# ========================================================================
"""
Definition (GfG): Technique where two pointers traverse data structure until condition is met.
Use Cases:
- Pair sum problems
- Sliding window
"""
def two_sum(nums, target):
    left, right = 0, len(nums)-1
    while left < right:
        curr_sum = nums[left] + nums[right]
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []

# ========================================================================
# 8. Window Sliding Technique (Day 8)
# ========================================================================
"""
Definition (GfG): Technique to reduce nested loops to single loop by maintaining window.
Applications:
- Subarray problems
- String matching
"""
def max_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(len(arr)-k):
        window_sum = window_sum - arr[i] + arr[i+k]
        max_sum = max(max_sum, window_sum)
    return max_sum

# ========================================================================
# 9. Prefix Sum Technique (Day 9)
# ========================================================================
"""
Definition (GfG): Technique where prefix array stores cumulative sum to answer range queries.
Time: O(1) after O(n) pre-processing
"""
def prefix_sum(arr):
    prefix = [0]*(len(arr)+1)
    for i in range(len(arr)):
        prefix[i+1] = prefix[i] + arr[i]
    return prefix

# ========================================================================
# 10. Strings (Day 10)
# ========================================================================
"""
Definition (GfG): Sequence of characters represented as objects in Python.
Key Properties:
- Immutable in Python
- Unicode support
"""
s = "GeeksForGeeks"
print(s[::-1])  # String reversal

# ========================================================================
# 11. Recursion (Day 11)
# ========================================================================
"""
Definition (GfG): Process where function calls itself directly/indirectly.
Requirements:
- Base case
- Recursive case
"""
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# ========================================================================
# 12. Matrix/Grid (Day 12)
# ========================================================================
"""
Definition (GfG): 2D array with rows and columns.
Applications:
- Graph representation
- Image processing
"""
matrix = [[1, 2], [3, 4]]
print(matrix[1][0])  # Access element: 3

# ========================================================================
# 13. Stack (Day 13)
# ========================================================================
"""
Definition (GfG): LIFO structure where elements are inserted/deleted from same end.
Operations:
- push(), pop(), peek()
"""
stack = []
stack.append(1)  # push
stack.pop()      # pop

# ========================================================================
# 14. Queue (Day 14)
# ========================================================================
"""
Definition (GfG): FIFO structure where elements are inserted at rear and removed from front.
Variations:
- Circular queue
- Priority queue
"""
from collections import deque
q = deque()
q.append(1)  # enqueue
q.popleft()  # dequeue

# ========================================================================
# 15. Deque (Day 15)
# ========================================================================
"""
Definition (GfG): Double-ended queue allowing insertions/deletions at both ends.
Advantages:
- O(1) operations at both ends
"""
dq = deque()
dq.appendleft(1)  # Front insert
dq.pop()          # Rear delete

# ========================================================================
# 16. Linked List (Day 16)
# ========================================================================
"""
Definition (GfG): Linear data structure with nodes containing data and address of next node.
Types:
- Singly, Doubly, Circular
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# ========================================================================
# 17. Tree (Day 17)
# ========================================================================
"""
Definition (GfG): Hierarchical structure with root node and subtrees of children.
Terminology:
- Root, Leaf, Height
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ========================================================================
# 18. Heap (Day 18)
# ========================================================================
"""
Definition (GfG): Complete binary tree where parent nodes satisfy heap property.
Types:
- Min-heap, Max-heap
"""
import heapq
heap = []
heapq.heappush(heap, 3)  # Insert
heapq.heappop(heap)      # Extract min

# ========================================================================
# 19. Graph (Day 19)
# ========================================================================
"""
Definition (GfG): Non-linear structure with vertices/nodes connected by edges.
Representations:
- Adjacency matrix/list
"""
graph = {
    'A': ['B', 'C'],
    'B': ['D']
}

# ========================================================================
# 20. Greedy Algorithms (Day 20)
# ========================================================================
"""
Definition (GfG): Algorithm paradigm that builds solution piece by piece choosing locally optimal.
Characteristics:
- No reconsideration of choices
"""
# Activity Selection Problem
def activity_selection(start, end):
    activities = list(zip(start, end))
    activities.sort(key=lambda x: x[1])
    selected = [activities[0]]
    for curr in activities[1:]:
        if curr[0] >= selected[-1][1]:
            selected.append(curr)
    return selected

# ========================================================================
# 21. Dynamic Programming (Day 21)
# ========================================================================
"""
Definition (GfG): Technique that solves problems by breaking into subproblems and storing results.
Key Properties:
- Overlapping subproblems
- Optimal substructure
"""
# Fibonacci with memoization
def fib(n, memo={}):
    if n in memo: return memo[n]
    if n <= 2: return 1
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

# ========================================================================
# 22. Other Algorithms (Day 22)
# ========================================================================
"""
Additional Algorithm Types:
- Backtracking
- Divide and Conquer
- Randomized Algorithms
"""
# Backtracking example (N-Queens)
def solve_n_queens(n):
    def backtrack(row, cols, diags, anti_diags, path):
        if row == n:
            res.append(path[:])
            return
        for col in range(n):
            curr_diag = row - col
            curr_anti = row + col
            if (col in cols or curr_diag in diags or curr_anti in anti_diags):
                continue
            cols.add(col)
            diags.add(curr_diag)
            anti_diags.add(curr_anti)
            path.append(col)
            backtrack(row+1, cols, diags, anti_diags, path)
            path.pop()
            cols.remove(col)
            diags.remove(curr_diag)
            anti_diags.remove(curr_anti)
    res = []
    backtrack(0, set(), set(), set(), [])
    return res