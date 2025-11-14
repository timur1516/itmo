from scipy.optimize import root

from lab2.src.io.util import *
from lab2.src.settings.config import LOG_DECIMALS
from lab2.src.settings.constants import *
from lab2.src.settings.equations import EQUATIONS
from lab2.src.settings.systems import SYSTEMS
from lab2.src.util.drawers import draw_equation, draw_system


def main():
    mode = choose_options('Выберите что будете решать', MODES)

    if mode == 1:
        equation_id = choose_options('Выберите уравнение', EQUATIONS) - 1
        method_id = choose_options('Выберите метод', EQ_METHODS_STRS) - 1
        method = EQ_METHODS[method_id]
        equation = EQUATIONS[equation_id]
        reader = create_reader()
        a, b = read_root_limits(reader)

        if not equation.is_single_root_exist(a, b):
            raise Exception('На выбранном отрезке нет корней либо их больше одного')

        eps = read_eps(reader)
        result = method(equation, a, b, eps)
        writer = create_writer()
        real_root = root(equation.f, (a + b) / 2).x[0]
        print_result(result, real_root, writer, LOG_DECIMALS)
        draw_equation(result.x, a, b, equation)

    if mode == 2:
        system_id = choose_options('Выберите систему', SYSTEMS) - 1
        method_id = choose_options('Выберите метод', SYS_METHODS_STRS) - 1
        reader = create_reader()
        initial_point = read_initial_point(reader, SYSTEMS[system_id].n)
        eps = read_eps(reader)
        system = SYSTEMS[system_id]
        method = SYS_METHODS[method_id]
        result = method(system, initial_point, eps)
        writer = create_writer()
        real_root = root(system.get_value, initial_point).x.tolist()
        print_result(result, real_root, writer, LOG_DECIMALS)
        draw_system(result.x, initial_point, system)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
