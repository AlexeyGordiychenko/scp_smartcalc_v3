from s21_model_wrapper import Model
import pytest


def test_mismatched_brackets_0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(2+3*((5-2)+(3+4)*(2-1)")


def test_mismatched_brackets_1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(2+3)((5-2)+(3+4)(2-1)))")


def test_mismatched_brackets_2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(23^2+45^2-sqrt(9)")


def test_mismatched_brackets_3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(ln((e^3))^2)+log(10^2)")


def test_mismatched_brackets_4():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sqrt((16+9)*2^3))")


def test_mismatched_brackets_5():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(asin(0.5)^2+atan(1)^2-")


def test_mismatched_brackets_6():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("((2+sin(30))*2")


def test_mismatched_brackets_7():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(sqrt(16+92)*3))")


def test_mismatched_brackets_8():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(((2+3)((5-2)+(3+4)(2-1))")


def test_mismatched_brackets_9():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sin(30)+cos(60--tan(45)")


def test_incorrect_unary_0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("-3*-5+15-4")


def test_incorrect_unary_1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("--4/2")


def test_incorrect_unary_2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("-+10^2")


def test_incorrect_unary_3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("--+3")


def test_incorrect_unary_4():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("+-3")


def test_incorrect_unary_5():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("5%-2")


def test_incorrect_unary_6():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("2*-")


def test_incorrect_unary_7():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("--3/42")


def test_incorrect_unary_8():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("-3*/5")


def test_incorrect_unary_9():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("6+-")


def test_incorrect_unary__0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("7/-")


def test_incorrect_unary__1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(+-+-8)")


def test_incorrect_unary__2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("-9*-")


def test_incorrect_unary__3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("++10/3")


def test_incorrect_unary__4():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("5*-(--3)")


def test_incorrect_unary__5():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("-4/-")


def test_several_operators_0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("2++2")


def test_several_operators_1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("3**5+15-4")


def test_several_operators_2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("4//2")


def test_several_operators_3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("10^^2")


def test_several_operators_4():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("5%%2")


def test_several_operators_5():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sin(30)+cos(60)++tan(45)")


def test_several_operators_6():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("acos(0.5)++asin(0.5)+atan(1)")


def test_several_operators_7():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(2+3)((5-2))+(3+4)(2-1)")


def test_several_operators_8():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sqrt(16+9*2)*3)/4")


def test_several_operators_9():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("ln(2)+log(10)++log(2)")


def test_functions_without_parentheses_0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos30+sin45*tan60")


def test_functions_without_parentheses_1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sqrt16+sqrt9*2")


def test_functions_without_parentheses_2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("ln2+log10-acos0.5")


def test_functions_without_parentheses_3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sin30*cos60+tan45")


def test_functions_without_parentheses_4():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("acos0.5+asin0.5+atan1")


def test_functions_without_parentheses_5():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sqrt16+9*2-3")


def test_functions_without_parentheses_6():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("ln(e^5)+log102")


def test_functions_without_parentheses_7():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("acos0.5+asin0.5")


def test_functions_without_parentheses_8():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos45*sin30+tan60")


def test_functions_without_parentheses_9():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sqrt16+sqrt(9*2)")


def test_expression_ends_on_operator_0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+sin")


def test_expression_ends_on_operator_1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+cos")


def test_expression_ends_on_operator_2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+tan")


def test_expression_ends_on_operator_3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+asin")


def test_expression_ends_on_operator_4():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+acos")


def test_expression_ends_on_operator_5():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+atan")


def test_expression_ends_on_operator_6():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+sqrt")


def test_expression_ends_on_operator_7():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+ln")


def test_expression_ends_on_operator_8():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+log")


def test_expression_ends_on_operator_9():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)/")


def test_expression_ends_on_operator_10():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)*")


def test_expression_ends_on_operator_11():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)^")


def test_expression_ends_on_operator_12():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)+")


def test_expression_ends_on_operator_13():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)-")


def test_expression_ends_on_operator_14():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30)+sin(45)*tan(60)mod")


def test_two_decimal_points_0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("2+2.25+3.25.48-3")


def test_two_decimal_points_1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("1..5 + 2")


def test_two_decimal_points_2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("3.4.5 - 1")


def test_two_decimal_points_3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("6..7 * 4")


def test_two_decimal_points_4():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("2 / 3..1")


def test_two_decimal_points_5():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sin(30.2.3)")


def test_two_decimal_points_6():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(4..56)")


def test_two_decimal_points_7():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("tan(5..89)")


def test_two_decimal_points_8():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("54..23 + sqrt(16)")


def test_two_decimal_points_9():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("log(10..10)")


def test_two_decimal_points__0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("ln(23..34)")


def test_loose_decimal_points_0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30).sin(5)")


def test_loose_decimal_points_1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("cos(30).5+2")


def test_loose_decimal_points_2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression(".sin(5)-8")


def test_loose_decimal_points_3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("5+7-2^.*2")


def test_loose_decimal_points_4():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression(". + 5")


def test_loose_decimal_points_5():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("6 * .")


def test_loose_decimal_points_6():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sqrt(.)")


def test_loose_decimal_points_7():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression(". / 3")


def test_loose_decimal_points_8():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sin(.)")


def test_loose_decimal_points_9():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("log(.)")


def test_loose_decimal_points__0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("2 + . * 4")


def test_loose_decimal_points__1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("- 2 / .")


def test_loose_decimal_points__2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("tan(45).")


def test_loose_decimal_points__3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression(".sin(45)")


def test_spaces_1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("sin(4 5)")


def test_spaces_2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("lo g(10)*2^3*5+x-x")


def test_incorrect_e_notation_0():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("5+2.3e.4")


def test_incorrect_e_notation_1():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("3.5-1.2e/2")


def test_incorrect_e_notation_2():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(4.5e + 2)*(6.7e2-3.2e-4)")


def test_incorrect_e_notation_3():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(2.1e5^3)/(x-e2)")


def test_incorrect_e_notation_4():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("(7.6e3mod5)+(e mod2)")


def test_incorrect_e_notation_5():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("ln(2.3 e+4)+log(7.6e3)")


def test_incorrect_e_notation_6():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("acos(0.5)-e")


def test_incorrect_e_notation_7():
    calculator = Model()
    with pytest.raises(ValueError, match=r"Invalid expression"):
        calculator.parse_expression("2-2.1e2.")
