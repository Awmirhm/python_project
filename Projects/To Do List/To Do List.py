import time


def done_list():
    '''
    This function is for done position in daily_to_do_list
    '''
    for i in daily_to_do_list:
        if i["position"] == "DONE":
            print("Completed to-do list =")
            # for key,value in i.items():
            #    print(f"{key} : {value}")


def doing_list():
    '''
    This function is for doing position in daily_to_do_list
    '''
    for i in daily_to_do_list:
        if i["position"] == "DOING":
            print("List of work in progress =")
            # for key,value in i.items():
            #    print(f"{key} : {value}")


def Cancel_list():
    '''
    This function is for cancel position in daily_to_do_list
    '''
    for i in daily_to_do_list:
        if i["position"] == "CANCEL":
            print("List of canceled tasks =")
            # for key,value in i.items():
            #    print(f"{key} : {value}")


done_list_1 = []
doing_list_1 = []
Cancel_list_1 = []

question = int(input("how many things do you have to do? "))

for i in range(question):
    daily_to_do_list = [
        {
            "work": input("please enter things to do: "),
            "position": input("please enter your work position [Done , Doing , Cancel]: ").upper()
        },
    ]
    print()
    time.sleep(0.6)
    if daily_to_do_list[0]["position"] == "DONE":
        done_list()
        done_list_1.append(daily_to_do_list)
        print(done_list_1)
        print()

    elif daily_to_do_list[0]["position"] == "DOING":
        doing_list()
        doing_list_1.append(daily_to_do_list)
        print(doing_list_1)
        print()

    elif daily_to_do_list[0]["position"] == "CANCEL":
        Cancel_list()
        Cancel_list_1.append(daily_to_do_list)
        print(Cancel_list_1)
        print()
time.sleep(1.5)
print()
print(f"Your Completed , ongoing and canceled tasks order :\n{done_list_1} \n{doing_list_1} \n{Cancel_list_1}")
