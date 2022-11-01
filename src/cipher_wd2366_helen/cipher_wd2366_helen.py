def cipher(text, shift, encrypt=True):

    """
    The Caesar cipher is one of the simplest and most widely known encryption techniques. In short, each letter is replaced by a letter some fixed number of positions down the alphabet. Apparently, Julius Caesar used it in his private correspondence.
        
    Parameters
    ----------
    text : ordinary text (string)
    shift : the number of shifts in the alphabet (integer)
    encrypt : choose encryption or decryption (boolean) 
        
    Returns
    -------
    text after encryption or decryption
       
    Examples
    --------
    >>> text = "helen"
    >>> cipher(text = text, shift = 1, encrypt=True)
    ''ifmfo"
   """

    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text