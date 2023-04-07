#Euclidean Algorithm to get GCD, LCM
def gcd_calculator(A, B):
    if (B == 0):
        return A
    else:
        return gcd_calculator(B, A % B)

temp_A, temp_B = map(int, input().split())
A = max(temp_A, temp_B)
B = min(temp_A, temp_B)
gcd = gcd_calculator(A, B)
print(gcd)
print(int(A * B / gcd))