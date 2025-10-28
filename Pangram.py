def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(sentence.lower())

# Example
text = "The quick brown fox jumps over a lazy dog"
if is_pangram(text):
    print("✅ It's a pangram!")
else:
    print("❌ Not a pangram.")
