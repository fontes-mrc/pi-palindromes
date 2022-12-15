def _n_first_primes(n: int) -> list[int]:
    """Return the first n primes."""
    primes = []
    x = 2
    while len(primes) < n:
        for i in range(2, x//2 +1):
            if x % i == 0:
                break
        else:
            primes.append(x)
        x += 1
    return primes

def _is_composite(n: int, base: int, s:int, t:int) -> bool:
    """Return True if n is composite, False otherwise."""
    if pow(base, t, n) == 1:
        return False
    for i in range(s):
        if pow(base, 2**i * t, n) == n-1:
            return False
    return True

def _miller_rabin_test(n: int, bases: list[int]) -> bool:
    t = n - 1
    s = 0
    while not t % 2:
        t >>= 1
        s += 1

    for base in bases:
        if base >= n:
            base %= n
        if _is_composite(n, base, s, t):
            return False
    return True

def isprime(n:int, large_precision: int=24) -> bool:
    """Return True if n is prime, False otherwise."""
    if n in [2, 3, 5]:
        return True
    
    if n < 2 or (n % 2) == 0 or (n % 3) == 0 or (n % 5) == 0:
        return False
    
    if n < 49:
        return True
    
    if (n %  7) == 0 or (n % 11) == 0 or (n % 13) == 0 or (n % 17) == 0 or \
       (n % 19) == 0 or (n % 23) == 0 or (n % 29) == 0 or (n % 31) == 0 or \
       (n % 37) == 0 or (n % 41) == 0 or (n % 43) == 0 or (n % 47) == 0:
        return False
    
    if n < 2809:
        return True
    
    if n < 31417:
        return pow(2, n, n) == 2 and n not in [7957, 8321, 13747, 18721, 19951, 23377]
    
    # lists for miller-rabin test:
    # https://miller-rabin.appspot.com/
    # https://arxiv.org/pdf/1509.00864.pdf
    # https://oeis.org/A014233
    
    if n < 341531:
        return _miller_rabin_test(n, [9345883071009581737])
    if n < 885594169:
        return _miller_rabin_test(n, [725270293939359937, 3569819667048198375])
    if n < 350269456337:
        return _miller_rabin_test(n, [4230279247111683200, 14694767155120705706, 16641139526367750375])
    if n < 55245642489451:
        return _miller_rabin_test(n, [2, 141889084524735, 1199124725622454117, 11096072698276303650])
    if n < 7999252175582851:
        return _miller_rabin_test(n, [2, 4130806001517, 149795463772692060, 186635894390467037, 3967304179347715805])
    if n < 585226005592931977:
        return _miller_rabin_test(n, [2, 123635709730000, 9233062284813009, 43835965440333360, 761179012939631437, 1263739024124850375])
    if n < 18446744073709551616:
        return _miller_rabin_test(n, [2, 325, 9375, 28178, 450775, 9780504, 1795265022])
    if n < 318665857834031151167461:
        return _miller_rabin_test(n, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37])
    if n < 3317044064679887385961981:
        return _miller_rabin_test(n, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41])
    
    return _miller_rabin_test(n, _n_first_primes(large_precision))