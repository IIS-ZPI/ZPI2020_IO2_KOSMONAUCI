from nbp.nbp import get_between_rate


def get_distribution_of_changes(currency_1, currency_2, start_time, end_time):
    data_for_currency_1 = get_between_rate('A', currency_1, start_time, end_time)
    data_for_currency_2 = get_between_rate('A', currency_2, start_time, end_time)

    if data_for_currency_1 is None or data_for_currency_2 is None:
        return 'Wrong some data'

    delta_currency_1 = calculate_deltas(data_for_currency_1['rates'])
    statistics_for_currency_1 = calculate_statistic(delta_currency_1)

    delta_currency_2 = calculate_deltas(data_for_currency_2['rates'])
    statistics_for_currency_2 = calculate_statistic(delta_currency_2)

    return statistics_for_currency_1, statistics_for_currency_2


def calculate_deltas(rates):
    delta_currency = []
    for index, rate in enumerate(rates):
        if index == 0:
            continue
        delta = float(rate[index]["mid"]) - float(rate[index - 1]["mid"])
        delta_currency.append(delta)

    return delta_currency


def calculate_statistic(delta_tab):
    min_value = min(delta_tab)
    max_value = max(delta_tab)

    scope = (max_value - min_value) / 10.0

    statistics = []

    start = min_value
    end = min_value + scope
    while True:
        if start > max_value:
            break

        count = 0
        for change_in_day in delta_tab:
            if start <= change_in_day < end:
                count = count + 1

        label = "[" + str(start) + ", " + str(end) + ")"
        statistics.append({'label': label, 'count': count})
        start = end
        end = start + scope

    return statistics
