import nbp


def test_get_table():
    data = nbp.get_table("A")
    assert data[0]['table'] == 'A'

    data = nbp.get_table("B")
    assert data[0]['table'] == 'B'

    data = nbp.get_table("C")
    assert data[0]['table'] == 'C'


def test_get_last_table():
    for i in range(1, 6, 2):
        data = nbp.get_last_table("A", i)
        assert data[0]['table'] == 'A'
        assert len(data) == i


def test_get_today_table():
    data = nbp.get_today_table("A")
    assert data[0]['table'] == 'A'

    # data = nbp.get_today_table("B")
    # assert data[0]['table'] == 'B'

    data = nbp.get_today_table("C")
    assert data[0]['table'] == 'C'

def test_get_date_table():
    data = nbp.get_date_table("A", "2020-01-01")
    assert data is None

    data = nbp.get_date_table("A", "2020-30-30")
    assert data is None

    data = nbp.get_date_table("A", "2020-01-02")
    assert data[0]['table'] == 'A'
    assert data[0]['effectiveDate'] == "2020-01-02"


def test_get_between_table():
    data = nbp.get_between_table("A", "2020-01-04", "2020-01-05")
    assert data is None

    data = nbp.get_between_table("A", "2020-01-10", "2020-01-05")
    assert data is None

    data = nbp.get_between_table("A", "2020-01-07", "2020-01-10")
    assert data[0]['table'] == 'A'
    assert data[0]['effectiveDate'] == "2020-01-07"
    assert data[1]['effectiveDate'] == "2020-01-08"
    assert data[2]['effectiveDate'] == "2020-01-09"
    assert data[3]['effectiveDate'] == "2020-01-10"


# rates
def test_get_current_rate():
    data = nbp.get_current_rate("A", "USD")
    assert data['code'] == "USD"

    data = nbp.get_current_rate("A", "CHF")
    assert data['code'] == "CHF"

    data = nbp.get_current_rate("A", "aaaaa")
    assert data is None


def test_get_last_rate():
    data = nbp.get_last_rate("A", "USD", 4)
    assert data['code'] == "USD"
    assert len(data['rates']) == 4

    data = nbp.get_last_rate("A", "CHF", 7)
    assert data['code'] == "CHF"
    assert len(data['rates']) == 7

    data = nbp.get_last_rate("A", "aaaaa", -5)
    assert data is None


def test_get_today_rate():
    data = nbp.get_today_rate("A", "USD")
    assert data['table'] == "A"
    assert data['code'] == 'USD'

    data = nbp.get_today_rate("A", "CHF")
    assert data['table'] == "A"
    assert data['code'] == 'CHF'

    data = nbp.get_today_rate("A", "sss")
    assert data is None


def test_get_date_rate():
    data = nbp.get_date_rate("A", "CHF", "2020-01-01")
    assert data is None

    data = nbp.get_date_rate("A", "CHF", "2020-30-30")
    assert data is None

    data = nbp.get_date_rate("A", "CHF", "2020-01-02")
    assert data['table'] == 'A'
    assert data['code'] == 'CHF'
    assert data['rates'][0]['effectiveDate'] == "2020-01-02"


def test_get_between_rate():
    data = nbp.get_between_rate("A", "CHF", "2020-01-04", "2020-01-05")
    assert data is None

    data = nbp.get_between_rate("A", "CHF", "2020-01-10", "2020-01-05")
    assert data is None

    data = nbp.get_between_rate("A", "CHF", "2020-01-07", "2020-01-10")
    assert data['table'] == 'A'
    assert data['rates'][0]['effectiveDate'] == "2020-01-07"
    assert data['rates'][1]['effectiveDate'] == "2020-01-08"
    assert data['rates'][2]['effectiveDate'] == "2020-01-09"
    assert data['rates'][3]['effectiveDate'] == "2020-01-10"


