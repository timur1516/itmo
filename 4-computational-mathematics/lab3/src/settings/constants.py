from lab3.core.methods import rectangles_method_right, rectangles_method_left, rectangles_method_middle, \
    trapezoid_method, simpson_method

METHODS_STRS = ['Метод прямоугольников (левый)', 'Метод прямоугольников (правый)', 'Метод прямоугольников (средний)',
                'Метод трапеций', 'Метод Симпсона']
METHODS = [rectangles_method_left, rectangles_method_right, rectangles_method_middle, trapezoid_method, simpson_method]
METHODS_RUNGE_K = [1, 1, 2, 2, 4]
