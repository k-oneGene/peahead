import datetime
from dateutil.relativedelta import relativedelta

# Takes html q_month, q_month_end and returns html week number.
# returns (week start, week end)   xxxx, (cleaned future?) start month, (created or fixed) end month)
def month_to_week(q_month, q_month_end):

    # First deal with q_month
    # For case of empty input. Form doesn't allow empty but someone can still manually type in URLs?
    if q_month is None:
        now = datetime.datetime.now()
        q_month_date_start = datetime.date(now.year, now.month, 1)
    else:
        q_month_all = q_month.split('-')
        q_month_date_start = datetime.date(int(q_month_all[0]), int(q_month_all[1]), 1)

    # To fit into HTML5 week format for SQL query later
    if q_month_date_start.isocalendar()[1] < 10:
        q_week = str(q_month_date_start.isocalendar()[0]) + '-W0' + str(q_month_date_start.isocalendar()[1])
    else:
        q_week = str(q_month_date_start.isocalendar()[0]) + '-W' + str(q_month_date_start.isocalendar()[1])

    # Second deal with q_month_end
    if q_month_end is None:
        q_month_date_end = datetime.date(q_month_date_start.year, q_month_date_start.month, 1)
    else:
        q_month_end_all = q_month_end.split('-')
        q_month_date_end = datetime.date(int(q_month_end_all[0]), int(q_month_end_all[1]), 1)

    q_month_date_end = q_month_date_end + relativedelta(months=+1)
    q_month_date_end = q_month_date_end - relativedelta(days=+1)

    # To fit into HTML5 week format for SQL query later
    if q_month_date_end.isocalendar()[1] < 10:
        q_week_end = str(q_month_date_end.isocalendar()[0]) + '-W0' + str(q_month_date_end.isocalendar()[1])
    else:
        q_week_end = str(q_month_date_end.isocalendar()[0]) + '-W' + str(q_month_date_end.isocalendar()[1])


    return q_week, q_week_end