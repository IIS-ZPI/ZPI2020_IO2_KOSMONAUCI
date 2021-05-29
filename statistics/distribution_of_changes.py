from nbp.nbp import get_between_rate


def get_distribution_of_changes(currency_1, currency_2, start_time, end_time):
    data_for_currency_1 = get_between_rate('A', currency_1, start_time, end_time)
    data_for_currency_2 = get_between_rate('A', currency_2, start_time, end_time)

    if data_for_currency_1 is None or data_for_currency_2 is None:
        return 'Wrong some data'

    delta = calculate_deltas(data_for_currency_1['rates'], data_for_currency_2['rates'])
    x, y = calculate_statistic(delta)

    return x, y


def calculate_deltas(rates_1, rates_2):
    delta_currency = []
    for index, rate in enumerate(rates_1):
        delta = float(rates_1[index]["mid"]) - float(rates_2[index]["mid"])
        delta_currency.append(delta)

    return delta_currency


def calculate_statistic(delta_tab):
    min_value = min(delta_tab)
    max_value = max(delta_tab)

    scope = (max_value - min_value) / 10.0

    y = []
    x = []

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
        x.append(label)
        y.append(count)
        start = end
        end = start + scope

    return x, y
