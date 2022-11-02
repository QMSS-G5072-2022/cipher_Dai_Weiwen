from cipher_wd2366_helen import cipher_wd2366_helen

import pytest
@pytest.mark.parametrize('text, shift, expected', [
    ('Helen', 1, 'Ifmfo'),
    ('helen', 1, 'ifmfo'),
    ('HELEN', 1, 'IFMFO'),
    ('My name is Helen', 1, 'Nz obnf jt Ifmfo')])

def test_cipher(text, shift, expected):
    assert cipher_wd2366_helen.cipher(text, shift) == expected, 'Function cipher not pass.'