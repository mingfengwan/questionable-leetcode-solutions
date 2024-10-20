class Solution(object):
    def findKthNumber(self, n, k):
        curr = 1
        k -= 1
        diff = len(str(n)) - 1

        # To count how many numbers exist between prefix1 and prefix2
        def count_steps(prefix1, prefix2):
            return (1 - 10 ** (diff + 1)) // (1 - 10) - max(prefix2 * (10 ** diff) - n - 1, 0)

        while k > 0:
            if curr * (10 ** diff) > n:
                diff -= 1
            step = count_steps(curr, curr + 1)
            # If the steps are less than or equal to k, we skip this prefix's subtree
            if step <= k:
                # Move to the next prefix and decrease k by the number of steps we skip
                curr += 1
                k -= step
            else:
                # Move to the next level of the tree and decrement k by 1
                curr *= 10
                k -= 1

        return curr
