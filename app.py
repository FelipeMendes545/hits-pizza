from flask import Flask, render_template

app = Flask(__name__)

# Categorias separadas
promocao20 = [
    {"nome": "Calabresa Acebolada", "ingredientes": "Molho especial, mussarela, calabresa, cebola", "preco_normal": 30, "preco_promocional": 20, "imagem": "PizzaCalabresa.jpg"},
    {"nome": "Frango c/ Catupiry", "ingredientes": "Molho especial, mussarela, frango, catupiry", "preco_normal": 30, "preco_promocional": 20, "imagem": "frango_catupiry.jpg"},
    {"nome": "Presunto", "ingredientes": "Molho especial, mussarela, presunto, orégano", "preco_normal": 30, "preco_promocional": 20, "imagem": "presunto.jpg"},
    {"nome": "Mussarela (dobro)", "ingredientes": "Molho especial, mussarela em dobro, orégano", "preco_normal": 30, "preco_promocional": 20, "imagem": "mussarela.jpg"},
    {"nome": "Marguerita", "ingredientes": "Molho especial, mussarela, tomate, manjericão", "preco_normal": 30, "preco_promocional": 20, "imagem": "marguerita.jpg"},
    {"nome": "Milho", "ingredientes": "Molho especial, mussarela, milho, orégano", "preco_normal": 30, "preco_promocional": 20, "imagem": "pizza_milho.jpg"},
    {"nome": "2 Queijos", "ingredientes": "Molho especial, mussarela, requeijão cremoso", "preco_normal": 30, "preco_promocional": 20, "imagem": "pizza_queijo.jpg"},
    {"nome": "Romeu e Julieta", "ingredientes": "Molho especial, mussarela, goiabada", "preco_normal": 30, "preco_promocional": 20, "imagem": "romeu_julieta.jpg"}
]

promocao30 = [
    {"nome": "Bacon", "ingredientes": "Molho especial, mussarela, bacon, cebola", "preco_normal": 40, "preco_promocional": 30, "imagem": "bacon.jpg"},
    {"nome": "Atum", "ingredientes": "Molho especial, mussarela, atum, orégano", "preco_normal": 40, "preco_promocional": 30, "imagem": "pizza_atum.jpg"},
    {"nome": "3 Queijos", "ingredientes": "Molho especial, mussarela, requeijão, parmesão", "preco_normal": 40, "preco_promocional": 30, "imagem": "pizza3queijo.jpg"},
    {"nome": "Lombinho Canadense", "ingredientes": "Molho especial, mussarela em dobro, orégano", "preco_normal": 40, "preco_promocional": 30, "imagem": "Pizza-lombo-canadense.jpg"},
    {"nome": "Portuguesa", "ingredientes": "Molho especial, mussarela, presunto, ovo, cebola, pimentão", "preco_normal": 40, "preco_promocional": 30, "imagem": "pizza_portuguesa.jpg"},
    {"nome": "Frango 3 Queijos", "ingredientes": "Molho especial, mussarela, frango, requeijão, parmesão", "preco_normal": 40, "preco_promocional": 30, "imagem": "pizza-de-frango3_queijo.jpg"},
    {"nome": "Calabresa c/ Catupiry", "ingredientes": "Molho especial, mussarela, calabresa, catupiry", "preco_normal": 40, "preco_promocional": 30, "imagem": "calabresa_catupiry.jpg"},
    {"nome": "Baiana", "ingredientes": "Molho especial, mussarela, calabresa apimentada, cebola", "preco_normal": 40, "preco_promocional": 30, "imagem": "pizza-baiana-portal-minha-receita.webp"},
    {"nome": "Chocolate c/ Avelã + MM’s", "ingredientes": "Massa artesanal, creme de leite, chocolate, confeitos", "preco_normal": 40, "preco_promocional": 30, "imagem": "pizza chocolate m&m.jpg"}
]


@app.route("/")
def index():
    return render_template("index.html", promocao20=promocao20, promocao30=promocao30)

if __name__ == "__main__":
    app.run(debug=True)
