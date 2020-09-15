import numpy as np, calculator, pytest

def test_add_int():
    assert calculator.add(1, 2) == 3                                            #test_add_exercise_1

def test_add_float():
        assert np.abs(calculator.add(0.1,0.2) - 0.3) < 1e-8                     #test_add_exercise_2

def test_add_string():                                                          #test_add_exercise_3
    assert calculator.add("Hello ","World") == "Hello World"

def test_factorial():                                                           #test_factorial_exercise_4
    assert calculator.factorial(5) == 120

def test_sin():                                                                 #test_sin_exercise_4
    assert np.abs(calculator.sin(5*np.pi/6, 20) - 0.5) < 1e-8

def test_divide():                                                              #test_divide_exercise_4
    assert calculator.divide(21,7) == 3

def test_subtract():                                                            #test_subtract_exercise_4
    assert calculator.subtract(7, 5) == 2

def test_times():                                                               #test_times_exercise_4
    assert calculator.times(2, 5) == 10

def test_add_string_number():                                                   #test_add_string_and_number_exercise_5
    with pytest.raises(TypeError):
        calculator.add("Hello", 2)

def test_divide_by_zero():                                                      #test_division_by_zero_exercise_5
    with pytest.raises(ZeroDivisionError):
        calculator.divide(2,0)


"----------------------------------- Exercise_6 ------------------------------------"

@pytest.mark.parametrize(
    "arg, expected_output", [[(-1, -1), -2], [(1, 1), 2], [(1, 0), 1]]
)
def test_add_parameterized(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output", [[(0.4, 0.2), 0.6], [(-0.3, 0.4), 0.1], [(0.1, 0.3), 0.4]]
)
def test_add_float_parameterized(arg, expected_output):
    assert np.abs(calculator.add(arg[0], arg[1]) - expected_output) < 1e-8


@pytest.mark.parametrize(
    "arg, expected_output", [[("Hi I'm", " hungry."), "Hi I'm hungry."], [("Hey ", ":)"), "Hey :)"], [("I am ", "running."), "I am running."]]
)
def test_add_string_parameterized(arg, expected_output):
    assert calculator.add(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output", [[(3), 6], [(4), 24], [(2), 2]]
)
def test_factorial_parameterized(arg, expected_output):
    assert calculator.factorial(arg) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output", [[(np.pi/6, 20), 1/2], [(np.pi/2, 20), 1], [(np.pi, 20), 0]]
)
def test_sin_parameterized(arg, expected_output):
    assert np.abs(calculator.sin(arg[0], arg[1]) - expected_output) < 1e-8


@pytest.mark.parametrize(
    "arg, expected_output", [[(2, 1), 2], [(20, 2), 10], [(140, 7), 20]]
)
def test_divide_parameterized(arg, expected_output):
    assert calculator.divide(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output", [[(2, 1), 1], [(-6, -5), -1], [(4, 9), -5]]
)
def test_subtract_parameterized(arg, expected_output):
    assert calculator.subtract(arg[0], arg[1]) == expected_output


@pytest.mark.parametrize(
    "arg, expected_output", [[(2, -4), -8], [(3, 5), 15], [(-5, -6), 30]]
)
def test_times_parameterized(arg, expected_output):
    assert calculator.times(arg[0], arg[1]) == expected_output
