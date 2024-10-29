import time
import matplotlib.pyplot as plt

def max_revenue(n, lengths, prices):
   
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        for j in range(len(lengths)):
            if lengths[j] <= i:  
                dp[i] = max(dp[i], dp[i - lengths[j]] + prices[j])

    return dp[n] 

def time_experiment():  
    test_cases = [
        (10, [3], [8])
        (20, [3, 5, 7, 9, 11], [8, 15, 20, 25, 30])
        (50, [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41], [i * 2 for i in range(20)])
        (100, [i for i in range(3, 43, 2)], [i * 3 for i in range(20)]),  
        (500, [i for i in range(5, 105, 5)], [i * 4 for i in range(20)])  
    ]

    products = [n * len(prices) for n, lengths, prices in test_cases]
    practical_times = []

    for n, lengths, prices in test_cases:
        start_time = time.time()
        max_revenue(n, lengths, prices)
        end_time = time.time()
        practical_times.append(end_time - start_time)

    scaling_constant = practical_times[0] / products[0]
    theoretical_times = [scaling_constant * product for product in products]

    plt.figure(figsize=(10, 6))
    plt.plot(products, practical_times, label="Practical Time", marker='o', color='b')
    plt.plot(products, theoretical_times, label="Theoretical Time (Scaled)", linestyle='--', color='r')
    plt.xlabel("Product of n and len(prices)")
    plt.ylabel("Time (seconds)")
    plt.title("Theoretical vs Practical Time Analysis for Max Revenue DP Problem")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.legend()
    plt.show()

time_experiment()
