import random
#you can change which letters, numbers, and symbols you dont want to display or you want to be added
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()_+{}][\/.,;:"

Use_for = lower_case + upper_case + number + symbols
#Length for pass is how long you want the password to be 
length_for_pass = 18

password = "".join(random.sample(Use_for, length_for_pass))
print("Your Randomly Generated Password Is:" + password)