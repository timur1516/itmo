from matplotlib import pyplot as plt

def plot_part_2(data, name):
    plt.plot(data)
    plt.title('График числовой последовательности')
    plt.xlabel('Индекс')
    plt.ylabel('Значение')
    plt.tight_layout()
    plt.savefig(f'lab1/img/{name}', dpi=300)
    plt.clf()