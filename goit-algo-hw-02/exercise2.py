from collections import deque

def is_palindrome(text):
    processed_text = text.lower().replace(" ", "")
    char_deque = deque(processed_text)
    
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True


print("Починаємо перевірку...")

test_strings = [
    "А роза упала на лапу Азора", 
    "Козак з казок", 
    "Привіт світ", 
    "Madam I am Adam", 
    "Hey_12321_yeh",
    "12321"
]

for s in test_strings:
    if is_palindrome(s):
        print(f"✅ '{s}' - це ПАЛІНДРОМ")
    else:
        print(f"❌ '{s}' - це НЕ паліндром")

print("Перевірку завершено.")