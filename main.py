print("-------------------------------------------------------------")
print("----------------------- Unit converter ----------------------")
c="y"
while c=="y":
    print("-------------------------------------------------------------")
    print("""\
    Unit Converter [OPTION]
    1. Kilometer to meter
    2. meter to centemeter 
    3. centemeter to milimeter
    4. exit
    """)
    print("-------------------------------------------------------------")
    option = int(input("Enter your option :- "))



    if option == 1:
        km = int(input("Enter the value in  Kilometer :- "))
        result = km*1000
        print(km,"km -----> ",result,"m")
    elif option == 2:
        me = int(input("Enter the value in  Meter :- "))
        result = me*100
        print(me,"m -----> ",result,"cm")
    elif option == 3:
        cm = int(input("Enter the value in  centemeter :- "))
        result = cm*10
        print(cm,"cm -----> ",result,"mm")
    elif option == 4:
        c=input("Are you want to go menu again y/n :- ")
        if c=='n':
            break