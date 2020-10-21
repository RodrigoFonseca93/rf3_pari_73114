#!/usr/bin/env python

#### Ex3 ####

from collections import namedtuple

Complex = namedtuple('Complex', ['r', 'i'])

def addComplex(x,y):
    x_r, x_i = x[0], x[1]
    y_r, y_i = y[0], y[1]

    ## x_r = x['r']
    ## x_i = x['i']

    z_r = x_r + y_r
    z_i = x_i + y_i

    return Complex(z_r, z_i)

def multiplyComplex(x, y):
    x_r, x_i = x[0], x[1]
    y_r, y_i = y[0], y[1]

    z_r = x_r * y_r - x_i * y_i
    z_i = x_r * y_i - x_i * y_r

    return Complex(z_r, z_i)

def printComplex(x):
    print('(' + str(x[0]) +', ' + str(x[1]) + 'i)')

def main():

    # define two complex numbers as tuples of size two
    c1 = Complex(5, 3)
    c2 = Complex(r=-2, i=7)

    # Test add
    c3 = addComplex(c1, c2)
    printComplex(c3)

    # test multiply
    printComplex(multiplyComplex(c1, c2))

if __name__ == '__main__':
    main()