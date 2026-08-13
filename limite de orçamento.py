meus_gastos = []

limite_orçamento = 250.00

def adicionar_gasto(valor):
    meus_gastos.append(valor)
    print(f"Gasto {valor} adicionada!")
    pass

def calcular_total_gasto():
    gasto = sum(meus_gastos)
    quant_gastos = len(meus_gastos)
    return gasto / quant_gastos

def verificar_orçamento(total):
    if total <= 250.0:
        print("Dentro do orçamento")
    else:
        print("🚨ATENÇÃO: VOCÊ ESTOUROU O ORÇAMENTO")

# Registrando os gastos do dia
adicionar_gasto(300.00)  
adicionar_gasto(210.00)  
adicionar_gasto(250.00)

total_fatura = calcular_total_gasto()
print(f"Total gasto até agora: R$ {total_fatura:.2f}")

verificar_orçamento(total_fatura)