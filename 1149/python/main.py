nums = input().split(" ")

current_num_to_sum = int(nums[0])

last_num = None

idx = 1

sum = 0

while idx < len(nums) and (last_num is None or last_num <= 0):
    last_num = int(nums[idx])
    idx += 1

while last_num > 0:
    sum += current_num_to_sum
    current_num_to_sum += 1
    last_num -= 1
print(sum)