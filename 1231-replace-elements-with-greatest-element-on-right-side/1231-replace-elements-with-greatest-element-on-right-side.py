class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        last = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            print(arr[i])
            if arr[i] > last:
                temp = arr[i]
                arr[i] = last
                last = temp
            else:
                arr[i] = last

        arr[-1] = -1
        #arr[0] = last
        return arr