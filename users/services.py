import stripe

from drf.settings import STRIPE_KEY

stripe.api_key = STRIPE_KEY


def create_product(name):
    return stripe.Product.create(name=name)


def create_price(amount, product):
    return stripe.Price.create(
        currency="rub",
        unit_amount=amount * 80,
        product=product.get('id')
    )


def create_session(price):
    session = stripe.checkout.Session.create(
        line_items=[{"price": price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')