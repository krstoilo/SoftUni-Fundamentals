import re

pattern = r'((-?\d+)(\.\d+)?)'
string_g = "M3ph-0.5s-0.5t0.0**"

nums = re.findall(pattern, string_g)
print(nums)
new_nums = []
for n in range(len(nums)):
    new_nums.append(nums[n][0])
print(new_nums)