class IntegerToRoman:
    _value_map = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
        1: 'I'
    }

    def __init__(self, number):
        self.number = number

    def to_roman(self):
        result = ""
        num = self.number

        
        for value, roman in IntegerToRoman._value_map.items():
            while num >= value:
                result += roman
                num -= value

        return result


number = input("Enter a number u want to convert: ")
converter = IntegerToRoman(number)
roman_numeral = converter.to_roman()
print(f"{number} in Roman numerals is {roman_numeral}")
