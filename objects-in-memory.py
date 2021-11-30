# Setup
a = [1,2,3,4]
b = [1,2,3,4]

# ID function
# print(id(a))
# print(id(b))
# b = a
# print(id(a))
# print(id(b))

# is Operator
# comparison = a is b
# print(comparison) # -> False
# b = a
# comparison = a is b
# print(comparison) # -> True

# Unexpected results
# a = 15000
# b = 15000
# print(a is b)
#
# a = "H"
# b = "H"
# print(a is b)

# Pass by Reference
class Sale():
    def __init__(self, value):
        self.value = value

def print_data(seq):
    # print(id(seq))
    for elem in seq:
        print(elem)

def multiply_by_two(seq):
    for i in range(len(seq)):
        seq[i] *= 2

def find_total(sales):
    total = 0
    for sale in sales:
        total += sale.value
    return total

# print(id(a))
# print_data(a)
# multiply_by_two(a)
# print_data(a)

sales = [Sale(100), Sale(200), Sale(300)]
print(find_total(sales))


