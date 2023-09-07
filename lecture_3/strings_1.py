# new_name: str = input('type name:')

# greet_message: str = "hello bob"
# # greet_message: str = (
# #     greet_message[:-3] + new_name
# # )

# greet_message: str = \
#     greet_message.replace('bob',new_name) (replace перезначает переменную и возвращает копию измененной)
# print(greet_message)

# _____________________

# river: str = 'mmississippi'

# print(
#     'm' + river.lstrip('misp') # удаляют все буквы до запятой слева
# )

# river: str = 'mmississippi'

# print(
#     'm' + river.rstrip('p') # удаляют все буквы до запятой справа
# )

# words: str = '<!---dsa das das---!>'

# print(
#     words.strip('<!>-').split() #удаляет сначала лишние символы потом делит на слова
# )



import string # импорт тех которые в питоне, потом которые установили и
numbers: str = string.digits

word: str = 'hello12o b32ob ho312w ar3e y231ou'

# for number in numbers:
#     word = word.replace(numbers,'')  
# _______

_word: str = ''

for ch in word:
    if ch in word:
        continue
    else:
        _word += ch

word = _word 

del _word

print(
    word = word.replace(numbers,'')
)