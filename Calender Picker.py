Year_Calender = [
[
    [1, 2, 3, 4, 5, 6, 7],
    [8, 9, 10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19, 20, 21],
    [22, 23, 24, 25, 26, 27, 28],
    [29, 30, 31, 0, 0, 0, 0]

],

 [
    [0, 0, 0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9, 10, 11],
    [12, 13, 14, 15, 16, 17, 18],
    [19, 20, 21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30, 0, 0]
],

 [

    [0, 0, 0, 0, 0, 1, 2],
    [3, 4, 5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14, 15, 16],
    [17, 18, 19, 20, 21, 22, 23],
    [24, 25, 26, 27, 28, 29, 30],
    [31, 0, 0, 0, 0, 0, 0]
]
 ]
year_counter = 0

def calender_picker():

    for month_calender in Year_Calender:
        month_index = Year_Calender.index(month_calender)
        for row in month_calender:
            row_index = month_calender.index(row)
            for integer in row:
                integer_index = row.index(integer)
                global year_counter

                current_day = Year_Calender[month_index][row_index][integer_index]
                nth_month_day = Year_Calender[((month_index) + year_counter)][row_index][integer_index]

                while year_counter <= 12:

                    if current_day == nth_month_day :
                        print("March " + str(integer) + " falls on the same day of the week as April " + str(integer))

                    else:
                        print("March " + str(integer) + " does not fall on the same day of the week as April " + str(integer))
                    year_counter = year_counter + 1

calender_picker()