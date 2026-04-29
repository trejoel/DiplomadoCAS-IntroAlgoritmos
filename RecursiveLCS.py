def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs_recursive(X, Y, m - 1, n - 1)
    else:
        return max(lcs_recursive(X, Y, m, n - 1), lcs_recursive(X, Y, m - 1, n))



def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Ejemplo de uso
#X = "AGGTABCCADAT"
#Y = "GXTXAYBADT"
X = "ACCGGTCGAGTGCGCGGAAGCCGGCCGAA"
Y = "GTCGTTCGGAATGCCGTTGCTCTGTAAA"
#print("LCS (Recursivo):", lcs_recursive(X, Y, len(X), len(Y))) 
print("LCS (DP):", lcs_dp(X, Y))  # Salida esperada: 4
