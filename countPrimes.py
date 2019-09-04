# 204. Count Primes
# Count the number of prime numbers less than a non-negative number, n.
# Example:
# Input: 10
# Output: 4
# Explanation:
# There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


class Solution:
    def countPrimesSimple(self, n: int) -> int:
        """
        Time to sift out multiples of p is proportional to n/p,
        so overall = O(n/2 + n/3 + n/5 + n/7, ...) -> O(n log log n)
        Space: O(n), which is the biggest problem with simple sieve.
        """
        if n < 2:
            return 0

        primes = []
        is_prime = [False, False] + [True for i in range(n-1)]

        for x in range(2, n):
            if is_prime[x]:
                primes.append(x)
            for i in range(x*2, n, x):
                is_prime[i] = False

        return len(primes)

    def countPrimesOptimized(self, n: int) -> int:
        """
        Asymptiotic time and space coplexity are same for basic sieving,
        but practical improvement to runtime by sieving p's multiples
        from p^2 instead of p, since all numbers of the
        form `kp` where k < p have already been sieved out.
        Storage is also be reduced by ignoring even numbers.
        """
        if n < 2:
            return 0

        size = (n - 3) // 2 + 1  # -3 for 0,1,2 and // 2 to ignore evens
        primes = [2]
        is_prime = [True for i in range(size)]  # represents if (2i+3) is prime

        for i in range(size):
            if is_prime[i]:
                p = 2 * i + 3
                primes.append(p)
                # Sieve from p^2, where p^2 = (2i+3)^2  = (4i^2 + 12i + 9)
                # Index in is_prime is (2i^2 + 6i + 3)
                # because is_prime[i] = 2i + 3.
                for j in range(2 * i**2 + 6 * i + 3, size, p):
                    is_prime[j] = False

        return len(primes) - 1 if primes[-1] == n else len(primes)
