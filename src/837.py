
def new21Game(n, k, maxPts):
  # quando o jogo termina, o ponto está em [k..k - 1 + maxPts]
    # P = 1, se n >= k - 1 + maxPts
    # P = 0, se n < k (observe as restrições já possuem k <= n)
    if k == 0 or n >= k - 1 + maxPts:
      return 1.0

    ans = 0.0
    # dp[i] := provar ter em pontos
    dp = [1.0] + [0] * n
    # P(i - 1) + P(i - 2) + ... + P(i - maxPts)
    windowSum = dp[0]

    for i in range(1, n + 1):

      dp[i] = windowSum / maxPts
      if i < k:
        windowSum += dp[i]
      else:  
        ans += dp[i]
      if i - maxPts >= 0:
        windowSum -= dp[i - maxPts]

    return ans

n = 10
k = 1
maxPts = 10

print(new21Game(n, k, maxPts))
