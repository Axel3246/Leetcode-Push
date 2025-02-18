class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        # 1. Create two stacks to keep track
        ss = []
        st = []

        # 2. Compute the first stack
        for char in s:
            if char == '#':
                if ss:
                    ss.pop()
            else:
                ss.append(char)

        # 3. Compute the second stack
        for char in t:
            if char == '#':
                if st:
                    st.pop()
            else:
                st.append(char)

        # Return the comparison
        return ss == st