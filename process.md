## Simulation Details

Start with some number of players, say 1000. In the beginning, you will have
an initial probability distribution for cooperators (let's call them
**type C**), defectors (**type D**) and loners (**type L**): each player
object will be labeled with its type.

We will assume that
the contribution by each cooperator in an active round, $c$, equals 1,
the rate of interest $r$ equals 1.8, and
the amount given to each loner, $\sigma$, equals 0.3. The number of participants in an active round, $N$, equals 5.

The simulation will proceed by repeating the following steps many times (say 10000 times):

1. Initialize individual payoffs to 0.
2. Play 100 active rounds: in each such round, choose $N$ random players to participate, and update their payoffs based on the usual equations: if $n_c$ is the number of type-C players among the chosen ones, then the payoffs for each type-C player is $\frac{r \cdot n_c}{N} -1$, each type-D player is $\frac{r \cdot n_c}{N}$ and each type-L player is $\sigma$. Keep accumulating the payoffs.
3. Now, choose 10 random pairs of players without replacement. For each pair $(p_1, p_2)$, compute the difference in their payoffs (i.e. payoff of first on the pair minus the payoff of the second in the pair). If this difference is $d$, then change the type of the first player (in the pair) to the type of the second player with probability equal to
$\frac{1}{1 + e^{d}}$. Intuitively, if $d$ is very close to zero, the probability is close to half, but if $d$ gets more and more positive, the probability of change tends to 0 if the first players payoff is
superior to the send one's payoff. Likewise, as the value of $d$ gets more and more negative, the probability of change gets closer to 1.
4. Recalculate the new proportions of type C, D and L players after step 3.

You will of course, keep track of the proportions after each complete
iteration of the four steps. Plot these on the simplex to see how the
system is evolving.