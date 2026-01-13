import numpy as np
import plotext as plt

def slotted_aloha(n, p_values, trials):
    empirical_results = []
 #   analytical_results = []

    for p in p_values:
        # Simulating Bernoulli trials for n nodes over many slots
        transmissions = np.random.binomial(1, p, (trials, n))
        # A success is a slot where exactly one node transmitted
        success_count = np.sum(np.sum(transmissions, axis=1) == 1)
        # at how many slots only one node transmitted is calculated adn stored in success_count
        empirical_results.append(success_count / trials)

        # 2. Analytical Calculation: n * p * (1-p)^(n-1)
#        print(f"p-value -> {p}, Empirical value -> {success_count/trials}, Analytical prob -> {p_succ}")

    return empirical_results

# Parameters
n = 10
p_values = [round(x, 1) for x in np.arange(0.1, 1.1, 0.1)] # 0.1 to 1.0 
trials = 1000

# Run Simulation
emp = slotted_aloha(n, p_values, trials)

# Save results to l2_fullrollnumber.txt
# header = "p_value  empirical  analytical"
# data = np.column_stack((p_values, emp, ana))
# np.savetxt('l2_cs23b051.txt', data, header=header)

# Plotting with plotext
"""
plt.clf()
plt.scatter(p_values, emp, label="Empirical", marker="dot", color="red")
plt.plot(p_values, ana, label="Analytical", color="blue")
plt.title(f"Slotted ALOHA Throughput (n={n})")
plt.xlabel("Probability p")
plt.ylabel("Success Prob")
plt.grid(True)
plt.show()
plt.savefig("l2_cs23b051.txt")
print(f"Simulation complete. Data saved to l2_cs23b051.txt")
"""
