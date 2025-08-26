class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while nums2 :
            nums1[m] = nums2.pop()
            m = m +1
          # Outer loop to traverse the array
     S   for i in range( m - 1):
            swapped = False 
        
        # Last i elements are already in place
            for j in range(m - i - 1):
          
            # If the current element is greater
            # than the next element
                if nums1[j] > nums1[j + 1]:
              
                # Swap the elements
                    nums1[j], nums1[j + 1] = nums1[j + 1], nums1[j]
                    swapped = True 

        # If no two elements were swapped by inner loop,
        # then break the loop
            if not swapped:
                break
     
