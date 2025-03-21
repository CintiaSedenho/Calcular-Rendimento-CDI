# Recebendo as variáveis pelo teclado
valor_investido = float(input("Digite o valor investido: R$ "))
cdi_medio_mensal = float(input("Digite a média mensal do CDI (ex: 0.0093 para 0,93%): "))
juros_percentual = float(input("Digite a taxa de juros aplicada sobre o CDI (ex: 1.09 para 109%): "))
ir_percentual = float(input("Digite a alíquota de imposto de renda sobre os juros (ex: 0.15 para 15%): "))
periodo_meses = int(input("Digite o período em meses: "))

# Calculando o rendimento mensal
rendimento_mensal = cdi_medio_mensal * juros_percentual

# Calculando o rendimento após o período de meses (usando a fórmula de juros compostos)
valor_futuro = valor_investido * (1 + rendimento_mensal) ** periodo_meses

# Calculando o valor dos juros recebidos
juros_recebidos = valor_futuro - valor_investido

# Calculando o imposto de renda sobre os juros
ir_pago = juros_recebidos * ir_percentual

# Calculando o valor líquido final
valor_liquido = valor_futuro - ir_pago

# Exibindo os resultados
print(f"Valor líquido final: R${valor_liquido:.2f}")
print(f"Juros recebidos: R${juros_recebidos:.2f}")
print(f"Imposto de Renda pago: R${ir_pago:.2f}")