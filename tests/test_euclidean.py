from python.euclidean import gcd
assert gcd(48, 12)[0] == 12
assert gcd(17, 13)[0] == 1
assert gcd(100, 25)[0] == 25
assert gcd(0, 5)[0] == 5
assert gcd(48, 0)[0] == 48
assert gcd(-24, 18)[0] == 6
assert gcd(12, 4)[0] == 4
assert gcd(48, 12)[1] == 1
assert gcd(17, 13)[1] == 3
assert gcd(100, 25)[1] == 1
assert gcd(0, 5)[1] == 1
assert gcd(48, 0)[1] == 0
print("All test cases passed!")