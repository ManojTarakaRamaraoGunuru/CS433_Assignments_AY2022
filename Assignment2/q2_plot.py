import numpy as np
import matplotlib.pyplot as plt


def get_vals(stats):
    lines = [s for s in stats.split('\n') if 'sec' in s]
    tp = [float(line.split()[-2]) for line in lines]
    tp = tp[:-2] # last is the avg; remove
    return tp

T = 120 # total time
intvl = 1 # interval
file1 = 'g_B_1'
file2 = 'g_C_1'
file3 = 'g_D_1'
question = 'g'
iteration = '1'
with open(file1 + '.txt') as f:
    stats1 = f.read()
with open(file2 + '.txt') as f:
    stats2 = f.read()
with open(file3 + '.txt') as f:
    stats3 = f.read()

tp1 = get_vals(stats1)
tp2 = get_vals(stats2)
tp3 = get_vals(stats3)
t = np.arange(0, T, intvl)
plt.plot(t, tp1)
plt.plot(t, tp2)
plt.plot(t, tp3)
plt.xlabel('time (sec)')
plt.ylabel('throughput (Mbps)')
plt.ylim(0, 600)
plt.legend(["throughput at B", "throughput at C", "throughput at D"])
plt.savefig('2' + question + iteration + '.png')