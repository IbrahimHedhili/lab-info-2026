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

def main():
    fract = Fraction(2,3)
    fract.print()
    print("Ibra")
    print(Fraction.__init__.__name__)
if __name__ == "__main__":
    main()