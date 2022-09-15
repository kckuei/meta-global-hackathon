# Objective:
# Want to maximize the amount of fun from visiting scary rollercoasters

# Subject to Constraints:
# 1. A valid sequence abides by the rules...
#   a. rollercoasters must immediately follow one another
#   b. scariness of ith-1 coaster must be less than ith coaster
# 2. Add 10 units of fun per rollercoaster visisted

# Input
# File of integers on each line representing scariness of a rollercoaster

# Output
# File with integer value expressing total/maximized units of fun

# Pseudocode
# we basically want to get the maximum possible length of sequences of
# consecutively increasing numbers, then multiply that by 2

def load_nums(path):
    with open(path) as f:
        lines = f.readlines()
        nums = [int(line.rstrip()) for line in lines]
    return nums


def write_fun(path, fun):
    with open(path, 'w') as f:
        f.write(str(fun))


def maximum_length(nums):
    max_length = 0
    length = 1
    for i, _ in enumerate(nums[:-2]):
        if nums[i-1] > nums[i]:
            length += 1
        else:
            length = 1
        max_length = max([length, max_length])
    return max_length


def maximum_fun(length):
    return 10 * length


# scary_nums = load_nums('rollercoasters_medium_sample_input.txt')
scary_nums = load_nums('rollercoasters_medium_input.txt')
length = maximum_length(scary_nums)
fun = maximum_fun(length)
write_fun('./rollercoasters_medium_output.txt', fun)

print(f"Max length: {length}")
print(f"Max fun: {fun}")
