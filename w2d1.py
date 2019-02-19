#Have the user enter the total cost of the home
total_cost = int(input("What does the house cost? "))
# total_cost = 100000

#The average percentage needed for down payment.
down_payment_needed = float(total_cost * 0.25)

#Friendly this is what you have so far.
print("You will need to save " + str(down_payment_needed) + "0 for this home. ")

# have the user enter what they make in a year
annual_salary = float(input("What do you make a year? "))
# annual_salary = 250000

#have the user enter what percentage of their monthly salary they want to save each month
portion_saved = float(input("What percentage of your monthly salary do you want to save during a month? "))
# portion_saved = .10

monthly_salary_savings = annual_salary / 12 * portion_saved

# print(total_cost, down_payment_needed, annual_salary, portion_saved)

# Since you are just starting to save, your current savings is $0.00, and your starting month value is 0. However, you also have an interest of .04 from your bank for keeping the money in their bank that you can calculate.
current_savings = 0
current_month = 0
interest_rate = 0.04

#Now we need to determine what your monthly savings will be and how many months it will take for you to save up that amount.
while current_savings < down_payment_needed:
    #first, you need to have a ongoing count of months increasing by one month after 30 days. 
    current_month += 1
    # now we will need to determine what your starting current savings is each month. 
    monthly_return = current_savings * interest_rate / 12
    #  we need to re-evaluate your currents savings each month
    current_savings = monthly_return + current_savings
    # now we need to determine what the new total
    current_savings = monthly_salary_savings + current_savings


print("It will take you " + str(current_month) + " to save that up that amount.")









