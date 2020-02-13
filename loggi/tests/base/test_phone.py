import pytest
from base.utils.phone import format_phone_number

@pytest.mark.parametrize(
    'phone_number, expected_formatted_phone',
    [
        pytest.param('11912345678', '(11) 91234-5678', id='1'),
        pytest.param('912345678', '91234-5678', id='2'),
        pytest.param('52648388', '5264-8388', id='3'),
        pytest.param('1152648388', '(11) 5264-8388', id='4'),
        pytest.param('(11) 95264-8388', '(11) 95264-8388', id='5'),
    ]
)
def test_valid_cases(phone_number, expected_formatted_phone):
    formatted_phone = format_phone_number(phone_number)

    assert formatted_phone == expected_formatted_phone


def test_invalid_case():
    formatted_phone = format_phone_number('phone_number')

    assert formatted_phone == None