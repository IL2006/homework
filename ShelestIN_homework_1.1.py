#вывести среднюю букву, если число букв в слове нечётное и две средних буквы, если число букв чётное
print("Введите слово из латинских букв:")
my_word= input(" ") #Ввод с клавиатуры
if len(my_word) % 2 != 0:                   # Если кол-во введенных букв нечетное
    print(my_word[len(my_word)//2])               #определяем средний элемент в строке при целочисленном делении длины строки
else:                                 #если кол-во введенных букв четное
    print(my_word[len(my_word)//2-1:len(my_word)//2+1]) #выводим диапазон средний двух значений строки