from dataa import *
print("""\
    -------------------------------------------------------------
    ----------------------- Unit converter ----------------------
""")
while True:
    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||                     Unit Converter                      ||
    ||                    Main Menu [OPTION]                   ||
    ||                 1. Distance Conversion                  ||
    ||                 2.                                      ||
    ||                 3.                                      ||
    ||                 4. exit                                 ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    """)
    option=int(input("Select option :-"))
    
    
    if option == 1:
        while True:
            print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||                    Distance Converter                   ||
    ||                      Menu [OPTION]                      ||
    ||                 1. Kilometer  <----> Meter              ||
    ||                 2. Meter      <----> Centemeter         ||
    ||                 3. Centemeter <----> Milimeter          ||
    ||                 4. exit                                 ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            """)
            slection = int(input("Select option :-"))

            if slection == 1:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]               ||
    ||                        Sub_Menu                         ||
    ||                 1. Kilometer -----> Meter               ||
    ||                 2. Meter     -----> Kilometer           ||
    ||                 3. exit                                 ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options == 1:
                        w = 1
                    elif options == 2:
                        w = 2
                    elif options == 3:
                        c=input("Are you want to go menu again y/n :- ")
                        if c=='y':
                            break
                        else:
                            continue
                    ds = int(input("Enter distance :-"))
                    rs = km_to_m(ds, w)
                    print(rs[0],rs[1])
            elif slection == 2:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]               ||
    ||                        Sub_Menu                         ||
    ||                 1. Meter      -----> Centemeter         ||
    ||                 2. Centemeter -----> Meter              ||
    ||                 3. exit                                 ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options == 1:
                        w = 1
                    elif options == 2:
                        w = 2
                    elif options == 3:
                        c=input("Are you want to go menu again y/n :- ")
                        if c=='y':
                            break
                        else:
                            continue
                    ds = int(input("enter distance :- "))
                    rs = m_to_cm(ds, w)
                    print(rs[0],rs[1])
            elif slection == 3:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]               ||
    ||                        Sub_Menu                         ||
    ||                 1. Centemeter -----> Milimeter          ||
    ||                 2. Milimeter  -----> Centemeter         ||
    ||                 3. exit                                 ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options == 1:
                        w = 1
                    elif options == 2:
                        w = 2
                    elif options == 3:
                        c=input("Are you want to go menu again y/n :- ")
                        if c=='y':
                            break
                        else:
                            continue
                    ds = int(input("enter distance :- "))
                    rs = cm_to_mm(ds, w)
                    print(rs[0],rs[1])
            elif slection == 4:
                c=input("Are you want to go menu again y/n :- ")
                if c=='y':
                    break
    elif option == 4:
        c=input("Are you want to go menu again y/n :- ")
        if c=='y':
            break


