def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
# Using our generator
for number in count_up_to(5):
    print(number)