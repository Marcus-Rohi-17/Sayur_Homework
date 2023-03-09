'''
Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp 
You can limit the quantity to single digit number.
'''
#Declare Fruit list
fruits_list = ['apple', 'orange', 'banana']
print('What do you want to buy?')
#quantity must be in single digit
print('The quantity of the fruits must be less then 10')
#Declare Numbers list
number_in_letters = ['one','two','three','four','five','six','seven','eight','nine']
digits = "123456789"
#Get the input from the user
user_need = input('Enter the required fruits and count: ')
#Convert string into list
required_fruits = user_need.split()
count = 0
fruit_count = 0
#Initialy declare the required fruit list and quantity list
required_fruits_list = []
quantity_list = []
#quantity = ''
#Iterate the user input and get the required count of the fruit
for i in required_fruits:
    if i in fruits_list: 
        required_fruits_list.append(i)
        fruit_count+=1
    if i in number_in_letters:
        quantity_list.append(i)
        count +=1
        #quantity = i
    if i in digits:
        quantity_list.append(i)
        count +=1
        #quantity = i

if count == 0:
    print('How much you want?')
    customer_need = input('Enter the required quantity: ')
    required_fruits = customer_need.split()
    for i in required_fruits:
        if i in number_in_letters:
            quantity_list.append(i)
            count +=1
            #quantity = i
        if i in digits:
            quantity_list.append(i)
            count +=1
            #quantity = i

#Get the size of required fruits list & quantity list
length_of_required_fruits_list = len(required_fruits_list)
length_of_quantity_list = len(quantity_list)

#print the quantity and fruit details
if(length_of_required_fruits_list == length_of_quantity_list):
    for i in range(length_of_quantity_list):
        print('Customer need ',quantity_list[i], required_fruits_list[i])
#if user entered detail is wrong, then show the error message
else:
    print('please enter the required fruits and quantity')


'''
if fruit_count > 0 and count > 0:
    print('The user want ',quantity)
else:
    print('please enter the required fruits and quantity')
'''
