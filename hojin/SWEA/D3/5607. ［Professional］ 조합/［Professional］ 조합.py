MOD = 1234567891
MAX = 1000000

fact = [1] * (MAX + 1)
for i in range(1, MAX + 1):
    fact[i] = fact[i - 1] * i % MOD

T = int(input())
for tc in range(1, T + 1):
    n, r = map(int, input().split())
    ans = fact[n] * pow(fact[r] * fact[n - r] % MOD, MOD - 2, MOD) % MOD
    print(f"#{tc} {ans}")