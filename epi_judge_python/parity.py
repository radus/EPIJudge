from test_framework import generic_test

def simple_parity(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1 
        x >>= 1
    return result

cache = [simple_parity(i) for i in range(65536)]
    
def parity(x: int) -> int:
    result = 0
    while x:
        last_bits = x & 0xFFFF
        result ^= cache[last_bits]
        x >>=  16
    return result

if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
