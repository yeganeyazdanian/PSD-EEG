import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import Data

data = Data.Fin_Means()
#(num1,num2,num3) = (relaxed,untimed,timed)
alpha_means, alpha_std = (data["Relaxed"]["means"][0], data["UnTimed"]
                          ["means"][0], data["Timed"]["means"][0]), (1, 1, 1)
theta_means, theta_std = (data["Relaxed"]["means"][2], data["UnTimed"]
                          ["means"][2], data["Timed"]["means"][2]), (1, 1, 1)
beta_means, beta_std = (data["Relaxed"]["means"][1], data["UnTimed"]
                        ["means"][1], data["Timed"]["means"][1]), (1, 1, 1)

ind = np.arange(len(alpha_means))  # the x locations for the groups
width = 0.1  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(ind - width, alpha_means, width, yerr=alpha_std,
                label='alpha')
rects2 = ax.bar(ind + width/2, beta_means, width, yerr=beta_std,
                label='beta')
rects3 = ax.bar(ind + width+width, theta_means, width, yerr=theta_std,
                label='theta')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Mean PSD')
ax.set_title('Session type')
ax.set_xticks(ind)
ax.set_xticklabels(('Relaxed', 'Untimed', 'Timed'))
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0, 'right': 1, 'left': -1}

    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(offset[xpos]*3, 3),  # use 3 points offset
                    textcoords="offset points",  # in both directions
                    ha=ha[xpos], va='bottom')


autolabel(rects1, "left")
autolabel(rects2, "right")
autolabel(rects3, "right")
fig.tight_layout()

plt.show()
