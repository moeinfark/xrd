from mp_api.client import MPRester
from pymatgen.analysis.diffraction.xrd import XRDCalculator
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
import matplotlib.pyplot as plt
import numpy as np
import json
import os
from dotenv import load_dotenv, dotenv_values

load_dotenv()

# Initialize MPRester with your Materials Project API key
api_key = os.getenv("MP_API_KEY")
mpr = MPRester(api_key)

material_id = "mp-1008728"
# Retrieve the relevant structure
structure = mpr.get_structure_by_material_id(material_id)

# Use the conventional structure to ensure that peaks are labelled with the conventional Miller indices
sga = SpacegroupAnalyzer(structure)
conventional_structure = sga.get_conventional_standard_structure()

# Obtain an XRD diffraction pattern
calculator = XRDCalculator(wavelength="CuKa")
pattern = calculator.get_pattern(conventional_structure,two_theta_range=None)

# Define the x-axis range
x_min = min(pattern.x)
x_max = max(pattern.x)
x_range = np.linspace(x_min, x_max, num=1000)

# Initialize intensity values to zeros
y_values = np.zeros_like(x_range)

# Find the indices in the x_range that correspond to the angles from the XRD pattern
indices = np.searchsorted(x_range, pattern.x)

# Assign the intensities from the XRD pattern to the corresponding indices in the y_values array
y_values[indices] = pattern.y

data = {
    "x": pattern.x.tolist(),
    "y": pattern.y.tolist()
}

json_data = json.dumps(data)

with open(f"{material_id}.json", 'w') as file:
    file.write(json_data)

# Plot XRD pattern
plt.figure(figsize=(10, 6))
plt.plot(x_range, y_values, color='blue')
plt.xlabel('2-Theta (degrees)')
plt.ylabel('Intensity')
plt.title('XRD Pattern')
plt.grid(True)
plt.show()
