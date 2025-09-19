
nums = [-3, 4, -2, 0, 5]
positive_nums = [n for n in nums if n > 0]
print("Positive numbers:", positive_nums
squares = [n**2 for n in nums]
print("Squares:", squares)


word = "education"
vowels = [ch for ch in word if ch in 'aeiouAEIOU']
print("Vowels:", vowels)


ordinals = [ord(ch) for ch in word]
print("Ordinal values:", ordinals)
