produto = {
    "Nome":"Notebook",
    "Preco": 3500.0,
    "Quantidade": 4 
}

produto["Preco"] = 4000.00
produto["Marca"] = "Acer Aspire"

del produto["Quantidade"]

print(produto)
