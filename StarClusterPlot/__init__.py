from matplotlib import pyplot as plt

def ClusterVis(data, x_scale = 6.75, y_scale = 12):

  RA = data['ra']
  DEC = data['dec']
  g = data['g']
  r = data['r']

  data['B'] = g + 0.3130*(g-r) + 0.2271
  data['V'] = g - 0.5784*(g-r) - 0.0038

  B = data['B']
  V = data['V']

  data['temperature'] = 4600 * (1/((0.92 * (B - V)) + 1.7) + 1/((0.92 * (B - V)) + 0.62))
  data['temperature'] = data['temperature'].where(data['temperature'] >= 1667).where(data['temperature'] <= 26000)
  temperature = data['temperature']

  def Kelvin_to_xyY(T):
    if T >= 1667 and T < 2222:
      x = -0.2661239*(10**9)/(T**3) - 0.2343580*(10**6)/(T**2) + 0.8776956*(10**3)/T + 0.179910
      y = -1.1063814*(x**3) - 1.34811020*(x**2) + 2.1855832*x - 0.20219683
    elif T >= 2222 and T < 4000:
      x = -0.2661239*(10**9)/(T**3) - 0.2343580*(10**6)/(T**2) + 0.8776956*(10**3)/T + 0.179910
      y = -0.9549476*(x**3) - 1.37418593*(x**2) + 2.09137015*x - 0.16748867
    else:
      x = -3.0258469*(10**9)/(T**3) + 2.1070379*(10**6)/(T**2) + 0.2226347*(10**3)/T + 0.240390
      y = +3.0817580*(x**3) - 5.87338670*(x**2) + 3.75112997*x - 0.37001483
    return x, y

  def xyY_to_XYZ(x, y):
    Y = 1
    X = x/y
    Z = (1-x-y)/y
    return X,Y,Z

  def XYZ_to_RGB(X,Y,Z):
    R = (3.240479*X) + (-1.537150*Y) + (-0.498535*Z)
    G = (-0.969256*X) + (1.875992*Y) + (0.041556*Z)
    B = (0.055648*X) + (-0.204043*Y) + (1.057311*Z)

    R = min(max(R, 0), 1)
    G = min(max(G, 0), 1)
    B = min(max(B, 0), 1)
    return R, G, B

  def Kelvin_to_RGB(T):
    xyY = Kelvin_to_xyY(T)
    XYZ = xyY_to_XYZ(xyY[0], xyY[1])
    RGB = XYZ_to_RGB(XYZ[0], XYZ[1], XYZ[2])
    return RGB

  data['RGB'] = data['temperature'].apply(Kelvin_to_RGB)

  RGB = data['RGB']

  fig, ax = plt.subplots(figsize=(x_scale, y_scale))
  ax.set_facecolor('#252525')
  ax.scatter(RA,DEC, s=0.05, marker='o', c=RGB)

  return fig


#--------------------------------------------------------------------------------------------------------------------------------------------#


def HRDiagram(data, left_bound = -3, right_bound = 4, lower_bound = -10, upper_bound = 25, x_scale = 12, y_scale = 6.75):

  g = data['g']
  r = data['r']

  data['B'] = g + 0.3130*(g-r) + 0.2271
  data['V'] = g - 0.5784*(g-r) - 0.0038

  B = data['B']
  V = data['V']

  data['temperature'] = 4600 * (1/((0.92 * (B - V)) + 1.7) + 1/((0.92 * (B - V)) + 0.62))
  data['temperature'] = data['temperature'].where(data['temperature'] >= 1667).where(data['temperature'] <= 26000)
  temperature = data['temperature']

  def Kelvin_to_xyY(T):
    if T >= 1667 and T < 2222:
      x = -0.2661239*(10**9)/(T**3) - 0.2343580*(10**6)/(T**2) + 0.8776956*(10**3)/T + 0.179910
      y = -1.1063814*(x**3) - 1.34811020*(x**2) + 2.1855832*x - 0.20219683
    elif T >= 2222 and T < 4000:
      x = -0.2661239*(10**9)/(T**3) - 0.2343580*(10**6)/(T**2) + 0.8776956*(10**3)/T + 0.179910
      y = -0.9549476*(x**3) - 1.37418593*(x**2) + 2.09137015*x - 0.16748867
    else:
      x = -3.0258469*(10**9)/(T**3) + 2.1070379*(10**6)/(T**2) + 0.2226347*(10**3)/T + 0.240390
      y = +3.0817580*(x**3) - 5.87338670*(x**2) + 3.75112997*x - 0.37001483
    return x, y

  def xyY_to_XYZ(x, y):
    Y = 1
    X = x/y
    Z = (1-x-y)/y
    return X,Y,Z

  def XYZ_to_RGB(X,Y,Z):
    R = (3.240479*X) + (-1.537150*Y) + (-0.498535*Z)
    G = (-0.969256*X) + (1.875992*Y) + (0.041556*Z)
    B = (0.055648*X) + (-0.204043*Y) + (1.057311*Z)

    R = min(max(R, 0), 1)
    G = min(max(G, 0), 1)
    B = min(max(B, 0), 1)

    return R, G, B

  def Kelvin_to_RGB(T):
    xyY = Kelvin_to_xyY(T)
    XYZ = xyY_to_XYZ(xyY[0], xyY[1])
    RGB = XYZ_to_RGB(XYZ[0], XYZ[1], XYZ[2])
    return RGB

  data['RGB'] = data['temperature'].apply(Kelvin_to_RGB)

  RGB = data['RGB']

  x_axis = g-r
  x_axis = x_axis.where(x_axis <= right_bound).where(x_axis >= left_bound)
  y_axis = r
  y_axis = y_axis.where(y_axis <= upper_bound).where(y_axis >= lower_bound)

  fig, ax = plt.subplots(figsize=(x_scale, y_scale))
  ax.set_facecolor('#252525')
  ax.invert_yaxis()
  ax.scatter(x_axis, y_axis, s=0.05, marker='o', c=RGB)

  return fig


#--------------------------------------------------------------------------------------------------------------------------------------------#


def Temp_to_RGB(T):

  def Kelvin_to_xyY(T):
    if T >= 1667 and T < 2222:
      x = -0.2661239*(10**9)/(T**3) - 0.2343580*(10**6)/(T**2) + 0.8776956*(10**3)/T + 0.179910
      y = -1.1063814*(x**3) - 1.34811020*(x**2) + 2.1855832*x - 0.20219683
    elif T >= 2222 and T < 4000:
      x = -0.2661239*(10**9)/(T**3) - 0.2343580*(10**6)/(T**2) + 0.8776956*(10**3)/T + 0.179910
      y = -0.9549476*(x**3) - 1.37418593*(x**2) + 2.09137015*x - 0.16748867
    else:
      x = -3.0258469*(10**9)/(T**3) + 2.1070379*(10**6)/(T**2) + 0.2226347*(10**3)/T + 0.240390
      y = +3.0817580*(x**3) - 5.87338670*(x**2) + 3.75112997*x - 0.37001483
    return x, y

  def xyY_to_XYZ(x, y):
    Y = 1
    X = x/y
    Z = (1-x-y)/y
    return X,Y,Z

  def XYZ_to_RGB(X,Y,Z):
    R = (3.240479*X) + (-1.537150*Y) + (-0.498535*Z)
    G = (-0.969256*X) + (1.875992*Y) + (0.041556*Z)
    B = (0.055648*X) + (-0.204043*Y) + (1.057311*Z)

    R = min(max(R, 0), 1)
    G = min(max(G, 0), 1)
    B = min(max(B, 0), 1)

    return R, G, B

  xyY = Kelvin_to_xyY(T)
  XYZ = xyY_to_XYZ(xyY[0], xyY[1])
  RGB = XYZ_to_RGB(XYZ[0], XYZ[1], XYZ[2])
  return RGB