class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        maxArea = 0
        stack = []

        for i in range(n + 1):
            while stack and (i == n  or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         stack = []

#         leftMost = [-1] * n
#         for i in range(n):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()
#             if stack:
#                 leftMost[i] = stack[-1]
#             stack.append(i)

#         stack = []
#         rightMost = [n] * n
#         for i in range(n - 1, -1, -1):
#             while stack and heights[stack[-1]] >= heights[i]:
#                 stack.pop()
#             if stack:
#                 rightMost[i] = stack[-1]
#             stack.append(i)

#         maxArea = 0
#         for i in range(n):
#             leftMost[i] += 1
#             rightMost[i] -= 1
#             maxArea = max(maxArea, heights[i] * (rightMost[i] - leftMost[i] + 1))
#         return maxArea
        
# class MinIdx_Segtree:
#     def __init__(self, N, A):
#         self.n = N
#         self.INF = int(1e9)
#         self.A = A
#         while (self.n & (self.n - 1)) != 0:
#             self.A.append(self.INF)
#             self.n += 1
#         self.tree = [0] * (2 * self.n)
#         self.build()

#     def build(self):
#         for i in range(self.n):
#             self.tree[self.n + i] = i
#         for j in range(self.n - 1, 0, -1):
#             a = self.tree[j << 1]
#             b = self.tree[(j << 1) + 1]
#             if self.A[a] <= self.A[b]:
#                 self.tree[j] = a
#             else:
#                 self.tree[j] = b

#     def update(self, i, val):
#         self.A[i] = val
#         j = (self.n + i) >> 1
#         while j >= 1:
#             a = self.tree[j << 1]
#             b = self.tree[(j << 1) + 1]
#             if self.A[a] <= self.A[b]:
#                 self.tree[j] = a
#             else:
#                 self.tree[j] = b
#             j >>= 1

#     def query(self, ql, qh):
#         return self._query(1, 0, self.n - 1, ql, qh)

#     def _query(self, node, l, h, ql, qh):
#         if ql > h or qh < l:
#             return self.INF
#         if l >= ql and h <= qh:
#             return self.tree[node]
#         a = self._query(node << 1, l, (l + h) >> 1, ql, qh)
#         b = self._query((node << 1) + 1, ((l + h) >> 1) + 1, h, ql, qh)
#         if a == self.INF:
#             return b
#         if b == self.INF:
#             return a
#         return a if self.A[a] <= self.A[b] else b

# class Solution:
#     def getMaxArea(self, heights, l, r, st):
#         if l > r:
#             return 0
#         if l == r:
#             return heights[l]
#         minIdx = st.query(l, r)
#         return max(max(self.getMaxArea(heights, l, minIdx - 1, st),
#                        self.getMaxArea(heights, minIdx + 1, r, st)),
#                    (r - l + 1) * heights[minIdx])

#     def largestRectangleArea(self, heights):
#         n = len(heights)
#         st = MinIdx_Segtree(n, heights)
#         return self.getMaxArea(heights, 0, n - 1, st)

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         n = len(heights)
#         maxArea = 0

#         for i in range(n):
#             height = heights[i]

#             rightMost = i + 1
#             while rightMost < n and heights[rightMost] >= height:
#                 rightMost += 1

#             leftMost = i
#             while leftMost >= 0 and heights[leftMost] >= height:
#                 leftMost -= 1

#             rightMost -= 1
#             leftMost += 1
#             maxArea = max(maxArea, height * (rightMost - leftMost + 1))
#         return maxArea