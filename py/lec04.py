import numpy as np


# * ========== Numpy Array ==========
baseline_high = 14.48
highs = np.array(
    [
        baseline_high - 0.880,  # 1850
        baseline_high - 0.093,  # 1900
        baseline_high + 0.105,  # 1950
        baseline_high + 0.684,  # 2000
    ]
)

print("Highs = ", highs)

average_high = np.sum(highs) / len(highs)
print("Average high = ", average_high)

average_high_np = np.mean(highs)
print("Average high (using np.mean) = ", average_high_np)

highs_fahrenheit = 9 / 5 * highs + 32
print("Highs in Fahrenheit = ", highs_fahrenheit)

average_high_fahrenheit = np.mean(highs_fahrenheit)
print("Average high in Fahrenheit = ", average_high_fahrenheit)

highs_diff = np.diff(highs)
print("Highs differences = ", highs_diff)

# * NumPy Arrays have their own methods and properties
# * Invoke properties and methods of NumPy Arrays
print("Number of highs:                 ", highs.size)
print("Shape of highs array:            ", highs.shape)
print("Sum of highs:                    ", highs.sum())
print("Mean of highs:                   ", highs.mean())
print("Max high:                        ", highs.max())
print("Min high:                        ", highs.min())
print("Standard deviation of highs:     ", highs.std())
print("Variance of highs:               ", highs.var())

# * Or use NumPy functions
print("Number of highs:                 ", np.size(highs))
print("Shape of highs array:            ", np.shape(highs))
print("Sum of highs:                    ", np.sum(highs))
print("Mean of highs:                   ", np.mean(highs))
print("Max high:                        ", np.max(highs))
print("Min high:                        ", np.min(highs))
print("Standard deviation of highs:     ", np.std(highs))
print("Variance of highs:               ", np.var(highs))

# ! btw, if you use a script editor like VS Code, or IDE like PyCharm,
# ! you can find the difference between methods and functions in the editor hints:
# ! when you invoke a method, like `highs.mean()`, you will see the `method` signature.
# ! when you invoke a function, like `np.mean(highs)`, you will see the `function` signature.
# ! methods are associated with the object (array) they belong to,
# ! while functions are standalone and take the object as an argument.

# * some other useful NumPy functions

# Each of below functions takes an array as an argument and returns a single value.
print("Product of all elements together:    ", np.prod(highs))
print("Sum of all elements together:        ", np.sum(highs))
print("Mean of all elements together:       ", np.mean(highs))
print("Median of all elements together:     ", np.median(highs))
print("Standard deviation:                  ", np.std(highs))
print("Variance:                            ", np.var(highs))
print("Maximum value:                       ", np.max(highs))
print("Minimum value:                       ", np.min(highs))
print("Index of maximum value:              ", np.argmax(highs))
print("Index of minimum value:              ", np.argmin(highs))
print("All elements are true?               ", np.all(highs > 0))
print("Any element is true?                 ", np.any(highs > 0))
print("Counting non-zero elements:          ", np.count_nonzero(highs))
print("\n")

# Each of below functions takes an array as an argument and returns an array of values.
print("Differences between adjacent elements: ", np.diff(highs))
print("Cumulative sum of elements:            ", np.cumsum(highs))
print("Cumulative product of elements:        ", np.cumprod(highs))
print("Exponential of all elements:           ", np.exp(highs))
print("Natural logarithm of all elements:     ", np.log(highs))
print("Square root of all elements:           ", np.sqrt(highs))
print("Rounded to nearest integer:            ", np.rint(highs))
print("Rounded to 1 decimal place:            ", np.round(highs, 1))
print("Sorted array:                          ", np.sort(highs))
print("Indices that would sort the array:     ", np.argsort(highs))
print("Unique elements of the array:          ", np.unique(highs))
print("\n")

# Each of below functions takes an array of strings and returns an array.
strs = np.array(["apple", "banana", "cherry", "date", "elderberry"])
print("Original array of strings:   ", strs)
print("Lowercase:                   ", np.char.lower(strs))
print("Uppercase:                   ", np.char.upper(strs))
print("Capitalized:                 ", np.char.capitalize(strs))
print("Stripped:                    ", np.char.strip(strs))  # strip whitespace
print("Stripped:                    ", np.char.strip(strs, "ae"))  # strip 'a' and 'e'
print("Concatenated with '-fruit':  ", np.char.add(strs, "-fruit"))
print("Joined with ', ':            ", np.char.join(", ", strs))
print("Split by 'a':                ", np.char.split(strs, "a"))
print("Length of each string:       ", np.char.str_len(strs))
print("Replace 'a' with '@':        ", np.char.replace(strs, "a", "@"))
print("Contains 'e':                ", np.char.find(strs, "e"))  # returns index or -1
print("Count of 'e':                ", np.char.count(strs, "e"))
print("is alphanumeric:             ", np.char.isalnum(strs))
print("is alphabetic:               ", np.char.isalpha(strs))
print("is numeric:                  ", np.char.isnumeric(strs))
print("is lower:                    ", np.char.islower(strs))
print("is upper:                    ", np.char.isupper(strs))
print("is title:                    ", np.char.istitle(strs))
print("is whitespace:               ", np.char.isspace(strs))
print("\n")

# Each of below functions takes both an array of strings and a search string; each returns an array.
print("Count of 'e':        ", np.char.count(strs, "e"))
print("Find 'e' from start: ", np.char.find(strs, "e"))
print("Find 'e' from end:   ", np.char.rfind(strs, "e"))
print("Starts with 'b':     ", np.char.startswith(strs, "b"))
print("Ends with 'y':       ", np.char.endswith(strs, "y"))
print("\n")

# * ========== Range (about np.arange)==========

# ! Ranges are defined using the `np.arange` function,
# ! which takes either one, two, or three arguments:
# ! a start, and end, and a 'step'.

# 3 ways to call `np.arange`:
range1 = np.arange(5)  # 0, 1, 2, 3, 4
range2 = np.arange(2, 5)  # 2, 3, 4
range3 = np.arange(2, 10, 2)  # 2, 4, 6, 8
range4 = np.arange(1.5, -1, -0.5)  # 1.5, 1, 0.5, 0, -0.5
print("Range with 1 argument (end=5): ", range1)
print("Range with 2 arguments (start=2,end=5): ", range2)
print("Range with 3 arguments (start=2,end=10,step=2): ", range3)
print("Range with 4 arguments (start=1.5,end=-1,step=-0.5): ", range4)
print("\n")

# * ========== Example: Leibniz’s formula for π ==========
positive_term_denominators = np.arange(1, 1_000_000, 4)
negative_term_denominators = positive_term_denominators + 2

positive_terms = 1 / positive_term_denominators
negative_terms = 1 / negative_term_denominators

fraction_sum = positive_terms.sum() - negative_terms.sum()
# fraction_sum = np.sum(positive_terms) - np.sum(negative_terms)

Leibniz_pi = fraction_sum * 4
print("Approximation of π using Leibniz’s formula with 1 million terms: ", Leibniz_pi)
print("\n")

# * ========== More on NumPy Array ==========

baseline_low = 3.00
lows = np.array(
    [
        baseline_low - 0.872,  # 1850
        baseline_low - 0.629,  # 1900
        baseline_low - 0.126,  # 1950
        baseline_low - 0.728,  # 2000
    ]
)

temperature_range = highs - lows
print("Highs = ", highs)
print("Lows = ", lows)
print("Temperature ranges = ", temperature_range)
print("\n")

# * ========== Example: Wallis’ Formula for π ==========
even = np.arange(2, 1_000_001, 2)
one_below_even = even - 1
one_above_even = even + 1

wallis_terms = (even / one_below_even) * (even / one_above_even)
wallis_pi = wallis_terms.prod() * 2
# wallis_pi = np.prod(wallis_product) * 2
print("Approximation of π using Wallis’ formula with 1 million terms: ", wallis_pi)
print("\n")
