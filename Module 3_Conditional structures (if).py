# Task 1, ZanderLength

length_of_zander = int(input("What is the length of zander? "))
min_length = 42

if length_of_zander < min_length:
    below_the_size_limit = (min_length - length_of_zander)
    print("This zander is", below_the_size_limit, "cm shorter than the required length. Release the fish back into the lake")
else:
    print("Enjoy your humt!!!")


# Task 2, cabin class

cabin_class = input("Enter the cabin class of a cruise ship: ")

if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck")
else:
    print("Invalid cabin class")



# Task 3, gender and hemoglobin value

gender = input("Enter gender ")
hemoglobin = int(input("Enter the level of hemoglobin? "))

if gender == "female":
    if hemoglobin < 117:
        print("Your hemoglobin level is low.")
    elif hemoglobin > 155:
        print("Your hemoglobin level is high.")
    else:
        print("Your hemoglobin level is normal.")
if gender == "male":
    if hemoglobin < 134:
        print("Your hemoglobin level is low.")
    elif hemoglobin > 167:
        print("Your hemoglobin level is high.")
    else:
        print("Your hemoglobin level is normal.")


# Task 4, leap year

year = int(input("What is the year? "))

if year < 99:
    if year % 4 == 0 :
        print(year, "is a leap year")
    else:
        print(year, "is not a leap year")
else:
    if year % 4 == 0 :
        if year % 100 != 0:
            print(year, "is a leap year")
        else :
            if year % 400 == 0:
                print(year, "is a leap year")
            else:
                print(year, "is not a leap year")
    else:
        print(year, "is not a leap year")
