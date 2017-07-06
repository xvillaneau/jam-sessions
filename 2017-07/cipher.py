""" Example class-based solution to get your started.  Feel
free to use this as a start, but you can use a function based
solution instead of a class if you prefer! """


def normalize(message):
    """
    Convert any string into a no-spaces capitalized string
    :param message: Input string or key to convert
    :type message: str
    :return: Normalized string or key
    """
    return filter(str.isalpha, message.upper())


def tabula_recta(msg, key):
    """
    Get the ciphered letter from the matching key letter and message letter
    
    :param msg: Message letter
    :param key: Key letter
    :return: Encrypted letter
    """
    orig = ord('A')

    i_m = ord(msg) - orig
    i_k = ord(key) - orig

    return chr((i_m + i_k) % 26 + orig)


class AlphabetCipher:
    def __init__(self, keyphrase):
        """ Do initial setup with keyphrase and anything
        else needed to encode / decode. """

    def encode(self, plaintext):
        """ Write your code to encode the plaintext into
        ciphertext. """
        ciphertext = None
        # Add your code here
        return ciphertext

    def decode(self, ciphertext):
        """ Write your code to decode the ciphertext back
        into a plaintext message. """
        plaintext = None
        # Add your code here
        return plaintext
