import pytest
from mock import MagicMock
from messaging.helpers.twillio import {
    whatsapp_rating_reply_message,
    RESOLVER_RATING_TO_DRIVER_CALL_CODE,
    WHATSAPP_RATINGS_REPLY_BAD,
    WHATSAPP_RATINGS_REPLY_GOOD,
    WHATSAPP_RATINGS_REPLY_DONT_UNDERSTAND
}


@pytest.mark.parametrize('response, intention, expected_message', [
    ('boa', RESOLVER_RATING_TO_DRIVER_CALL_CODE, WHATSAPP_RATINGS_REPLY_GOOD),
    ('ruim', RESOLVER_RATING_TO_DRIVER_CALL_CODE, WHATSAPP_RATINGS_REPLY_BAD),
    ('nao entendi', RESOLVER_RATING_TO_DRIVER_CALL_CODE,WHATSAPP_RATINGS_REPLY_DONT_UNDERSTAND)
], id=('boa', 'ruim', 'nao entendi'))
def test_whatsapp_rating_reply_message(response, intention, expected_message):
    recipient = MagicMock(first_name="")

    result = whatsapp_rating_reply_message(
        intention=intention,
        response=response,
        recipient=recipient
    )

    assert result == expected_message