"""
prints the first twenty words of the Fibonacci sequence. The sequence is defined as follows: the first term is equal
 to 0, the second is equal to 1, each subsequent term is the sum of the previous two.
"""

penult_term = 0
last_term = 1

terms_cnt = 2

print(f'{penult_term} {last_term}', end=' ')

while terms_cnt <= 20:
    new_term = penult_term + last_term
    print(new_term, end=' ')

    penult_term = last_term
    last_term = new_term

    terms_cnt += 1
