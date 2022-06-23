import random
#you can change which letters, numbers, and symbols you dont want to display or you want to be added
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbols = "!@#$%^&*()_+{}][\/.,;:"
Use_for = lower_case + upper_case + number + symbols
usefor = str(Use_for)
#Length for pass is how long you want the password to be 
length_for_pass = input("How long do you want the password to be? (Be sure to incude only numbers and stay within the 84 character limit) ")
lengthforpass = int(length_for_pass)
password = "".join(random.sample(usefor, lengthforpass))
passy = str(password)
print("Your Randomly Generated Password Is :" + passy)
