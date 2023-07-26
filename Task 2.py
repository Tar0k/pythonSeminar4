# задача 2 необязательная.
# Даны два многочлена, которые вводит пользователь.
# Задача - сформировать многочлен, содержащий сумму многочленов.
# Степени многочленов могут быть разные.
#
# например на входе 2x^2 + 4x + 5 = 0 и 5x^3 - 3*x^2 - 12 = 0
# на выходе будет 5x^3 - x^2 + 4х - 7 = 0
# можно использовать модуль re
import re
from collections import OrderedDict


def find_degrees(polynom: str):
    split_by_members = re.findall(r"^.+?(?=[+=-])|[+-].+?(?=[+=-])", polynom)
    x_degree = {}
    for member in split_by_members:
        if "x^" in member:
            split_by_degree = member.split("x^")
            val = split_by_degree if split_by_degree[0] != "" else [1, split_by_degree[1]]
            x_degree[int(val[1])] = int(val[0])
        elif "x" in member:
            member = member.replace("x", "")
            if len(member) > 0:
                x_degree[1] = int(member)
            else:
                x_degree[1] = 1
        else:
            x_degree[0] = int(member)
    return x_degree


first_member = "2x^2 + 4x + 5 = 0".replace(" ", "").replace("*", "")
second_member = "5x^3 - 3*x^2 - 12 = 0".replace(" ", "").replace("*", "")
print(first_member)
print(second_member)
# Создаем словарь степеней, где ключ - степень, значение - множитель
first_degrees = find_degrees(first_member)
second_degrees = find_degrees(second_member)

# Складываем словари по ключу в один
new_members = {item: first_degrees[item] if item not in second_degrees else first_degrees[item] + second_degrees[item]
               for item in first_degrees}
for item in second_degrees:
    if item not in first_degrees:
        new_members[item] = second_degrees[item]
new_members = sorted(new_members.items(), key=lambda item: item[0], reverse=True)
# print(new_members)

# Создаем текстовые версии для членов многочлена
text_members = []
for member in new_members:
    if member[1] == 0:
        break

    text_member = ""
    if member[1] > 0:
        text_member += "+ "
    else:
        text_member += "- "

    if member[0] > 1:
        text_member += f"{abs(member[1])}x^{member[0]}" if abs(member[1]) != 1 else f"x^{member[0]}"
    elif member[0] == 1:
        text_member += f"{abs(member[1])}x" if abs(member[1]) != 1 else "x"
    else:
        text_member += f"{abs(member[1])}"
    text_members.append(text_member)

result = " ".join(text_members).lstrip("+ ").lstrip("- ") + " = 0"
print(result)


