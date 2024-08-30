faturamento_diario = [100, 200, 150, 0, 0, 300, 250, 0, 0, 400, 50, 0, 500, 0, 0, 100, 200, 0, 0, 300, 250, 0, 0, 400, 50, 0, 500]

dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]

if not dias_com_faturamento:
    print("Não há dados de faturamento para calcular.")
else:
    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_media = len([valor for valor in dias_com_faturamento if valor > media_mensal])

    print(f"Menor valor de faturamento: R${menor_faturamento:.2f}")
    print(f"Maior valor de faturamento: R${maior_faturamento:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
