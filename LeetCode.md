# Python LeetCode 必会

只收 **LC / FAANG 面试能写、能讲** 的东西。可运行版本：[Python-LeetCode必会.ipynb](./Python-LeetCode必会.ipynb)。

**能用：** `list` 当栈，`deque` 当队列，`heapq`，`Counter`，`defaultdict`，`@cache`。  
**手写：** 二分（不要依赖 `bisect`）。链表 / 树节点平台会给。  
**不要先学：** 线段树、KMP、状压。

| 题目给的 n | 你最多能写 | 面试里通常对应 |
|------------|------------|----------------|
| n ≤ 20 | 指数，`2^n`、`n!` | 回溯、状压 |
| n ≤ 10^3 | `O(n²)` 勉强，`O(n³)` 危险 | 双重循环、简单 DP |
| n ≤ 10^5 | 必须 `O(n)` 或 `O(n log n)` | 哈希、双指针、堆、二分、排序 |

---

## 模式总表

| 模式 | 细分 | 题目 |
|------|------|------|
| 双指针 | [对撞](#p-collide) | [167](#lc-167) [11](#lc-11) [15](#lc-15) [125](#lc-125) [42](#lc-42) |
| | [同向](#p-same) | [26](#lc-26) [283](#lc-283) [75](#lc-75) |
| 滑动窗口 | [最长合法](#p-win-long) | [3](#lc-3) [424](#lc-424) |
| | [最短合法](#p-win-short) | [209](#lc-209) [76](#lc-76) |
| | [固定窗口](#p-win-fixed) | [438](#lc-438) |
| | [单调队列](#p-win-mq) | [239](#lc-239) |
| 链表 | [反转](#p-list-rev) | [206](#lc-206) [92](#lc-92) [25](#lc-25) |
| | [快慢](#p-list-slow) | [876](#lc-876) [141](#lc-141) [142](#lc-142) [234](#lc-234) |
| | [dummy](#p-list-dummy) | [19](#lc-19) [21](#lc-21) [86](#lc-86) |
| | [相交](#p-list-cross) | [160](#lc-160) |
| | [深拷贝 / 相加](#p-list-copy) | [138](#lc-138) [2](#lc-2) |
| 哈希 | [互补查找](#p-hash-lookup) | [1](#lc-1) |
| | [分组](#p-hash-group) | [49](#lc-49) |
| | [连续段](#p-hash-run) | [128](#lc-128) |
| 前缀 | [哈希](#p-prefix) | [560](#lc-560) |
| | [前缀积](#p-prefix-prod) | [238](#lc-238) |
| | [差分](#p-diff) | [1109](#lc-1109) |
| | [二维](#p-prefix-2d) | [304](#lc-304) |
| 二分 | [下标](#p-bin-idx) | [35](#lc-35) |
| | [对答案](#p-bin-ans) | [875](#lc-875) |
| | [左右边界](#p-bin-bound) | [34](#lc-34) |
| | [旋转 / 峰值](#p-bin-rot) | [33](#lc-33) [153](#lc-153) [162](#lc-162) [74](#lc-74) |
| 栈 | [匹配](#p-stack) | [20](#lc-20) |
| | [单调栈](#p-mono-stack) | [739](#lc-739) [84](#lc-84) |
| | [计算 / 解码](#p-stack-eval) | [150](#lc-150) [224](#lc-224) [394](#lc-394) |
| 堆 | [Top K](#p-heap-k) | [215](#lc-215) [347](#lc-347) |
| | [多路合并](#p-heap-merge) | [23](#lc-23) |
| | [对顶堆](#p-heap-dual) | [295](#lc-295) |
| | [最短路](#p-dijkstra) | [743](#lc-743) |
| 二叉树 | [递归](#p-tree-rec) | [104](#lc-104) [226](#lc-226) [101](#lc-101) |
| | [分治 LCA](#p-tree-dnc) | [236](#lc-236) |
| | [层序](#p-tree-bfs) | [102](#lc-102) [199](#lc-199) |
| | [路径](#p-tree-path) | [543](#lc-543) [124](#lc-124) [112](#lc-112) |
| | [构造](#p-tree-build) | [105](#lc-105) |
| | [迭代中序](#p-tree-inorder) | [94](#lc-94) |
| | [序列化](#p-tree-ser) | [297](#lc-297) |
| BST | [验证 / 插入](#p-bst-ok) | [98](#lc-98) [701](#lc-701) [450](#lc-450) |
| | [第 K 小](#p-bst-k) | [230](#lc-230) |
| | [LCA](#p-bst-lca) | [235](#lc-235) |
| | [建树](#p-bst-build) | [108](#lc-108) |
| | [迭代器](#p-bst-iter) | [173](#lc-173) |
| | [后继](#p-bst-suc) | [285](#lc-285) |
| 网格 | [DFS](#p-grid-dfs) | [200](#lc-200) |
| | [多源 BFS](#p-grid-bfs) | [994](#lc-994) |
| 图 | [克隆](#p-graph-clone) | [133](#lc-133) |
| | [二分图](#p-bipartite) | [785](#lc-785) |
| | [单词变换](#p-word-bfs) | [127](#lc-127) |
| 回溯 | [排列](#p-bt-perm) | [46](#lc-46) [47](#lc-47) |
| | [子集](#p-bt-sub) | [78](#lc-78) |
| | [组合](#p-bt-comb) | [39](#lc-39) [40](#lc-40) |
| | [括号 / 电话](#p-bt-paren) | [22](#lc-22) [17](#lc-17) |
| | [网格](#p-bt-grid) | [79](#lc-79) |
| | [分割回文](#p-bt-pal) | [131](#lc-131) |
| 区间 | [合并 / 插入](#p-interval) | [56](#lc-56) [57](#lc-57) |
| | [扫描线](#p-sweep) | [253](#lc-253) [435](#lc-435) |
| 拓扑 | [Kahn](#p-topo) | [207](#lc-207) [210](#lc-210) |
| 并查集 | [合并](#p-uf) | [721](#lc-721) |
| 设计 | [Trie](#p-trie) | [208](#lc-208) |
| | [LRU](#p-lru) | [146](#lc-146) |
| | [最小栈](#p-min-stack) | [155](#lc-155) |
| | [O(1) 随机](#p-rand) | [380](#lc-380) |
| DP | [线性](#p-dp-lin) | [198](#lc-198) |
| | [Kadane](#p-kadane) | [53](#lc-53) |
| | [网格](#p-dp-grid) | [62](#lc-62) [64](#lc-64) |
| | [完全背包](#p-dp-unb) | [322](#lc-322) |
| | [0-1 背包](#p-dp-01) | [416](#lc-416) |
| | [LIS](#p-lis) | [300](#lc-300) |
| | [字符串](#p-dp-str) | [1143](#lc-1143) [72](#lc-72) [139](#lc-139) [91](#lc-91) |
| | [股票](#p-stock) | [121](#lc-121) [122](#lc-122) |
| | [树](#p-dp-tree) | [337](#lc-337) |
| 贪心 | [跳跃 / 环路 / 任务](#p-greedy) | [55](#lc-55) [134](#lc-134) [621](#lc-621) |
| 回文 | [中心扩展](#p-pal) | [5](#lc-5) |
| 位运算 | [XOR / 计数](#p-bit) | [136](#lc-136) [191](#lc-191) |
| 数学 | [快速幂](#p-pow) | [50](#lc-50) |
| 矩阵 | [旋转 / 螺旋 / 置零](#p-matrix) | [48](#lc-48) [54](#lc-54) [73](#lc-73) |
| | [从角搜索](#p-matrix-search) | [240](#lc-240) |
| 快选 | [第 K 大](#p-qselect) | [215](#lc-215-qs) |
| 循环定位 | [找重复](#p-cycle) | [287](#lc-287) |
| 排列 | [下一个](#p-next-perm) | [31](#lc-31) |

---

## 开写骨架

```python
from typing import List, Optional
from collections import defaultdict, Counter, deque, OrderedDict
from functools import cache
from heapq import heappush, heappop, heappushpop
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ...
```

---

## 会反复敲的语法

```python
# 除法：// 向下；向上 -(-a // b)。不要 math.ceil(a / b)
a, b = b, a
1 < x < n
s[0], s[-1], s[1:3], s[::-1], "".join(parts)
ord('A'), chr(65), ord(c) - ord('a')   # → 0..25
st.append(x); st.pop(); st[-1]          # 栈
q = deque([start]); q.append(x); q.popleft()
d = {}; d[k] = v; k in d; d.get(k, 0)   # 判断用 in
g = defaultdict(list); g[src].append(dst)
cnt = Counter(nums)
g = [[0] * n for _ in range(m)]         # 禁止 [[0]*n]*m
sorted(pairs, key=lambda x: (x[0], -x[1]))
```

假值：`None`、`0`、`''`、`[]`。空列表写 `if not nums`。`None` 用 `is None`。

`dict`：下一步是 `if k in d`。`defaultdict`：下一步是 `+= 1` 或 `.append`。

---

<a id="p-collide"></a>
## 双指针 · 对撞

有序（或高度这类能比较的量）时，两端各放一个指针。和太小就右移左端，太大就左移右端。每人最多走一遍，O(n)。先想清谁先动。

```
lo, hi = 0, n - 1
while lo < hi:
    if too_small: lo += 1
    elif too_big: hi -= 1
    else:        命中；停或两边同时收
```

<a id="lc-167"></a>
### LC 167 两数之和 II（有序）

本质上：有序数组里找两个数，和为 `target`，返回 1-based 下标。

```python
def twoSumSorted(numbers, target):
    lo, hi = 0, len(numbers) - 1
    while lo < hi:
        s = numbers[lo] + numbers[hi]
        if s == target:
            return [lo + 1, hi + 1]
        if s < target:
            lo += 1
        else:
            hi -= 1
    return []
```

<a id="lc-11"></a>
### LC 11 盛最多水的容器

本质上：两条竖线与 x 轴围出的最大面积。矮的一端往里收。

```python
def maxArea(height):
    lo, hi = 0, len(height) - 1
    ans = 0
    while lo < hi:
        ans = max(ans, min(height[lo], height[hi]) * (hi - lo))
        if height[lo] < height[hi]:
            lo += 1
        else:
            hi -= 1
    return ans
```

<a id="lc-15"></a>
### LC 15 三数之和（去重）

本质上：所有不重复的三元组，和为 0。先排序，固定 `i`，剩下对撞，跳过相同的 `i` / `lo` / `hi`。

```python
def threeSum(nums):
    nums.sort()
    n, ans = len(nums), []
    for i in range(n):
        if i and nums[i] == nums[i - 1]:
            continue
        lo, hi = i + 1, n - 1
        while lo < hi:
            s = nums[i] + nums[lo] + nums[hi]
            if s == 0:
                ans.append([nums[i], nums[lo], nums[hi]])
                lo += 1
                hi -= 1
                while lo < hi and nums[lo] == nums[lo - 1]:
                    lo += 1
                while lo < hi and nums[hi] == nums[hi + 1]:
                    hi -= 1
            elif s < 0:
                lo += 1
            else:
                hi -= 1
    return ans
```

<a id="lc-125"></a>
### LC 125 验证回文串

本质上：忽略非字母数字和大小写之后，是不是回文。

```python
def isPalindrome(s):
    lo, hi = 0, len(s) - 1
    while lo < hi:
        while lo < hi and not s[lo].isalnum():
            lo += 1
        while lo < hi and not s[hi].isalnum():
            hi -= 1
        if s[lo].lower() != s[hi].lower():
            return False
        lo += 1
        hi -= 1
    return True
```

<a id="lc-42"></a>
### LC 42 接雨水

本质上：柱子之间能接住的雨水总量。

```python
def trap(height):
    lo, hi = 0, len(height) - 1
    left_max = right_max = ans = 0
    while lo < hi:
        if height[lo] < height[hi]:
            left_max = max(left_max, height[lo])
            ans += left_max - height[lo]
            lo += 1
        else:
            right_max = max(right_max, height[hi])
            ans += right_max - height[hi]
            hi -= 1
    return ans
```

---

<a id="p-same"></a>
## 双指针 · 同向

`fast` 扫描，`slow` 写已处理区的下一位。适合原地删、移、分区。三指针是同向再加一个从右往左的边界。

```
slow = 0
for fast in 0 .. n-1:
    if nums[fast] 该留下:
        nums[slow] = nums[fast]
        slow += 1
# [0, slow) 是结果
```

<a id="lc-26"></a>
### LC 26 删除有序数组中的重复项

本质上：原地去掉相邻重复，返回新长度。

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    slow = 1
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow - 1]:
            nums[slow] = nums[fast]
            slow += 1
    return slow
```

<a id="lc-283"></a>
### LC 283 移动零

本质上：把 0 全部挪到末尾，非零相对顺序不变。

```python
def moveZeroes(nums):
    slow = 0
    for fast, x in enumerate(nums):
        if x != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
```

<a id="lc-75"></a>
### LC 75 颜色分类（三指针）

本质上：原地把 0 / 1 / 2 排好。

```python
def sortColors(nums):
    p0, i, p2 = 0, 0, len(nums) - 1
    while i <= p2:
        if nums[i] == 0:
            nums[p0], nums[i] = nums[i], nums[p0]
            p0 += 1
            i += 1
        elif nums[i] == 2:
            nums[p2], nums[i] = nums[i], nums[p2]
            p2 -= 1          # i 不前进
        else:
            i += 1
```

---

<a id="p-win-long"></a>
## 滑动窗口 · 最长合法

右端一格格扩；窗口一旦不合法，左端一直缩到合法。每个下标进一次出一次，O(n)。求的是过程中窗口的最大长度。

```
left = 0
for right in 0 .. n-1:
    把 a[right] 加进窗口
    while 窗口不合法:
        丢掉 a[left]；left += 1
    ans = max(ans, right - left + 1)
```

<a id="lc-3"></a>
### LC 3 无重复字符的最长子串

本质上：没有重复字符的最长子串长度。

```python
def lengthOfLongestSubstring(s):
    seen = set()
    left = ans = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        ans = max(ans, right - left + 1)
    return ans
```

<a id="lc-424"></a>
### LC 424 替换后的最长重复字符

本质上：最多改 `k` 次，能得到的最长相同字母子串。窗口内 `max频次 + k ≥ 窗口长` 就合法。

```python
def characterReplacement(s, k):
    cnt, left, best, ans = Counter(), 0, 0, 0
    for right, ch in enumerate(s):
        cnt[ch] += 1
        best = max(best, cnt[ch])
        while right - left + 1 - best > k:
            cnt[s[left]] -= 1
            left += 1
        ans = max(ans, right - left + 1)
    return ans
```

---

<a id="p-win-short"></a>
## 滑动窗口 · 最短合法

右端扩到窗口合法；合法就尽量左缩，每次缩完记长度。求的是满足条件的最小窗口。

```
left = 0
for right in 0 .. n-1:
    把 a[right] 加进窗口
    while 窗口合法:
        ans = min(ans, right - left + 1)
        丢掉 a[left]；left += 1
```

<a id="lc-209"></a>
### LC 209 长度最小的子数组

本质上：和 ≥ `target` 的最短连续子数组长度。

```python
def minSubArrayLen(target, nums):
    left = s = 0
    ans = math.inf
    for right, x in enumerate(nums):
        s += x
        while s >= target:
            ans = min(ans, right - left + 1)
            s -= nums[left]
            left += 1
    return 0 if ans is math.inf else ans
```

<a id="lc-76"></a>
### LC 76 最小覆盖子串

本质上：覆盖 `t` 全部字符的最短子串。`miss` 记还缺几种字符，缩到不合法为止。

```python
def minWindow(s, t):
    need, window = Counter(t), Counter()
    miss, left = len(need), 0
    best, start = math.inf, 0
    for right, ch in enumerate(s):
        window[ch] += 1
        if window[ch] == need[ch]:
            miss -= 1
        while miss == 0:
            if right - left + 1 < best:
                best, start = right - left + 1, left
            out = s[left]
            if window[out] == need[out]:
                miss += 1
            window[out] -= 1
            left += 1
    return "" if best is math.inf else s[start:start + best]
```

---

<a id="p-win-fixed"></a>
## 滑动窗口 · 固定窗口

窗口长度锁死为 k：右进一个，满了就左出一个。用计数 / 和判断当前窗口是否符合。

```
for i in 0 .. n-1:
    把 a[i] 加进窗口
    if i >= k:
        丢掉 a[i - k]
    if 窗口长度为 k 且合法:
        记录答案
```

<a id="lc-438"></a>
### LC 438 找到字符串中所有字母异位词

本质上：所有和 `p` 互为异位词的子串起点。

```python
def findAnagrams(s, p):
    need, window = Counter(p), Counter()
    miss, k, ans = len(need), len(p), []
    for i, ch in enumerate(s):
        window[ch] += 1
        if window[ch] == need[ch]:
            miss -= 1
        if i >= k:
            out = s[i - k]
            if window[out] == need[out]:
                miss += 1
            window[out] -= 1
        if i >= k - 1 and miss == 0:
            ans.append(i - k + 1)
    return ans
```

---

<a id="p-win-mq"></a>
## 滑动窗口 · 单调队列

队列存下标，对应值严格递减。新来的把队尾所有更小的挤掉；过期的从队头扔。队头永远是窗口最大。

```
q = deque()          # 下标，nums[q] 递减
for i in 0 .. n-1:
    while q 非空 and nums[q[-1]] <= nums[i]: q.pop()
    q.append(i)
    if q[0] <= i - k: q.popleft()
    if i >= k - 1: 答案 = nums[q[0]]
```

<a id="lc-239"></a>
### LC 239 滑动窗口最大值

本质上：每个长度为 `k` 的窗口里的最大值。

```python
def maxSlidingWindow(nums, k):
    q, ans = deque(), []
    for i, x in enumerate(nums):
        while q and nums[q[-1]] <= x:
            q.pop()
        q.append(i)
        if q[0] <= i - k:
            q.popleft()
        if i >= k - 1:
            ans.append(nums[q[0]])
    return ans
```

---

<a id="p-list-rev"></a>
## 链表 · 反转

没有下标，只能改 `next`。三个引用轮换：先把后继存下来，再把当前指向前一个。

```
prev, cur = None, head
while cur:
    nxt = cur.next
    cur.next = prev
    prev, cur = cur, nxt
return prev
```

<a id="lc-206"></a>
### LC 206 反转链表

本质上：原地把整条链反过来，返回新头。

```python
def reverseList(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    return prev
```

<a id="lc-92"></a>
### LC 92 反转链表 II（区间）

本质上：只反转第 `left` 到第 `right` 个节点。dummy 走到 `left` 前一个，头插 `right-left` 次。

```python
def reverseBetween(head, left, right):
    dummy = ListNode(0, head)
    pre = dummy
    for _ in range(left - 1):
        pre = pre.next
    cur = pre.next
    for _ in range(right - left):
        nxt = cur.next
        cur.next = nxt.next
        nxt.next = pre.next
        pre.next = nxt
    return dummy.next
```

<a id="lc-25"></a>
### LC 25 K 个一组翻转链表

本质上：每 k 个反转一段，不足 k 的保持原样。先探到第 k 个，再把这段反转接到 dummy 上。

```python
def reverseKGroup(head, k):
    dummy = ListNode(0, head)
    pre = dummy
    while True:
        tail = pre
        for _ in range(k):
            tail = tail.next
            if not tail:
                return dummy.next
        nxt = tail.next
        prev, cur = nxt, pre.next
        while cur is not nxt:
            tmp = cur.next
            cur.next = prev
            prev, cur = cur, tmp
        new_head = pre.next
        pre.next = tail
        pre = new_head
```

---

<a id="p-list-slow"></a>
## 链表 · 快慢

`fast` 一次两步，`slow` 一次一步。fast 到尾 → slow 在中点；两者相遇 → 有环。环入口：相遇后再从 head 齐步走。

```
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    # 中点：循环结束 slow 就是
    # 环：slow is fast 则有环；再从 head 齐走找入口
```

<a id="lc-876"></a>
### LC 876 链表的中间结点

本质上：中间那个节点（偶数个取后一个）。

```python
def middleNode(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

<a id="lc-141"></a>
### LC 141 环形链表

本质上：链上有没有环。

```python
def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

<a id="lc-142"></a>
### LC 142 环形链表 II（找入口）

本质上：环从哪个节点开始，没有环则 `None`。

```python
def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            p = head
            while p is not slow:
                p, slow = p.next, slow.next
            return p
    return None
```

<a id="lc-234"></a>
### LC 234 回文链表（中点 + 反转后半）

本质上：链上的值从前往后和从后往前是否一样。

```python
def isPalindromeList(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
    prev, cur = None, slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev, cur = cur, nxt
    while prev:
        if head.val != prev.val:
            return False
        head, prev = head.next, prev.next
    return True
```

---

<a id="p-list-dummy"></a>
## 链表 · dummy

真正的头可能会被删掉或换掉，先挂一个空节点在前面，最后返回 `dummy.next`。删倒数第 n：fast 先走 n 步再和 slow 一起走。

```
dummy = ListNode(0, head)
cur = dummy
# 或 slow = fast = dummy；fast 先走 n 步
...
return dummy.next
```

<a id="lc-19"></a>
### LC 19 删除链表的倒数第 N 个结点（再加快慢）

本质上：删掉倒数第 n 个，返回新头。fast 先走 n 步。

```python
def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    slow = fast = dummy
    for _ in range(n):
        fast = fast.next
    while fast.next:
        slow, fast = slow.next, fast.next
    slow.next = slow.next.next
    return dummy.next
```

<a id="lc-21"></a>
### LC 21 合并两个有序链表

本质上：两条有序链合成一条有序链。

```python
def mergeTwoLists(a, b):
    dummy = cur = ListNode()
    while a and b:
        if a.val <= b.val:
            cur.next, a = a, a.next
        else:
            cur.next, b = b, b.next
        cur = cur.next
    cur.next = a or b
    return dummy.next
```

<a id="lc-86"></a>
### LC 86 分隔链表（双链）

本质上：小于 `x` 的节点保持相对顺序排到前面。

```python
def partition(head, x):
    small_d, large_d = ListNode(), ListNode()
    s, l = small_d, large_d
    while head:
        if head.val < x:
            s.next = head
            s = s.next
        else:
            l.next = head
            l = l.next
        head = head.next
    l.next = None
    s.next = large_d.next
    return small_d.next
```

---

<a id="p-list-cross"></a>
## 链表 · 相交

两条链长度不同。走完自己就接对方：`p` 走 `A+B`，`q` 走 `B+A`，第一次相遇就是交点（没交则都走到 None）。

```
p, q = headA, headB
while p is not q:
    p = p.next if p else headB
    q = q.next if q else headA
return p
```

<a id="lc-160"></a>
### LC 160 相交链表

本质上：两条链第一个相交节点，没有则 `None`。

```python
def getIntersectionNode(a, b):
    p, q = a, b
    while p is not q:
        p = p.next if p else b
        q = q.next if q else a
    return p
```

---

<a id="p-list-copy"></a>
## 链表 · 深拷贝 / 相加

随机指针：先建 `旧→新` 映射，再接 `next` / `random`。两数相加：逐位加，进位单独当一圈。

```
mp = {}
for 每个旧节点: mp[旧] = 新节点(旧.val)
for 每个旧节点: mp[旧].next / .random = mp.get(对应)
```

<a id="lc-138"></a>
### LC 138 随机链表的复制

本质上：复制带 `random` 指针的链表。

```python
def copyRandomList(head):
    if not head:
        return None
    mp = {}
    cur = head
    while cur:
        mp[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:
        mp[cur].next = mp.get(cur.next)
        mp[cur].random = mp.get(cur.random)
        cur = cur.next
    return mp[head]
```

<a id="lc-2"></a>
### LC 2 两数相加

本质上：两条逆序数链相加，返回新链。

```python
def addTwoNumbers(l1, l2):
    dummy = cur = ListNode()
    carry = 0
    while l1 or l2 or carry:
        s = carry
        if l1:
            s += l1.val
            l1 = l1.next
        if l2:
            s += l2.val
            l2 = l2.next
        cur.next = ListNode(s % 10)
        carry = s // 10
        cur = cur.next
    return dummy.next
```

---

<a id="p-hash-lookup"></a>
## 哈希 · 互补查找

边走边存。当前 x 需要的另一半是 `need`；先查表再写入，避免自己配自己（按题意）。

```
idx = {}
for i, x in enumerate(a):
    if need(x) in idx: return idx[need(x)], i
    idx[x] = i
```

<a id="lc-1"></a>
### LC 1 两数之和

本质上：无序数组里找两个数，和为 `target`，返回下标。

```python
def twoSum(nums, target):
    idx = {}
    for i, x in enumerate(nums):
        if target - x in idx:
            return [idx[target - x], i]
        idx[x] = i
```

---

<a id="p-hash-group"></a>
## 哈希 · 分组

把「同类」压成一个可哈希的 key（排序后的串、计数元组），同一 key 丢进同一个桶。

```
g = defaultdict(list)
for x in items:
    g[feature(x)].append(x)
return g.values()
```

<a id="lc-49"></a>
### LC 49 字母异位词分组

本质上：互为异位词的串分到同一组。

```python
def groupAnagrams(strs):
    g = defaultdict(list)
    for s in strs:
        g[tuple(sorted(s))].append(s)
    return list(g.values())
```

---

<a id="p-hash-run"></a>
## 哈希 · 连续段

先全部放进 set。只从一段的起点（`x-1` 不在）开始往后数，每段只扫一遍，总 O(n)。

```
st = set(a)
for x in st:
    if x - 1 in st: continue          # 不是起点
    y = x
    while y + 1 in st: y += 1
    ans = max(ans, y - x + 1)
```

<a id="lc-128"></a>
### LC 128 最长连续序列

本质上：能排成连续整数的最长长度。

```python
def longestConsecutive(nums):
    st, ans = set(nums), 0
    for x in st:
        if x - 1 in st:
            continue
        y = x
        while y + 1 in st:
            y += 1
        ans = max(ans, y - x + 1)
    return ans
```

---

<a id="p-prefix"></a>
## 前缀和 · 哈希

`sum(l..r) = pre[r+1] - pre[l]`。要和为 k，就是当前前缀 `s` 之前出现过多少次 `s - k`。先查再把当前 `s` 记进去。

```
cnt = {0: 1}          # 空前缀
s = 0
for x in a:
    s += x
    ans += cnt[s - k]
    cnt[s] += 1
```

<a id="lc-560"></a>
### LC 560 和为 K 的子数组

本质上：有多少个连续子数组的和等于 `k`。

```python
def subarraySum(nums, k):
    cnt = Counter({0: 1})
    s = ans = 0
    for x in nums:
        s += x
        ans += cnt[s - k]
        cnt[s] += 1
    return ans
```

---

<a id="p-prefix-prod"></a>
## 前缀 · 前缀积

不能用除法时，答案 `[i] = 左边所有积 × 右边所有积`。先从左扫一遍，再从右扫一遍。

```
ans[i] 先放 i 左边的积
再从右往左乘上 i 右边的积
```

<a id="lc-238"></a>
### LC 238 除自身以外数组的乘积

本质上：每个位置等于其余元素的积，O(n) 且不用除法。

```python
def productExceptSelf(nums):
    n = len(nums)
    ans = [1] * n
    left = 1
    for i in range(n):
        ans[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):
        ans[i] *= right
        right *= nums[i]
    return ans
```

---

<a id="p-diff"></a>
## 前缀 · 差分

区间加：`diff[l] += d`，`diff[r+1] -= d`，最后前缀和还原。只改端点，O(1) 更新。

```
diff[l] += d
if r + 1 < n: diff[r + 1] -= d
# 还原: for i in 1..n-1: a[i] = a[i-1] + diff[i]
```

<a id="lc-1109"></a>
### LC 1109 航班预订统计

本质上：多次给 `[first, last]` 的座位都加 `seats`，返回每班总座位数。

```python
def corpFlightBookings(bookings, n):
    diff = [0] * n
    for first, last, seats in bookings:
        diff[first - 1] += seats
        if last < n:
            diff[last] -= seats
    for i in range(1, n):
        diff[i] += diff[i - 1]
    return diff
```

---

<a id="p-prefix-2d"></a>
## 前缀 · 二维

`pre[i+1][j+1] = 左上角 (0,0) 到 (i,j) 的和`。矩形和四角相减。

```
s = pre[r2+1][c2+1] - pre[r1][c2+1] - pre[r2+1][c1] + pre[r1][c1]
```

<a id="lc-304"></a>
### LC 304 二维区域和检索

本质上：多次查询子矩阵的和。

```python
class NumMatrix:
    def __init__(self, matrix):
        m, n = len(matrix), len(matrix[0])
        self.pre = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.pre[i + 1][j + 1] = (
                    matrix[i][j]
                    + self.pre[i][j + 1]
                    + self.pre[i + 1][j]
                    - self.pre[i][j]
                )
    def sumRegion(self, r1, c1, r2, c2):
        p = self.pre
        return p[r2 + 1][c2 + 1] - p[r1][c2 + 1] - p[r2 + 1][c1] + p[r1][c1]
```

---

<a id="p-bin-idx"></a>
## 二分 · 下标

在有序数组的下标上找第一个满足 `ok` 的位置。`lo < hi`，成立就把右边界收到 mid，否则丢掉左半。手写，不要 `bisect`。

```
lo, hi = 0, n                 # 答案落在 [lo, hi)
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid      # 第一个真
    else:       lo = mid + 1
return lo
```

<a id="lc-35"></a>
### LC 35 搜索插入位置（第一个 >=）

本质上：有序数组里 `target` 该插在哪（已存在就返回它所在下标）。

```python
def searchInsert(nums, target):
    lo, hi = 0, len(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

---

<a id="p-bin-ans"></a>
## 二分 · 对答案

答案本身有单调性：更大的 k 一定更可行。在值域 `[最小可能, 最大可能]` 上二分，`ok(mid)` 判定这个值行不行。

```
lo, hi = 最小答案, 最大答案
while lo < hi:
    mid = (lo + hi) // 2
    if ok(mid): hi = mid      # 还能更小
    else:       lo = mid + 1
return lo
```

<a id="lc-875"></a>
### LC 875 爱吃香蕉的珂珂

本质上：`h` 小时内吃完的最小速度。

```python
def minEatingSpeed(piles, h):
    def ok(k):
        return sum(-(-p // k) for p in piles) <= h
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if ok(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

---

<a id="p-bin-bound"></a>
## 二分 · 左右边界

同一个 `first_ge`：左边界是第一个 `>= target`，右边界是第一个 `>= target+1` 再减 1。找不到则特判。

```
L = first_ge(target)
R = first_ge(target + 1) - 1
if L == n or a[L] != target: 没有
else: [L, R]
```

<a id="lc-34"></a>
### LC 34 在排序数组中查找元素的第一个和最后一个位置

本质上：`target` 第一次和最后一次出现的下标，没有则 `[-1, -1]`。

```python
def searchRange(nums, target):
    def first_ge(x):
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if nums[mid] >= x:
                hi = mid
            else:
                lo = mid + 1
        return lo
    L = first_ge(target)
    if L == len(nums) or nums[L] != target:
        return [-1, -1]
    return [L, first_ge(target + 1) - 1]
```

---

<a id="p-bin-rot"></a>
## 二分 · 旋转 / 峰值

旋转数组：`mid` 落在有序的那一半里才能丢另一半。峰值：往更高的一侧走，一定能碰到峰。二维矩阵每行有序：先定行再定列，或一次当一维。

```
# 旋转：nums[lo] <= nums[mid] → 左半有序
if 左半有序:
    if 目标在左半: hi = mid
    else:           lo = mid + 1
else: 右半有序，对称处理

# 峰值：if a[mid] < a[mid+1]: lo = mid + 1
#       else: hi = mid
```

<a id="lc-33"></a>
### LC 33 搜索旋转排序数组

本质上：旋转过一次的有序数组里找 `target`，没有则 `-1`。

```python
def searchRotated(nums, target):
    lo, hi = 0, len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return mid
        if nums[lo] <= nums[mid]:
            if nums[lo] <= target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if nums[mid] < target <= nums[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return -1
```

<a id="lc-153"></a>
### LC 153 寻找旋转排序数组中的最小值

本质上：旋转数组里的最小元素。

```python
def findMin(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1
        else:
            hi = mid
    return nums[lo]
```

<a id="lc-162"></a>
### LC 162 寻找峰值

本质上：任一峰值下标。邻居更高就往那边走。

```python
def findPeakElement(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1
        else:
            hi = mid
    return lo
```

<a id="lc-74"></a>
### LC 74 搜索二维矩阵

本质上：每行从左到右、下一行比上一行末尾更大，找 `target`。

```python
def searchMatrix(matrix, target):
    m, n = len(matrix), len(matrix[0])
    lo, hi = 0, m * n
    while lo < hi:
        mid = (lo + hi) // 2
        val = matrix[mid // n][mid % n]
        if val >= target:
            hi = mid
        else:
            lo = mid + 1
    return lo < m * n and matrix[lo // n][lo % n] == target
```

---

<a id="p-stack"></a>
## 栈 · 匹配

后进的必须先关上。左括号入栈，右括号必须和栈顶配对。走完栈空才合法。

```
st = []
for ch in s:
    if ch 是开: st.append(ch)
    else:
        if 栈空 or 栈顶对不上: return False
        st.pop()
return 栈空
```

<a id="lc-20"></a>
### LC 20 有效的括号

本质上：括号是否全部正确配对。

```python
def isValid(s):
    pair = {')': '(', ']': '[', '}': '{'}
    st = []
    for ch in s:
        if ch in pair:
            if not st or st[-1] != pair[ch]:
                return False
            st.pop()
        else:
            st.append(ch)
    return not st
```

---

<a id="p-mono-stack"></a>
## 单调栈 · 下一个更大

栈里下标对应的值单调（通常递增）。当前值比栈顶大，栈顶的「下一个更大」就是当前。出栈那一刻答案就确定。

```
st = []                       # 下标，值递增
for i, x in enumerate(a):
    while st and a[st[-1]] < x:
        j = st.pop()
        ans[j] = i - j        # j 的下一个更大是 i
    st.append(i)
```

<a id="lc-739"></a>
### LC 739 每日温度

本质上：每个位置还要等几天才能遇到更高温度。

```python
def dailyTemperatures(temps):
    ans, st = [0] * len(temps), []
    for i, t in enumerate(temps):
        while st and temps[st[-1]] < t:
            j = st.pop()
            ans[j] = i - j
        st.append(i)
    return ans
```

---

<a id="p-stack-hist"></a>
## 单调栈 · 直方图

每个柱子能伸展到「下一个更小」和「上一个更小」之间。栈递增，出栈时右边界就是当前，左边界是新栈顶。

```
st = [-1]                       # 哨兵，高度 0
for i in 0 .. n:                # n 当右哨兵
    h = a[i] if i < n else 0
    while st[-1] != -1 and a[st[-1]] > h:
        height = a[st.pop()]
        width = i - st[-1] - 1
        ans = max(ans, height * width)
    st.append(i)
```

<a id="lc-84"></a>
### LC 84 柱状图中最大的矩形

本质上：直方图能围出的最大矩形面积。

```python
def largestRectangleArea(heights):
    heights.append(0)
    st, ans = [-1], 0
    for i, h in enumerate(heights):
        while st[-1] != -1 and heights[st[-1]] > h:
            height = heights[st.pop()]
            ans = max(ans, height * (i - st[-1] - 1))
        st.append(i)
    heights.pop()
    return ans
```

---

<a id="p-stack-eval"></a>
## 栈 · 计算 / 解码

数字和运算符用栈处理：遇到高优先级就先算栈顶；括号就递归或再开一层。解码：数字入次数栈，字母入串栈，碰到 `]` 弹出重复拼接。

```
# 逆波兰：数字入栈，运算符弹出两个算完再入
# 解码：num 累加；[ 把 num / 当前串压栈；] 弹出重复
```

<a id="lc-150"></a>
### LC 150 逆波兰表达式求值

本质上：后缀表达式的值。

```python
def evalRPN(tokens):
    st = []
    for t in tokens:
        if t in "+-*/":
            b, a = st.pop(), st.pop()
            if t == "+": st.append(a + b)
            elif t == "-": st.append(a - b)
            elif t == "*": st.append(a * b)
            else: st.append(int(a / b))      # 向 0 取整
        else:
            st.append(int(t))
    return st[-1]
```

<a id="lc-224"></a>
### LC 224 基本计算器

本质上：含 `+` `-` 和括号的表达式的值。符号栈：遇到 `(` 把当前符号压进去，`)` 弹出。

```python
def calculate(s):
    st, sign, num, ans = [], 1, 0, 0
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch in "+-":
            ans += sign * num
            num = 0
            sign = 1 if ch == "+" else -1
        elif ch == "(":
            st.append(ans)
            st.append(sign)
            ans, sign = 0, 1
        elif ch == ")":
            ans += sign * num
            num = 0
            ans *= st.pop()
            ans += st.pop()
    return ans + sign * num
```

<a id="lc-394"></a>
### LC 394 字符串解码

本质上：把 `k[encoded]` 展开。

```python
def decodeString(s):
    num_st, str_st = [], []
    num, cur = 0, []
    for ch in s:
        if ch.isdigit():
            num = num * 10 + int(ch)
        elif ch == "[":
            num_st.append(num)
            str_st.append(cur)
            num, cur = 0, []
        elif ch == "]":
            cur = str_st.pop() + cur * num_st.pop()
        else:
            cur.append(ch)
    return "".join(cur)
```

---

<a id="p-heap-k"></a>
## 堆 · Top K

Python 只有最小堆。求第 k 大：堆里只留 k 个，多了弹出最小，堆顶就是第 k 大。要大的先出来对数字塞 `-x`；字符串 / 对象当 payload 不要取负。

```
h = []
for x in a:
    heappush(h, x)
    if len(h) > k: heappop(h)
return h[0]
```

<a id="lc-215"></a>
### LC 215 数组中的第 K 个最大元素

本质上：第 k 大的那个数。

```python
def findKthLargest(nums, k):
    h = []
    for x in nums:
        heappush(h, x)
        if len(h) > k:
            heappop(h)
    return h[0]
```

<a id="lc-347"></a>
### LC 347 前 K 个高频元素

本质上：出现次数最高的 k 个数。堆按次数比，只留 k 个。

```python
def topKFrequent(nums, k):
    cnt = Counter(nums)
    h = []
    for x, c in cnt.items():
        heappush(h, (c, x))
        if len(h) > k:
            heappop(h)
    return [x for _, x in h]
```

---

<a id="p-heap-merge"></a>
## 堆 · 多路合并

k 路已有序。每路取一个头放进堆，弹出全局最小，再把那一路的下一个推进去。比较元组时带上路号，避免节点比不了。

```
h = [(头.val, i, 头) for 每路非空]
while h:
    val, i, node = heappop(h)
    接到答案后面
    if node.next: heappush(h, (node.next.val, i, node.next))
```

<a id="lc-23"></a>
### LC 23 合并 K 个升序链表

本质上：k 条有序链合成一条有序链。

```python
def mergeKLists(lists):
    h = []
    for i, node in enumerate(lists):
        if node:
            heappush(h, (node.val, i, node))
    dummy = cur = ListNode()
    while h:
        val, i, node = heappop(h)
        cur.next = node
        cur = cur.next
        if node.next:
            heappush(h, (node.next.val, i, node.next))
    return dummy.next
```

---

<a id="p-heap-dual"></a>
## 堆 · 对顶堆

小的一半用最大堆（塞 `-x`），大的一半用最小堆。始终 `|lo| == |hi|` 或 `|lo| == |hi|+1`。中位数是最大堆顶，或两顶平均。

```
lo = []          # 最大堆，存 -x
hi = []          # 最小堆
加 x: 先丢进 lo，再把 lo 顶挪到 hi；若 hi 更长，再挪回 lo
```

<a id="lc-295"></a>
### LC 295 数据流的中位数

本质上：动态加数，随时给当前中位数。

```python
class MedianFinder:
    def __init__(self):
        self.lo, self.hi = [], []          # 最大堆 / 最小堆
    def addNum(self, x):
        heappush(self.hi, -heappushpop(self.lo, -x))
        if len(self.hi) > len(self.lo):
            heappush(self.lo, -heappop(self.hi))
    def findMedian(self):
        if len(self.lo) > len(self.hi):
            return -self.lo[0]
        return (-self.lo[0] + self.hi[0]) / 2
```

---

<a id="p-dijkstra"></a>
## 堆 · 最短路（Dijkstra）

带正权的单源最短路。堆里放 `(dist, 点)`，弹出过时距离就跳过。松弛成功再入堆。

```
dist[src] = 0; h = [(0, src)]
while h:
    d, u = heappop(h)
    if d > dist[u]: continue
    for v, w in g[u]:
        if d + w < dist[v]: dist[v] = d+w; heappush(h, (d+w, v))
```

<a id="lc-743"></a>
### LC 743 网络延迟时间

本质上：从 `k` 出发，信号到达所有节点的最短时间，到不齐则 `-1`。

```python
def networkDelayTime(times, n, k):
    g = defaultdict(list)
    for u, v, w in times:
        g[u].append((v, w))
    dist = {k: 0}
    h = [(0, k)]
    while h:
        d, u = heappop(h)
        if d > dist.get(u, math.inf):
            continue
        for v, w in g[u]:
            nd = d + w
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                heappush(h, (nd, v))
    return max(dist.values()) if len(dist) == n else -1
```

---

<a id="p-tree-rec"></a>
## 二叉树 · 递归

空是边界。当前答案 = 按题意组合左右子树的答案（深度、路径和、是否平衡……）。

```
def f(node):
    if not node: return 边界
    L, R = f(node.left), f(node.right)
    return 用 L、R、node.val 拼
```

<a id="lc-104"></a>
### LC 104 二叉树的最大深度

本质上：根到最远叶子有几层。

```python
def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))
```

<a id="lc-226"></a>
### LC 226 翻转二叉树

本质上：左右子树整棵对调。

```python
def invertTree(root):
    if not root:
        return None
    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root
```

<a id="lc-101"></a>
### LC 101 对称二叉树

本质上：左右是否镜像。

```python
def isSymmetric(root):
    def same(a, b):
        if not a or not b:
            return a is b
        return a.val == b.val and same(a.left, b.right) and same(a.right, b.left)
    return not root or same(root.left, root.right)
```

---

<a id="p-tree-dnc"></a>
## 二叉树 · 分治

左右都找到目标 → 当前节点就是分界（LCA）。只在一边找到 → 答案在那一边。空或撞上目标就返回自己。

```
def f(node):
    if not node or node 是目标: return node
    L, R = f(node.left), f(node.right)
    if L and R: return node
    return L or R
```

<a id="lc-236"></a>
### LC 236 二叉树的最近公共祖先

本质上：`p` 和 `q` 最深的那个公共祖先。

```python
def lowestCommonAncestor(root, p, q):
    if not root or root is p or root is q:
        return root
    L, R = lowestCommonAncestor(root.left, p, q), lowestCommonAncestor(root.right, p, q)
    if L and R:
        return root
    return L or R
```

---

<a id="p-tree-bfs"></a>
## 二叉树 · 层序

队列。每次用 `for _ in range(len(q))` 把当前层全部弹出，同时把下一层孩子入队。一层一层处理。

```
q = deque([root])
while q:
    layer = []
    for _ in range(len(q)):
        node = q.popleft()
        layer.append(node.val)
        左右孩子非空则入队
    ans.append(layer)
```

<a id="lc-102"></a>
### LC 102 二叉树的层序遍历

本质上：按层从左到右列出节点值。

```python
def levelOrder(root):
    if not root:
        return []
    q, ans = deque([root]), []
    while q:
        layer = []
        for _ in range(len(q)):
            node = q.popleft()
            layer.append(node.val)
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        ans.append(layer)
    return ans
```

<a id="lc-199"></a>
### LC 199 二叉树的右视图

本质上：每一层最右边那个值。层序时取本层最后一个。

```python
def rightSideView(root):
    if not root:
        return []
    q, ans = deque([root]), []
    while q:
        ans.append(q[-1].val)
        for _ in range(len(q)):
            node = q.popleft()
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
    return ans
```

---

<a id="p-tree-path"></a>
## 二叉树 · 路径

后序：先拿到左右贡献，再更新全局（直径、最大路径和）。贡献只能是「单边向下」的非负值。路径是否存在则一边走一边减。

```
def dfs(node):
    if not node: return 0
    L = max(0, dfs(node.left))     # 负的不要
    R = max(0, dfs(node.right))
    ans = max(ans, L + R + node.val)   # 经过自己的路径
    return node.val + max(L, R)        # 只能带一边上去
```

<a id="lc-543"></a>
### LC 543 二叉树的直径

本质上：任意两节点间最长边数。

```python
def diameterOfBinaryTree(root):
    ans = 0
    def depth(node):
        nonlocal ans
        if not node:
            return 0
        L, R = depth(node.left), depth(node.right)
        ans = max(ans, L + R)
        return 1 + max(L, R)
    depth(root)
    return ans
```

<a id="lc-124"></a>
### LC 124 二叉树中的最大路径和

本质上：任意节点到任意节点的路径和最大（节点值可负）。

```python
def maxPathSum(root):
    ans = -math.inf
    def gain(node):
        nonlocal ans
        if not node:
            return 0
        L, R = max(0, gain(node.left)), max(0, gain(node.right))
        ans = max(ans, L + R + node.val)
        return node.val + max(L, R)
    gain(root)
    return ans
```

<a id="lc-112"></a>
### LC 112 路径总和

本质上：根到叶子是否存在一条路径和为 `target`。

```python
def hasPathSum(root, target):
    if not root:
        return False
    if not root.left and not root.right:
        return root.val == target
    rest = target - root.val
    return hasPathSum(root.left, rest) or hasPathSum(root.right, rest)
```

---

<a id="p-tree-build"></a>
## 二叉树 · 构造

前序第一个是根；中序里根左边是左子树。用哈希 O(1) 找根在中序的位置，再按长度切开。

```
pre[0] 是根
i = 中序里根的下标
左子树长度 = i - in_lo
递归建左 [pre_lo+1, ...) 右 [pre_lo+1+左长, ...)
```

<a id="lc-105"></a>
### LC 105 从前序与中序遍历序列构造二叉树

本质上：由 `preorder` + `inorder` 还原树（值不重复）。

```python
def buildTree(preorder, inorder):
    idx = {v: i for i, v in enumerate(inorder)}
    def build(plo, phi, ilo, ihi):
        if plo > phi:
            return None
        root = TreeNode(preorder[plo])
        i = idx[root.val]
        left_len = i - ilo
        root.left = build(plo + 1, plo + left_len, ilo, i - 1)
        root.right = build(plo + left_len + 1, phi, i + 1, ihi)
        return root
    n = len(preorder)
    return build(0, n - 1, 0, n - 1)
```

---

<a id="p-tree-inorder"></a>
## 二叉树 · 迭代中序

一路向左压栈，弹出来访问，再转向右孩子。BST 中序就是升序，验证 / 第 K 小都靠它。

```
st, cur = [], root
while st or cur:
    while cur:
        st.append(cur); cur = cur.left
    cur = st.pop()
    访问 cur
    cur = cur.right
```

<a id="lc-94"></a>
### LC 94 二叉树的中序遍历

本质上：左-根-右的节点值序列。

```python
def inorderTraversal(root):
    st, cur, ans = [], root, []
    while st or cur:
        while cur:
            st.append(cur)
            cur = cur.left
        cur = st.pop()
        ans.append(cur.val)
        cur = cur.right
    return ans
```

---

<a id="p-tree-ser"></a>
## 二叉树 · 序列化

前序，空节点写成 `#`。序列化一路拼；反序列化用迭代器，碰到 `#` 返回空。层序也可以，面试前序更短。

```
ser:  if not node: return '#'
      return str(val) + ',' + ser(left) + ',' + ser(right)
des:  x = next(it)
      if x == '#': return None
      node = TreeNode(int(x))
      node.left, node.right = des(), des()
```

<a id="lc-297"></a>
### LC 297 二叉树的序列化与反序列化

本质上：树 ↔ 字符串，能还原。

```python
class Codec:
    def serialize(self, root):
        def ser(node):
            if not node:
                return "#"
            return f"{node.val},{ser(node.left)},{ser(node.right)}"
        return ser(root)
    def deserialize(self, data):
        it = iter(data.split(","))
        def des():
            x = next(it)
            if x == "#":
                return None
            node = TreeNode(int(x))
            node.left, node.right = des(), des()
            return node
        return des()
```

---

<a id="p-bst-ok"></a>
## BST · 验证 / 插入

中序走出来必须严格递增。验证不能只比左右孩子：要带上下界，左子树全 `< 根`，右子树全 `>` 根。查找 / 插入只走一边。

```
# 验证
ok(node, lo, hi):
    if not node: return True
    if not lo < node.val < hi: return False
    return ok(left, lo, val) and ok(right, val, hi)

# 插入
if not root: return TreeNode(val)
if val < root.val: root.left = insert(root.left, val)
else:              root.right = insert(root.right, val)
```

<a id="lc-98"></a>
### LC 98 验证二叉搜索树

本质上：是不是 BST。

```python
def isValidBST(root):
    def ok(node, lo, hi):
        if not node:
            return True
        if not lo < node.val < hi:
            return False
        return ok(node.left, lo, node.val) and ok(node.right, node.val, hi)
    return ok(root, -math.inf, math.inf)
```

<a id="lc-701"></a>
### LC 701 二叉搜索树中的插入操作

本质上：插入 `val`，保持 BST（原树无此值）。

```python
def insertIntoBST(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insertIntoBST(root.left, val)
    else:
        root.right = insertIntoBST(root.right, val)
    return root
```

<a id="lc-450"></a>
### LC 450 删除二叉搜索树中的节点

本质上：删掉值为 `key` 的节点，保持 BST。没有右孩子用左顶上；有右孩子用后继（右子树最左）顶上。

```python
def deleteNode(root, key):
    if not root:
        return None
    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.right:
            return root.left
        if not root.left:
            return root.right
        suc = root.right
        while suc.left:
            suc = suc.left
        root.val = suc.val
        root.right = deleteNode(root.right, suc.val)
    return root
```

---

<a id="p-bst-k"></a>
## BST · 第 K 小

中序第 k 个就是第 k 小。迭代：一路向左，弹出计数，数到 k 停。不要先整棵中序再取。

```
while True:
    while root: st.append(root); root = root.left
    root = st.pop(); k -= 1
    if k == 0: return root.val
    root = root.right
```

<a id="lc-230"></a>
### LC 230 二叉搜索树中第 K 小的元素

本质上：BST 里第 k 小的值（1-based）。

```python
def kthSmallest(root, k):
    st = []
    while True:
        while root:
            st.append(root)
            root = root.left
        root = st.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right
```

---

<a id="p-bst-lca"></a>
## BST · LCA

`p`、`q` 都比当前小 → 答案在左；都大 → 在右；否则当前就是分叉点。不必像普通树那样两边都搜。

```
while root:
    if p.val < root.val and q.val < root.val: root = root.left
    elif p.val > root.val and q.val > root.val: root = root.right
    else: return root
```

<a id="lc-235"></a>
### LC 235 二叉搜索树的最近公共祖先

本质上：BST 里 `p` 和 `q` 的 LCA。

```python
def lowestCommonAncestorBST(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root
```

---

<a id="p-bst-build"></a>
## BST · 建树

有序数组的中点当根，左右递归，自然平衡。不要从一端一个个 insert（会退化成链）。

```
build(lo, hi):
    if lo > hi: return None
    mid = (lo + hi) // 2
    node = TreeNode(a[mid])
    node.left, node.right = build(lo, mid-1), build(mid+1, hi)
```

<a id="lc-108"></a>
### LC 108 将有序数组转换为二叉搜索树

本质上：升序数组建成高度平衡的 BST。

```python
def sortedArrayToBST(nums):
    def build(lo, hi):
        if lo > hi:
            return None
        mid = (lo + hi) // 2
        node = TreeNode(nums[mid])
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node
    return build(0, len(nums) - 1)
```

---

<a id="p-bst-iter"></a>
## BST · 迭代器

把「迭代中序」拆成对象：构造时一路向左压栈；`next` 弹出栈顶，若有右孩子再把右孩子一路向左压进去。均摊 O(1)，空间 O(h)。

```
__init__:  while root: st.append(root); root = root.left
next:      node = st.pop()
           cur = node.right
           while cur: st.append(cur); cur = cur.left
           return node.val
```

<a id="lc-173"></a>
### LC 173 二叉搜索树迭代器

本质上：中序依次给出下一个最小。

```python
class BSTIterator:
    def __init__(self, root):
        self.st = []
        while root:
            self.st.append(root)
            root = root.left
    def next(self):
        node = self.st.pop()
        cur = node.right
        while cur:
            self.st.append(cur)
            cur = cur.left
        return node.val
    def hasNext(self):
        return bool(self.st)
```

---

<a id="p-bst-suc"></a>
## BST · 后继

比 `p` 大的最小节点。`p` 有右孩子 → 右子树最左。否则从根往下走：当前比 `p` 大就记下来并去左，否则去右。

```
suc = None
while root:
    if p.val < root.val: suc, root = root, root.left
    else: root = root.right
```

<a id="lc-285"></a>
### LC 285 二叉搜索树中的中序后继

本质上：中序里 `p` 的下一个节点，没有则 `None`。

```python
def inorderSuccessor(root, p):
    suc = None
    while root:
        if p.val < root.val:
            suc, root = root, root.left
        else:
            root = root.right
    return suc
```

---

<a id="p-grid-dfs"></a>
## 网格 · DFS

连通块：踩到就改掉（或 `seen`），再向四邻递归。越界 / 不是目标格直接 return。数岛屿 = 每次踩到新的 `'1'` 就 +1 并 DFS 灭掉整块。

```
DIRS = [(0,1),(1,0),(0,-1),(-1,0)]
def dfs(r, c):
    if 越界 or grid[r][c] 不是目标: return
    grid[r][c] = 已访问
    for dr, dc in DIRS: dfs(r+dr, c+dc)

for 每个格子:
    if 是新连通块: ans += 1; dfs(i, j)
```

<a id="lc-200"></a>
### LC 200 岛屿数量

本质上：四连通的陆地块有几块。

```python
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def numIslands(grid):
    m, n = len(grid), len(grid[0])
    def dfs(r, c):
        if not (0 <= r < m and 0 <= c < n) or grid[r][c] != '1':
            return
        grid[r][c] = '0'
        for dr, dc in DIRS:
            dfs(r + dr, c + dc)
    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                ans += 1
                dfs(i, j)
    return ans
```

---

<a id="p-grid-bfs"></a>
## 网格 · 多源 BFS

所有起点一起入队，入队立刻标记。`for _ in range(len(q))` 算一层（一分钟）。无权最短路同一套。

```
q = deque(所有腐烂 / 起点)
seen 标记
minutes = 0
while q:
    for _ in range(len(q)):
        r, c = q.popleft()
        四邻若新鲜: 标记、入队
    if q 还非空: minutes += 1
```

<a id="lc-994"></a>
### LC 994 腐烂的橘子

本质上：全部腐烂要几分钟，不可能则 `-1`。

```python
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def orangesRotting(grid):
    m, n = len(grid), len(grid[0])
    q, fresh = deque(), 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1
    minutes = 0
    while q and fresh:
        for _ in range(len(q)):
            r, c = q.popleft()
            for dr, dc in DIRS:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc))
        minutes += 1
    return minutes if fresh == 0 else -1
```

---

<a id="p-graph-clone"></a>
## 图 · 克隆

哈希 `旧→新`。BFS/DFS 走到没见过的邻居就先建新节点再入队，再接线。和随机链表复制同一套。

```
mp[node] = 新节点(node.val)
for nei in node.neighbors:
    if nei not in mp: 先建再入队
    mp[node].neighbors.append(mp[nei])
```

<a id="lc-133"></a>
### LC 133 克隆图

本质上：复制无向连通图。

```python
def cloneGraph(node):
    if not node:
        return None
    mp = {node: Node(node.val)}
    q = deque([node])
    while q:
        cur = q.popleft()
        for nei in cur.neighbors:
            if nei not in mp:
                mp[nei] = Node(nei.val)
                q.append(nei)
            mp[cur].neighbors.append(mp[nei])
    return mp[node]
```

---

<a id="p-bipartite"></a>
## 图 · 二分图

相邻必须异色。每个连通块 BFS 染色，撞上同色就是否。也可 DFS。

```
color[start] = 0
for v in g[u]:
    if v 未染色: color[v] = color[u] ^ 1; 入队
    elif color[v] == color[u]: return False
```

<a id="lc-785"></a>
### LC 785 判断二分图

本质上：无向图能不能二分染色。

```python
def isBipartite(graph):
    color = {}
    for start in range(len(graph)):
        if start in color:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if v not in color:
                    color[v] = color[u] ^ 1
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
```

---

<a id="p-word-bfs"></a>
## 图 · 单词变换（隐式图 BFS）

节点是单词，边是只差一个字母。从 `beginWord` BFS，第一次到 `endWord` 的层数就是最短。用 set 删掉访问过的，避免回头。

```
q = deque([begin]); words 当 set
while q:
    for 本层:
        改每一位字母，在 words 里就入队并删掉
        碰到 end: return 步数
```

<a id="lc-127"></a>
### LC 127 单词接龙

本质上：`beginWord` 变到 `endWord` 的最短步数（每次改一个字母，必须在词表里），到不了则 0。

```python
from string import ascii_lowercase

def ladderLength(beginWord, endWord, wordList):
    words = set(wordList)
    if endWord not in words:
        return 0
    words.discard(beginWord)
    q, steps = deque([beginWord]), 1
    while q:
        for _ in range(len(q)):
            w = q.popleft()
            if w == endWord:
                return steps
            chars = list(w)
            for i in range(len(chars)):
                old = chars[i]
                for ch in ascii_lowercase:
                    chars[i] = ch
                    nxt = "".join(chars)
                    if nxt in words:
                        words.remove(nxt)
                        q.append(nxt)
                chars[i] = old
        steps += 1
    return 0
```

---

<a id="p-bt-perm"></a>
## 回溯 · 排列

每位都可以用剩下的任意元素。`used` 标记占位。选择 → 递归 → 撤销。`path[:]` 必须拷贝。

```
used = [False] * n
def dfs():
    if len(path) == n:
        ans.append(path[:]); return
    for i in 0 .. n-1:
        if used[i]: continue
        used[i] = True; path.append(a[i])
        dfs()
        path.pop(); used[i] = False
```

<a id="lc-46"></a>
### LC 46 全排列

本质上：所有不重复的排列。

```python
def permute(nums):
    ans, path, used = [], [], [False] * len(nums)
    def dfs():
        if len(path) == len(nums):
            ans.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i]:
                continue
            used[i] = True
            path.append(x)
            dfs()
            path.pop()
            used[i] = False
    dfs()
    return ans
```

<a id="lc-47"></a>
### LC 47 全排列 II（有重复）

本质上：含重复数字的不重复排列。先排序，同一层相同值只走第一个未用的。

```python
def permuteUnique(nums):
    nums.sort()
    ans, path, used = [], [], [False] * len(nums)
    def dfs():
        if len(path) == len(nums):
            ans.append(path[:])
            return
        for i, x in enumerate(nums):
            if used[i] or (i and x == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True
            path.append(x)
            dfs()
            path.pop()
            used[i] = False
    dfs()
    return ans
```

---

<a id="p-bt-sub"></a>
## 回溯 · 子集

从 `start` 往后选：每个元素选或不选。不回头，所以不用 `used`。空集也是合法子集，一开始就可以收 `path`。

```
def dfs(start):
    ans.append(path[:])
    for i in start .. n-1:
        path.append(a[i])
        dfs(i + 1)
        path.pop()
```

<a id="lc-78"></a>
### LC 78 子集

本质上：所有子集（含空集）。

```python
def subsets(nums):
    ans, path = [], []
    def dfs(start):
        ans.append(path[:])
        for i in range(start, len(nums)):
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
    dfs(0)
    return ans
```

---

<a id="p-bt-comb"></a>
## 回溯 · 组合

和子集一样从 `i` 往后选，但有目标和。可重复用则递归仍传 `i`；不可重复传 `i+1`。

```
def dfs(i, remain):
    if remain == 0: ans.append(path[:]); return
    if remain < 0 or i == n: return
    path.append(a[i])
    dfs(i, remain - a[i])     # 用；可重复传 i，不可重复传 i+1
    path.pop()
    dfs(i + 1, remain)        # 不用 a[i]
```

<a id="lc-39"></a>
### LC 39 组合总和（可重复）

本质上：能凑出 `target` 的所有组合，数字可重复用。

```python
def combinationSum(candidates, target):
    ans, path = [], []
    n = len(candidates)
    def dfs(i, remain):
        if remain == 0:
            ans.append(path[:])
            return
        if remain < 0 or i == n:
            return
        path.append(candidates[i])
        dfs(i, remain - candidates[i])
        path.pop()
        dfs(i + 1, remain)
    dfs(0, target)
    return ans
```

<a id="lc-40"></a>
### LC 40 组合总和 II（不可重复、有重复值）

本质上：每个数最多用一次，结果去重。排序后同一层跳过相同值；递归传 `i+1`。

```python
def combinationSum2(candidates, target):
    candidates.sort()
    ans, path = [], []
    n = len(candidates)
    def dfs(start, remain):
        if remain == 0:
            ans.append(path[:])
            return
        for i in range(start, n):
            if candidates[i] > remain:
                break
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            dfs(i + 1, remain - candidates[i])
            path.pop()
    dfs(0, target)
    return ans
```

---

<a id="p-bt-paren"></a>
## 回溯 · 括号 / 电话

括号：只要 `open < n` 就能加 `(`，只要 `close < open` 就能加 `)`。电话：每位对应一组字母，逐位展开。

```
if open < n:  加 '(' ；dfs(open+1, close)；撤销
if close < open: 加 ')' ；dfs(open, close+1)；撤销
```

<a id="lc-22"></a>
### LC 22 括号生成

本质上：n 对括号的所有合法串。

```python
def generateParenthesis(n):
    ans, path = [], []
    def dfs(open_n, close_n):
        if len(path) == 2 * n:
            ans.append("".join(path))
            return
        if open_n < n:
            path.append("(")
            dfs(open_n + 1, close_n)
            path.pop()
        if close_n < open_n:
            path.append(")")
            dfs(open_n, close_n + 1)
            path.pop()
    dfs(0, 0)
    return ans
```

<a id="lc-17"></a>
### LC 17 电话号码的字母组合

本质上：数字串对应的所有字母串。

```python
KEYS = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

def letterCombinations(digits):
    if not digits:
        return []
    ans, path = [], []
    def dfs(i):
        if i == len(digits):
            ans.append("".join(path))
            return
        for ch in KEYS[digits[i]]:
            path.append(ch)
            dfs(i + 1)
            path.pop()
    dfs(0)
    return ans
```

---

<a id="p-bt-grid"></a>
## 回溯 · 网格（单词搜索）

从每个格子出发，沿四邻走，当前字符对上就继续，走过的先改掉再还原。找到就提前停。

```
def dfs(r, c, i):
    if i == len(word): return True
    if 越界 or board[r][c] != word[i]: return False
    board[r][c] = '#'
    ok = 任一方向 dfs(..., i+1)
    board[r][c] = word[i]
    return ok
```

<a id="lc-79"></a>
### LC 79 单词搜索

本质上：网格里能否走出 `word`（不能重复走格）。

```python
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def exist(board, word):
    m, n = len(board), len(board[0])
    def dfs(r, c, i):
        if i == len(word):
            return True
        if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[i]:
            return False
        board[r][c] = "#"
        ok = any(dfs(r + dr, c + dc, i + 1) for dr, dc in DIRS)
        board[r][c] = word[i]
        return ok
    return any(dfs(i, j, 0) for i in range(m) for j in range(n))
```

---

<a id="p-bt-pal"></a>
## 回溯 · 分割回文

从 `start` 往后切：只有 `s[start:i]` 是回文才切一刀，继续。切到末尾收一份。

```
def dfs(start):
    if start == n: ans.append(path[:]); return
    for i in start+1 .. n:
        if s[start:i] 是回文:
            path.append(s[start:i]); dfs(i); path.pop()
```

<a id="lc-131"></a>
### LC 131 分割回文串

本质上：把串切成若干段，每段都是回文，列出所有切法。

```python
def partitionPalindrome(s):
    n, ans, path = len(s), [], []
    def pal(lo, hi):
        while lo < hi:
            if s[lo] != s[hi]:
                return False
            lo, hi = lo + 1, hi - 1
        return True
    def dfs(start):
        if start == n:
            ans.append(path[:])
            return
        for i in range(start, n):
            if pal(start, i):
                path.append(s[start:i + 1])
                dfs(i + 1)
                path.pop()
    dfs(0)
    return ans
```

---

<a id="p-interval"></a>
## 区间 · 合并

按左端排序。能和答案末尾重叠就并（右端取 max），否则新开一段。

```
intervals.sort()
ans = [intervals[0]]
for lo, hi in intervals[1:]:
    if lo <= ans[-1][1]:
        ans[-1][1] = max(ans[-1][1], hi)
    else:
        ans.append([lo, hi])
```

<a id="lc-56"></a>
### LC 56 合并区间

本质上：重叠区间并成互不重叠的几段。

```python
def merge(intervals):
    intervals.sort()
    ans = [intervals[0]]
    for lo, hi in intervals[1:]:
        if lo <= ans[-1][1]:
            ans[-1][1] = max(ans[-1][1], hi)
        else:
            ans.append([lo, hi])
    return ans
```

<a id="lc-57"></a>
### LC 57 插入区间

本质上：把新区间插进已有序且不重叠的列表，必要时合并。

```python
def insert(intervals, newInterval):
    ans = []
    lo, hi = newInterval
    inserted = False
    for a, b in intervals:
        if b < lo:
            ans.append([a, b])
        elif a > hi:
            if not inserted:
                ans.append([lo, hi])
                inserted = True
            ans.append([a, b])
        else:
            lo, hi = min(lo, a), max(hi, b)
    if not inserted:
        ans.append([lo, hi])
    return ans
```

---

<a id="p-sweep"></a>
## 区间 · 扫描线

会议室：按时间点扫，开始 +1、结束 -1，峰值就是同时进行的场数。不重叠：按右端排序，贪心保留结束早的。

```
# 会议室 II：把 (start, +1) (end, -1) 排序；end 优先于同点 start
# 删重叠：按 end 排序，能不相交就留
```

<a id="lc-253"></a>
### LC 253 会议室 II

本质上：最少要几间会议室。

```python
def minMeetingRooms(intervals):
    events = []
    for lo, hi in intervals:
        events.append((lo, 1))
        events.append((hi, -1))
    events.sort()                      # 同点先结束再开始
    cur = ans = 0
    for _, d in events:
        cur += d
        ans = max(ans, cur)
    return ans
```

<a id="lc-435"></a>
### LC 435 无重叠区间

本质上：最少删几个，剩下互不重叠。等价于最多留几段：按右端排序，能接就留。

```python
def eraseOverlapIntervals(intervals):
    intervals.sort(key=lambda x: x[1])
    keep, end = 0, -math.inf
    for lo, hi in intervals:
        if lo >= end:
            keep += 1
            end = hi
    return len(intervals) - keep
```

---

<a id="p-topo"></a>
## 拓扑 · Kahn

建边并统计入度。入度为 0 的进队，弹出时给邻居减入度，减到 0 再入队。能弹出 n 个则无环。

```
建图 g，indeg
q = deque(入度为 0 的点)
seen = 0
while q:
    u = q.popleft(); seen += 1
    for v in g[u]:
        indeg[v] -= 1
        if indeg[v] == 0: q.append(v)
return seen == n
```

<a id="lc-207"></a>
### LC 207 课程表

本质上：这些课在先修约束下能不能修完（有没有环）。

```python
def canFinish(n, prereq):
    g, indeg = [[] for _ in range(n)], [0] * n
    for a, b in prereq:                      # b → a
        g[b].append(a)
        indeg[a] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    seen = 0
    while q:
        u = q.popleft()
        seen += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return seen == n
```

<a id="lc-210"></a>
### LC 210 课程表 II

本质上：修课顺序；有环则返回空。Kahn 弹出时记下顺序。

```python
def findOrder(n, prereq):
    g, indeg = [[] for _ in range(n)], [0] * n
    for a, b in prereq:
        g[b].append(a)
        indeg[a] += 1
    q = deque([i for i in range(n) if indeg[i] == 0])
    ans = []
    while q:
        u = q.popleft()
        ans.append(u)
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0:
                q.append(v)
    return ans if len(ans) == n else []
```

---

<a id="p-uf"></a>
## 并查集 · 合并

`find` 带路径压缩：同一根 = 已连通。下标用 list，email 这种用 dict。union 把一边的根挂到另一边。

```
p[x] = x
find(x):
    if p[x] != x: p[x] = find(p[x])
    return p[x]
union(a, b): p[find(a)] = find(b)
```

<a id="lc-721"></a>
### LC 721 账户合并

本质上：共享 email 的账户合成一份，email 排序。同一账户里的 email 全 union，再按根收拢。

```python
def accountsMerge(accounts):
    p = {}
    def find(x):
        p.setdefault(x, x)
        if p[x] != x:
            p[x] = find(p[x])
        return p[x]
    def union(a, b):
        p[find(a)] = find(b)

    email_name = {}
    for acc in accounts:
        name = acc[0]
        for email in acc[1:]:
            email_name[email] = name
            union(acc[1], email)

    g = defaultdict(list)
    for email in email_name:
        g[find(email)].append(email)
    return [[email_name[root]] + sorted(emails) for root, emails in g.items()]
```

---

<a id="p-trie"></a>
## 设计 · Trie

每个节点一个 `ch` 字典指向孩子，`end` 标记是否成词。插入 / 查找沿字符往下走。

```
node = {ch: {}, end: False}
insert(word):
    cur = root
    for c in word:
        cur = cur.ch.setdefault(c, 新节点)
    cur.end = True
search / startsWith: 沿路走，看 end / 能否走完
```

<a id="lc-208"></a>
### LC 208 实现 Trie

本质上：实现 `insert` / `search` / `startsWith`。

```python
class Trie:
    def __init__(self):
        self.ch, self.end = {}, False
    def insert(self, word):
        cur = self
        for c in word:
            cur = cur.ch.setdefault(c, Trie())
        cur.end = True
    def _walk(self, s):
        cur = self
        for c in s:
            if c not in cur.ch:
                return None
            cur = cur.ch[c]
        return cur
    def search(self, word):
        cur = self._walk(word)
        return bool(cur) and cur.end
    def startsWith(self, prefix):
        return self._walk(prefix) is not None
```

---

<a id="p-lru"></a>
## 设计 · LRU

哈希 O(1) 查节点，双向链表 O(1) 调整顺序。访问 / 更新就把节点挪到尾（最新）；满了删头（最旧）。Python 用 `OrderedDict` 即可。

```
get(k):  没有 return -1；有则 move_to_end(k)，return val
put(k,v):
    d[k] = v; move_to_end(k)
    if len(d) > cap: d.popitem(last=False)    # 删头
```

<a id="lc-146"></a>
### LC 146 LRU 缓存

本质上：容量有限的缓存，满了淘汰最久没碰的。

```python
class LRUCache:
    def __init__(self, capacity):
        self.cap, self.d = capacity, OrderedDict()
    def get(self, key):
        if key not in self.d:
            return -1
        self.d.move_to_end(key)
        return self.d[key]
    def put(self, key, value):
        self.d[key] = value
        self.d.move_to_end(key)
        if len(self.d) > self.cap:
            self.d.popitem(last=False)
```

---

<a id="p-min-stack"></a>
## 设计 · 最小栈

再开一个栈同步记「到目前为止的最小」。入栈时 `min(x, 当前最小)`，出栈两边一起弹。

```
st, mn = [], []
push(x): st.append(x); mn.append(x if not mn else min(x, mn[-1]))
pop:     st.pop(); mn.pop()
getMin:  mn[-1]
```

<a id="lc-155"></a>
### LC 155 最小栈

本质上：O(1) 取栈里最小值。

```python
class MinStack:
    def __init__(self):
        self.st, self.mn = [], []
    def push(self, x):
        self.st.append(x)
        self.mn.append(x if not self.mn else min(x, self.mn[-1]))
    def pop(self):
        self.st.pop()
        self.mn.pop()
    def top(self):
        return self.st[-1]
    def getMin(self):
        return self.mn[-1]
```

---

<a id="p-rand"></a>
## 设计 · O(1) 随机

哈希存值→下标，数组存值。删：把要删的和末尾交换，再 pop，并改哈希。随机 `random.choice(arr)`。

```
d[val] = 下标; arr.append(val)
删: i = d[val]; arr[i] = arr[-1]; d[arr[i]] = i; pop; del d[val]
```

<a id="lc-380"></a>
### LC 380 O(1) 时间插入、删除和获取随机元素

本质上：不重复集合，插入 / 删除 / 等概率随机都 O(1)。

```python
import random

class RandomizedSet:
    def __init__(self):
        self.d, self.arr = {}, []
    def insert(self, val):
        if val in self.d:
            return False
        self.d[val] = len(self.arr)
        self.arr.append(val)
        return True
    def remove(self, val):
        if val not in self.d:
            return False
        i = self.d[val]
        last = self.arr[-1]
        self.arr[i] = last
        self.d[last] = i
        self.arr.pop()
        del self.d[val]
        return True
    def getRandom(self):
        return random.choice(self.arr)
```

---

<a id="p-dp-lin"></a>
## DP · 线性

`dp(i)` 只依赖后面（或前面）几个下标。`@cache` 挂嵌套函数，参数别传 `list`。边界先写出来。

```
@cache
def dp(i):
    if i 越界: return 0
    return max(dp(i+1),          # 不选 i
               a[i] + dp(i+2))   # 选 i
```

<a id="lc-198"></a>
### LC 198 打家劫舍

本质上：不相邻房子能偷到的最大金额。

```python
def rob(nums):
    n = len(nums)
    @cache
    def dp(i):
        if i >= n:
            return 0
        return max(dp(i + 1), nums[i] + dp(i + 2))
    return dp(0)
```

---

<a id="p-dp-unb"></a>
## DP · 完全背包

每种物品可用无限次。一维数组必须 **正序**（用到更新后的 `dp[s-x]`）。0-1 背包一维必须 **倒序**。

```
dp[0] = 0; 其余 inf
for x in items:
    for s in x .. W:                 # 完全：正序
        dp[s] = min(dp[s], dp[s-x] + 1)
# 0-1 则: for s in W .. x: 倒序
```

<a id="lc-322"></a>
### LC 322 零钱兑换

本质上：凑出 `amount` 的最少硬币数，凑不出则 `-1`。

```python
def coinChange(coins, amount):
    dp = [0] + [math.inf] * amount
    for x in coins:
        for s in range(x, amount + 1):
            dp[s] = min(dp[s], dp[s - x] + 1)
    return dp[amount] if dp[amount] < math.inf else -1
```

---

<a id="p-kadane"></a>
## DP · Kadane

扫一遍：当前子段要么接在后面，要么从这里重开。`cur = max(x, cur + x)`。要下标就多记 start。

```
cur = ans = a[0]
for x in a[1:]:
    cur = max(x, cur + x)
    ans = max(ans, cur)
```

<a id="lc-53"></a>
### LC 53 最大子数组和

本质上：连续子数组的最大和。

```python
def maxSubArray(nums):
    cur = ans = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        ans = max(ans, cur)
    return ans
```

---

<a id="p-dp-grid"></a>
## DP · 网格

`dp[i][j]` 只来自上方和左方。第一行 / 第一列单独铺。空间可压成一行。

```
dp[0][0] = 起点
dp[i][j] = 从左 + 从上   # 路径数相加；最小路径取 min 再加格子
```

<a id="lc-62"></a>
### LC 62 不同路径

本质上：只能右或下，从左上到右下有几条路。

```python
def uniquePaths(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    return dp[-1]
```

<a id="lc-64"></a>
### LC 64 最小路径和

本质上：只能右或下，路径和最小。

```python
def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [math.inf] * n
    dp[0] = 0
    for i in range(m):
        dp[0] += grid[i][0]
        for j in range(1, n):
            dp[j] = grid[i][j] + min(dp[j], dp[j - 1])
    return dp[-1]
```

---

<a id="p-dp-01"></a>
## DP · 0-1 背包

每件最多用一次。一维必须 **倒序**，否则同一件会被用多次（变成完全背包）。

```
dp[0] = True
for x in items:
    for s in W .. x:                 # 倒序
        dp[s] = dp[s] or dp[s - x]
```

<a id="lc-416"></a>
### LC 416 分割等和子集

本质上：能否拆成两个和相等的子集。目标和是总和的一半，0-1 背包能否恰好装满。

```python
def canPartition(nums):
    s = sum(nums)
    if s & 1:
        return False
    W = s // 2
    dp = [False] * (W + 1)
    dp[0] = True
    for x in nums:
        for t in range(W, x - 1, -1):
            dp[t] = dp[t] or dp[t - x]
        if dp[W]:
            return True
    return dp[W]
```

---

<a id="p-lis"></a>
## DP · LIS

`dp[i] = 以 i 结尾的最长递增`。朴素 O(n²)；n 大时用 tails 数组 + 二分 O(n log n)：`tails[len]` 是该长度递增子序列的最小结尾。

```
tails = []
for x in a:
    # 第一个 >= x 的位置换成 x；没有就 append
```

<a id="lc-300"></a>
### LC 300 最长递增子序列

本质上：最长严格递增子序列的长度（可不连续）。

```python
def lengthOfLIS(nums):
    tails = []
    for x in nums:
        lo, hi = 0, len(tails)
        while lo < hi:
            mid = (lo + hi) // 2
            if tails[mid] >= x:
                hi = mid
            else:
                lo = mid + 1
        if lo == len(tails):
            tails.append(x)
        else:
            tails[lo] = x
    return len(tails)
```

---

<a id="p-dp-str"></a>
## DP · 字符串

两个串：`dp(i, j)` 表示 `s[i:]` 和 `t[j:]`。LCS 取 max；编辑距离取 min 再加一步。一个串 + 词典：`dp(i)` 表示 `s[i:]` 能否拆开，枚举单词。

```
# LCS
dp(i, j) = 1+dp(i+1,j+1) if s[i]==t[j] else max(dp(i+1,j), dp(i,j+1))
# 编辑距离
相等则 dp(i+1,j+1)；否则 1 + min(插, 删, 改)
# Word Break
dp(i) = any(s[i:i+len(w)] == w and dp(i+len(w)) for w in words)
```

<a id="lc-1143"></a>
### LC 1143 最长公共子序列

本质上：两个串的 LCS 长度。

```python
def longestCommonSubsequence(text1, text2):
    @cache
    def dp(i, j):
        if i == len(text1) or j == len(text2):
            return 0
        if text1[i] == text2[j]:
            return 1 + dp(i + 1, j + 1)
        return max(dp(i + 1, j), dp(i, j + 1))
    return dp(0, 0)
```

<a id="lc-72"></a>
### LC 72 编辑距离

本质上：把 `word1` 变成 `word2` 的最少插入 / 删除 / 替换次数。

```python
def minDistance(word1, word2):
    @cache
    def dp(i, j):
        if i == len(word1) or j == len(word2):
            return len(word1) - i + len(word2) - j
        if word1[i] == word2[j]:
            return dp(i + 1, j + 1)
        return 1 + min(
            dp(i, j + 1),      # 插
            dp(i + 1, j),      # 删
            dp(i + 1, j + 1),  # 改
        )
    return dp(0, 0)
```

<a id="lc-139"></a>
### LC 139 单词拆分

本质上：`s` 能否拆成词典里的词（可重复用）。

```python
def wordBreak(s, wordDict):
    words = set(wordDict)
    n = len(s)
    @cache
    def dp(i):
        if i == n:
            return True
        for j in range(i + 1, n + 1):
            if s[i:j] in words and dp(j):
                return True
        return False
    return dp(0)
```

<a id="lc-91"></a>
### LC 91 解码方法

本质上：`12` 可以当 `AB` 或 `L`，数字串有几种解码方式。`0` 不能单独，`10`/`20` 合法，`27` 以上不能两位数。

```python
def numDecodings(s):
    n = len(s)
    @cache
    def dp(i):
        if i == n:
            return 1
        if s[i] == "0":
            return 0
        ans = dp(i + 1)
        if i + 1 < n and int(s[i:i + 2]) <= 26:
            ans += dp(i + 2)
        return ans
    return dp(0)
```

---

<a id="p-stock"></a>
## DP · 股票

只交易一次：扫一遍，记历史最低，卖出利润取 max。不限次数：只要涨就加（等价于每次上涨都做）。

```
# 一次：ans = max(ans, x - mn); mn = min(mn, x)
# 无限：ans += max(0, a[i] - a[i-1])
```

<a id="lc-121"></a>
### LC 121 买卖股票的最佳时机

本质上：只能买卖一次的最大利润。

```python
def maxProfit(prices):
    mn, ans = math.inf, 0
    for x in prices:
        ans = max(ans, x - mn)
        mn = min(mn, x)
    return ans
```

<a id="lc-122"></a>
### LC 122 买卖股票的最佳时机 II

本质上：能买卖任意次（不能同时持有）的最大利润。

```python
def maxProfitII(prices):
    return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))
```

---

<a id="p-dp-tree"></a>
## DP · 树

每个节点两个状态：选自己 / 不选自己。选了就不能选儿子。后序返回一对值。

```
def dfs(node):  # (选, 不选)
    if not node: return 0, 0
    Ls, Ln = dfs(node.left)
    Rs, Rn = dfs(node.right)
    选 = node.val + Ln + Rn
    不选 = max(Ls, Ln) + max(Rs, Rn)
    return 选, 不选
```

<a id="lc-337"></a>
### LC 337 打家劫舍 III

本质上：二叉树上不相邻节点的最大和。

```python
def robTree(root):
    def dfs(node):
        if not node:
            return 0, 0
        Ls, Ln = dfs(node.left)
        Rs, Rn = dfs(node.right)
        steal = node.val + Ln + Rn
        skip = max(Ls, Ln) + max(Rs, Rn)
        return steal, skip
    return max(dfs(root))
```

---

<a id="p-greedy"></a>
## 贪心 · 跳跃 / 环路 / 任务

跳跃：维护当前能到的最远，扫过一遍还没到终点就是 False。加油站：总油不够则不可能；从亏空最大的下一站出发。任务：空档 = `max(0, (max频-1)*(n+1) + 并列最多的个数 - len(tasks))`。

```
# 跳跃: far = max(far, i + a[i]); 若 i > far: 到不了
# 加油站: 总 tank < 0 则 -1；cur < 0 则起点改成 i+1、cur 清零
```

<a id="lc-55"></a>
### LC 55 跳跃游戏

本质上：能否从下标 0 跳到最后。

```python
def canJump(nums):
    far = 0
    for i, x in enumerate(nums):
        if i > far:
            return False
        far = max(far, i + x)
    return True
```

<a id="lc-134"></a>
### LC 134 加油站

本质上：绕环一圈的起始加油站，不可能则 `-1`（保证唯一）。

```python
def canCompleteCircuit(gas, cost):
    if sum(gas) < sum(cost):
        return -1
    tank = start = 0
    for i, (g, c) in enumerate(zip(gas, cost)):
        tank += g - c
        if tank < 0:
            tank, start = 0, i + 1
    return start
```

<a id="lc-621"></a>
### LC 621 任务调度器

本质上：相同任务之间至少隔 `n` 个单位，完成全部的最短时间。

```python
def leastInterval(tasks, n):
    freq = list(Counter(tasks).values())
    mx = max(freq)
    mx_cnt = freq.count(mx)
    return max(len(tasks), (mx - 1) * (n + 1) + mx_cnt)
```

---

<a id="p-pal"></a>
## 回文 · 中心扩展

每个位置当中心（奇）和缝当中心（偶），向两边扩。最长回文子串、回文子串个数都这一套。不要先上 DP。

```
def expand(lo, hi):
    while lo >= 0 and hi < n and s[lo] == s[hi]:
        lo -= 1; hi += 1
    return lo + 1, hi - 1          # 闭区间
```

<a id="lc-5"></a>
### LC 5 最长回文子串

本质上：最长回文子串本身。

```python
def longestPalindrome(s):
    n, best = len(s), (0, 0)
    def expand(lo, hi):
        while lo >= 0 and hi < n and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        return lo + 1, hi - 1
    for i in range(n):
        for lo, hi in (expand(i, i), expand(i, i + 1)):
            if hi - lo > best[1] - best[0]:
                best = (lo, hi)
    lo, hi = best
    return s[lo:hi + 1]
```

---

<a id="p-bit"></a>
## 位运算 · XOR / 计数

成对的抵消，剩下的就是只出现一次的 / 缺失的。`n & (n-1)` 清掉最低的 1；循环就能数 1 的个数。

```
xor 全部 → 落单的那个
n & (n - 1)  去掉最低位的 1
n & -n       最低位的 1
```

<a id="lc-136"></a>
### LC 136 只出现一次的数字

本质上：其它都出现两次，找出只出现一次的。

```python
def singleNumber(nums):
    x = 0
    for v in nums:
        x ^= v
    return x
```

<a id="lc-191"></a>
### LC 191 位 1 的个数

本质上：有多少个 1。

```python
def hammingWeight(n):
    ans = 0
    while n:
        n &= n - 1
        ans += 1
    return ans
```

---

<a id="p-pow"></a>
## 数学 · 快速幂

指数对半分：`x^n = (x^{n//2})^2`，奇数再乘一次 `x`。负数指数先算正的再取倒数。`math.gcd(a, b)` 直接用。

```
if n == 0: return 1
half = pow(x, n // 2)
return half * half * (x if n 奇数 else 1)
```

<a id="lc-50"></a>
### LC 50 Pow(x, n)

本质上：`x^n`，n 可为负。

```python
def myPow(x, n):
    if n < 0:
        x, n = 1 / x, -n
    ans = 1
    while n:
        if n & 1:
            ans *= x
        x *= x
        n >>= 1
    return ans
```

---

<a id="p-matrix"></a>
## 矩阵 · 旋转 / 螺旋 / 置零

旋转 90° 顺时针：先转置再每行反转。螺旋：四边界往里收。置零：第一行第一列当标记，先记再清，避免提前抹掉标记。

```
# 旋转: for i: for j>i: swap (i,j)(j,i)；再 row.reverse()
# 螺旋: t,b,l,r 四边界，走完一圈收一圈
# 置零: 用第 0 行/列当标记
```

<a id="lc-48"></a>
### LC 48 旋转图像

本质上：原地顺时针转 90°。

```python
def rotate(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()
```

<a id="lc-54"></a>
### LC 54 螺旋矩阵

本质上：顺时针一圈圈读出。

```python
def spiralOrder(matrix):
    if not matrix:
        return []
    t, b, l, r, ans = 0, len(matrix) - 1, 0, len(matrix[0]) - 1, []
    while t <= b and l <= r:
        for j in range(l, r + 1):
            ans.append(matrix[t][j])
        t += 1
        for i in range(t, b + 1):
            ans.append(matrix[i][r])
        r -= 1
        if t <= b:
            for j in range(r, l - 1, -1):
                ans.append(matrix[b][j])
            b -= 1
        if l <= r:
            for i in range(b, t - 1, -1):
                ans.append(matrix[i][l])
            l += 1
    return ans
```

<a id="lc-73"></a>
### LC 73 矩阵置零

本质上：某格是 0，就把整行整列置 0，原地。

```python
def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])
    col0 = any(matrix[i][0] == 0 for i in range(m))
    row0 = any(matrix[0][j] == 0 for j in range(n))
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    if row0:
        for j in range(n):
            matrix[0][j] = 0
    if col0:
        for i in range(m):
            matrix[i][0] = 0
```

---

<a id="p-matrix-search"></a>
## 矩阵 · 从角搜索

每行从左到右、每列从上到下递增，但从左上二分不行（右边和下边都更大）。从**右上**出发：太大往左，太小往下，一次丢掉一行或一列，O(m+n)。

```
r, c = 0, n - 1
while r < m and c >= 0:
    if a[r][c] == target: 找到
    elif a[r][c] > target: c -= 1
    else: r += 1
```

<a id="lc-240"></a>
### LC 240 搜索二维矩阵 II

本质上：每行每列递增（下一行开头不必比上一行结尾大），找 `target`。

```python
def searchMatrixII(matrix, target):
    m, n = len(matrix), len(matrix[0])
    r, c = 0, n - 1
    while r < m and c >= 0:
        if matrix[r][c] == target:
            return True
        if matrix[r][c] > target:
            c -= 1
        else:
            r += 1
    return False
```

---

<a id="p-qselect"></a>
## 快选 · 第 K 大

快排的 partition：枢轴最终位置就是第几大。只要那一侧有 k 就只递归那一侧，平均 O(n)。面试堆更稳；写快选要随机枢轴，防有序退化。

```
k 大 = 从小到大第 n-k 个
partition 后 pivot 在 p:
    p == n-k: 就是它
    p <  n-k: 右边找
    p >  n-k: 左边找
```

<a id="lc-215-qs"></a>
### LC 215 快选写法

本质上：和第 K 大同一题，不用堆。

```python
import random

def findKthLargestQS(nums, k):
    target = len(nums) - k
    def partition(lo, hi):
        p = random.randint(lo, hi)
        nums[p], nums[hi] = nums[hi], nums[p]
        i = lo
        for j in range(lo, hi):
            if nums[j] < nums[hi]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[hi] = nums[hi], nums[i]
        return i
    lo, hi = 0, len(nums) - 1
    while True:
        p = partition(lo, hi)
        if p == target:
            return nums[p]
        if p < target:
            lo = p + 1
        else:
            hi = p - 1
```

---

<a id="p-cycle"></a>
## 循环定位 · 找重复

`1..n` 放进 `n+1` 个格子，把值当成 next 指针，就变成链表找环入口（和 142 同一套）。不能改数组时用这招。

```
slow = fast = 0
slow, fast = a[slow], a[a[fast]]     # 直到相遇
再从 0 和相遇点齐走，相遇就是重复
```

<a id="lc-287"></a>
### LC 287 寻找重复数

本质上：`n+1` 个数都在 `1..n`，有且仅有一个重复，不能改数组。

```python
def findDuplicate(nums):
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    p = 0
    while p != slow:
        p, slow = nums[p], nums[slow]
    return p
```

---

<a id="p-next-perm"></a>
## 排列 · 下一个

从右找第一处上升 `a[i] < a[i+1]`；再从右找第一个 `> a[i]` 的与它交换；然后把 `i+1` 后面反转。没有上升就是最大排列，整体反转。

```
i = n-2; while i>=0 and a[i] >= a[i+1]: i -= 1
if i >= 0:
    j = n-1; while a[j] <= a[i]: j -= 1
    swap i, j
反转 a[i+1:]
```

<a id="lc-31"></a>
### LC 31 下一个排列

本质上：改成字典序下一个更大排列；已经最大就变成最小。

```python
def nextPermutation(nums):
    n = len(nums)
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    lo, hi = i + 1, n - 1
    while lo < hi:
        nums[lo], nums[hi] = nums[hi], nums[lo]
        lo += 1
        hi -= 1
```

---

## 交题前

1. 二维用推导式  
2. 队列 `deque`，栈 `list`  
3. 回溯 `path[:]`；有重复先排序，同一层跳过相同值  
4. BFS 入队就进 `seen`  
5. 空、单节点、全相同、`k=0`  
6. 网格越界  
7. 编号从 0 还是 1  
8. `@cache` 不传 `list`  
9. `//` 对负数向下  
10. `n=1e5` 不要双层循环  
11. BST 验证带上下界，不能只比左右孩子  
12. 0-1 背包一维倒序，完全背包正序  

先默写：哈希、对撞/同向/滑窗、链表快慢 + dummy + 反转、前缀和/差分、二分（含旋转）、栈/单调栈、堆、树递归 + 层序 + 路径、**BST 验证/插入/第 K/LCA/建树**、网格 BFS、图 BFS、回溯、区间扫描、拓扑、并查集。Trie / LRU / 最小栈各写一遍。最后 DP（线性、Kadane、网格、背包、LIS、字符串、股票、树）。
