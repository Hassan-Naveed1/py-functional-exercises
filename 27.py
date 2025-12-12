#27.	Filter out duplicate values using filter().
nums = [10,20,20,10,30,40,50,50,40,30]
final_list = []

seen = set()
for n in nums:
    if n not in seen:
        seen.add(n)
        final_list.append(n)

print(final_list)

no_duplicate = filter(lambda x : not ( x in seen or seen.add(x)),nums)
print(final_list)