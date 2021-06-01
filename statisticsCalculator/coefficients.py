from nbp.nbp import *
import statistics as stats

def get_coefficients(currency_1, start_time, end_time):
    data_for_currency_1 = get_between_rate('A', currency_1, start_time, end_time)

    if data_for_currency_1  is None:
        return 'Wrong some data'
    t=data_for_currency_1['rates']

    delta_currency = calculate_deltas(data_for_currency_1['rates'])
    coefficients_result = CoefficientsResult()
    coefficients_result.median=stats.median(delta_currency)
    coefficients_result.mode=stats.mode(delta_currency)
    coefficients_result.stDeviation=stats.pstdev(delta_currency)
    coefficients_result.coefficientVariation= coefficients_result.stDeviation/stats.mean(delta_currency)*100

    return coefficients_result

def calculate_deltas(rates):
    delta_currency = []
    for index, rate in enumerate(rates):
        if index == 0:
            continue

        delta = float(rate['mid']) - float(rates[index - 1]["mid"])
        delta_currency.append(delta)

    return delta_currency

class CoefficientsResult:
    def __init__(self):
        self.median=0.0
        self.mode=0.0
        self.stDeviation=0.0
        self. coefficientVariation=0.0

