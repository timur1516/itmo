import os

import numpy as np

from lab1.src.part1 import latex_part_1
from lab1.src.part2 import plot_part_2
from lab1.src.part3 import latex_part_3, plot_part_3
from lab1.src.part4 import plot_part_4
from lab1.src.part5 import latex_part_5
from lab1.src.part6 import do_part_6
from lab1.src.part7 import do_part_7


def main():
    data = np.loadtxt("lab1/data/data.txt")

    tex1 = latex_part_1(data)
    print(f'\n{tex1}\n')

    plot_part_2(data, 'part2.png')

    tex3 = latex_part_3(data)
    print(f'\n{tex3}\n')
    plot_part_3(data, 'part3.png')

    plot_part_4(data, 'part4.png')

    latex_part_5(data)

    generated_data = do_part_6(data)

    do_part_7(data, generated_data)


if __name__ == '__main__':
    main()
