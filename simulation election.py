# load packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Set underlying parameters
n = 10000  # number of trials (double used — could make this two different ones)
p = 0.48   # baseline probability
bw = 0.001 # bin width

# Create table
tab = pd.DataFrame({
    'sim': np.arange(1, 10001),
    'wins': np.zeros(10000)
})

# Simulate
np.random.seed(42) # set seed for reproducibility
tab['wins'] = np.random.binomial(n, p, 10000)  # corrected to match the size of simulations (10000)

# Calculate the 95% CI
lower_bound = np.quantile(tab['wins'] / n, 0.025)
upper_bound = np.quantile(tab['wins'] / n, 0.975)

# Start plot
plt.figure(figsize=(10,6))
# Frequency polygon (Histogram)
counts, bins, _ = plt.hist(tab['wins'] / n, bins=np.arange(0, 1, bw), histtype='step', density=True, color='blue')

# Calculate bin midpoints for the fill_between
bin_midpoints = (bins[:-1] + bins[1:]) / 2

# Add the 95% CI lines
plt.axvline(x=lower_bound, linestyle='--', color='red')
plt.axvline(x=upper_bound, linestyle='--', color='red')

# Highlight the area between the confidence intervals
plt.fill_between(bin_midpoints, 0, counts, where=(bin_midpoints >= lower_bound) & (bin_midpoints <= upper_bound), color='gray', alpha=0.2)

# Set x-axis limits from 46% to 50%
plt.xlim(0.46, 0.50)

# Labels and formatting
plt.xlabel('Simulated Trump win probability')
plt.xticks(np.arange(0.46, 0.51, 0.01), [f'{x:.0%}' for x in np.arange(0.46, 0.51, 0.01)])
plt.gca().yaxis.set_visible(False)  # Hide the y-axis

# export as png
plt.savefig('simulation_plot_py.png', dpi=300, bbox_inches='tight')

# show it
plt.tight_layout()
plt.show()
