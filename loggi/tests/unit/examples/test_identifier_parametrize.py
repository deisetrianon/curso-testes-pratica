from examples.identifier import Identifier
import pytest

@pytest.fixture(scope='module', params=['ab', 'abcdef'])
def obj_identifier(request):
    return (Identifier(), request.param)

# @pytest.mark.parametrize(
#     'identif',
#     [
#         pytest.param('a', id='CT2'),
#         pytest.param('ab', id='2 valid characters'),
#         pytest.param('abcde'),
#         pytest.param('abcdef'),
#         pytest.param('a1'),
#      ]
# )
# def test_all_valid_cases(identif):

def test_all_valid_cases(obj_identifier):
    identifier = obj_identifier[0]

    is_valid = identifier.validate_identifier(obj_identifier[1])

    assert is_valid is True


def test_exception_raised(obj_identifier):
    identifier = obj_identifier[0]

    with pytest.raises(ValueError) as error:
        identifier.validate_identifier('')

    assert str(error.value) == "Identificador inválido"


# $ docker-compose up --build
# $ docker exec -ti aula_testes_app bash
# $ cd loggi
# $ pytest

## Coverage dos testes
# pytest tests/unit/examples/test_identifier_with_parametrize.py --cov=examples.identifier## Quando há parametrize e lista os testes por parâmetro
# pytest tests/unit/examples/test_identifier_with_parametrize.py --vvv

## Quando há pytest.set_trace
# pytest tests/unit/examples/test_identifier_with_parametrize.py --trace

## Quando o teste falha, ele mostra as variáveis locais que os teste utilizou
# pytest tests/unit/examples/test_identifier_with_parametrize.py --showlocals

## Mostra setup para cada teste (as fixtures ajudam a realizar setups de funções apenas uma vez):
# pytest tests/unit/examples/test_identifier_with_parametrize.py --setup -show