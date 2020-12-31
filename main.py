from Distance import *
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
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||                                   Distance Converter                              ||
    ||                                   Menu [OPTION]                                   ||
    ||                 1. Nautical mile (nmi)  ----> [mm, cm, m,  km, in, ft, yd, mi ]   ||
    ||                 2. Mile (mi)            ----> [mm, cm, m,  km, in, ft, yd, nmi]   ||
    ||                 3. Yard(yd)             ----> [mm, cm, m,  km, in, ft, mi, nmi]   ||
    ||                 4. Foot/Feet(ft)        ----> [mm, cm, m,  km, in, yd, mi, nmi]   ||
    ||                 5. Inch(in)             ----> [mm, cm, m,  km, ft, yd, mi, nmi]   ||
    ||                 6. Kilometer (km)       ----> [mm, cm, m,  in, ft, yd, mi, nmi]   ||
    ||                 7. Meter (m)            ----> [mm, cm, km, in, ft, yd, mi, nmi]   ||
    ||                 8. Centimeter (cm)      ----> [mm,  m, km, in, ft, yd, mi, nmi]   ||
    ||                 9. Millimeter (mm)      ----> [cm,  m, km, in, ft, yd, mi, nmi]   ||
    ||                10. exit                                                           ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
            """)
            slection = int(input("Select option :-"))
            if slection == 1:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]                       ||
    ||                        Sub_Menu                                 ||
    ||                 1. Nautical mile (nmi)  ----->  Millimeter (mm) ||
    ||                 2. Nautical mile (nmi)  ----->  Centimeter (cm) ||
    ||                 3. Nautical mile (nmi)  ----->  Meter (m)       ||
    ||                 4. Nautical mile (nmi)  ----->  Kilometer (km)  ||
    ||                 5. Nautical mile (nmi)  ----->  Inch(in)        ||
    ||                 6. Nautical mile (nmi)  ----->  Foot/feet(ft)   ||
    ||                 7. Nautical mile (nmi)  ----->  Yard(yd)        ||
    ||                 8. Nautical mile (nmi)  ----->  mile(mi)        ||
    ||                 9. Exit                                         ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options < 9 and option >= 1:
                        w = options
                        ds = int(input("Enter distance :-"))
                        rs = nautical_mile(ds, w)
                        print(rs[0],rs[1])
                    else:
                        c=input("Are you want exit y/n :- ")
                        if c=='y' or c=='Y':
                            break
                        else:
                            continue
                    
            elif slection == 2:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]                       ||
    ||                        Sub_Menu                                 ||
    ||                 1. mile (mi)  ----->  Millimeter (mm)           ||
    ||                 2. mile (mi)  ----->  Centimeter (cm)           ||
    ||                 3. mile (mi)  ----->  Meter (m)                 ||
    ||                 4. mile (mi)  ----->  Kilometer (km)            ||
    ||                 5. mile (mi)  ----->  Inch(in)                  ||
    ||                 6. mile (mi)  ----->  Foot/feet(ft)             ||
    ||                 7. mile (mi)  ----->  Yard(yd)                  ||
    ||                 8. mile (mi)  ----->  nautical mile (nmi)       ||
    ||                 9. Exit                                         ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options < 9 and option >= 1:
                        w = options
                        ds = int(input("Enter distance :-"))
                        rs = mile(ds, w)
                        print(rs[0],rs[1])
                    else:
                        c=input("Are you want exit y/n :- ")
                        if c=='y' or c=='Y':
                            break
                        else:
                            continue
                    
            elif slection == 3:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]                       ||
    ||                        Sub_Menu                                 ||
    ||                 1. Yard (yd)  ----->  Millimeter (mm)           ||
    ||                 2. Yard (yd)  ----->  Centimeter (cm)           ||
    ||                 3. Yard (yd)  ----->  Meter (m)                 ||
    ||                 4. Yard (yd)  ----->  Kilometer (km)            ||
    ||                 5. Yard (yd)  ----->  Inch(in)                  ||
    ||                 6. Yard (yd)  ----->  Foot/feet(ft)             ||
    ||                 7. Yard (yd)  ----->  mile(mi)                  ||
    ||                 8. Yard (yd)  ----->  Nautical mile (nmi)       ||
    ||                 9. Exit                                         ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options < 9 and option >= 1:
                        w = options
                        ds = int(input("Enter distance :-"))
                        rs = yard(ds, w)
                        print(rs[0],rs[1])
                    else:
                        c=input("Are you want exit y/n :- ")
                        if c=='y' or c=='Y':
                            break
                        else:
                            continue
            elif slection == 4:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]                       ||
    ||                        Sub_Menu                                 ||
    ||                 1. Foot/feet(ft)  ----->  Millimeter (mm)       ||
    ||                 2. Foot/feet(ft)  ----->  Centimeter (cm)       ||
    ||                 3. Foot/feet(ft)  ----->  Meter (m)             ||
    ||                 4. Foot/feet(ft)  ----->  Kilometer (km)        ||
    ||                 5. Foot/feet(ft)  ----->  Inch(in)              ||
    ||                 6. Foot/feet(ft)  ----->  Yard (yd)             ||
    ||                 7. Foot/feet(ft)  ----->  mile(mi)              ||
    ||                 8. Foot/feet(ft)  ----->  Nautical mile (nmi)   ||
    ||                 9. Exit                                         ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options < 9 and option >= 1:
                        w = options
                        ds = int(input("Enter distance :-"))
                        rs = foot(ds, w)
                        print(rs[0],rs[1])
                    else:
                        c=input("Are you want exit y/n :- ")
                        if c=='y' or c=='Y':
                            break
                        else:
                            continue

            elif slection == 5:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]                       ||
    ||                        Sub_Menu                                 ||
    ||                 1. Inch(in)  ----->  Millimeter (mm)            ||
    ||                 2. Inch(in)  ----->  Centimeter (cm)            ||
    ||                 3. Inch(in)  ----->  Meter (m)                  ||
    ||                 4. Inch(in)  ----->  Kilometer (km)             ||
    ||                 5. Inch(in)  ----->  Foot/feet(ft)              ||
    ||                 6. Inch(in)  ----->  yard(yd)                   ||
    ||                 7. Inch(in)  ----->  mile(mi)                   ||
    ||                 8. Inch(in)  ----->  Nautical mile (nmi)        ||
    ||                 9. Exit    99                                   ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options < 9 and option >= 1:
                        w = options
                        ds = int(input("Enter distance :-"))
                        rs = inch(ds, w)
                        print(rs[0],rs[1])
                    else:
                        c=input("Are you want exit y/n :- ")
                        if c=='y' or c=='Y':
                            break
                        else:
                            continue

            elif slection == 6:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]                       ||
    ||                        Sub_Menu                                 ||
    ||                 1. Kilometer (km)  ----->  Millimeter (mm)      ||
    ||                 2. Kilometer (km)  ----->  Centimeter (cm)      ||
    ||                 3. Kilometer (km)  ----->  Meter (m)            ||
    ||                 4. Kilometer (km)  ----->  Inch(in)             ||
    ||                 5. Kilometer (km)  ----->  Foot/feet(ft)        ||
    ||                 6. Kilometer (km)  ----->  yard(yd)             ||
    ||                 7. Kilometer (km)  ----->  mile(mi)             ||
    ||                 8. Kilometer (km)  ----->  Nautical mile (nmi)  ||
    ||                 9. Exit                                         ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options < 9 and option >= 1:
                        w = options
                        ds = int(input("Enter distance :-"))
                        rs = kilometer(ds, w)
                        print(rs[0],rs[1])
                    else:
                        c=input("Are you want exit y/n :- ")
                        if c=='y' or c=='Y':
                            break
                        else:
                            continue

            elif slection == 7:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]                       ||
    ||                        Sub_Menu                                 ||
    ||                 1. Meter (m)  ----->  Millimeter (mm)           ||
    ||                 2. Meter (m)  ----->  Centimeter (cm)           ||
    ||                 3. Meter (m)  ----->  Kilometer (km)            ||
    ||                 4. Meter (m)  ----->  Inch(in)                  ||
    ||                 5. Meter (m)  ----->  Foot/feet(ft)             ||
    ||                 6. Meter (m)  ----->  yard(yd)                  ||
    ||                 7. Meter (m)  ----->  mile(mi)                  ||
    ||                 8. Meter (m)  ----->  Nautical mile (nmi)       ||
    ||                 9. Exit                                         ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options < 9 and option >= 1:
                        w = options
                        ds = int(input("Enter distance :-"))
                        rs = meter(ds, w)
                        print(rs[0],rs[1])
                    else:
                        c=input("Are you want exit y/n :- ")
                        if c=='y' or c=='Y':
                            break
                        else:
                            continue

            elif slection == 8:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]                       ||
    ||                        Sub_Menu                                 ||
    ||                 1. Centimeter (cm)  ----->  Millimeter (mm)     ||
    ||                 2. Centimeter (cm)  ----->  Meter (m)           ||
    ||                 3. Centimeter (cm)  ----->  Kilometer (km)      ||
    ||                 4. Centimeter (cm)  ----->  Inch(in)            ||
    ||                 5. Centimeter (cm)  ----->  Foot/feet(ft)       ||
    ||                 6. Centimeter (cm)  ----->  yard(yd)            ||
    ||                 7. Centimeter (cm)  ----->  mile(mi)            ||
    ||                 8. Centimeter (cm)  ----->  Nautical mile (nmi) ||
    ||                 9. Exit                                         ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options < 9 and option >= 1:
                        w = options
                        ds = int(input("Enter distance :-"))
                        rs = centimeter(ds, w)
                        print(rs[0],rs[1])
                    else:
                        c=input("Are you want exit y/n :- ")
                        if c=='y' or c=='Y':
                            break
                        else:
                            continue

            elif slection == 9:
                while True:
                    print("""
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
    ||               Distance Converter [OPTION]                       ||
    ||                        Sub_Menu                                 ||
    ||                 1. Millimeter (mm)  ----->  Centimeter (cm)     ||
    ||                 2. Millimeter (mm)  ----->  Meter (m)           ||
    ||                 3. Millimeter (mm)  ----->  Kilometer (km)      ||
    ||                 4. Millimeter (mm)  ----->  Inch(in)            ||
    ||                 5. Millimeter (mm)  ----->  Foot/feet(ft)       ||
    ||                 6. Millimeter (mm)  ----->  yard(yd)            ||
    ||                 7. Millimeter (mm)  ----->  mile(mi)            ||
    ||                 8. Millimeter (mm)  ----->  Nautical mile (nmi) ||
    ||                 9. Exit                                         ||
    :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                    """)
                    options = int(input("Select option :-"))
                    if options < 9 and option >= 1:
                        w = options
                        ds = int(input("Enter distance :-"))
                        rs = millimeter(ds, w)
                        print(rs[0],rs[1])
                    else:
                        c=input("Are you want exit y/n :- ")
                        if c=='y' or c=='Y':
                            break
                        else:
                            continue

            elif slection == 10:
                c=input("Are you want to go menu again y/n :- ")
                if c=='y' or c=='Y':
                    break
    elif option == 4:
        c=input("Are you want to go menu again y/n :- ")
        if c=='y' or c=='Y':
            print("Thanks for using Unit conversion")
            break


