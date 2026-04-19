# Given probabilities
p_r_yes = 0.2
p_r_no = 0.8

p_s_given_r_yes = 0.01
p_s_given_r_no = 0.4

p_w_given_s_given_r_yes = 0.99   # P(W=Yes | S=Yes, R=Yes)
p_w_given_s_given_r_no = 0.01    # P(W=Yes | S=No, R=Yes)

p_w_given_s_yes_r_yes = 0.9      # P(W=Yes | S=Yes, R=No)
p_w_given_s_no_r_no = 0.1        # P(W=Yes | S=No, R=No)

# Step 1: P(W=Yes | R=Yes)
p_w_given_r_yes = (
    p_s_given_r_yes * p_w_given_s_given_r_yes +
    (1 - p_s_given_r_yes) * p_w_given_s_given_r_no
)

# Step 2: P(W=Yes | R=No)
p_w_given_r_no = (
    p_s_given_r_no * p_w_given_s_yes_r_yes +
    (1 - p_s_given_r_no) * p_w_given_s_no_r_no
)

# Step 3: Total probability P(W=Yes)
p_w_yes = (
    p_w_given_r_yes * p_r_yes +
    p_w_given_r_no * p_r_no
)

# Step 4: Bayes theorem P(R=Yes | W=Yes)
p_r_given_yes = (p_w_given_r_yes * p_r_yes) / p_w_yes

# Print results
print("P(W=Yes | R=Yes):", p_w_given_r_yes)
print("P(W=Yes | R=No):", p_w_given_r_no)
print("P(W=Yes):", p_w_yes)
print("P(R=Yes | W=Yes):", p_r_given_yes)