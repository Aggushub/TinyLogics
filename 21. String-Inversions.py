#InfoSys SP Coding Qn #2
'''
You are given an array of strings.
For every pair (i, j) such that i < j, if:

-> str[i] > str[j]   (lexicographically)

then it is called a lexicographical inversion → increase the inversion count.

Return the total number of inversions.
'''

def countInversions(arr):
    def mergeSort(arr):
        if len(arr) <= 1:
            return arr, 0
        
        mid = len(arr) // 2
        left, invL = mergeSort(arr[:mid])
        right, invR = mergeSort(arr[mid:])
        
        merged, invM = merge(left, right)
        return merged, invL + invR + invM

    def merge(left, right):
        i = j = inv = 0
        result = []
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                inv += (len(left) - i)   # All remaining in left are > right[j]
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result, inv

    _, total_inversions = mergeSort(arr)
    return total_inversions

# Example:
arr = ["dog", "cat", "apple"]
print(countInversions(arr))  # Output: 3