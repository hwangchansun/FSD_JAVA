name = "Tom"
balance = 12.4567

# 1: use the plus to concatenate the output
print(name+" has $" + str(balance))

# 2: print values next to each other
print(name + " has $", balance)

# 3: use formatting modes
print("%s has $%.2f"%(name, balance)) # 2 decimal points
print("%10s has $%15.2f"%(name, balance)) # 앞에 공백
print("%-10s has $%-15.2f"%(name, balance)) # 뒤에 공백

# 4: using the format function from string
print("{} has ${}".format(name, balance))
print("{:10} has ${:15.3f}".format(name, balance))
print("{:10} has ${:<15.3f}".format(name, balance))
print("{:10} has ${:0>15.3f}".format(name, balance)) # fill up with zero
print("{:*^10} has ${:0>15.3f}".format(name, balance))

# 5: using the f command
print(f'{name} has ${balance}')
print(f'{name} has ${balance:$^15.3f}') # add the dollar sign