# -*- coding: utf-8 -*-
"""

@author: Steinn Ymir Agustsson
"""
import matplotlib.pyplot as plt

def main():
    pass

def plot_lines(data,  normalization='None', range=None, color_range=(0,1),
               x_label='',y_label='', xlim=None, ylim=None,
               savefig=False, save_dir='E:/data/FLASH/', save_name='fig', static_curve=None):
    """

    :param data:
    :param normalization:
    :param range:
    :param color_range:
    :return:
    """
    f, axis = plt.subplots(1, 1, figsize=(8, 6), sharex=True)

    if range is None:
        from_ = 0
        to_= len(data[:,...])
    else:
        from_ = range[0]
        to_ = range[1]


    n_curves = len(data[from_:to_,0])
    print(n_curves)
    cm_subsection = np.linspace(color_range[0], color_range[1], n_curves)
    colors = [cm.coolwarm(1 - x) for x in cm_subsection]

    for i, color in enumerate(colors[from_:to_]):
        label = '{}'.format(i)  # 20*(i+from_),
        curve = data[i + from_, :]  # result_unpumped[i]
        if normalization == 'sum':
            curve /= curve.sum()
        elif normalization == 'max':
            curve /= curve.max()

        axis.plot(curve, '-', color=color, label=label)
    #    axis[1].plot(x_axis_energy,curve_pump, '-', color=color,label=label)
    if static_curve is not None:
        plt.plot(static_curve, '--', color='black', label='static')
    plt.grid()
    plt.legend(fontsize='large')
    plt.xlabel(x_label, fontsize='xx-large')
    plt.ylabel(y_label, fontsize='xx-large')
    plt.xticks(fontsize='large')
    plt.yticks(fontsize='large')
    if xlim is not None:
        plt.xlim(xlim[0],xlim[1])
    if ylim is not None:
        plt.ylim(ylim[0],ylim[1])

    if savefig:
        plt.savefig('{}{}.png'.format(save_dir,save_name), dpi=200, facecolor='w',
                edgecolor='w',
                orientation='portrait', papertype=None, format=None,
                transparent=True, bbox_inches=None, pad_inches=0.1,
                frameon=None)
    plt.show()

if __name__ == '__main__':
    main()
