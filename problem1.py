"""
MULTIPLES OF 3 or 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

COMPLETED, answer = 233168
"""

def multiple_sum(divisor: int, limit: int, found_divs: set) -> int:
    ret_sum = 0
    for i in range(divisor, limit, divisor):
        if i in found_divs:
            continue
        ret_sum += i
        found_divs.add(i)
    return ret_sum, found_divs

if __name__=='__main__':
    checked_divisors = set()
    mult1_sum, checked_divisors = multiple_sum(5, 1000, checked_divisors)
    mult2_sum, checked_divisors = multiple_sum(3, 1000, checked_divisors)
    sum_of_multiples = mult1_sum + mult2_sum
    print(sum_of_multiples)