# Solution 1
def rotate(nums, k):
    n = len(nums)
    start_idx = (n-k) % n
    nums[:] = nums[start_idx:] + nums[:start_idx]

# Example usage:
arr = [1, 2, 3, 6, 3, 2, 5, 2]
rotate(arr, 5)
print(arr)  # Output: [6, 3, 2, 5, 2, 1, 2, 3]

# Time Complexity Analysis: O(n)
# Slicing = O(n)
# In Place Reassignment = O(n)

# Space Complexity: O(n)
# Slicing + Concatenation = O(n



# Solution 2 (Space Complexity = O(1), Time Complexity = O(n))
def rotate(nums, k):
    n = len(nums)
    k = k % n
    
    # Step 1: Reverse the entire list -> O(n)
    nums.reverse()
    
    # Step 2: Reverse the first k elements -> O(k)
    nums[:k] = reversed(nums[:k])
    
    # Step 3: Reverse the rest of the elements -> O(n-k)
    nums[k:] = reversed(nums[k:])