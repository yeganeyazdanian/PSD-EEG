from mpl_toolkits.axes_grid.anchored_artists import AnchoredText
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import random

import Data

data = Data.Fin_Means()

timedY = [data["Timed"]["patients"]["p1"]["theta"],
          data["Timed"]["patients"]["p2"]["theta"],
          data["Timed"]["patients"]["p3"]["theta"],
          data["Timed"]["patients"]["p4"]["theta"]]

untimedY = [data["UnTimed"]["patients"]["p1"]["theta"],
            data["UnTimed"]["patients"]["p2"]["theta"],
            data["UnTimed"]["patients"]["p3"]["theta"],
            data["UnTimed"]["patients"]["p4"]["theta"]]
x = [1, 2, 3, 4]
fig, ax = plt.subplots()
plt.plot(x, timedY, "#008abd", marker="o", markersize=10, linewidth=3)
plt.plot(x, untimedY, "#d43800", marker="o", markersize=10, linewidth=3)
at = AnchoredText("Red: Untimed theta\nBlue: Timed theta",
                  prop=dict(size=8), frameon=True,
                  loc=2,
                  )
at.patch.set_boxstyle("round,pad=0.,rounding_size=0.2")
ax.add_artist(at)
plt.xlabel('Patients')
plt.ylabel('Mean PSD (db)')

plt.show()
