# Students reading this: Don't edit anything in here!

import numpy as np
from ipywidgets import interact, FloatSlider, IntSlider
from scipy.stats import norm
import matplotlib.pyplot as plt
from IPython.display import display, HTML, IFrame, clear_output
import babypandas as bpd
import folium

# Don't change this cell; just run it.
def plot_meteorites(meteorite_df, center=(39.0, -0), zoom=2):
    m = folium.Map(location=center, min_zoom=2, zoom_start=zoom, max_bounds=True)
    for _, row in meteorite_df.get(['latitude', 'longitude', 'name', 'seen_falling'])._pd.iterrows():
        folium.CircleMarker(
            location=[row['latitude'], row['longitude']],
            popup=row['name'], 
            color='orange' if row['seen_falling'] else 'blue',
            alpha=0.2,
            radius=3, 
            fill=True
        ).add_to(m)
    display(m)

def faster_perm_test():
    html_string = '''
    <iframe src="https://docs.google.com/presentation/d/1DxLk33J26gtzmkhJISLFSGVz_ioYlDYUBTIjJ5J_YMg/embed?start=false&loop=false&delayms=3000&rm=minimal"
    frameborder="0" width="810" height="455" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"
    style="clip-path: inset(15px 5.5px 25px 5px);">
    '''
    display(HTML(html_string))

def cdf_ppf_interact(z_value):
    z = np.linspace(-3.5, 3.5)
    fig, ax = plt.subplots(2, 1, figsize=(6, 6), gridspec_kw={'hspace': 0.3, 'height_ratios': [1, 2]})
    plt.xlabel('z')
    
    
    ax[0].set_title('Standard Normal Distribution')
    pdf_line = ax[0].plot(z, norm.pdf(z), color='C0')
    pdf_text = ax[0].text(0, 0, '', ha='center', va='bottom')
    

    ax[1].set_title(f'Cumulative Distribution Function (CDF)', zorder=0)
    cdf_baseline = ax[1].plot(z, norm.cdf(z), color='pink')
    cdf_text = ax[1].text(0, 0, '', ha='left', va='bottom', bbox=dict(facecolor='white', alpha=0.9))
    
    
    cdf = norm.cdf(z_value)
    
    shade_lower_bound = np.linspace(-3.5, z_value)
    shade_upper_bound = norm.pdf(shade_lower_bound)       
    shaded_area = ax[0].fill_between(shade_lower_bound, 0, shade_upper_bound, color='red', alpha=0.3)
    pdf_text.set_text(f'area under the curve = {cdf:.2f}')
    
    updated_x_values = np.linspace(-3.5, z_value)
    cdf_line = ax[1].plot(updated_x_values, norm.cdf(updated_x_values), color='tab:red')

    cdf_vertical = ax[1].vlines(x=z_value, ymin=0, ymax=cdf, color='black', linestyles='dashed', zorder=10)

    cdf_horizontal = ax[1].hlines(y=cdf, xmin=-3.5, xmax=z_value, color='black', linestyles='dashed', zorder=10)

    cdf_dot = cdf_dot = ax[1].scatter(x=z_value, y=cdf+0.002, color='black', zorder=10)

    cdf_text.set_text(f'norm.cdf({z_value:.2f}) = {cdf:.2f} = area under standard normal curve\nnorm.ppf({cdf:.2f}) = {z_value:.2f} = z')
    cdf_text.set_position((-3.5, cdf + 0.05))

    plt.show()


def decadal_interact(decade, df):
    seen_since = df[df.get('year') >= 1900]
    n = seen_since[seen_since.get('decade') == decade].shape[0]
    
    simulated_medians = np.array([])
    for i in np.arange(1000):
        simulated_median = seen_since.sample(n).get('mass').median()
        simulated_medians = np.append(simulated_medians, simulated_median)
        
    observed_median = seen_since[seen_since.get('decade') == decade].get('mass').median()
    decadal_p_value = np.count_nonzero(simulated_medians <= observed_median) / len(simulated_medians)
    
    
    bpd.DataFrame().assign(simulated_medians=simulated_medians).plot(kind='hist', density=True, bins=30, ec='w', figsize=(10, 5))
    plt.axvline(x=observed_median, color='black', label=f'observed_median (p-value: {decadal_p_value:.4f})')
    plt.xlabel(f"Decade = {decade}")
    plt.legend();
    plt.show()
