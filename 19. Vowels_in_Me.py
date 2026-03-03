#Magpii Coding Qn
def count_vowels(word):
    vowels = "aeiou"
    return sum(1 for ch in word.lower() if ch in vowels)

print("python:", count_vowels("python"))
print("js:", count_vowels("js"))
