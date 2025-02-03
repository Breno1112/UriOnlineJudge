test_cases_count = int(input())

while test_cases_count > 0:

    nums = input().split(" ")
    pa = int(nums[0])
    pb = int(nums[1])
    ga = float(nums[2])
    gb = float(nums[3])

    years = 0
    while pa <= pb and years <= 100:
        pa = int(pa * ((ga / 100) + 1))
        pb = int(pb * ((gb / 100) + 1))
        years += 1
    if years > 100:
        print("Mais de 1 seculo.")
    else:
        print(f"{years} anos.")
    test_cases_count -= 1