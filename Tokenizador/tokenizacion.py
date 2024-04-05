from typing import NamedTuple
import re

line_num = 1

def tokenize(code):
    keywords  = {'for','if', 'else', 'while', 'def', 'return'}

    token_specification  = [
        ('comentario', r'//[^\n]*'),                          # comentario
        ('identificador', r'[a-zA-Z_]+[a-zA-Z\d\w]*'),        # Identificador
        ('real', r'[+-]?\d+(\.\d+)?[Ee][+-]?\d+'),            # Real (notación científica)
        ('flotante', r'[+-]?\d+\.\d+'),                       # Flotante
        ('entero', r'[+-]?\d+'),                              # Entero
        ('suma', r'\+'),                                      # Suma
        ('resta', r'-'),                                      # Resta
        ('multiplicación', r'\*'),                            # Multiplicación
        ('division', r'/'),                                   # División
        ('potencia', r'\^'),                                  # Potencia     
        ('menor_igual', r'<='),                               # Menor o igual que
        ('mayor_igual', r'>='),                               # Mayor o igual que        
        ('diferente', r'!='),                                 # Diferente de
        ('menor_que', r'<'),                                  # Menor que
        ('mayor_que', r'>'),                                  # Mayor que        
        ('asignacion', r'='),                                 # Asignación   
        ('cadena', r'"[^"]*"'),                               # Cadena
        ('a_parentesis', r'\('),                              # Paréntesis de apertura
        ('c_parentesis', r'\)'),                              # Paréntesis de cierre
        ('a_corchete', r'{'),                                 # Llave de apertura
        ('c_corchete', r'}'),                                 # Llave de cierre
        ('a_corchete_box', r'\['),                            # Corchete de apertura
        ('c_corchete_box', r'\]') ,                           # Corchete de cierre
        ('newline',  r'\n'),                                  # Salto de linea
        ('skip',     r'[ \t]+'),                              # tabulaciones etc 
        ('mismatch', r'.'),                                   # cualquier otro caracter
        
    ]

    
     
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)

    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group()
        if kind == 'identificador' and value in keywords:
            kind = "reservada"
        elif kind == 'skip' or  kind == 'newline':
            continue
        elif kind == 'mismatch':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        yield kind


print_text = []    
print_tokens = []
with open('code.txt', 'r') as archivo:
        for line in archivo:            
            tokens = tokenize(line)
            print_tokens = []        
            for token in tokens:
                if token != "":
                    print_tokens.append(token)
            if print_tokens != []:
                print_text.append(print_tokens)
            line_num += 1


for line in print_text:
   print( line)   
      