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


def tabula_versa(crp, key):
    """
    Convert an encrypted letter to clear letter from its matching key

    :param crp: Encrypted letter
    :param key: Key letter
    :return: Message letter
    """
    return chr((ord(crp) - ord(key)) % 26 + ord('A'))


class AlphabetCipher:
    def __init__(self, keyphrase):
        """ Do initial setup with keyphrase and anything
        else needed to encode / decode. """
        self.key = normalize(keyphrase)

    def __oper(self, func, text):
        """Apply a function that takes a letter and a key letter to a message"""
        repeat_key = self.key * (len(text) // len(self.key) + 1)
        couples = zip(normalize(text), repeat_key)
        return str.join('', (func(*t) for t in couples))

    def encode(self, plaintext):
        """Encode the plaintext into ciphertext. """
        return self.__oper(tabula_recta, plaintext)

    def decode(self, ciphertext):
        """Decode the ciphertext back into a plaintext message."""
        return self.__oper(tabula_versa, ciphertext)
