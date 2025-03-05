class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        title = title.lower()
        arr = title.split(" ")

        for i in range(len(arr)):
            if len(arr[i]) < 3:
                arr[i] = arr[i].lower()
            else:
                title = arr[i]
                title = title[0].upper() + title[1:]
                arr[i] = title
        
        return " ".join(arr)