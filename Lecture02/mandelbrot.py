import numpy as np
import matplotlib.pyplot as plt
import sys
#from numba import jit, prange


def get_parameters(min_radius, min_angle):
    # Returns a 1D array of evenly spaced complex number, angle in degrees
    radii_counter = int(2/min_radius)
    angles_counter = int(360/min_angle)
    radii  = np.linspace(min_radius, 2, radii_counter)
    angles = np.linspace(0, 2*np.pi, angles_counter, endpoint=False)
    
    unit_parameters = np.exp(angles*1j) # e^(i*theta) like numbers
    parameters = np.empty(radii_counter*angles_counter+1, dtype=complex)
    parameters[0] = 0
    for i in range(len(radii)): # Assign a block of size angles*counter
        parameters[1+i*angles_counter : 1+(i+1)*angles_counter] = radii[i]*unit_parameters
    
    return parameters

#@jit(nopython=True, parallel=True)
def get_mandelbrot_set(N: int, parameters):
    z = parameters
    for i in range(N):
        z = z**2 + parameters
        for j in range(len(z)):
            if np.abs(z[j]) > 2:
                z[j] = np.nan
    
    return z

iter = 100
my_parameters = get_parameters(min_radius=0.01, min_angle=0.1)
mandelbrot_numbers = get_mandelbrot_set(N=iter, parameters=my_parameters)

x_data = []
y_data = []
for i in range(len(my_parameters)):
    if np.isfinite(mandelbrot_numbers[i]):
        x_data.append(np.real(my_parameters[i]))
        y_data.append(np.imag(my_parameters[i]))

print(f"Used {len(my_parameters)} parameters and performed {len(my_parameters)*iter} calculations")
plt.scatter(x_data, y_data, s=0.5, color="red")
plt.show()