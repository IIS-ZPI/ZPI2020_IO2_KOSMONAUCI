from datetime import datetime

from dateutil.relativedelta import relativedelta

from nbp.nbp import get_between_rate


def get_session_count(table, currency, last_date):
    # count = [raises, no changes, downs]
    count = [0, 0, 0]

    current_date = datetime.today() - relativedelta(days=1)
    old_mid = None
    while current_date >= last_date:
        new_data = get_between_rate(table=table, code=currency, start_date=last_date.strftime("%Y-%m-%d"), end_date=(last_date + relativedelta(weeks=1)).strftime("%Y-%m-%d"))

        if new_data is not None:
            for r in new_data["rates"]:
                mid = r["mid"]
                if old_mid is not None:
                    if old_mid < mid:
                        count[0] += 1
                    elif old_mid > mid:
                        count[2] += 1
                    else:
                        count[1] += 1

                old_mid = mid

        last_date = last_date + relativedelta(weeks=1)

    labels = ['raises', 'stable', 'downs']
    return labels, count


def get_last_weeks_count(currency, n=1):
    return get_session_count('A', currency, datetime.today() - relativedelta(weeks=n))


def get_last_months_count(currency, n=1):
    return get_session_count('A', currency, datetime.today() - relativedelta(months=n))
