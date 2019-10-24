"""
@=lc id=692 lang=python3 tag=heapsort

[692] Top K Frequent Words

Given a non-empty list of words, return the k most frequent elements.

Your answer should be sorted by frequency from highest to lowest.
If two words have the same frequency, word with lower alphabetical first.

Constraints:
    1. k is always valid, 1 <= k <= len(words).
    2. Input words contain only lowercase letters.


Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:
Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
       k = 4
Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.


Complexity
Time: O(n log n) -> n for counts, worst case n pushes of logn heap + k for ret
Space: O(n) -> worst case n for counts, n for heap = 2n
"""


import collections, heapq


class Solution:
    WordFreq = collections.namedtuple('WordFreq', ('freq', 'word'))
    
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Note: Python sorts tuples by every field.
        So when we add (-freq, word), heap prefers tuples first with
        frequency (use -freq to sort by highest) and then alphabetically by word.
        """
        counts = collections.Counter(words)
        freq_heap = [self.WordFreq(-freq, word) for word, freq in counts.items()]
        heapq.heapify(freq_heap)
        return [heapq.heappop(freq_heap).word for _ in range(k)]

