# Merge 2 sorted Arrays into 1
def merge_arrays(arr1, arr2):
    merged = []
    i, j = 0, 0

    # Traverse both arrays
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    # Append remaining elements of arr1 (if any)
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1

    # Append remaining elements of arr2 (if any)
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    return merged

# Example usage:
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
result = merge_arrays(arr1, arr2)
print(result)  # Output: [1, 2, 3, 4, 5, 6]