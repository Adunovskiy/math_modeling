import numpy as np
def grav_accel(phi = 0, h = 0):
  """ Ускорение свободного падения 
      phi - широта места наблюдения
      h - высота над поверхностью Земли
  """
  g = 9.780318 * (1 + 0.005302 * (np.sin(phi)) ** 2 - 0.000006 * (np.sin(2 * phi) ** 2) - 0.000003086 * h)
  return g
print(grav_accel(22, 100))

def losing_weigth_function(mass = 50, phi_0 = 54, phi_end = 0, h_0 = 0, h_end = 3000):
  """ Функция, определяющая вес
  """
  P_0 = grav_accel(phi_0, h_0) * mass
  P_end = grav_accel(phi_end, h_end) * mass
  delta_P = (P_end - P_0) * 100
  if delta_P > 0:
    print("Вы похудеете на:", delta_P, 'г')
  elif delta_P < 0:
    print("Вы поправитесь на:", delta_P * (-1), 'г')
  else:
    print('Ты - жиробас, сида дома!')
losing_weigth_function(70, 31, 43, 0, -11022)
