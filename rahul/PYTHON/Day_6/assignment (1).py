class AgeError(Exception):
    pass
def check_age(x):
    if x <= 0:
        raise AgeError("Age can not be negative")
 

try:
    check_age(-1)
except AgeError as e:
    print("Age Error:",e)