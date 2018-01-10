# convert input dates to datetime format
# separate by months

from datetime import datetime, date, timedelta
import calendar

def payTime(startDate, endDate, convention, period): #date_format = 'yyyy-mm-dd'
    sDate = datetime.strptime(startDate, '%Y-%m-%d').date()
    eDate = datetime.strptime(endDate, '%Y-%m-%d').date()
    sDateTup = date.timetuple(sDate)
    eDateTup = date.timetuple(eDate)

    datesList = [sDate, eDate]   # date array with start and end
    endMonths = eDateTup[1]      # end date month
    if eDateTup[0] > sDateTup[0]: # determines no. of months between start and end dates
        endMonths += 12*(eDateTup[0]-sDateTup[0]) # endMonths-sDateTup[1] is the actual value for no. of months
    endYear = sDateTup[0]   # sets year variable to start year
    if period == 'monthly' or period == 'bimonthly':
        stRange = sDateTup[1]
        endRange = endMonths+1
        mp = True
    if period == 'annually' or period == 'biannually':
        stRange = endYear
        endRange = eDateTup[0]+1
        mp = False

    for i in range(stRange, endRange): # loops from start month to end month
        modI = (i % 12)          # first month
        if modI == 0: modI = 12  # first month 1-12
        modJ = ((i + 1) % 12)    # second month
        if modJ == 0: modJ = 12  # second month 1-12
        periodIter = calendar.monthrange(endYear,modI)[1] # determines days in month i
        if period == 'annually': monthBreaks = ['-01-01', '-12-31']
        if period == 'biannually': monthBreaks = ['-01-01', '-06-30', '-07-01', '-12-31']
        if period == 'monthly': monthBreaks = [01, periodIter]
        if period == 'bimonthly': monthBreaks = [01, (periodIter/2), (periodIter/2)+1, periodIter]

        for j in range(len(monthBreaks)):
            if mp == True: moda = str('-'+ str(modI) +'-'+ str(monthBreaks[j]))
            if mp == False: moda = str(monthBreaks[j]) # moda is '-month-day'
            date_added = (str(endYear) + moda)
            datesList.append(datetime.strptime(date_added, '%Y-%m-%d').date())

        if modJ < modI or mp == False: endYear += 1

    tempDateList = []
    for u in range(len(datesList)):
        if datesList[u] > sDate and datesList[u] < (eDate - timedelta(3)): # td is number of days new cycle cutoff
            tempDateList.append(datesList[u])
    tempDateList.append(sDate)
    tempDateList.append(eDate)
    tempDateList.sort()

        # if penultimate values are too close to endDate, remove
        # ensure that there are an even number of values in array

# remove duplicates
# if penultimate value is too close to end date, remove it
# add adjusted convention

    datesArr = []
    while len(tempDateList) > 2:          # breaks dates array into sets of two
        datesArr.append(tempDateList[:2])
        tempDateList = tempDateList[2:]
    datesArr.append(tempDateList)
    print datesArr
    return datesArr