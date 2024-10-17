class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        if denominator != 0:
            self.denominator = denominator
        else:
            raise ValueError("Error: Denominator cannot be Zero")

    def add(self, other):
        self.other = other
        first_new_numerator = self.numerator * other.denominator
        second_new_numerator = other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        numerator = first_new_numerator + second_new_numerator
        return Fraction(numerator, denominator)


    def subtract(self, other):
        first_new_numerator = self.numerator * other.denominator
        second_new_numerator = other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        numerator = first_new_numerator - second_new_numerator
        return Fraction(numerator, denominator)
    
    def multiply(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    
    def divide(self, other):
        if other.numerator == 0:
            raise ValueError("Error: Connot Divide by Zero")
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)
    
    def simplify(self):
        high_common_factor = 1
        for i in range(1, min(self.numerator, self.denominator) + 1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                high_common_factor = i
                
        numerator = self.numerator/high_common_factor
        denominator = self.denominator/high_common_factor

        return Fraction(int(numerator), int(denominator))


    def __str__(self):
        return f'{self.numerator}/{self.denominator}'



# Test your implementation
fraction1 = Fraction(1, 4)
fraction2 = Fraction(1, 2)

fraction3 = fraction1.add(fraction2)
print(fraction3)  # Should output "6/8"

fraction4 = fraction3.simplify()
print(fraction4)  # Should output "3/4"
