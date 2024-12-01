

km_percorrido = float(input('Digite a quantidade de KM percorrido pelo carro: '))
dias_alugado = int(input('Digite a quantidade de dias que ficou com o carro: '))
valor_diaria = dias_alugado * 60
valor_km_rodada = km_percorrido * 0.15
total = valor_diaria + valor_km_rodada
print(f' O km percorridos foi de {km_percorrido:.0f} km e ficou com o carro {dias_alugado} dias')
print(f'O valor das diarias totalizou em R${valor_diaria:.2f} e de km percorrido em R${valor_km_rodada:.2f}, o valor total a ser pago será de R${total:.2f}')