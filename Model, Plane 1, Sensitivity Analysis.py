import random
ROWS = 30
COLUMNS = 6
counter = 0
new_seats = []
used_seats = []
times = []
used_seats_formal = []
seats = (ROWS*COLUMNS)
while counter < 1000:
    time_taken = 0
    i = 1
    new_seats.clear()
    used_seats.clear()
    used_seats_formal.clear()
    counter += 1
    while i <= seats:
        new_seats.append(i) 
        i += 1
    while len(new_seats) >= 1:
        seat_number = random.choice(new_seats)
        new_seats.remove(seat_number)
        used_seats.append(seat_number)
        row = int(seat_number/COLUMNS) + 1
        if row == 31:
            row = 30
        column = seat_number
        while True:
            if column < 7:
                break
            else:
                column -= 6
                continue
        p_gender = random.randint(1, 100)
        if p_gender <= 48:
            gender = "f"
        else:
            gender = "m"
        p_age = random.randint(1, 100)
        if p_age <= 15:
            age_class = "child"
        elif p_age >= 65:
            age_class = "elderly"
        else:
            age_class = "middle"
        if gender == "m" and age_class == "middle":
            walking_speed = 1.43
        if gender == "f" and age_class == "middle":
            walking_speed = 1.35
        if gender == "m" and age_class == "elderly":
            walking_speed = 1.19
        if gender == "f" and age_class == "elderly":
            walking_speed = 1.10
        else:
            walking_speed = 0.63
        p_carry_on = random.randint(1, 1000)
        p_disobedience = random.randint(1, 10000)
        ##############
        carry_ons = 0
        if p_disobedience <= 100:
            time_taken += random.randint(60, 180)
        ##############
        p_wheelchair = random.randint(1, 100000)
        if p_wheelchair <= 76:
            time_taken += random.randint(7, 27)
        p_unaccompanied = random.randint(1, 1000)
        if p_unaccompanied <= 22 and carry_ons > 0 and age_class == "child":
            time_taken += random.randint(7, 17)
        p_elderly_help = random.randint(1, 1000)
        if p_elderly_help <= 478 and carry_ons > 0 and age_class == "elderly":
            time_taken += random.randint(8, 12)
        p_language_mismatch = random.randint(1, 1000)
        if p_language_mismatch <= 67 and carry_ons > 0:
            time_taken += random.randint(15, 25)
        p_pregnant = random.randint(1, 10000)
        if p_pregnant <= 44 and carry_ons > 0 and gender == "f":
            time_taken += random.randint(7, 17)
        p_short = random.randint(1, 100)
        if gender == "f" and p_short <= 18 and carry_ons > 0:
            time_taken += random.randint(6, 10)
        elif gender == "m" and p_short <= 1 and carry_ons > 0:
            time_taken += random.randint(6, 10)
        while carry_ons > 0:
            p_stowing = random.randint(1, 10000)
            if p_stowing <= 6602:
                time_taken += random.randint(5, 15)
                carry_ons -= 1
            else:
                time_taken += 0
                carry_ons -= 1
        interference_counter = 1
        interference_list = []
        interference_list.clear()
        while interference_counter < row:
            interference_list.append(1/(30 - interference_counter))
            interference_counter += 1
        aisle_interference = 0.73 * sum(interference_list)
        time_taken += (aisle_interference * random.randint(5, 15))
        walking_time = row + (1.54 * walking_speed)
        time_taken += walking_time
        seat = "{}/{}".format(row, column)
        used_seats_formal.append(seat)
        if column == 1:
            column_seat_2 = "{}/{}".format(row, 2)
            column_seat_3 = "{}/{}".format(row, 3)
            if column_seat_2 in used_seats_formal:
                interference_time = (1 + 2 + 3 + 2)
                time_taken += interference_time
            elif column_seat_3 in used_seats_formal:
                interference_time = (1 + 1 + 3 + 1)
                time_taken += interference_time
            elif column_seat_2 in used_seats_formal and column_seat_3 in used_seats_formal:
                interference_time = (2 + 3 + 3 + 3)
                time_taken += interference_time
            else:
                interference_time = column * 1
                time_taken += interference_time         
        elif column == 2:
            column_seat_3 = "{}/{}".format(row, 3)
            if column_seat_3 in used_seats_formal:
                interference_time = (1 + 1 + 2 + 1)
                time_taken += interference_time
            else:
                interference_time = (column * 1)
                time_taken += interference_time
        elif column == 6:
            column_seat_5 = "{}/{}".format(row, 5)
            column_seat_4 = "{}/{}".format(row, 4)
            if column_seat_5 in used_seats_formal:
                interference_time = (1 + 2 + 3 + 2)
                time_taken += interference_time
            elif column_seat_4 in used_seats_formal:
                interference_time = (1 + 1 + 3 + 1)
                time_taken += interference_time
            elif column_seat_5 in used_seats_formal and column_seat_4 in used_seats_formal:
                interference_time = (2 + 3 + 3 + 3)
                time_taken += interference_time
            else:
                interference_time = (column - 3) * 1
                time_taken += interference_time
        elif column == 5:
            column_seat_4 = "{}/{}".format(row, 4)
            if column_seat_4 in used_seats_formal:
                interference_time = (1 + 1 + 2 + 1)
                time_taken += interference_time
            else:
                interference_time = (column - 3) * 1
                time_taken += interference_time
        elif column == 4:
            time_taken += (column - 3) * 1
        else:
            time_taken += column * 1
    times.append(time_taken)

print("the mean is {}".format((sum(times)/len(times))))