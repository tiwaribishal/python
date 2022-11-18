'''take input of age from person
determine the oldest and young '''

first  = int(input("age of person 1:"))

second = int(input("age of 2 person :"))

third = int(input("age of 3  person :"))


if first>second and first > third:
    print ("first is older")

elif second>first and second >third :
    print ("second is older")

elif third>first and third >first :
    print("third is older")
