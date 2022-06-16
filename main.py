print("TASK 1")
product_list = ["sour cream", "veggies", "beaf", "pickles"]
while True:
    command = input("Enter one of the following commands:\n\t'add' to add products into your list\n\t'delete' to delete product(s) from your list\n\t'show' to show the full list\n\t"
                    "'search' to search products in your list\n\t'clear' to clear the full list\nEnter command:").lower()
    if command == "add":
        prod_name = input("Input product's title:")
        product_list.append(prod_name)
    elif command == "delete":
        prod_name = input("Input product's   title:")
        if prod_name not in product_list:
            print("This product is not in the list")
            continue
        product_list.remove(prod_name)
    elif command == "show":
        print(product_list)
    elif command == "search":
        prod_name = input("Input product's title:")
        print(prod_name)
        if prod_name not in product_list:
            print("No product found")
    elif command == "clear":
        product_list.clear()
    elif command == "stop":
        break

print("TASK 2")

kapital, year = int(input("Enter initial deposit($):")), int(input("Enter period(year(s):"))
percent = 10
for i in range(1, year + 1):
    prom = final = kapital * (1 + 0.1) ** i
    final = kapital * ((1 + 0.1) ** year)
    print(f'year: {int(i)}, income: {int(prom)}')
print("The amount of money a client will get by the end of bank deposit:", int(final))


print("TASK 3")
n = int(input("Enter number:"))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("TASK 4")
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i % 5 == 0:
        if i > 500:
            break
        if i > 150:
            continue
        print(i)

print("TASK 5 --")
f_num = 0  # first num (первая цифра)
s_num = 1  # second num (вторая, последующая цифра)
a = int(input())
lisonacci = []
for i in range(a):
    f_num, s_num = s_num, f_num + s_num # в s_num передается значение первой (f num), а новая s num прнимает значение суммы f & s
    lisonacci.append(s_num)
print(lisonacci)