# start date 1 Jan 2017
# end date 15 Jan 2017
# convention unadjusted
# period monthly
# convert input dates to datetime format
# separate by months

from datetime import datetime, date
import calendar

def payTime(startDate, endDate, convention, period): #date_format = 'yyyy-mm-dd'
    sDate = datetime.strptime(startDate, '%Y-%m-%d').date()
    eDate = datetime.strptime(endDate, '%Y-%m-%d').date()
    sDateTup = date.timetuple(sDate)
    eDateTup = date.timetuple(eDate)

    datesList = [sDate, eDate]
    endMonths = eDateTup[1]
    if eDateTup[0] > sDateTup[0]:
        endMonths += 12*(eDateTup[0]-sDateTup[0])
    if endMonths > sDateTup[1]:
        endYear = sDateTup[0]

        for i in range(sDateTup[1], endMonths):

            modI = (i % 12)          # first month
            if modI == 0: modI = 12  # first month
            modJ = ((i + 1) % 12)    # second month
            if modJ == 0: modJ = 12  # second month
            periodIter = calendar.monthrange(sDateTup[0],modI)[1]

            if period == 'monthly':
                nDate = (str(endYear) +'-'+ str(modI) +'-'+ str(periodIter))
                if modJ < modI: endYear += 1
                bDate = (str(endYear) +'-'+ str(modJ) + '-01')
                datesList.append(datetime.strptime(nDate, '%Y-%m-%d').date())
                datesList.append(datetime.strptime(bDate, '%Y-%m-%d').date())

            if period == 'bimonthly':
                if (sDateTup[2] < (periodIter / 2) and i == sDateTup[1]) or (i > sDateTup[1]):# and eDate > (datesList[-1]+)):
                    midMonthDate = str(endYear) +'-'+ str(modI) +'-'+ str(periodIter/2)
                    datesList.append(datetime.strptime(midMonthDate, '%Y-%m-%d').date())

                    midMonthDateNext = str(endYear) +'-'+ str(modI) +'-'+ str((periodIter/2)+1)
                    datesList.append(datetime.strptime(midMonthDateNext, '%Y-%m-%d').date())

                # if (eDateTup[2] )
                nDate = (str(endYear) +'-'+ str(modI) +'-'+ str(periodIter))
                if modJ < modI: endYear += 1
                bDate = (str(endYear) +'-'+ str(modJ) + '-01')
                datesList.append(datetime.strptime(nDate, '%Y-%m-%d').date())
                datesList.append(datetime.strptime(bDate, '%Y-%m-%d').date())

    datesList.sort()
    datesArr = []
    while len(datesList) > 2:          # breaks dates array into sets of two
        datesArr.append(datesList[:2])
        datesList = datesList[2:]
    datesArr.append(datesList)
    return datesArr