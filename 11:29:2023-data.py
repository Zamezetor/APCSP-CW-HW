# Logan White 11/29/2023
# 11/29/2023-data.py
# data assignment
# CC BY-NC-SA 4.0
# Imports
# Variables
dictionary_list = []
# Functions


def customer_info():
    name = input("Greetings, What is your name?\n")
    data_limit = int(input("In MB, what is your monthly data allotment?\n"))
    months = int(input("How many months have you been using data\n"))
    data_used = []
    for i in range(months):
        data_used.append(int(input("How much data was used in month #" + str(i+1) + "?\n")))
    cust_dict = dict(name=name, data_limit=data_limit, months=months, used_data=data_used)
    dictionary_list.append(cust_dict)


def customer_amount():
    amount = int(input("How many customers are being recorded? "))
    for i in range(amount):
        customer_info()


def data_calc(customer):
    rollover = 0
    overage = 0
    over_tmp = 0
    for i in range(len(dictionary_list[customer]['used_data'])):
        """print(dictionary_list[customer]['used_data'][i])"""
        if dictionary_list[customer]['used_data'][i] < dictionary_list[customer]['data_limit']:
            rollover += (dictionary_list[customer]['data_limit'] - dictionary_list[customer]['used_data'][i])
        elif dictionary_list[customer]['used_data'][i] > dictionary_list[customer]['data_limit']:
            over_tmp += rollover + dictionary_list[customer]['data_limit']
            overage += (10 * abs(over_tmp - dictionary_list[customer]['used_data'][i]))/100
            rollover = 0
            over_tmp = 0
    if 0 < overage:
        print(dictionary_list[customer]['name'] + " has overage fees of $" + str(overage))
        print(dictionary_list[customer]['name'] + " has " + str(dictionary_list[customer]['data_limit'])
              + "MB this month")
        dictionary_list[customer].update({"Current_Period": int(dictionary_list[customer]['data_limit'])})
        rollover = 0
    elif rollover >= 0:
        print(dictionary_list[customer]['name'] + " has a rollover amount of " + str(rollover) + "MB")
        print(dictionary_list[customer]['name'] + " can use " + str(rollover + dictionary_list[customer]['data_limit'])
              + "MB this month")  # , rollover from previous months cannot rollover again.")
        print(overage)
        dictionary_list[customer].update({"Current_Period": int(rollover + dictionary_list[customer]['data_limit'])})


def admin_info():
    print("User ; Data")
    for i in range(len(dictionary_list)):
        print(dictionary_list[i]['name'] + " ; " + str(dictionary_list[i]['Current_Period'] + "MB"))


# Code
customer_amount()
print("Disclaimer: Excess Rollover Data After An Overage Does Not Continue to Rollover and if " +
      "You Have Unpaid Overage Fees, Rollover is Not Added to Your Current Data")
for c in range(len(dictionary_list)):
    data_calc(c)
print("Admin Information: \n Displaying Users and Current Data Allotment.")
admin_info()
