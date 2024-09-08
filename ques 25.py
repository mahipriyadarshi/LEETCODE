class Solution:
    def has_exactly_two_divisors(self, n):
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False

        primes = [i for i in range(2, n + 1) if is_prime[i]]
        return primes
    def nonSpecialCount(self,l, r):


        primes = self.has_exactly_two_divisors(int(r ** 0.5))
        count = 0

        for prime in primes:
            square = prime * prime
            if l <= square <= r:
                count += 1

        total_count = r - l + 1

        return total_count - count





if __name__ == "__main__":
    pointer = Solution()
    l,r=4,16
    print(pointer.nonSpecialCount(l,r))