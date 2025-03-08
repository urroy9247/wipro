'''Common pdb commands:
 
n (next): Execute the next line
s (step): Step into function calls
c (continue): Resume execution
q (quit): Exit the debugger
'''
import pdb
rah = 10
def test():
    x = 10
    y = 20
    pdb.set_trace()  # Start debugger 
    result = x + y
    print(result)

test()