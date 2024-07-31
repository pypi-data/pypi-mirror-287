#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This module provides functions for encoding and decoding text using DNAbits.

Functions:
- encode_string: Encodes a string using DNAbits.
- decode_string: Decodes a string encoded with DNAbits.
- encode_list: Encodes all strings in a list using DNAbits.
- decode_list: Decodes all strings in a list encoded with DNAbits.
- str_to_bin: Converts a string to a binary representation.
- bin_to_str: Converts a binary representation to a string.

Author: Diogo de J. S. Machado
Date: 30/07/2024
"""

def encode_string(input_string):
    """
    Encodes a string with DNAbits.

    Parameters
    ----------
    input_string : string
        Natural language text string to be encoded.

    Returns
    -------
    encoded_string : string
        Encoded text.

    Example
    -------
    Encode a string.

    >>> input_string = "Hello world!"
    >>> encoded_string = encode_string(input_string)
    >>> print(encoded_string)
    AGACCCGCATGCATGCTTGCAAGATCTCTTGCGATCATGCACGCCAGA
    """
    
    input_string = str_to_bin(input_string)
    
    # Split the binary string into two parts
    text_0 = input_string[0::2]
    text_1 = input_string[1::2]
    
    # Convert binary pairs to DNA characters
    binary_pairs = zip(text_0, text_1)
    dna_chars = {'00': 'A', '01': 'G', '10': 'C', '11': 'T'}
    encoded_string = ''.join(dna_chars[b0 + b1] for b0, b1 in binary_pairs)
    
    return encoded_string

def decode_string(input_string):
    """
    Decodes a string with DNAbits reverse.

    Parameters
    ----------
    input_string : string
        Text string encoded with DNAbits.

    Returns
    -------
    decoded_string : string
        Decoded text.

    Example
    -------
    Decode a string.

    >>> encoded_string = "AGACCCGCATGCATGCTTGCAAGATCTCTTGCGATCATGCACGCCAGA"
    >>> decoded_string = decode_string(encoded_string)
    >>> print(decoded_string)
    Hello world!
    """
    
    # Define the DNA to binary mapping
    dna_to_bin = {'A': '00', 'G': '01', 'C': '10', 'T': '11'}
    
    # Convert DNA string to binary string
    binary_string = ''.join(dna_to_bin[char] for char in input_string)
    
    # Convert binary string to ASCII string
    decoded_string = ''.join(bin_to_str(binary_string[i:i+8])
                             for i in range(0, len(binary_string), 8))
    
    return decoded_string

def encode_list(string_list, verbose=False):
    """
    Encodes all strings in a list with DNAbits.	
    
    Parameters
    ----------
    string_list : list
        List of string to be encoded.
    verbose  : bool
        If True displays progress.

    Returns
    -------
    encoded_list : list
        List with all encoded text in string format.
        
    Example
    -------
    Encode the strings in a list and view the result of the first item.

    >>> import biotext as bt
    >>> string_list = ['Hello','world','!']
    >>> encoded_list = bt.dnabits.encode_list(string_list)
    >>> print(encoded_list)
    ['AGACCCGCATGCATGCTTGC', 'TCTCTTGCGATCATGCACGC', 'CAGA']
    """
    
    list_size = len(string_list)
    selectedEncoder = lambda x: encode_string(x)

    encoded_list = []
    if verbose:
        print('Encoding text...')
    for c,i in enumerate(string_list):
        seq = selectedEncoder(i)
        encoded_list.append(seq)
        if verbose and (c+1) % 10000 == 0:
            print (str(c+1)+'/'+str(list_size))
    if verbose:
        print (str(list_size)+'/'+str(list_size))
    return encoded_list

def decode_list(input_list,output_file=None,verbose=False):
    """
    Decodes all strings in a list with reverse DNAbits.	
    
    Parameters
    ----------
    string_list : list
        List of string encoded with DNAbits.
    verbose  : bool
        If True displays progress.

    Returns
    -------
    decoded_list : list of string
        List with all decoded text.
        
    Example
    --------
    Decode the strings in a list and view the result with a loop.

    >>> import biotext as bt
    >>> encoded_list = ['AGACCCGCATGCATGCTTGC', 'TCTCTTGCGATCATGCACGC', 'CAGA']
    >>> decoded_list = bt.dnabits.decode_list(encoded_list)
    >>> print(decoded_list)
    ['Hello', 'world', '!']
    """
    
    list_size = len(input_list)
    selectedEncoder = lambda x: decode_string(x)
    
    decoded_list = []
    if verbose:
        print('Decoding text...')
    for c,i in enumerate(input_list):
        c+=1
        if verbose and (c+1) % 10000 == 0:
            print(str(c+1)+'/'+str(list_size))
        decoded_list.append((selectedEncoder(str(i))))
    if verbose:
        print(str(list_size)+'/'+str(list_size))
    
    return decoded_list

def str_to_bin(string):
    return ''.join(f'{ord(char):08b}'[::-1] for char in string)

def bin_to_str(string):
    res = ''
    for idx in range(int(len(string)/8)):
        cstr = string[idx*8:(idx+1)*8]
        cstr=cstr[::-1]
        tmp = chr(int(cstr, 2))
        res += tmp
    return res