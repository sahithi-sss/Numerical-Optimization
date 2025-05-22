def convert_base_fractional(number_str:str, from_base:int, to_base:int, precision:int = 10) -> str:
    if not(2<= from_base <= 36 and 2<= to_base <= 36):
        raise ValueError("Base must be between 2 and 36")
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def to_decimal(number_str):
        if "." in number_str:
            int_part, frac_part = number_str.split(".")
        else:
            int_part, frac_part = number_str, ''
    
        int_value = int(int_part, from_base)
        frac_val = 0
        for i, digit in enumerate(frac_part):
            frac_val += digits.index(digit.upper()) / (from_base ** (i+1))

        return int_value + frac_val
    
    def from_decimal(decimal_number):
        int_part = int(decimal_number)
        frac_part = decimal_number - int_part

        # Convert integer part
        result = ""
        if int_part == 0:
            result = "0"
        
        while int_part > 0:
            result = digits[int_part % to_base] + result
            int_part //= to_base

        # Convert fractional part
        if frac_part > 0:
            result += "."
            for _ in range(precision):
                frac_part *= to_base
                digit = int(frac_part)
                result += digits[digit]
                frac_part -= digit
                if frac_part == 0:
                    break

        return result

    # Convert to decimal first, then to target base
    decimal_value = to_decimal(number_str)
    return from_decimal(decimal_value)

# Example usage
if __name__ == "__main__":
    # Example 1: Convert 101.101 from binary to decimal
    result1 = convert_base_fractional("101.101", 2, 10)
    print(f"101.101 (binary) = {result1} (decimal)")

    # Example 2: Convert 0.5 from decimal to binary
    result2 = convert_base_fractional("0.5", 10, 2)
    print(f"0.5 (decimal) = {result2} (binary)")

    # Example 3: Convert 1A.8 from hexadecimal to decimal
    result3 = convert_base_fractional("1A.8", 16, 10)
    print(f"1A.8 (hex) = {result3} (decimal)")