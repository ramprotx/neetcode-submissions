class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n                                  # rotating by n is a no-op, so reduce k (e.g. k=10, n=7 -> 3)

        def reverse(l: int, r: int) -> None:    # reverse nums[l..r] in place
            while l < r:                        # two pointers moving toward the middle
                nums[l], nums[r] = nums[r], nums[l]   # swap the two ends
                l, r = l + 1, r - 1             # step both pointers inward

        reverse(0, n - 1)                       # [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]  (last k now in front, but backwards)
        reverse(0, k - 1)                       # [7,6,5,...]     -> [5,6,7,4,3,2,1]  (fix the order of the first k)
        reverse(k, n - 1)                       # [...,4,3,2,1]   -> [5,6,7,1,2,3,4]  (fix the order of the rest)