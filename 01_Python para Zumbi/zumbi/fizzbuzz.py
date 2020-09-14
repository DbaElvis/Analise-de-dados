# Coding Dojo do Curso Python para Zumbis
# -*- coding: cp1252 -*-
'''
FizzBuzz
Neste problema, você deverá exibir uma lista de 1 a 100,
um em cada linha, com as seguintes exceções:
Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
'''
def teste(obtido, esperado):
  if obtido == esperado:
    prefixo = ' Passou!'
  else:
    prefixo = ' Erro...'
  print ('%s obtido: %s esperado: %s' % (prefixo, repr(obtido), repr(esperado)))

def fizzbuzz(n):
  if n % 3 == 0 and n % 5 == 0:
    return 'fizzbuzz'
  if n % 3 == 0:
    return 'fizz'
  if n % 5 == 0:
    return 'buzz'
  return n

def main():
  teste(fizzbuzz(1), 1)
  teste(fizzbuzz(2), 2)
  teste(fizzbuzz(3), 'fizz')
  teste(fizzbuzz(4), 4)
  teste(fizzbuzz(5), 'buzz')
  teste(fizzbuzz(15), 'fizzbuzz')
  teste(fizzbuzz(30), 'fizzbuzz')
  teste(fizzbuzz(148), 148)

if __name__ == '__main__':
  main()
