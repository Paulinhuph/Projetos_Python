# --- DEFINIÇÃO DAS FUNÇÕES (As Regras de Negócio) ---
def para_dolar(reais, taxa):
    return reais / taxa
def para_real(dolar, taxa):
    return dolar * taxa
# --- CONFIGURAÇÕES GLOBAL ---
TAXA_CAMBIO = 6.00
# --- PROGRAMA PRINCIPAL ---
print("1- Real para Dólar \n2- Dólar para Real")
escolha = input("Escolha a opção (1/2): ")
if escolha == "1":
    v = float(input("Valor em R$: "))
    resultado = para_dolar(v, TAXA_CAMBIO)
    print(f"Resultado: US$ {resultado:.2f}")
elif escolha == "2":
    v = float(input("Valor em US$: "))
    resultado = para_real(v, TAXA_CAMBIO)
    print(f"Resultado: R$ {resultado:.2f}")
