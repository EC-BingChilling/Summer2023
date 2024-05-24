import numpy as np

# Initialize variables
num_rounds = 100
num_players = 10
cooperation_cost = 1
interest_rate = 3
loner_payoff = 0.5

# Initialize player strategies randomly
strategies = np.random.choice(['cooperate', 'defect', 'loner'], size=num_players)

for round in range(num_rounds):
    # Calculate payoffs based on strategies
    payoff_cooperators = -cooperation_cost + interest_rate * cooperation_cost * num_cooperators / num_players
    payoff_defectors = interest_rate * cooperation_cost * num_cooperators / num_players

    # Calculate average payoff
    average_payoff = (payoff_cooperators * num_cooperators + payoff_defectors * num_defectors + loner_payoff * num_loners) / num_players

    # Update frequencies based on replicator dynamics
    num_cooperators += num_cooperators * (payoff_cooperators - average_payoff)
    num_defectors += num_defectors * (payoff_defectors - average_payoff)
    num_loners += num_loners * (loner_payoff - average_payoff)

    # Normalize frequencies so they sum to 1
    total = num_cooperators + num_defectors + num_loners
    num_cooperators /= total
    num_defectors /= total
    num_loners /= total