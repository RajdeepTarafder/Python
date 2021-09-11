def add_time(start, duration, day_of_week=False):
    week_days_index={"monday":0,"tuesday":1,"wednesday":2,"thursday":3,"friday":4,"saturday":5,"sunday":6}
    week_days_array=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    duration_tup=duration.partition(":")
    duration_hrs=int(duration_tup[0])
    duration_min=int(duration_tup[2])

    start_tup=start.partition(":")
    start_min_tup=start_tup[2].partition(" ")
    start_hrs=int(start_tup[0])
    start_min=int(start_min_tup[0])

    am_pm=start_min_tup[2]
    am_pm_flip={"AM":"PM","PM":"AM"}

    amt_of_days=int(duration_hrs /24)

    end_min=start_min+duration_min
    if(end_min >=60):
        start_hrs +=1
        end_min=end_min % 60
    end_hrs=(start_hrs+ duration_hrs) % 12
    amt_of_am_pm_flip=int((start_hrs+ duration_hrs)/ 12)

    end_min=end_min if end_min>9 else "0" +str(end_min)
    end_hrs=end_hrs =12 if end_hrs==0 else end_hrs

    if (am_pm=="PM" and start_hrs+ (duration_hrs % 12) >=12):
        amt_of_days +=1

    am_pm=am_pm_flip[am_pm] if amt_of_am_pm_flip % 2 ==1 else am_pm

    returnTime =str(end_hrs) + ":" + str(end_min) + " " + am_pm

    if( day_of_week):
        day_of_week=day_of_week.lower()
        index=(int(week_days_index[day_of_week]) + amt_of_days) % 7
        new_day= week_days_array[index]
        returnTime += "," + " "+ new_day

    if(amt_of_days ==1):
        return returnTime + " " +"(next day)"
    elif(amt_of_days > 1):
        return returnTime +" " + "(" +str(amt_of_days)+" " + "days later)"

    return returnTime
