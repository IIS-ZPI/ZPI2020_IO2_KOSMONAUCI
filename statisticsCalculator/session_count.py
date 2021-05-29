from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta

from nbp.nbp import get_date_rate


def get_session_count(table, currency, target_date):
    # count = [raises, no changes, downs]
    count = [0, 0, 0]

    next_date = datetime.today() - timedelta(1)
    old_data = None
    while next_date >= target_date:
        new_data = get_date_rate(table=table, code=currency, date=next_date.strftime("%Y-%m-%d"))

        if new_data is not None:
            new_data = new_data["rates"][0]["mid"]
            if old_data is not None:
                if old_data < new_data:
                    count[0] += 1
                elif old_data > new_data:
                    count[2] += 1
                else:
                    count[1] += 1

            old_data = new_data

        next_date = next_date - timedelta(1)
        labels=['raises', 'stable','downs']

    return labels,count


def get_last_weeks_count(currency, n=1):
    return get_session_count('A', currency, datetime.today() - relativedelta(weeks=n))


def get_last_months_count(currency, n=1):
    return get_session_count('A', currency, datetime.today() - relativedelta(months=n))
