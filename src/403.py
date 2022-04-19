def canCross(stones):

    # Tamanho da lista de pedras
    n = len(stones)

    dp = [[False] * (n + 1) for _ in range(n)]

    # Definindo como ponto base
    dp[0][0] = True

    # Iterar i de [1,n-1] e para cada i, iterar j de [0,i-1] e vamos definir diferença = pedras[i] – pedras[j] 
    # que é o salto feito pelo sapo para alcançar a iª pedra da jª pedra, se possível. 

    for i in range(1, n):
        for j in range(i):
            k = stones[i] - stones[j]
    
        if k > n:
            continue

        # Movimentações (pulos) possíveis
        for x in (k - 1, k, k + 1):
            if 0 <= x <= n:
                dp[i][k] |= dp[j][x]     
    
    return any(dp[-1])

# Exemplo de lista de entrada de pedras
stones = [0,1,2,3,4,8,9,11]

# Print do resultado dos pulos, true para sucesso e false para falha
print(canCross(stones))
