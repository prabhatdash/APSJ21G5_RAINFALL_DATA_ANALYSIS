import functions
def dashboard():
    print("ENTER 1 TO PRINT THE MAXIMUM RAINFALL")
    print("ENTER 2 TO PRINT THE MINIMUM RAINFALL")
    print("ENTER 3 TO PRINT AVERAGE RAINFALL")
    print("ENTER 4 TO PRINT THE NAME OF SUBDIVISION WITH MAXIMUM RAINFALL")
    print("ENTER 5 TO PRINT THE NAME OF SUBDIVISION WITH MINIMUM RAINFALL")
    print("ENTER 6 TO PRINT MINIMUM RAINFALL OF A PARTICULAR MONTH")
    print("ENTER 7 TO PRINT MAXIMUM RAINFALL OF A PARTICULAR MONTH")
    print("ENTER 8 TO PLOT A GRAPH SHOWING ANNUAL MEAN RAINFALL OF EVERY SUBDIVISION")
    print("ENTER 9 T0 PLOT A GRAPH SHOWING THE RAINFALL TREND")
    print("ENTER 10 TO EXIT")
    inp=int(input())
    if inp==1:
        functions.max_rainfall()
        dashboard()
    elif inp==2:
        functions.min_rainfall()
        dashboard()
    elif inp==3:
        functions.avg_rainfall()
        dashboard()
    elif inp==4:
        functions.name_max()
        dashboard()
    elif inp==5:
        functions.name_min()
        dashboard()
    elif inp==6:
        functions.month_min()
        dashboard()
    elif inp==7:
        functions.month_max()
        dashboard()
    elif inp==8:
        functions.graph_1()
        dashboard()
    elif inp==9:
        functions.graph_2()
        dashboard()
    elif inp==10:
        exit()