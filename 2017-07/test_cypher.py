
import cipher


def test_normalize():
    """Test cipher.normalize"""
    all_caps = "IAMANALLCAPSSTRING"
    assert cipher.normalize(all_caps) == all_caps
    assert cipher.normalize("I AM AN ALL CAPS STRING") == all_caps
    assert cipher.normalize("I* am an all CAPS string!!!!") == all_caps


def test_tabula_recta():
    """Test cipher.tubula_recta"""
    assert cipher.tabula_recta('A', 'A') == 'A'
    assert cipher.tabula_recta('A', 'B') == 'B'
    assert cipher.tabula_recta('B', 'A') == 'B'
    assert cipher.tabula_recta('B', 'B') == 'C'
    assert cipher.tabula_recta('A', 'Z') == 'Z'
    assert cipher.tabula_recta('Z', 'A') == 'Z'
    assert cipher.tabula_recta('Z', 'Z') == 'Y'


def test_tabula_versa():
    """Test cipher.tubula_versa"""
    assert cipher.tabula_versa('A', 'A') == 'A'
    assert cipher.tabula_versa('B', 'A') == 'B'
    assert cipher.tabula_versa('Z', 'A') == 'Z'
    assert cipher.tabula_versa('A', 'B') == 'Z'
    assert cipher.tabula_versa('B', 'B') == 'A'
    assert cipher.tabula_versa('C', 'B') == 'B'
    assert cipher.tabula_versa('Z', 'B') == 'Y'
    assert cipher.tabula_versa('A', 'Z') == 'B'
    assert cipher.tabula_versa('B', 'Z') == 'C'
    assert cipher.tabula_versa('Z', 'Z') == 'A'


def test_encoding():
    """Write tests to ensure your encoding program works."""
    # Example, based on the instructions
    encoder = cipher.AlphabetCipher('PYTHONISGREAT')
    ciphertext = encoder.encode('NEXTTHURSDAYATSEVENTHIRTY')
    assert ciphertext == 'CCQAHUCJYUEYTIQXCSABZOIXY'


def test_decoding():
    """Write tests to ensure your decoding program works."""
    # Example, based on the instructions
    decoder = cipher.AlphabetCipher('PYTHONISGREAT')
    plaintext = decoder.decode('CCQAHUCJYUEYTIQXCSABZOIXY')
    assert plaintext == 'NEXTTHURSDAYATSEVENTHIRTY'

# Feel free to write further tests to ensure your code works
# for any edge cases!
