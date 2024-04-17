from s21_model_wrapper_gcov import Model


def test_credit_0():
    calculator = Model()
    res = calculator.credit_annuity(91930155.62, 11, 15.04)
    assert res.monthly_start == 1428069.86
    assert res.over == 96575065.90
    assert res.total == 188505221.52


def test_credit_1():
    calculator = Model()
    res = calculator.credit_annuity(49042836.76, 10, 21.02)
    assert res.monthly_start == 981180.99
    assert res.over == 68698882.04000002
    assert res.total == 117741718.80000001


def test_credit_2():
    calculator = Model()
    res = calculator.credit_annuity(26162102.37, 48, 13.339)
    assert res.monthly_start == 291313.65
    assert res.over == 141634560.03
    assert res.total == 167796662.40


def test_credit_3():
    calculator = Model()
    res = calculator.credit_differentiated(91469864.23, 4, 14.719)
    assert res.monthly_start == 3027576.2811261415
    assert res.monthly_end == 1928996.2154097462
    assert res.over == 27487875.68686126
    assert res.total == 118957739.91686127


def test_credit_4():
    calculator = Model()
    res = calculator.credit_differentiated(41071637.5, 21, 3.12723)
    assert res.monthly_start == 270016.402608001
    assert res.monthly_end == 163407.42545284104
    assert res.over == 13539764.835666098
    assert res.total == 54611402.3356661


def test_credit_5():
    calculator = Model()
    res = calculator.credit_differentiated(6659040.58, 3, 16.50267)
    assert res.monthly_start == 276549.97378473496
    assert res.monthly_end == 187517.1445650081
    assert res.over == 1694167.5502953725
    assert res.total == 8353208.130295373
