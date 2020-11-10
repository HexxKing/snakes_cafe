
# assignments ===============================================
divider = "*" * 38
whitespace = " "
border = "*" * 2
welcome = "Welcome to the Snakes Cafe! "
menu_msg = "Please see our menu below.  "
appetizers = "Appetizers"
app_dict = {"Wings" : 0, "Cookies" : 0, "Spring Rolls" : 0}
entrees = "Entrees"
ent_dict = {"Salmon" : 0, "Steak" : 0, "Meat Tornado" : 0, "A Literal Garden" : 0}
desserts = "Desserts"
dess_dict = {"Ice Cream" : 0, "Cake" : 0, "Pie" : 0}
drinks = "Drinks"
drink_dict = {"Coffee" : 0, "Tea" : 0, "Unicorn Tears" : 0}
all_items = [app_dict, ent_dict, dess_dict, drink_dict]

# function declarations ====================================
def menu_header(text):
  print(border + whitespace * 3 + text + whitespace * 3 + border)

def whitespace_line():
  print("\n")

def item_header(catagory):
  print("\n")
  print(catagory)
  print("-" * len(catagory))

def list_items(dict):
  for key in dict:
    print(key)

def added_msg(order, list):
# if the order matches a key in any of the dicts, then add one to its value
# ** 1 order of Wings have been added to your meal **
# def ask_again(list):
  # while item in list == True:
    for item in list:
    # if order in item:
      while order in item:
        value = item[order] + 1
        item[order] = value
        if value == 1:
            quantity = "order"
        if value > 1:
          quantity = "orders"
        print("** " + str(value) + " " + quantity + " of " + order + " have been added to your meal **")
        order = input(">")
    # added_msg(order)
      if order == "quit":
          break





# Invoke =====================================================
print(divider)
menu_header(welcome)
menu_header(menu_msg)
print(border + whitespace * 36)
print(border + " To quit at any time, type \"quit\" " + border)
print(divider)

item_header(appetizers)
list_items(app_dict)

item_header(entrees)
list_items(ent_dict)

item_header(desserts)
list_items(dess_dict)

item_header(drinks)
list_items(drink_dict)

whitespace_line()
print(divider)
print(border + " What would you like to order? " + border)
response = input(">")
added_msg(response, all_items)
# ask_again(all_items)