
from . import cipher


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
