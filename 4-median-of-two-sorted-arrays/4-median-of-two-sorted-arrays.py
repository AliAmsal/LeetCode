class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = []
        l = len(nums1) + len(nums2)
        pos = (l+1)/2
        print(pos)
            
        if l%2 == 1:
            a = 0
            b = 0
            for i in range(int(pos)):
                if a >= len(nums1):
                    arr.append(nums2[b])
                    b += 1
                elif b >= len(nums2):
                    arr.append(nums1[a])
                    a += 1
                elif nums1[a] < nums2[b]:
                    arr.append(nums1[a])
                    a += 1
                else:
                    arr.append(nums2[b])
                    b += 1
            #print(arr)
            return arr[-1]
        else:
            pos += 0.5
            a = 0
            b = 0
            for i in range(int(pos)):
                if a >= len(nums1):
                    arr.append(nums2[b])
                    b += 1
                elif b >= len(nums2):
                    arr.append(nums1[a])
                    a += 1
                elif nums1[a] < nums2[b]:
                    arr.append(nums1[a])
                    a += 1
                else:
                    arr.append(nums2[b])
                    b += 1
            print(arr)
            return (arr[-1] + arr[-2])/2