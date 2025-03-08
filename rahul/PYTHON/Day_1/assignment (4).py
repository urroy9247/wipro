nopos=0
noneg=0
while True:
   x=int(input("Enter value for x , To stop enter 0 "))
   if x==0:
      break               # break is used to exit from the loop

   if x < 0 :
      noneg=noneg+1

   if x > 0 :
      nopos=nopos+1

print("Total no of positive  nos  = " , nopos)
print("Total no of negative  nos  = ",  noneg)
