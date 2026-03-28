def count_vowels_consonants(sentence: str):
    vowels = "аеёиоуыэюя"
    consonants = "бвгджзйклмнпрстфхцчшщ"

    sentence = sentence.lower()

    vowel_count = 0
    consonant_count = 0

    for _ in sentence:
        if _ in vowels:
            vowel_count += 1
        elif _ in consonants:
            consonant_count += 1

    print(f"Количество гласных: {vowel_count}")
    print(f"Количество согласных: {consonant_count}")

count_vowels_consonants("Протестим - эту программу")