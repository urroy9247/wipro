class InvalidProdCode(Exception):

      pass

def order_prod(x):

    if x <= 0 :

        raise InvalidProdCode("Prod code can not be negative ")

try:

    order_prod(-5)

except InvalidProdCode  as e:

    print(e)

 