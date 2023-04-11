import pandas as pd
from datetime import datetime

def workingdays(date1, date2,startday,endday):
    '''
    date1: start datetime
    date2: end datetime
    returns the number of working days between two dates including both the dates
    '''
    days_num = (date2 - date1).days + 1 
    
    if days_num > 7:
        if startday <= 5:
            non_workingdays = 2
        else:
            non_workingdays = 1
        
        if endday == 5:
            non_workingdays += 1
        
        elif  endday== 6:
            non_workingdays += 2
        
        remaining_days = days_num - ((7 - startday) + (endday + 1))
        non_workingdays += ((remaining_days // 7) * 2)
        
    
    elif days_num == 7:
        non_workingdays = 2
            
    else:
        
        week_days=pd.date_range(date1,date2)
        non_workingdays=len([i for i in week_days if i.weekday()>4])  
    workdays=days_num-non_workingdays
    return workdays



def end_date_working_hours(hour):
    '''
    hour: end date hour
    returns the number of working hours on the end date
    '''

    if hour<=9:
        return 0
    elif hour>9 and hour<=17:
        return hour-9
    else:
        return 8


def start_date_working_hours(hour):
        '''
        hour: start date hour
        returns the number of working hours on the start date
        '''
    
        if hour>9 and hour<17:
            return 17-hour
        elif hour<=9:
            return 8
        else:
            return 0



def business_hours(start_datetime_str,end_datetime_str):
    '''
    start_datetime_str: start datetime string in ISO datetime format
    end_datetime_str: end datetime string in ISO datetime format
    returns the number of business hours(9:00 AM- 17:00 PM) between two dates
    '''
    
    
    
    try:
        start_datetime=datetime.fromisoformat(start_datetime_str)
        end_datetime=datetime.fromisoformat(end_datetime_str)
        if start_datetime>end_datetime:
            return 'start datetime should be before than end datetime'

        

        start_day = start_datetime.weekday()
        end_day = end_datetime.weekday()
    

        workdays=workingdays(start_datetime.date(),end_datetime.date(),start_day,end_day)
        


        if (start_day==5 or start_day==6) and (end_day==5 or end_day==6):
        
            business_hours_val=workdays*8

        elif (start_day==5 or start_day==6) and (end_day!=5 or end_day!=6):
       
            working_hours=end_date_working_hours(end_datetime.hour)
            business_hours_val=((workdays-1)*8)+working_hours

        elif (start_day!=5 or start_day!=6) and (end_day==5 or end_day==6):
                
            working_hours=start_date_working_hours(start_datetime.hour)
            business_hours_val=((workdays-1)*8)+working_hours
                
    
        else:
               
            startworking_hours=start_date_working_hours(start_datetime.hour)
            endworking_hours=end_date_working_hours(end_datetime.hour)
            business_hours_val=((workdays-2)*8)+(startworking_hours+ endworking_hours)
    
        return business_hours_val

    except:
        return 'invalid inputs for date parameter'
        


    
    