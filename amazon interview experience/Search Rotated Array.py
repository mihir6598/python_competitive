 def search(self, A: List[int], key: int) -> int:
        low, high = 0, len(A) - 1
    
        while low <= high:
            mid = (low + high) // 2
            if key == A[mid]:
                return mid

            # This condition implies the first half of the array is ascending
            if A[low] <= A[mid]:
                # Is the key is in the first half?
                if key >= A[low] and key < A[mid]:
                    high = mid
                else:
                    low = mid + 1
            else: # The second half is ascending
                if key > A[mid] and key <= A[high]: # Is the key in the second half of the array?
                    low = mid + 1
                else:
                    high = mid

        return -1