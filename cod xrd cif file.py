import numpy as np
import matplotlib.pyplot as plt
from pymatgen.ext.matproj import MPRester
from pymatgen.io.cif import CifParser
from pymatgen.analysis.diffraction.xrd import XRDCalculator
import json

# Load CIF file
cif_file_name="1000099.cif"
parser = CifParser(cif_file_name)
structure = parser.parse_structures()[0]

# Initialize XRD calculator
xrd_calculator = XRDCalculator()

# Calculate XRD pattern
xrd_pattern = xrd_calculator.get_pattern(structure,two_theta_range=None)

# Extract angles and intensities
angles = xrd_pattern.x
intensities = xrd_pattern.y

# Define the range of angles based on the minimum and maximum values
min_angle = min(angles)
max_angle = max(angles)
x_range = np.arange(min_angle-5, max_angle+5, 0.01)


# Initialize intensity values to zeros
y_values = np.zeros_like(x_range)

# Find the indices in the x_range that correspond to the angles from the XRD pattern
indices = np.searchsorted(x_range, angles)

# Assign the intensities from the XRD pattern to the corresponding indices in the y_values array
y_values[indices] = intensities

data = {
    "x": xrd_pattern.x.tolist(),
    "y": xrd_pattern.y.tolist()
}

json_data = json.dumps(data)

with open(f"{cif_file_name}.json", 'w') as file:
    file.write(json_data)

# Plot XRD pattern
plt.figure(figsize=(10, 6))
plt.plot(x_range, y_values, color='b', linewidth=2)
plt.xlabel('2θ (degrees)')
plt.ylabel('Intensity (a.u.)')
plt.title('XRD Pattern')
plt.grid(True)
plt.show()