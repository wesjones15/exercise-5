from datetime import datetime, date
from dateutil.relativedelta import relativedelta as rd
import calendar

def payTime(startDate, endDate, convention, period): #date_format = 'yyyy-mm-dd'
    sDate = datetime.strptime(startDate, '%Y-%m-%d').date()
    eDate = datetime.strptime(endDate, '%Y-%m-%d').date()
    sDateTup = date.timetuple(sDate)
    eDateTup = date.timetuple(eDate)

    datesList = [eDate, sDate]   # date array with start and end
    endMonths = eDateTup[1]      # end date month
    if eDateTup[0] > sDateTup[0]: # determines no. of months between start and end dates
        endMonths += 12*(eDateTup[0]-sDateTup[0]) # endMonths-sDateTup[1] is the actual value for no. of months
    endYear = sDateTup[0]   # sets year variable to start year
    if 'monthly' in period:
        stRange = sDateTup[1]
        endRange = endMonths+1
    if 'annually' in period:
        stRange = endYear
        endRange = eDateTup[0]+1

    for i in range(stRange, endRange): # loops from start month to end month
        endYear = date.timetuple(datesList[-1])[0]
        periodIter = calendar.monthrange(endYear,date.timetuple(datesList[-1])[1])[1] # determines days in month i

        if period == 'annually': monthBreaks = [rd(years=1,days=-1), rd(years=1)]
        if period == 'biannually': monthBreaks = [rd(months=6,days=-1), rd(months=6), rd(years=1,days=-1), rd(years=1)]
        if period == 'monthly': monthBreaks = [rd(months=1,days=-1),rd(months=1)]
        if period == 'bimonthly': monthBreaks = [rd(days=(periodIter/2)-1), rd(days=periodIter/2),rd(months=1,days=-1),rd(months=1)]

        tempList = []
        for j in range(len(monthBreaks)):
            date_added = datesList[-1] + monthBreaks[j]
            tempList.append(date_added)
        datesList += tempList

    tempDateList = []
    for u in range(len(datesList)):
        if datesList[u] > sDate and datesList[u] < (eDate - rd(days=3)): # td is number of days new cycle cutoff
            tempDateList.append(datesList[u])
    tempDateList.append(sDate)
    tempDateList.append(eDate)

    if convention == 'adjusted': # pushes date forward if it occurs on weekend
        for u in range(len(tempDateList)):
            eachDate = tempDateList[u].weekday()
            if eachDate >= 5:
                anotherTempValue = tempDateList[u] + rd(days=(7 - int(eachDate)))
                if anotherTempValue in tempDateList: anotherTempValue += rd(days=1)
                tempDateList[u] = anotherTempValue
    tempDateList.sort()

    datesArr = []
    while len(tempDateList) > 2:          # breaks dates array into sets of two
        datesArr.append(tempDateList[:2])
        tempDateList = tempDateList[2:]
    datesArr.append(tempDateList)
    return datesArr