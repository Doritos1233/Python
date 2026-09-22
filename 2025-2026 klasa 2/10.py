def compress(text):
    if not text:
        return "nie ma zadnego tekstu."
    
    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i-1]:
            count += 1
        else:
            result += text[i-1] + str(count)
            count = 1
    
    result += text[-1] + str(count)
    return result


user_input = input("Wpisz tekst do kompresji: ")


compressed_text = compress(user_input)

print("=" * 30)
print(f"Oryginał: {user_input}")
print(f"Skompresowany: {compressed_text}")

