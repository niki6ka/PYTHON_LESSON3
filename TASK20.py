"""
*Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q, Z – 10 очков.
А русские буквы оцениваются так: А, В, Е, И, Н, О, Р, С, Т – 1 очко; ДКЛМПУ – 2 очка; БГЁЬЯ – 3 очка;
 ЙЫ – 4 очка; ЖЗХЦЧ – 5 очков; ШЭЮ – 8 очков; ФЩЪ – 10 очков. Напишите программу,
 которая вычисляет стоимость введенного пользователем слова.
"""
scrable_word = input("ENTER IN CAPITAL LETTERS THE WORD TO COUNT: ")

eng_dct = {
 1: 'AEIOULNSTR',
 2: 'DG',
 3: 'BCMP',
 4: 'FHVWY',
 5: 'K',
 8: 'JX',
10: 'QZ'
}
rus_dct = {
 1: 'АВЕИНОРСТ',
 2: 'ДКЛМПУ',
 3: 'БГЁЬЯ',
 4: 'ЙЫ',
 5: 'ЖЗХЦЧ',
 8: 'ШЭЮ',
10: 'ФЩЪ'
}
result = [key for letter in scrable_word for key, value in eng_dct.items() if letter in value]
result2 = [key for letter in scrable_word for key, value in rus_dct.items() if letter in value]
if result > result2:
    print(sum(result))
else:
    print(sum(result2))

