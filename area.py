import math

def retaining_wall_design(H, gamma, phi, mu, SF):
    """
    Calculate the base width and area of steel reinforcement for a cantilever retaining wall.

    Parameters:
    H (float): Height of the wall in meters.
    gamma (float): Density of the backfill in kN/m³.
    phi (float): Angle of internal friction in degrees.
    mu (float): Coefficient of friction.
    SF (float): Safety factor.

    Returns:
    tuple: Base width in meters, area of steel reinforcement in mm².
    """
    phi_rad = math.radians(phi)
    
    Ka = (1 - math.sin(phi_rad)) / (1 + math.sin(phi_rad))
    
    Pa = 0.5 * gamma * H**2 * Ka
    
    B = Pa / (gamma * H * mu * SF)
    
    fy = 415  # Yield strength of steel in MPa
    Ast = (Pa * H * 1000) / (0.87 * fy)
    
    return B, Ast

# Manual input from the user
try:
    H = float(input("Enter the height of the wall (in meters): "))
    gamma = float(input("Enter the density of the backfill (in kN/m³): "))
    phi = float(input("Enter the angle of internal friction (in degrees): "))
    mu = float(input("Enter the coefficient of friction: "))
    SF = float(input("Enter the safety factor: "))
    
    base_width, steel_area = retaining_wall_design(H, gamma, phi, mu, SF)
    print(f"The base width of the retaining wall is: {round(base_width, 2)} meters")
    print(f"The required area of steel reinforcement is: {round(steel_area, 2)} mm²")
except ValueError:
    print("Please enter valid numerical values.")
