"""
DSA SORTING & SEARCHING ALGORITHMS CHEATSHEET
"""

# ===========================================================================
# 1. SELECTION SORT
# ===========================================================================
"""
Definition: In-place comparison sort that divides the list into sorted and unsorted parts.
Time Complexity: O(n²) in all cases
Space Complexity: O(1)
Use Case: Small datasets, memory constraint situations
"""
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Example:
print("Selection Sort:", selection_sort([64, 25, 12, 22, 11]))

# ===========================================================================
# 2. RADIX SORT
# ===========================================================================
"""
Definition: Non-comparative sort that processes digits from least to most significant.
Time Complexity: O(nk) where k is number of digits
Space Complexity: O(n+k)
Use Case: Sorting numbers with fixed digit length
"""
def radix_sort(arr):
    max_num = max(arr)
    exp = 1
    while max_num // exp > 0:
        counting_sort_by_digit(arr, exp)
        exp *= 10
    return arr

def counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1
        
    for i in range(1, 10):
        count[i] += count[i-1]
        
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index]-1] = arr[i]
        count[index] -= 1
        i -= 1
        
    for i in range(n):
        arr[i] = output[i]

# Example:
print("Radix Sort:", radix_sort([170, 45, 75, 90, 802, 24, 2, 66]))

# ===========================================================================
# 3. INSERTION SORT
# ===========================================================================
"""
Definition: Builds the sorted array one item at a time by comparisons.
Time Complexity: O(n²) worst case, O(n) best case (already sorted)
Space Complexity: O(1)
Use Case: Small or nearly sorted datasets
"""
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

# Example:
print("Insertion Sort:", insertion_sort([12, 11, 13, 5, 6]))

# ===========================================================================
# 4. COUNTING SORT
# ===========================================================================
"""
Definition: Non-comparison sort that counts occurrences of each value.
Time Complexity: O(n+k) where k is range of input
Space Complexity: O(n+k)
Use Case: Integer sorting with limited range
"""
def counting_sort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)
    output = [0] * len(arr)
    
    for num in arr:
        count[num] += 1
        
    for i in range(1, len(count)):
        count[i] += count[i-1]
        
    for num in reversed(arr):
        output[count[num]-1] = num
        count[num] -= 1
        
    return output

# Example:
print("Counting Sort:", counting_sort([4, 2, 2, 8, 3, 3, 1]))

# ===========================================================================
# 5. LINEAR SEARCH
# ===========================================================================
"""
Definition: Sequentially checks each element until a match is found.
Time Complexity: O(n)
Space Complexity: O(1)
Use Case: Unsorted data or small datasets
"""
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Example:
print("Linear Search Index:", linear_search([10, 50, 30, 70, 20], 30))

# ===========================================================================
# 6. ARRAYS
# ===========================================================================
"""
Definition: Contiguous memory locations storing elements of same type.
Key Operations:
- Access: O(1)
- Search: O(n)
- Insert/Delete at end: O(1)
- Insert/Delete at middle: O(n)
"""
array = [10, 20, 30, 40, 50]
array.append(60)  # Insert at end
array.pop(2)      # Remove at index 2 (30)

# ===========================================================================
# 7. BINARY SEARCH
# ===========================================================================
"""
Definition: Divide-and-conquer search in sorted arrays.
Time Complexity: O(log n)
Space Complexity: O(1)
Use Case: Sorted data
"""
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example:
print("Binary Search Index:", binary_search([10, 20, 30, 40, 50], 40))

# ===========================================================================
# 8. BUBBLE SORT
# ===========================================================================
"""
Definition: Repeatedly swaps adjacent elements if in wrong order.
Time Complexity: O(n²) worst/average case, O(n) best case (optimized version)
Space Complexity: O(1)
Use Case: Educational purposes, small datasets
"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

# Example:
print("Bubble Sort:", bubble_sort([64, 34, 25, 12, 22, 11, 90]))

# ===========================================================================
# 9. QUICK SORT
# ===========================================================================
"""
Definition: Divide-and-conquer using pivot element.
Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n) (stack space)
Use Case: General purpose sorting, large datasets
"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr)//2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example:
print("Quick Sort:", quick_sort([10, 7, 8, 9, 1, 5]))

# ===========================================================================
# 10. MERGE SORT
# ===========================================================================
"""
Definition: Divide-and-conquer using recursion and merging sorted subarrays.
Time Complexity: O(n log n) in all cases
Space Complexity: O(n)
Use Case: Stable sorting needed, large datasets
"""
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        
        merge_sort(L)
        merge_sort(R)
        
        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
            
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# Example:
print("Merge Sort:", merge_sort([38, 27, 43, 3, 9, 82, 10]))