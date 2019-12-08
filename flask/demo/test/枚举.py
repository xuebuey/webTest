from enum import Enum

class VIP(Enum):
    YELLOW = 0
    GREEN = 1
    BLACK = 2
    RED = 3

print(VIP.BLACK)
print(type(VIP.BLACK))
print(VIP.BLACK.name)
print(type(VIP.BLACK.name))
print(VIP.BLACK.value)

for v in VIP:
    print(v)