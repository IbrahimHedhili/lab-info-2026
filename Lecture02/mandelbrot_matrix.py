import numpy as np
import matplotlib.pyplot as plt
import sys
import time

def get_parameters(min_radius, min_angle):
    # Returns a 1D array of evenly spaced complex number, angle in degrees
    radii_counter = int(2/min_radius)
    angles_counter = int(360/min_angle)
    radii  = np.linspace(min_radius, 2, radii_counter)
    angles = np.linspace(0, 2*np.pi, angles_counter, endpoint=False)
    
    unit_parameters = np.exp(angles*1j) # e^(i*theta) like numbers

    params = np.empty((radii_counter, angles_counter), dtype=complex)
    for r in range(radii_counter):
            params[r, :] = radii[r]*unit_parameters
    
    return params


def get_mandelbrot_set(N: int, parameters):
    z = parameters
    r,c = parameters.shape
    Maschera_booleana = np.full((r,c), True)

    for i in range(N):
        z = z**2 + parameters
        scappati = np.abs(z) >  2 
        scappati = scappati & Maschera_booleana
        Maschera_booleana[scappati] = False
        z[scappati] = np.nan

    return z


def graphXY(mandelbrot_numbers, my_parameters, m_rows, m_columns):
    x_data = []
    y_data = []
    for r in range(m_rows):
        for c in range(m_columns):
            if np.isfinite(mandelbrot_numbers[r, c]):
                x_data.append(np.real(my_parameters[r, c]))
                y_data.append(np.imag(my_parameters[r, c]))
    return x_data, y_data




print("Starting timer")
start_timer = time.time()
iter = 100
my_parameters = get_parameters(min_radius=0.001, min_angle=0.1)
mandelbrot_numbers = get_mandelbrot_set(N=iter, parameters=my_parameters)

m_rows, m_columns = my_parameters.shape

x_data, y_data = graphXY(mandelbrot_numbers, my_parameters, m_rows, m_columns)

print(f"Used {m_rows * m_columns} parameters and performed {m_rows * m_columns * iter} calculations")

end_timer = time.time()
print(f"Time to execute the script = {((end_timer - start_timer)):.4} seconds")

plt.scatter(x_data, y_data, s=3, color="red")
plt.show()