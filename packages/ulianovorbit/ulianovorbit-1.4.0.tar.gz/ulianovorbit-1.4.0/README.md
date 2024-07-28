# UlianovOrbit

## Overview

The **UlianovOrbit** repository contains two Python libraries designed for modeling and analyzing elliptical orbits using the Ulianov Orbital Model (UOM). This model offers a simplified approach to celestial mechanics by utilizing the Ulianov Ellipse Parameter (\(U_e\)) and Ulianov Elliptical Trigonometric Functions. The UOM reduces the complexity traditionally associated with orbital models, making it particularly useful for scenarios such as satellite launches, close encounters, or collision avoidance.

## Libraries

### 1. ulianovellips.py

This library provides functions and classes essential for handling Ulianov elliptical functions, which are crucial for modeling and analyzing elliptical orbits in the UOM. It includes calculations for Ulianov Elliptical Cosine and Sine, conversions between different parameter sets, and various other tools for working with ellipses in a general context.

#### Key Functions:
- `cosuell`: Computes the Ulianov Elliptical Cosine function.
- `sinuell`: Computes the Ulianov Elliptical Sine function.
- `calc_Ue`: Calculates the Ulianov Ellipse Parameter (\(U_e\)).
- `calc_ab`: Converts Ulianov parameters to standard ellipse parameters \(a\) and \(b\).
- `rotate_axis`: Rotates the coordinates in the (x, y) plane.
- `ulianov_ellipse_ue`: Represents the Ulianov ellipse using \(U_e\).
- `ulianov_ellipse_ab`: Represents the Ulianov ellipse using \(a\) and \(b\).
- `ellipse_ab`: Calculates parameters for the standard ellipse.
- `ellipse_ue`: Calculates parameters for the Ulianov ellipse.

### 2. ulianovorbit.py

This library focuses on calculating orbital parameters using the Ulianov Orbital Model. It includes routines for both 2D and 3D orbital calculations, providing methods to derive parameters from velocity and position data. The main classes, `uom_params` and `orbit_vect`, store model parameters and orbital vectors, respectively.

#### Key Functions:
- `calc_time`: Calculates time and corresponding position and velocity for a given angle.
- `calc_angle`: Calculates angle and corresponding position and velocity for a given time.
- `calc_orb_angle`: Calculates orbit positions and velocities over a range of angles.
- `calc_orb_time`: Calculates orbit positions and velocities over a range of times.
- `kepler_to_ulianov`: Converts Keplerian parameters to Ulianov parameters.
- `kepler_to_ulianov_6p`: Converts all six Keplerian parameters to Ulianov parameters.
- `ulianov_to_kepler`: Converts Ulianov parameters to Keplerian parameters.
- `get_UOM_params_2D_vel`: Calculates UOM parameters from a 2D velocity vector (to be implemented).
- `get_UOM_params_2D_pos`: Calculates UOM parameters from two 2D position vectors (to be implemented).
- `get_UOM_params_3D_vel`: Calculates UOM parameters from a 3D velocity vector (to be implemented).
- `get_UOM_params_3D_pos`: Calculates UOM parameters from two 3D position vectors (to be implemented).

## Getting Started

To use these libraries, clone this repository and install the necessary packages using pip:

```bash
pip install ulianovellipse
pip install ulianovorbit
```

### Example of Use

To utilize the routines, import the desired modules at the beginning of your Python program:

```python
import numpy as np
from ulianovellipse import eu
from ulianovorbit import ou
from ulianovorbit import uom_params, orbit_vect

# Define the mass of the celestial body being orbited (Earth's mass in kg)
M1 = 5.972e24

# Define the minimum orbital distance (R0) and initial velocity (V0)
R0 = 1e8
V0 = 2500

# Calculate the Ulianov Ellipse Parameter (Ue) and other parameters
Ue = ou.calc_Ue(R0, V0, M1)

# Convert the Ulianov parameters to semi-major (a) and semi-minor (b) axes
a, b = eu.calc_ab(R0, Ue)

# Calculate the mass using semi-major axis, semi-minor axis, and initial velocity
Mab = ou.calc_mass_ab_v0(a, b, V0)

# Calculate the orbital periods using different methods
TKepler = ou.calc_orbit_time_ab_m(a, M1)       # Kepler's formula
Torb1 = ou.calc_orbit_time_ab_v0(a, b, V0)     # Using velocity
Torb2 = ou.calc_orbit_time_r0v0_m(R0, V0, M1)  # Using R0 and V0

# Define the parameters for the orbit using the uom_params class
param = uom_params(R0=R0, V0=V0, Ue=Ue, ang_i=0, ang_omega=0, ang_ell=0, time_alpha0=0)

# Calculate the orbital trajectory and velocities
orbit1 = ou.calc_orb_angle(param, alpha0_dg=0, alpha_max_dg=360, delta_alpha_dg=0.01)

# Find the maximum x-component of the velocity in the calculated trajectory
mx = max(orbit1.v_x)
```


## Ulianov Oorit Model (UOM) Python Routines Implementation

The Ulianov Orbital Model (UOM) was implemented using Python, providing a library named `ulianovorbit.py`. This library defines several objects and routines for modeling and analyzing elliptical orbits.

### UOM Python Objects

The Python objects in `ulianovorbit.py` are defined using the `class` attribute. Two main classes are:

**uom_params class:**
This class defines the UOM parameters such as \(R_0\), \(V_0\), \(U_e\), inclination angle \(i\), longitude of the ascending node angle \(\Omega\), ellipse angle \(E_{ang}\), and the time associated with angle \(\alpha = 0\) (\(t_0\)).

```python
class uom_params:
    def __init__(self, R0=1, V0=1, Ue=1, ang_i=0, ang_omega=0, ang_ell=0, time_alpha0=0):
        self.R0 = R0
        self.Ue = Ue
        self.V0 = V0
        self.ang_i = ang_i
        self.ang_omega = ang_omega
        self.ang_ell = ang_ell
        self.time_alpha0 = time_alpha0
```

**orbit_vect class:**
This class organizes the results obtained by UOM routines, defining vectors to store data: ellipse positions (\(e_x\), \(e_y\), \(e_z\)) and velocities (\(v_x\), \(v_y\), \(v_z\)). For the 2D case, the \(z\) values are defined as zero. Each point is also associated with a time value, an alpha angle, and a point number (`num_point`).

```python
class orbit_vect:
    def __init__(self):
        self.e_x = []
        self.e_y = []
        self.e_z = []
        self.v_x = []
        self.v_y = []
        self.v_z = []
        self.alpha = []
        self.time = []
        self.num_point = []
```

### UOM Python Orbit Calculations

The UOM includes routines to obtain orbit positions and velocities as functions of time and angle.

**Routines to Obtain a Single Point:**

**calc_time routine:**
Calculates the time and corresponding position and velocity for a given angle. The input parameters include a `uom_params` object, the target angle in degrees (`alpha_dg`), and an optional angular step (`delta_angle_dg`, default is 0.01). The routine returns the time, position coordinates (\(e_x\), \(e_y\), \(e_z\)), and velocity components (\(v_x\), \(v_y\), \(v_z\)).

```python
def calc_time(self, param, alpha_dg, delta_angle_dg=0.01, use_3d=False):
    return time, ex, ey, ez, vx, vy, vz
```

**calc_angle routine:**
Calculates the angle and corresponding position and velocity for a given time. Input parameters include a `uom_params` object, the target time (`target_time`), and an optional angular step (`delta_angle_dg`, default is 0.01). The routine returns the angle, position coordinates (\(e_x\), \(e_y\), \(e_z\)), and velocity components (\(v_x\), \(v_y\), \(v_z\)).

```python
def calc_angle(self, param, target_time, delta_angle_dg=0.01, use_3d=False):
    return alpha, ex, ey, ez, vx, vy, vz
```

**Routines to Obtain Lists of Points:**

**calc_orb_angle routine:**
Calculates orbit positions and velocities over a range of angles. Input parameters include a `uom_params` object, the initial angle in degrees (`alpha0_dg`), maximum angle in degrees (`alpha_max_dg`), angular step in degrees (`delta_alpha_dg`), and optional maximum simulation time (`time_max`). The routine returns an `orbit_vect` object.

```python
def calc_orb_angle(self, param, alpha0_dg, alpha_max_dg, delta_alpha_dg, time_max=None, msg=False, use_3d=False):
    return orbit_values
```

**calc_orb_time routine:**
Calculates orbit positions and velocities over a range of times. Input parameters include a `uom_params` object, initial time (`time0`), time step (`delta_time`), maximum time (`time_max`), and optional maximum angle in degrees (`alpha_max_dg`). The routine returns an `orbit_vect` object.

```python
def calc_orb_time(self, param, time0, delta_time, time_max, alpha_max_dg=None, msg=False, use_3d=False):
    return orbit_values
```

### UOM Parameters Calculation Routines

The UOM defines routines for extracting parameters from body trajectory data:

**2D Parameter Calculation Routines:**

**get_UOM_params_2D_vel routine:**
Calculates UOM parameters from a position and velocity vector in 2D. Input parameters include position coordinates (`x0, y0`), time (`t0`), velocity components (`vx0, vy0`), and the mass of the orbiting body (`M`). Returns a `uom_params` object.

```python
def get_UOM_params_2D_vel(x0, y0, t0, vx0, vy0, M):
    return param
```

**get_UOM_params_2D_pos routine:**
Calculates UOM parameters from two position vectors in 2D. Input parameters include initial and final position coordinates and times (`x0, y0, t0, x1, y1, t1`) and the mass of the orbiting body (`M`). Returns a `uom_params` object.

```python
def get_UOM_params_2D_pos(x0, y0, t0, x1, y1, t1, M):
    return param
```

**3D Parameter Calculation Routines:**

**get_UOM_params_3D_vel routine:**
Calculates UOM parameters from a position and velocity vector in 3D. Input parameters include position coordinates (`x0, y0, z0`), time (`t0`), velocity components (`vx0, vy0, vz0`), and the mass of the orbiting body (`M`). Returns a `uom_params` object.

```python
def get_UOM_params_3D_vel(x0, y0, z0, t0, vx0, vy0, vz0, M):
    return param
```

**get_UOM_params_3D_pos routine:**
Calculates UOM parameters from two position vectors in 3D. Input parameters include initial and final position coordinates and times (`x0, y0, z0, t0, x1, y1, z1, t1`) and the mass of the orbiting body (`M`). Returns a `uom_params` object.

```python
def get_UOM_params_3D_pos(x0, y0, z0, t0, x1, y1, z1, t1, M):
    return param
```

### UOM Parameters Conversion Routines

The UOM includes functions to convert between Keplerian and Ulianov parameters:

**kepler_to_ulianov function:**
Converts Keplerian parameters \(a\) (semi-major axis) and \(e\) (eccentricity) to Ulianov parameters \(R_0\), \(V_0\), and \(U_e\). 

```python
def kepler_to_ulianov(self, a, e, M):
    return R0, Ue
```

**kepler_to_ulianov_6p function:**
Converts all six Keplerian parameters to Ulianov parameters. Returns a `uom_params` object.

```python
def kepler_to_ulianov_6p(self, a, e, ang_i_dg, ang_omega_dg, ang_ell_dg, alpha_dg, t0, v, M):
    return param
```

**ulianov_to_kepler function:**
Converts Ulianov parameters \(R_0\) and \(U_e\) to Keplerian parameters \(a\) and \(e\).

```python
def ulianov_to_kepler(self, R0, Ue):
    return a, e
```

### UOM General Calculation Routines

The UOM provides routines for calculating various orbital properties:

**calc_velocity function:**
Calculates orbital velocity at a specific distance \( d \) given \( U_e \), \( R_0 \), and \( V_0 \).

```python
def calc_velocity(self, Ue, R0, V0, d):
    return V
```

**calc_v0 function:**
Calculates the maximum orbital velocity \( V_0 \) using \( U_e \), \( R_0 \), and the mass \( M \).

```python
def calc_v0(self, Ue, R0, M):
    return V0
```

**calc_ue function:**
Determines \( U_e \) using \( V_0 \), \( R_0 \), and \( M \).

```python
def calc_ue(self, R0, V0, M):
    return Ue
```

**calc_mass_ab

_v0 function:**
Calculates the mass \( M \) using \( a \), \( b \), and \( V_0 \).

```python
def calc_mass_ab_v0(self, a, b, V0):
    return M
```

**calc_mass_r0v0_ue function:**
Calculates the mass \( M \) using \( R_0 \), \( V_0 \), and \( U_e \).

```python
def calc_mass_r0v0_ue(self, R0, V0, Ue):
    return M
```

**calc_orbit_length_ab function:**
Calculates the orbit length using \( a \) and \( b \). Applies Ramanujan's ellipse formula.

```python
def calc_orbit_length_ab(self, a, b):
    return Le
```

**calc_orbit_time_ab_v0 function:**
Calculates the orbital period using \( a \), \( b \), and \( V_0 \).

```python
def calc_orbit_time_ab_v0(self, a, b, V0):
    return orbit_time
```

**calc_orbit_time_ab_m function:**
Calculates the orbital period using \( a \) and \( M \).

```python
def calc_orbit_time_ab_m(self, a, M):
    return orbit_time
```

**calc_orbit_time_r0v0_m function:**
Calculates the orbital period using \( R_0 \), \( V_0 \), and \( M \).

```python
def calc_orbit_time_r0v0_m(self, R0, V0, M):
    return orbit_time
```

**calc_orbit_time_ue_v0 function:**
Calculates the orbital period using \( U_e \), \( R_0 \), and \( V_0 \).

```python
def calc_orbit_time_ue_v0(self, Ue, R0, V0):
    return orbit_time
```


## Reference

For detailed information and theoretical background on the Ulianov Orbital Model, refer to the paper:

Ulianov, P. Y., "Ulianov Orbital Model. Describing Kepler Orbits Using Only Five Parameters and Using Ulianov Elliptical Trigonometric Function: Elliptical Cosine and Elliptical Sine," June 2024. Available at: [Academia](https://www.academia.edu/122397626)

