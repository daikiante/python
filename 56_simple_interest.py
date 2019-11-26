# 単利計算
# 元本*金利*運用期間 = 単利


def simple_interest(p, t, r):
    return p * (r / 100) * t


p = int(input('Enter the amount (/Rs):'))
t = int(input('Enter the hold span (/Year):'))
r = int(input('Enter the interest (/%):'))


print(simple_interest(p,t,r))