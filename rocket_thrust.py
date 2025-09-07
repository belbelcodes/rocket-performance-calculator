# Simple Rocket Thrust Calculator
# Belle's first propulsion project 🚀

# Thrust Equation:
# F = mdot * Ve + (Pe - Pa) * Ae
# where:
#   mdot = mass flow rate of propellant (kg/s)
#   Ve   = exhaust velocity (m/s)
#   Pe   = exhaust pressure (Pa)
#   Pa   = ambient pressure (Pa)
#   Ae   = nozzle exit area (m^2)

def calculate_thrust(mdot, Ve, Pe, Pa, Ae):
    return mdot * Ve + (Pe - Pa) * Ae

if __name__ == "__main__":
    # Example numbers (you can change these later):
    mdot = 5.0       # kg/s
    Ve   = 2500.0    # m/s
    Pe   = 101325.0  # Pa (same as sea level)
    Pa   = 101325.0  # Pa
    Ae   = 0.2       # m^2

    thrust = calculate_thrust(mdot, Ve, Pe, Pa, Ae)
    print(f"Rocket thrust: {thrust:.2f} N")
