# 5) Escreva um programa que inverta os caracteres de um string.

def revert_string( s: str ) -> str:
    
    reverted: str = ''

    len_str = len( s )

    for i in range( len_str ):
        reverted += s[ len_str - i - 1 ]

    return reverted

print( revert_string("Target") )