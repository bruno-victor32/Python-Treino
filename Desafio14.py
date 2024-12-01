#Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

temperatura_c = float(input('Digite o valor da temperatura em ºC: '))
temperatura_f = float(input('Digite o valor da temperatura em ºF: '))
temp_f = (temperatura_c * 9/5) +32
temp_c = (temperatura_f - 32) * 5/9
print(f'O valor da temperatura digitado em Celsius foi {temperatura_c}ºC, convertido para Fahrenheit  {temp_f}ºF')
print(f'O valor da temperatura digitado em Fahrenheit foi {temperatura_f}ºF, convertido para Celsius  {temp_c:.2f}°C')