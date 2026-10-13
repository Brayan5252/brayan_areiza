import math

alpha = float(input("Ingresa el ángulo a en grados: "))
beta = float(input("Ingresa el ángulo β en grados: "))


alpha_rad = math.radians(alpha)
beta_rad = math.radians(beta)

resultado_suma_sen = 2 * math.sin((alpha_rad + beta_rad) / 2) * math.cos((alpha_rad - beta_rad) / 2)
print(f"Resultado de sin(a) + sin(β): {resultado_suma_sen}")


resultado_suma_cos = 2 * math.cos((alpha_rad + beta_rad) / 2) * math.cos((alpha_rad - beta_rad) / 2)
print(f"Resultado de cos(a) + cos(β): {resultado_suma_cos}")

