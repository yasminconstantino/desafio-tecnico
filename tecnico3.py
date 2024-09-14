'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

'''

import json

def analisar_faturamento(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)

    valores = [item['valor'] for item in dados if item['valor'] > 0]
    if not valores:
        return None, None, 0

    media = sum(valores) / len(valores)
    menor = min(valores)
    maior = max(valores)
    acima_media = sum(1 for valor in valores if valor > media)

    return menor, maior, acima_media

# usando a função criada e referenciando o arquivo dados.json
arquivo_json = 'dados.json'  # Substitua pelo nome do seu arquivo
menor, maior, dias_acima_media = analisar_faturamento(arquivo_json)

if menor is not None:
    print(f"Menor valor de faturamento: R$ {menor:.2f}")
    print(f"Maior valor de faturamento: R$ {maior:.2f}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")
else:
    print("Não há dados de faturamento válidos no arquivo.")