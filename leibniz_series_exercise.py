def approximate_pi(n_terms):
    def approximate_pi(n_terms):
    leibniz_series = []
    for i in range(n_terms):
        sign = (-1) ** i  # Alternates between 1 and -1
        denominator = 2 * i + 1  # Odd numbers: 1, 3, 5, 7, ...
        term = sign * (1 / denominator)
        leibniz_series.append(term)
    pi_approx = 4 * sum(leibniz_series)
    return pi_approx
print(approximate_pi(10))   # Should be close to 3.14
print(approximate_pi(1000)) # Should be close to 3.14

