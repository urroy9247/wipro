fruits_list = ["mango","banana","apple","guava","pomogranete"]
newfruits = [ i  for i in fruits_list if 4 <= len(i) <= 5]
print(newfruits)