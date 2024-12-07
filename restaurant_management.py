# this code is for restaurant management sysytem and this is my first project
# learning new things




print("This is our menu: ")
print("Pizza -> 500")
print("Burger -> 250")
print("noodles -> 120")
print("pasta -> 200")
print("sandwich -> 70")
print("colddrink -> 50")
print("coffee -> 60")
print("tea -> 50")


bill=0
rate = {"pizza":500, "burger":250, "noodles":120,"pasta":200,"sandwich":70,"colddrink":50,"coffee":60,"tea":50}
customer = True
while customer:
    item = input("Your order: ")
    order = item.split(" ")
    for items in order:
        freq=int(input(f"Enter how many {items} you want? "))
        for food in order:
            bill+=rate[food.lower()]*freq
    choice=input("you want to order more?")
    if choice.lower()=="no":
        customer=False


print(f"Your bill is {bill}\nThank you for visiting")
