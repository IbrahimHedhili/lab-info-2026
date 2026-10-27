from math import gcd
class Fraction :
    def __init__ (self, numerator, denominator) :
        if denominator == 0 :
          raise ValueError ('Denominator cannot be zero')
        if type(numerator) != int:
          raise TypeError ('Numerator must be an integer')
        if not isinstance(denominator, int ):
          raise TypeError ('Denominator must be an integer')
        
        common_divisor = gcd (numerator, denominator) 
        self.numerator = numerator // common_divisor
        self.denominator = int(denominator / common_divisor) 

    def print (self) :
        print (str (self.numerator) + '/' + str (self.denominator))

    def returnString (self) :
        return str (self.numerator) + '/' + str (self.denominator)

    def __add__ (self, other) :
        '''
        implements the addition of two fractions.
        This function will be callable with the + symbol
        '''
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction (new_numerator, new_denominator)
    
    def __sub__ (self, other) : 
        '''
        implements the subtractio of two fractions.
        This function will be callable with the - symbol
        '''
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return Fraction (new_numerator, new_denominator)
    
    def __mul__ (self, other) :
        '''
        implements the multiplation of two fractions.
        This function will be callable with the * symbol
        '''
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return Fraction (new_numerator, new_denominator)
    
    def __truediv__ (self, other) :
        '''
        implements the division of two fractions.
        This function will be callable with the / symbol
        '''
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return Fraction (new_numerator, new_denominator)

def verify_Fraction(fraction):
    if type(fraction) != Fraction:
        raise TypeError('fraction must be of type Fraction')
    fraction.print()

def verify_Fraction_operations(fraction1, fraction2):
    verify_Fraction(fraction1)
    verify_Fraction(fraction2)
    add_fraction = fraction1 + fraction2
    sub_fraction = fraction1 - fraction2
    mul_fraction = fraction1 * fraction2
    truediv_fraction = fraction1 / fraction2
    print(fraction1.returnString() + " + " + fraction2.returnString() + " = " + add_fraction.returnString())
    print(fraction1.returnString() + " - " + fraction2.returnString() + " = " + sub_fraction.returnString())
    print(fraction1.returnString() + " * " + fraction2.returnString() + " = " + mul_fraction.returnString())
    print(fraction1.returnString() + " / " + fraction2.returnString() + " = " + truediv_fraction.returnString())
    


    
    
