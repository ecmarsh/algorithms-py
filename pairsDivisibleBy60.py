# 1010. Pairs of Songs with Total Durations Divisble by 60 (Dropbox)
# In a list of songs, the i-th song has a duration of time[i] seconds.
# Return the number of pairs of songs for which their total duration in seconds
# is divisible by 60.
# Formally, the number of indices `i < j` with `(time[i] + time[j]) % 60 == 0`.

# Example 1:
# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
#  (time[0] = 30, time[2] = 150): total duration 180
#  (time[1] = 20, time[3] = 100): total duration 120
#  (time[1] = 20, time[4] = 40): total duration 60

# Example 2:
# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120.

# Constraints:
# 1 <= time.length <= 60000
# 1 <= time[i] <= 500


class BruteSolution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        """
        Time: O(n^2), where n is len(times)
        Space: O(1)
        """
        if len(time) < 2:
            return 0

        pairs = 0

        for i, t1 in enumerate(time[:-1]):
            for t2 in time[i+1:]:
                if (t1 + t2) % 60 == 0:
                    pairs += 1

        return pairs
