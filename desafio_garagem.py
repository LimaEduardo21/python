carro = {
    "Marca" : "Honda",
    "Ano" : 1996,
    "Modelo" : "Civic G6"
}

def exibir_ficha(carros):
    print("\n=== FICHA TECNICA===")
    print(f"Marca: {carros['Marca']}")
    print(f"Ano: {carros['Ano']}")
    print(f"Modelo: {carros['Modelo']}")

exibir_ficha(carro)

carro["cor"] = "Branco"
print(f"Cor cadastrada: {carro['cor']}")
exibir_ficha(carro)