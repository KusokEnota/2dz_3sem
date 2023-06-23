""""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions"""

from fractions import Fraction

drob_a = '1/2'
drob_b = '1/3'

def slozhenie(drob_1, drob_2):
    result = Fraction(drob_1) + Fraction(drob_2)
    return str(result)

def mult(drob_1, drob_2):
    result = Fraction(drob_1) * Fraction(drob_2)
    return str(result)

print(slozhenie(drob_a, drob_b))
print(mult(drob_a, drob_b))

