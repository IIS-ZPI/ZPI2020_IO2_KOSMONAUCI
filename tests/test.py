import unittest
from statisticsCalculator import coefficients
from statisticsCalculator import distribution_of_changes


def test_calculate_deltas_correct_output(self):
    input = [{'no': '103/A/NBP/2021', 'effectiveDate': '2021-05-31', 'mid': 3.6724},
             {'no': '104/A/NBP/2021', 'effectiveDate': '2021-06-01', 'mid': 3.659},
             {'no': '105/A/NBP/2021', 'effectiveDate': '2021-06-02', 'mid': 3.6659},
             {'no': '106/A/NBP/2021', 'effectiveDate': '2021-06-04', 'mid': 3.6931},
             {'no': '107/A/NBP/2021', 'effectiveDate': '2021-06-07', 'mid': 3.6656}]
    expected_output = [-0.0134000000000003, 0.00690000000000035, 0.02719999999999967, -0.027499999999999858]
    result = coefficients.calculate_deltas(input)
    self.assertEqual(result, expected_output)


def test_calculate_deltas_incorrect_output(self):
    input = [{'no': '103/A/NBP/2021', 'effectiveDate': '2021-05-31', 'mid': 3.6724},
             {'no': '104/A/NBP/2021', 'effectiveDate': '2021-06-01', 'mid': 3.659},
             {'no': '105/A/NBP/2021', 'effectiveDate': '2021-06-02', 'mid': 3.6659},
             {'no': '106/A/NBP/2021', 'effectiveDate': '2021-06-04', 'mid': 3.6931},
             {'no': '107/A/NBP/2021', 'effectiveDate': '2021-06-07', 'mid': 3.6656}]
    expected_output = [0, 0, 0, 0]
    result = coefficients.calculate_deltas(input)
    self.assertNotEqual(result, expected_output)


def test_calculate_deltas_empty_input(self):
    input = []
    expected_output = []
    result = coefficients.calculate_deltas(input)
    self.assertEqual(result, expected_output)


def test_get_coefficients_empty_currency(self):
    currency = ''
    start_date = '01-05-2021'
    end_date = '01-06-2021'
    expected_output = 'Wrong some data'
    result = coefficients.get_coefficients(currency, start_date, end_date)
    self.assertEqual(result, expected_output)


def test_get_distribution_of_changes_same_currencies(self):
    currency_1 = 'USD'
    currency_2 = 'USD'
    start_date = '01-05-2021'
    end_date = '01-06-2021'
    expected_output = [], []
    result = distribution_of_changes.get_distribution_of_changes(currency_1, currency_2, start_date, end_date)
    self.assertEqual(result, expected_output)


def test_calculate_rates1_to_rates2_correct_output(self):
    rate_1 = [{'no': '087/A/NBP/2021', 'effectiveDate': '2021-05-07', 'mid': 3.7861}]
    rate_2 = [{'no': '087/A/NBP/2021', 'effectiveDate': '2021-05-07', 'mid': 4.5764}]
    expected_output = [1.2087372229999207]
    result = distribution_of_changes.calculate_rates1_to_rates2(rate_1, rate_2)
    self.assertEqual(result, expected_output)


def test_calculate_rates1_to_rates2_incorrect_output(self):
    rate_1 = [{'no': '087/A/NBP/2021', 'effectiveDate': '2021-05-07', 'mid': 3.7861}]
    rate_2 = [{'no': '087/A/NBP/2021', 'effectiveDate': '2021-05-07', 'mid': 4.5764}]
    expected_output = [0]
    result = distribution_of_changes.calculate_rates1_to_rates2(rate_1, rate_2)
    self.assertNotEqual(result, expected_output)


def test_calculate_rates1_to_rates2_empty_input(self):
    rate_1 = []
    rate_2 = []
    expected_output = []
    result = distribution_of_changes.calculate_rates1_to_rates2(rate_1, rate_2)
    self.assertEqual(result, expected_output)


def test_calculate_delta_correct_output(self):
    relations = [1.2087372229999207, 1.2170538500520098, 1.2162925841019354, 1.2135038445108928]
    expected_output = [0.008316627052089132, -0.000761265950074419, -0.002788739591042644]
    result = distribution_of_changes.calculate_delta(relations)
    self.assertEqual(result, expected_output)


def test_calculate_delta_empty_input(self):
    relations = []
    expected_output = []
    result = distribution_of_changes.calculate_delta(relations)
    self.assertEqual(result, expected_output)


def test_calculate_statistic_correct_output(self):
    delta_tab = [0.008316627052089132, -0.000761265950074419, -0.002788739591042644, -0.0072132008479863785]
    expected_output = (['[-0.0072,\n-0.0057)',
                        '[-0.0057,\n-0.0041)',
                        '[-0.0041,\n-0.0026)',
                        '[-0.0026,\n-0.001)',
                        '[-0.001,\n0.0006)',
                        '[0.0006,\n0.0021)',
                        '[0.0021,\n0.0037)',
                        '[0.0037,\n0.0052)',
                        '[0.0052,\n0.0068)',
                        '[0.0068,\n0.0083)',
                        '[0.0083,\n0.0099)'],
                       [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1])
    result = distribution_of_changes.calculate_statistic(delta_tab)
    self.assertEqual(result, expected_output)


def test_calculate_statistic_incorrect_output(self):
    delta_tab = [0.008316627052089132, -0.000761265950074419, -0.002788739591042644, -0.0072132008479863785]
    expected_output = ([], [])
    result = distribution_of_changes.calculate_statistic(delta_tab)
    self.assertNotEqual(result, expected_output)
