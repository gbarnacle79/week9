name = names.get_full_name()
print(name)
if name[0] == 'A':
    prize = '£{}.random.randint(1,10)'
if name[0] == 'B':
    prize = '£{}.random.randint(2,20)'
if name[0] == 'C':
    prize = '£{}.random.randint(3,30)'
if name[0] == 'D':
    prize = '£{}.random.randint(4,40)'
if name[0] == 'E':
    prize = '£{}.random.randint(5,50)'
if name[0] == 'F':
    prize = '£{}.random.randint(6,60)'
if name[0] == 'G':
    prize = '£{}.random.randint(7,70)'
if name[0] == 'H':
    prize = '£{}.random.randint(8,80)'
if name[0] == 'I':
    prize = '£{}.random.randint(9,90)'
if name[0] == 'J':
    prize = '£{}.random.randint(10,100)'
if name[0] == 'K':
    prize = '£{}.random.randint(11,110)'
if name[0] == 'L':
    prize = '£{}.random.randint(12,120)'
if name[0] == 'M':
    prize = '£{}.random.randint(13,130)'
if name[0] == 'N':
    prize = '£{}.random.randint(14,140)'
if name[0] == 'O':
    prize = '£{}.random.randint(15,150)'
if name[0] == 'P':
    prize = '£{}.random.randint(16,160)'
if name[0] == 'Q':
    prize = '£{}.random.randint(17,170)'
if name[0] == 'R':
    prize = '£{}.random.randint(18,180)'
if name[0] == 'S':
    prize = '£{}.random.randint(19,190)'
if name[0] == 'T':
    prize = '£{}.random.randint(20,200)'
if name[0] == 'U':
    prize = '£{}.random.randint(21,210)'
if name[0] == 'V':
    prize = '£{}.random.randint(22,220)'
if name[0] == 'W':
    prize = '£{}.random.randint(23,230)'
if name[0] == 'X':
    prize = '£{}.random.randint(24,240)'
if name[0] == 'Y':
    prize = '£{}.random.randint(25,250)'
if name[0] == 'Z':
    prize = '£{}.random.randint(26,260)'

if prize < 50 and prize > 0:
    future = "Will lose it to an online scam"
if prize < 100 and prize > 50:
    future = "Will lose it investing on a 'Big Chungus' NFT"
if prize < 150 and prize > 100:
    future = "Will lose it behind the sofa"
if prize < 250 and prize > 200:
    future = "Will lose it gambling on a turtle race"
if prize > 250:
    future = "Will lose it by spending the money on a new laptop that breaks the next day (didn't pay for the warranty)" 


print(name, prize, future)