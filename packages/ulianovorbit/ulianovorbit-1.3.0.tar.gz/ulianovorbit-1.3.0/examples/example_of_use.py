
import numpy as np
import matplotlib.pyplot as plt
from ulianovellipse import eu
from ulianovorbit import ou


M1 = 5.972e24
M2 = 1.0e4  # Massa da pedra em kg

R0 = 1e8
V0 = 2500
Ue = ou.calc_Ue(R0,V0,M1)
a,b=eu.calc_ab(R0,Ue)
print(f"Conversion test 1 V0 ={V0:.2f}: \na={a:.2f},b={b:.2f}, Ue={Ue:.4f}, R0={R0:.2f}")

Ue = 1.8
V0 = ou.calc_v0(Ue, R0,M1)
a,b=eu.calc_ab(R0,Ue)
print(f"Conversion test 2 Ue ={Ue:.4f}: \na={a:.2f},b={b:.2f}, V0={V0:.2f},  R0={R0:.2f}")

Mab = ou.calc_mass_ab_v0(a,b,V0)
Mue = ou.calc_mass_r0v0_ue(R0,V0,Ue)
print(f"Mass calculation:  ")
print(f" M1          = {M1:.4E}")
print(f" M1(a,b,V0)  = {Mab:.4E}")
print(f" M1(R0,V0,Ue)= {Mue:.4E}")


TKepler = 2*np.pi*np.sqrt(a**3/(ou.G*M1))
Torb1 = ou.calc_orbit_time_ab_m(a,M1)
Torb2 = ou.calc_orbit_time_ab_v0(a,b,V0)
Torb3 = ou.calc_orbit_time_r0v0_m(R0,V0,M1)

print(f"Orbital time test")
print(f"T Kepler       ={TKepler} s  ") 
print(f"Torb(a,b,v0)   ={Torb2} s ,rel = {Torb2/TKepler}")
print(f"Torb(a,M1)     ={Torb1} s ,rel = {Torb1/TKepler} ")
print(f"Torb(R0,V0,M1) ={Torb3} s ,rel = {Torb3/TKepler}")

  