import numpy as np
import plotext as plt

def slotted_aloha(n, p_values, trials):
    empirical_results = []
    analytical_results = []

    for p in p_values:
        transmissions = np.random.binomial(1, p, (trials, n))
        success_count = np.sum(np.sum(transmissions, axis=1) == 1)
        empirical_results.append(success_count / trials)

        p_succ = n * p * ((1 - p)**(n - 1))
        analytical_results.append(p_succ)
        print(f"p-value -> {p}, Empirical -> {success_count/trials:.4f}, Analytical -> {p_succ:.4f}")

    return empirical_results, analytical_results

# Parameters
n = 10
p_values = [round(x, 1) for x in np.arange(0.1, 1.1, 0.1)]
trials = 1000

# Run Simulation
emp, ana = slotted_aloha(n, p_values, trials)

# 1. Save RAW DATA to l2_cs23b051.txt (as requested by the task)
#header = "p_value  empirical  analytical"
data = np.column_stack((p_values, emp, ana))
#np.savetxt('l2_cs23b051.txt', data, header=header, fmt='%.4f')

# 2. Plotting with plotext
plt.clf()

# PLOT ANALYTICAL FIRST (The background line)
plt.plot(p_values, ana, label="Analytical", color="blue")

# PLOT EMPIRICAL SECOND (The dots on top)
# Using marker="bold" or "fcircle" for better visibility
plt.scatter(p_values, emp, label="Empirical", marker="x", color="red")


plt.title(f"Slotted ALOHA Throughput (n={n})")
plt.xlabel("Probability p")
plt.ylabel("Success Prob")
plt.grid(True)
plt.show()

# If you want to save the TEXT VERSION of the plot:
plt.save_fig("l2_cs23b051.txt")

print(f"\nSimulation complete.")
#print(f"Data saved to: l2_cs23b051.txt")
print(f"Visual plot saved to: l2_cs23b051.txt")
print(data)
