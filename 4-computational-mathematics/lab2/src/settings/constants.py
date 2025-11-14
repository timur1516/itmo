from lab2.src.method.equation_methods import chord_method, secant_method, simple_iteration_method
from lab2.src.method.system_methods import newton_method

MODES = ['Нелинейное уравнение', 'Система нелинейных уравнений']
EQ_METHODS_STRS = ['Метод хорд', 'Метод секущих', 'Метод простых итераций']
EQ_METHODS = [chord_method, secant_method, simple_iteration_method]
SYS_METHODS_STRS = ['Метод Ньютона']
SYS_METHODS = [newton_method]
IO_METHODS = ['Консоль', 'Файл']
