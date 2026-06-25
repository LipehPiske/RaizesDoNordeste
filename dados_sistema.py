# BANCO DE DADOS (Simulando o sistema da franquia)

usuarios = {
    "cliente": {"senha": "987", "perfil": "CLIENTE", "loja": None},
    "funcionario1": {"senha": "Matriz", "perfil": "FUNCIONARIO", "loja": "Unidade Matriz (Loja 01)"},
    "funcionario2": {"senha": "Shop", "perfil": "FUNCIONARIO", "loja": "Unidade Shopping (Loja 02)"},
    "funcionario3": {"senha": "Centro", "perfil": "FUNCIONARIO", "loja": "Unidade Centro (Loja 03)"},
    "chefe": {"senha": "Admin", "perfil": "ADM", "loja": None}
}

cardapio = {
    1: {"item": "Tapioca Recheada", "preco": 9.00},
    2: {"item": "Cuscuz Recheado", "preco": 12.00},
    3: {"item": "Bolo de Macaxeira", "preco": 6.00},
    4: {"item": "Suco Regional", "preco": 5.00},
    5: {"item": "Café da Manhã Completo", "preco": 25.00}
}

estoque = {
    "Tapioca Recheada": 300,
    "Cuscuz Recheado": 180,
    "Bolo de Macaxeira": 198,
    "Suco Regional": 201,
    "Café da Manhã Completo": 231
}

dados_todas_lojas = {
    "Unidade Matriz (Loja 01)": {
        "funcionarios": ["Carlos (Gerente)", "Suelen (Atendente)", "Jurandir (Cozinheiro)"],
        "estoque": {"Tapioca Recheada": 100, "Cuscuz Recheado": 50, "Bolo de Macaxeira": 67, "Suco Regional": 67, "Café da Manhã Completo": 86},
        "meta_diaria": 1000.00,
        "venda_atual": 350.00
    },
    "Unidade Shopping (Loja 02)": {
        "funcionarios": ["Mariana (Gerente)", "Bruno (Atendente)", "Francisca (Cozinheira)"],
        "estoque": {"Tapioca Recheada": 100, "Cuscuz Recheado": 60, "Bolo de Macaxeira": 65, "Suco Regional": 74, "Café da Manhã Completo": 75},
        "meta_diaria": 2000.00,
        "venda_atual": 850.00
    },
    "Unidade Centro (Loja 03)": {
        "funcionarios": ["Renato (Gerente)", "Julia (Atendente)", "Arlete (Cozinheira)"],
        "estoque": {"Tapioca Recheada": 100, "Cuscuz Recheado": 70, "Bolo de Macaxeira": 66, "Suco Regional": 60, "Café da Manhã Completo": 70},
        "meta_diaria": 1500.00,
        "venda_atual": 400.00
    }
}

formas_pagamento = {
    1: "Pix",
    2: "Cartão de Débito",
    3: "Cartão de Crédito"
}

dados_matriz = {
    "vendas_totais_reais": 1600.00, 
    "produtos_vendidos": {"Tapioca Recheada": 25, "Cuscuz Recheado": 15, "Bolo de Macaxeira": 20},
    "auditoria_alertas": [
        "ALERTA AUDITORIA: Desconto de 10% na compra pelo aplicado nos pedidos",
        "ALERTA AUDITORIA: Cancelamento de 1x 'Cuscuz' feito pelo Bruno (Loja 02) às 08h40",
        "ALERTA AUDITORIA: Cancelamento de 2x 'Bolo de Macaxeira' feito pela Julia (Loja 03) às 09h35",
        "ALERTA AUDITORIA: Cancelamento de 1x 'Tapioca Recheada' feito pela Suelen (Loja 01) às 11h25"  
    ]
}

materiais_sistema = {
    "Matriz": [
        "Manual Geral",
        "Contrato Padrão Jurídico",
        "Diretrizes de Expansão e Novas Unidades"
    ],
    "Franquias (Operação Local)": [
        "Ficha Técnica Padronizada",
        "Manual Do Consumidor",
        "Guia de Higiene e Controle de Estoque Local"
    ]
}