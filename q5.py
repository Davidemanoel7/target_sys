# 5) Escreva um programa que inverta os caracteres de um string.

def revert_string( s: str ) -> str:
    
    reverted: str = ''

    len_str = len( s )

    for i in range( len_str ):
        reverted += s[ len_str - i - 1 ]

    return reverted

string_original = str( input( "Digite uma palavra para ser revertida: \n"))

print( revert_string( string_original ) )