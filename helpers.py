def rr(i, rc):
    i %= 4
    return i-1-rc if (i+rc) % 2 == 0 else 0
def rb(i, rc):
    i = (i + 1 - rc) % 4
    return -1 if i < 2 else 1
def rc(i, dp):
    return (dp[0] * rr(i, 0) + dp[1] * rr(i, 1), dp[0] * rr(i-1, 0) + dp[1] * rr(i-1, 1))

if __name__ == "__main__":
    print((rr(0, 0), rr(0, 1)))
    print((rr(1, 0), rr(1, 1)))
    print((rr(2, 0), rr(2, 1)))
    print((rr(3, 0), rr(3, 1)))

    print(rc(0, (1, 0)))
    print(rc(1, (1, 0)))
    print(rc(2, (1, 0)))
    print(rc(3, (1, 0)))
    
    print(rc(0, (1, 1)))
    print(rc(1, (1, 1)))
    print(rc(2, (1, 1)))
    print(rc(3, (1, 1)))