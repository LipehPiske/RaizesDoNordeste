from flask import Flask, jsonify, request
import random
# Importei as variáveis do banco de dados
from dados_sistema import cardapio, estoque, dados_matriz, dados_todas_lojas

app = Flask(__name__)

@app.route("/simular_compra", methods=["POST"])
def simular_compra():
    # Simula o cliente escolhendo um meio de compra aleatório (App, Totem, etc)
    opcao_meio = random.choice([1, 2, 3, 4])
    
    # Escolher um produto do seu cardápio
    produto_id = random.choice(list(cardapio.keys()))
    item = cardapio[produto_id]["item"]
    preco = cardapio[produto_id]["preco"]

    # Verificação do estoque
    if estoque[item] > 0:
        # Desconto na compra pelo App
        if opcao_meio == 1:
            preco *= 0.90
        
        # Deduz do estoque e atualiza o faturamento
        estoque[item] -= 1
        dados_matriz["vendas_totais_reais"] += preco
        dados_todas_lojas["Unidade Matriz (Loja 01)"]["venda_atual"] += preco
        dados_matriz["produtos_vendidos"][item] = dados_matriz["produtos_vendidos"].get(item, 0) + 1

        return jsonify({
            "status": "Sucesso",
            "mensagem": f"Comprou {item} por R${preco:.2f} via meio [{opcao_meio}]",
            "estoque_restante": estoque[item]
        }), 200
    else:
        return jsonify({
            "status": "Erro",
            "mensagem": f"Item {item} Esgotado no estoque!"
        }), 400

if __name__ == "__main__":
    # Roda o servidor Flask
    app.run(debug=True, port=5000)