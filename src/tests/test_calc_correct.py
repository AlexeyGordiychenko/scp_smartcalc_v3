from scp_model_wrapper_gcov import Model
import pytest


def test_correct_expressions_0():
    calculator = Model()
    calculator.parse_expression("2+2")
    assert calculator.calculate() == 4


def test_correct_expressions_1():
    calculator = Model()
    calculator.parse_expression("3*5+15-4")
    assert calculator.calculate() == 26


def test_correct_expressions_2():
    calculator = Model()
    calculator.parse_expression("4/2")
    assert calculator.calculate() == 2.0


def test_correct_expressions_3():
    calculator = Model()
    calculator.parse_expression("10^2")
    assert calculator.calculate() == 100


def test_correct_expressions_4():
    calculator = Model()
    calculator.parse_expression("(-1)")
    assert calculator.calculate() == -1


def test_correct_expressions_5():
    calculator = Model()
    calculator.parse_expression("+3")
    assert calculator.calculate() == 3


def test_correct_expressions_6():
    calculator = Model()
    calculator.parse_expression("-3")
    assert calculator.calculate() == -3


def test_correct_expressions_7():
    calculator = Model()
    calculator.parse_expression("5mod2")
    assert calculator.calculate() == 1


def test_correct_expressions_8():
    calculator = Model()
    calculator.parse_expression("cos(0.7853981633974483)")
    assert calculator.calculate() == 0.7071067811865476


def test_correct_expressions_9():
    calculator = Model()
    calculator.parse_expression("sin(0.5235987755982988)")
    assert calculator.calculate() == 0.49999999999999994


def test_correct_expressions_10():
    calculator = Model()
    calculator.parse_expression("tan(0.7853981633974483)")
    assert calculator.calculate() == 0.9999999999999999


def test_correct_expressions_11():
    calculator = Model()
    calculator.parse_expression("acos(0.5)")
    assert calculator.calculate() == 1.0471975511965979


def test_correct_expressions_12():
    calculator = Model()
    calculator.parse_expression("asin(0.5)")
    assert calculator.calculate() == 0.5235987755982989


def test_correct_expressions_13():
    calculator = Model()
    calculator.parse_expression("atan(1)")
    assert calculator.calculate() == 0.7853981633974483


def test_correct_expressions_14():
    calculator = Model()
    calculator.parse_expression("sqrt(16)")
    assert calculator.calculate() == 4.0


def test_correct_expressions_15():
    calculator = Model()
    calculator.parse_expression("ln(2)")
    assert calculator.calculate() == 0.6931471805599453


def test_correct_expressions_16():
    calculator = Model()
    calculator.parse_expression("log(10)")
    assert calculator.calculate() == 1.0


def test_correct_expressions_17():
    calculator = Model()
    calculator.parse_expression("(2+3)*(5-2)")
    assert calculator.calculate() == 15


def test_correct_expressions_18():
    calculator = Model()
    calculator.parse_expression("2*3^2")
    assert calculator.calculate() == 18


def test_correct_expressions_19():
    calculator = Model()
    calculator.parse_expression("ln(2^5)")
    assert calculator.calculate() == 3.4657359027997265


def test_correct_expressions_20():
    calculator = Model()
    calculator.parse_expression("2+2*3+(4/2)^2")
    assert calculator.calculate() == 12.0


def test_correct_expressions_21():
    calculator = Model()
    calculator.parse_expression(
        "sin(0.5235987755982988)+cos(1.0471975511965979)-tan(0.7853981633974483)")
    assert calculator.calculate() == -1.1102230246251565e-16


def test_correct_expressions_22():
    calculator = Model()
    calculator.parse_expression("sqrt(16)+sqrt(9)*2")
    assert calculator.calculate() == 10.0


def test_correct_expressions_23():
    calculator = Model()
    calculator.parse_expression("ln(2)+log(10)-log(2)")
    assert calculator.calculate() == 1.3921171848959641


def test_correct_expressions_24():
    calculator = Model()
    calculator.parse_expression("(2+3)*(5-2)+(3+4)*(2-1)")
    assert calculator.calculate() == 22


def test_correct_expressions_25():
    calculator = Model()
    calculator.parse_expression("23^2+45^2")
    assert calculator.calculate() == 2554


def test_correct_expressions_26():
    calculator = Model()
    calculator.parse_expression("ln(2^5)+log(10^2)")
    assert calculator.calculate() == 5.465735902799727


def test_correct_expressions_27():
    calculator = Model()
    calculator.parse_expression("acos(0.5)+asin(0.5)+atan(1)")
    assert calculator.calculate() == 2.356194490192345


def test_correct_expressions_28():
    calculator = Model()
    calculator.parse_expression(
        "(2+sin(0.5235987755982988))*(2-cos(1.0471975511965979))")
    assert calculator.calculate() == 3.75


def test_correct_expressions_29():
    calculator = Model()
    calculator.parse_expression("sqrt(16+9*2)")
    assert calculator.calculate() == 5.830951894845301


def test_correct_expressions_30():
    calculator = Model()
    calculator.parse_expression(
        "cos(0.5235987755982988)+sin(0.7853981633974483)*tan(1.0471975511965979)")
    assert calculator.calculate() == 2.0907702751760278


def test_correct_expressions_31():
    calculator = Model()
    calculator.parse_expression("sqrt(16+92)+45-2")
    assert calculator.calculate() == 53.392304845413264


def test_correct_expressions_32():
    calculator = Model()
    calculator.parse_expression("ln(2)+log(10)-acos(0.5)")
    assert calculator.calculate() == 0.6459496293633475


def test_correct_expressions_33():
    calculator = Model()
    calculator.parse_expression("(2+3)+((5-2)+(3+4)*(2-1))")
    assert calculator.calculate() == 15


def test_correct_expressions_34():
    calculator = Model()
    calculator.parse_expression("23^2+45^2-sqrt(9)mod16")
    assert calculator.calculate() == 2551.0


def test_correct_expressions_35():
    calculator = Model()
    calculator.parse_expression("ln((2^3)^2)+log(10^2)")
    assert calculator.calculate() == 6.1588830833596715


def test_correct_expressions_36():
    calculator = Model()
    calculator.parse_expression("sqrt((16+9)*2^3)")
    assert calculator.calculate() == 14.142135623730951


def test_correct_expressions_37():
    calculator = Model()
    calculator.parse_expression("asin(0.5)^2+atan(1)^2")
    assert calculator.calculate() == 0.8910059528761227


def test_correct_expressions_38():
    calculator = Model()
    calculator.parse_expression("(2+sin(0.5235987755982988))*2")
    assert calculator.calculate() == 5.0


def test_correct_expressions_39():
    calculator = Model()
    calculator.parse_expression("sqrt(16+9*2)*3")
    assert calculator.calculate() == 17.492855684535904


def test_correct_expressions_40():
    calculator = Model()
    calculator.parse_expression("(2+3)*5+x-4mod2")
    assert calculator.calculate(2896) == 2921


def test_correct_expressions_41():
    calculator = Model()
    calculator.parse_expression(
        "sqrt(16)+cos(x)+sin(3.14159/2)+tan(3.14159/4)")
    assert calculator.calculate(9339) == 5.42235654692368


def test_correct_expressions_42():
    calculator = Model()
    calculator.parse_expression("acos(1)+asin(1)+atan(1)+ln(1)+log(10)")
    assert calculator.calculate() == 3.356194490192345


def test_correct_expressions_43():
    calculator = Model()
    calculator.parse_expression("2^3*5+15-x+sqrt(16)")
    assert calculator.calculate(8395) == -8336.0


def test_correct_expressions_44():
    calculator = Model()
    calculator.parse_expression("cos(0)+sin(3.14159/2)-tan(3.14159/X)+acos(1)")
    assert calculator.calculate(9977) == 1.9996851167572804


def test_correct_expressions_45():
    calculator = Model()
    calculator.parse_expression("asin(0)*atan(1)/5mod4+log(x)")
    assert calculator.calculate(6371) == 3.8042076050820413


def test_correct_expressions_46():
    calculator = Model()
    calculator.parse_expression("sqrt(x)+cos(0)-sin(3.14159/2)*tan(3.14159/4)")
    assert calculator.calculate(7522) == 86.729465754981


def test_correct_expressions_47():
    calculator = Model()
    calculator.parse_expression("acos(1)+asin(0)^atan(1)+ln(1)+x")
    assert calculator.calculate(3443) == 3443.0


def test_correct_expressions_48():
    calculator = Model()
    calculator.parse_expression("log(10)*2^3*5+x-X")
    assert calculator.calculate(2065) == 40.0


def test_correct_expressions_49():
    calculator = Model()
    calculator.parse_expression("sqrt(16)modx+cos(0)+sin(3.14159/2)")
    assert calculator.calculate(4641) == 5.99999999999912


def test_correct_expressions_50():
    calculator = Model()
    calculator.parse_expression("tan(3.14159/4)+acos(1)-asin(0)*x")
    assert calculator.calculate(4033) == 0.9999986732059836


def test_correct_expressions_51():
    calculator = Model()
    calculator.parse_expression("atan(1)+ln(1)*log(10)/x")
    assert calculator.calculate(1924) == 0.7853981633974483


def test_correct_expressions_52():
    calculator = Model()
    calculator.parse_expression("x^3*5+15-x+sqrt(16)")
    assert calculator.calculate(1810) == 29648703209.0


def test_correct_expressions_53():
    calculator = Model()
    calculator.parse_expression("cos(X)-1modx+sin(3.14159/2)*tan(3.14159/4)")
    assert calculator.calculate(3398) == 0.359324287215802


def test_correct_expressions_54():
    calculator = Model()
    calculator.parse_expression("acos(1)+asin(0)^atan(1)+ln(1)")
    assert calculator.calculate() == 0.0


def test_correct_expressions_55():
    calculator = Model()
    calculator.parse_expression("log(10)*2^3*5+x-4")
    assert calculator.calculate(162) == 198.0


def test_correct_expressions_56():
    calculator = Model()
    calculator.parse_expression("sqrt(16)-cos(0)+sin(3.14159/2)")
    assert calculator.calculate() == 3.99999999999912


def test_correct_expressions_57():
    calculator = Model()
    calculator.parse_expression("tan(3.14159/4)+acos(1)*asin(0)")
    assert calculator.calculate() == 0.9999986732059836


def test_correct_expressions_58():
    calculator = Model()
    calculator.parse_expression("atan(1)+ln(1)/log(10)")
    assert calculator.calculate() == 0.7853981633974483


def test_correct_expressions_59():
    calculator = Model()
    calculator.parse_expression("2^3*5+x-4+sqrt(16)")
    assert calculator.calculate(4299) == 4339.0


def test_correct_expressions_60():
    calculator = Model()
    calculator.parse_expression("( 2 + 3 ) * 5 + x - 4  mod  2")
    assert calculator.calculate(2896) == 2921


def test_correct_expressions_61():
    calculator = Model()
    calculator.parse_expression(" X ^ 3 * 5+15-x+sqrt(16) ")
    assert calculator.calculate(1810) == 29648703209.0


def test_correct_expressions_62():
    calculator = Model()
    calculator.parse_expression("2 ^ 2 ^ 3 ")
    assert calculator.calculate() == 256


def test_correct_expressions_63():
    calculator = Model()
    calculator.parse_expression("(5+2.3e4)/(3.5-1.2e2)")
    assert calculator.calculate() == -197.46781115879827


def test_correct_expressions_64():
    calculator = Model()
    calculator.parse_expression("(4.5e3+2)*(6.7e2-3.2e-4)")
    assert calculator.calculate() == 3016338.55936


def test_correct_expressions_65():
    calculator = Model()
    calculator.parse_expression("(2.1e5^3)/(x-2.3e2)")
    assert calculator.calculate(6550) == 1465348101265.8228


def test_correct_expressions_66():
    calculator = Model()
    calculator.parse_expression("(7.6e3mod5)+(3.4e4mod2)")
    assert calculator.calculate() == 0.0


def test_correct_expressions_67():
    calculator = Model()
    calculator.parse_expression(
        "sin(0.5235987755982988)+cos(0.7853981633974483)")
    assert calculator.calculate() == 1.2071067811865475


def test_correct_expressions_68():
    calculator = Model()
    calculator.parse_expression(
        "tan(1.0471975511965976)-sin(1.5707963267948966)")
    assert calculator.calculate() == 0.7320508075688767


def test_correct_expressions_69():
    calculator = Model()
    calculator.parse_expression("asin(1)+acos(0)")
    assert calculator.calculate() == 3.141592653589793


def test_correct_expressions_70():
    calculator = Model()
    calculator.parse_expression("atan(1)-asin(0.5)")
    assert calculator.calculate() == 0.26179938779914935


def test_correct_expressions_71():
    calculator = Model()
    calculator.parse_expression("ln(2.3e+4)+log(7.6e3)")
    assert calculator.calculate() == 13.924063087192078


def test_correct_expressions_72():
    calculator = Model()
    calculator.parse_expression(
        "(sin(0.7853981633974483)+3.4e2)*(log(100)^3)/(xmod3)")
    assert calculator.calculate(5710) == 2725.6568542494924


def test_correct_expressions_73():
    calculator = Model()
    calculator.parse_expression("acos(0.5)-(2.3e3/ln(5))")
    assert calculator.calculate() == -1428.0231519359106


def test_correct_expressions_74():
    calculator = Model()
    calculator.parse_expression(
        "(tan(1.0471975511965976)+1.2e-2)*(2.3e4^2)/(5mod3)+4.8e+4")
    assert calculator.calculate() == 461349438.60196793


def test_correct_expressions_75():
    calculator = Model()
    calculator.parse_expression("asin(0.5)+(4.5e-3*ln(2))")
    assert calculator.calculate() == 0.5267179379108187


def test_correct_expressions_76():
    calculator = Model()
    calculator.parse_expression("(atan(1)+3.4e4)*(2.3e2^3)/(7mod2)")
    assert calculator.calculate() == 413687555939.45404


def test_correct_expressions_77():
    calculator = Model()
    calculator.parse_expression("ln(7.6e3)+log(100)*cos(0.7853981633974483)")
    assert calculator.calculate() == 10.350117088647519


def test_correct_expressions_78():
    calculator = Model()
    calculator.parse_expression(
        "(sin(0.5235987755982988)+2.1e5)*(3.4e4^2)/(50e-1mod2)")
    assert calculator.calculate() == 242760578000000.0


def test_correct_expressions_79():
    calculator = Model()
    calculator.parse_expression("acos(0.5)-(2.3e3/ln(4.5e3))")
    assert calculator.calculate() == -272.377166514941


def test_correct_expressions_80():
    calculator = Model()
    calculator.parse_expression(
        "(tan(0.7853981633974483)+1.2e2)*(7.6e3^2)/(3mod2)")
    assert calculator.calculate() == 6988960000.0


def test_correct_expressions_81():
    calculator = Model()
    calculator.parse_expression("asin(0.5)+(2.1e5*ln(2))")
    assert calculator.calculate() == 145561.4315163641


def test_correct_expressions_82():
    calculator = Model()
    calculator.parse_expression("(atan(1)+6.7e-2)*(3.4e+4^3)/(7mod3)")
    assert calculator.calculate() == 33502657414173.305


def test_correct_expressions_83():
    calculator = Model()
    calculator.parse_expression(
        "(x+2.3e4)/(X-1.2e2)+1.1e-1^(2*1.0471975511965976)")
    assert calculator.calculate(8106) == 3.9048905738199187


def test_correct_expressions_84():
    calculator = Model()
    calculator.parse_expression(
        "(4.5e3+2)*(6.7e2-3.2e4)+sin(20.943951023931955)+cos(41.88790204786391)")
    assert calculator.calculate() == -141047659.63397458


def test_correct_expressions_85():
    calculator = Model()
    calculator.parse_expression("(2.1e5^3)/(x-2.3e2)+tan(62.831853071795855)")
    assert calculator.calculate(1580) == 6860000000000.0


def test_correct_expressions_86():
    calculator = Model()
    calculator.parse_expression("(7.6e3mod5)+(3.4e4mod2)-asin(1)-acos(0)")
    assert calculator.calculate() == -3.141592653589793


def test_correct_expressions_87():
    calculator = Model()
    calculator.parse_expression(
        "sin(0.5235987755982988)+cos(0.7853981633974483)-atan(1)+acos(0)")
    assert calculator.calculate() == 1.9925049445839957


def test_correct_expressions_88():
    calculator = Model()
    calculator.parse_expression(
        "tan(1.0471975511965976)-sin(1.5707963267948966)+ln(2.3e4)-log(7.6e3)")
    assert calculator.calculate() == 6.894486710199372


def test_correct_expressions_89():
    calculator = Model()
    calculator.parse_expression(
        "(sin(0.7853981633974483)+3.4e2)*(log(100)^3)/(7mod3)+8.4e2^(1.5707963267948966)")
    assert calculator.calculate() == 41940.20011530107


def test_correct_expressions_90():
    calculator = Model()
    calculator.parse_expression(
        "acos(0.5)-(2.3e3/ln(5))+tan(62.831853071795855)")
    assert calculator.calculate() == -1428.0231519359106


def test_correct_expressions_91():
    calculator = Model()
    calculator.parse_expression(
        "(tan(1.0471975511965976)+1.2e2)*(2.3e4^2)/(5mod3)+asin(0.5)")
    assert calculator.calculate() == 32198127439.12557


def test_correct_expressions_92():
    calculator = Model()
    calculator.parse_expression("(atan(1)+3.4e4)*(2.3e2^3)/(7mod2)+ln(7.6e3)")
    assert calculator.calculate() == 413687555948.38995


def test_correct_expressions_93():
    calculator = Model()
    calculator.parse_expression("(1.2e1 * 2) + (2.1e2 / 8.1e0)")
    assert calculator.calculate() == 49.925925925925924


def test_correct_expressions_94():
    calculator = Model()
    calculator.parse_expression("1/x")
    with pytest.raises(ValueError, match=r"Division by zero"):
        calculator.calculate()
    assert calculator.calculate(2) == 0.5
