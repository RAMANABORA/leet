class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:

        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first[idx] = min(first[idx], i)
            last[idx] = i

        intervals = []

        # Find valid intervals
        for c in range(26):

            if last[c] == -1:
                continue

            l = first[c]
            r = last[c]
            i = l
            valid = True

            while i <= r:

                idx = ord(s[i]) - ord('a')

                # This character appeared before l
                if first[idx] < l:
                    valid = False
                    break

                # Include all occurrences of this character
                r = max(r, last[idx])

                i += 1

            if valid:
                intervals.append((l, r))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        end = -1

        for l, r in intervals:

            if l > end:
                result.append(s[l:r + 1])
                end = r

        return result