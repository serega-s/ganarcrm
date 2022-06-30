import stripe

from django.conf import settings


def create_checkout_session(team, price_id):
    """Service for creating a checkout session
    """
    return stripe.checkout.Session.create(
        client_reference_id=team.id,
        success_url='%s?session_id={CHECKOUT_SESSION_ID}' % settings.FRONTEND_WEBSITE_SUCCESS_URL,
        cancel_url=f'{settings.FRONTEND_WEBSITE_CANCEL_URL}',
        payment_method_types=['card'],
        mode='subscription',
        line_items=[{
            'price': price_id,
            'quantity': 1
        }]
    )
