nums = (1,2,3,4,5,6,7,8)

print("original nums ",nums)

result = map(lambda x: x+x+x,nums)
print("\n triple the number is :")
print(list(result))