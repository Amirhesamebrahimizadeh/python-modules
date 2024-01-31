import math
import random

three_digit_code = random.randint(100, 999)

print(f"3 digit code: {three_digit_code}")




digit_1 = str(random.randint(1, 6))
digit_2 = str(random.randint(1, 6))
digit_3 = str(random.randint(1, 6))
digit_4 = str(random.randint(1, 6))

four_digit_code = digit_1 + digit_2 + digit_3 + digit_4

print(f"4 digit code: {four_digit_code}")
