from django.template import Library
from utils import utils
register = Library()


@register.filter
def formata_preco(val):
    return f'R$ {val:.2f}'.replace('.', ',')


@register.filter
def cart_total(carrinho):
    return utils.cart_total(carrinho)


@register.filter
def totals_cart(carrinho):
    return utils.totals_cart(carrinho)


@register.filter
def qtd_cart(carrinho):
    return utils.qtd_cart(carrinho)
