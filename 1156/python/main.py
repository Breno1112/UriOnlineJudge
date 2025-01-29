# Initialize sum S
S = 1

# Loop to calculate the sum from the second term to the last term
for i in range(1, 20):  # There are 20 terms in total (odd numbers from 1 to 39)
    numerator = 2*i + 1       # Generate even numbers: 2, 4, 6, ..., 38
    denominator = 2 ** i
    to_add = numerator / denominator
    S += (to_add)  # Add each fraction to the sum

# Print the final result
print('{:.2f}'.format(round(S, 2)))
