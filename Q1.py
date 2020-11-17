def tld(inputs):
    return inputs.split('.')[-1]
inputs = []
input1 = input("Enter an URL ")
while input1 != "":
	inputs.append(input1)
	input1 = input("Enter an URL ")
print(inputs)
output=sorted(inputs, key=tld)
print("sorted list is: ")
print(output)