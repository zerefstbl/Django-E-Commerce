from operator import itemgetter


def cart_total(carrinho):
    return sum([item['quantidade'] for item in carrinho.values()])


def totals_cart(carrinho):
    return sum(
        [
            item.get('preco_quantitativo_promocional')
            if item.get('preco_quantitativo_promocional')
            else item.get('preco_quantitativo')
            for item
            in carrinho.values()

        ]
    )


def qtd_cart(carrinho):
    return sum(
        [
            item.get('quantidade')
            for item
            in carrinho.values()

        ]
    )
