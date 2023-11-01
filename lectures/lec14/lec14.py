# Originally written by... I don't know? Janine? NOPE. Justin?
# Modified in Winter 2022 by Suraj to draw histograms

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation

def sampling_animation(population, sample_size):
    sizes = np.arange(1, 251, 5)
    means = np.array([])
    np.random.seed(4242)
    for _ in range(sizes[-1]):
        s = population.sample(sample_size)
        m = s.get('Delay').mean()
        means = np.append(means, m)

    bins = np.arange(10, 25, 1)
    n, _ = np.histogram(means[:1], bins)

    def prepare_animation(bar_container):
        def animate(i):
            plot_data = means[:sizes[i]]
            n, _ = np.histogram(plot_data, bins)
            for count, rect in zip(n, bar_container.patches):
                rect.set_height(count)
            return bar_container.patches
        return animate

    fig, ax = plt.subplots(figsize=(10, 5))
    _, _, bar_container = ax.hist(means, bins, density=True,
                                  ec='w');
    ax.set_ylim(top=100)

    ani = FuncAnimation(fig, 
                                  prepare_animation(bar_container), 
                                  frames=50,
                                  repeat=False, blit=True);

    return ani, means
