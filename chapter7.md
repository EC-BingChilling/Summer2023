# Chapter 7 Evolutionary Game Theory
Many behaviors involve the interactions of organisms in an environment so we have to consider the success of the organisms overall based on their actions. 

Their strategy is the organism's genetically determined characteristics and behaviors and the payoffs depend on strategies (characteristics) of the organisms they interact with.

## 7.1 Fitness as a Result of Interaction
In evolutionary settings, game theory can explain phenomena of why certain features don't exist on certain organisms. 

Ex. Small beetles get a mutation and now some of the population of beetles are small and some of the population of beetles are large. Because the larger beetles have more metabolic requirements they end up having a negative effect on fitness since it needs more food to support itself. Large beetles are likely to be driven out of the population over time through multiple generations. 

### Interaction Among Organisms
Beetles with larger body size are more effective at claiming an above average share of food.

Outcomes:
- Same size = equal share of food
- Large v Small = Large gets majority
- Large experiences less of fitness benefit in all cases from a givern quantity of food because they have a high metabolism

|          |       | Beetle 2 |       |
|----------|-------|----------|-------|
|          |       | Small    | Large |
| Beetle 1 | Small | 5,5      | 1,8   |
|          | Large | 8,1      | 3,3   |

Figure 7.1. The body-size game. 

We need to think about strategies that operative over longer time scales and shifting over populations because the sizes aren't strategies but instead they're hardwired to one of these stratgies in their lifetime. 

<<<<<<< HEAD
As before we start with a(1-x) being used for the population that uses S and x being the population that uses T.
**The expected payoff of playing S with with a random interaction in this population**
- With the probability of 1-x it meets another player of S it gets a payoff of a
- with the probability of x meeting anopther player of T it gets a payoff of b
the expected payoff is: a(1-x)+bx

**The expected payoff of playing T with with a random interaction in this population**
- With the probability of 1-x it meets another player of S it gets a payoff of c
- with the probability of x meeting anopther player of T it gets a payoff of d
the expected payoff is: c(1-x)+dx

S is evolutionarily stable if and only if a>c or a=c and b>d for the inequality a(1-x)+bx>C(1-x)+dx.
- When a > c the left hand side is larger when x is sufficently small. 
- When a = c the left hand side is only larger if b > d
- When a < c the left hand side will be smaller when x is suffeciently small.

Two things need to be true in order for S to be evolutionarily stable and they are:  
- The payoff of using S against S must be at least as large as the payoff of S against T becuase T would have a higher fitness and then will grow over time.
- If S and T are equally good responses to S then for S to be evolutionarily stable S players must do better in their interaction with T.
=======
## 7.2 Evolutionarily Stable Strategies

Revisiting Nash Equilibrium
- **Nash equilibrium** in two-player games implies no incentive to deviate from current stratgies. 
- Represents a stable choice of stratgies that tend to persist.

Evolutionarily Stable Strategy Example
- **Evolutionarily stable strategy** is a strategy that can't easily be invaded by alternate strategies when it's the majority/prevalent in a population. 
- Beetles are in food competitions and assuming that there is a large population and no significant repeated interactions. 
- Beetle fitness depends on average fitness in pairwise interactions. 
- Fitness determines reproductive success (offstring with the same strategy).

Defining Evolutionarily Stable Strategy
- A strategy is evolutionarily stable if when the entire population uses it, small groups with different strategies will die off over generations.
- Invaders: Migrants or mutants with new behaviors.
- Key: Invaders should have strictly lower fitness than the majority strategy users
- Lower fitness leads to subpopulation shrinkage and eventual exxtinction over generations.

Fitness: Expected payoff from interactions with random popualtion members   
Strategy T invades strategy S at level x if:   
- x fraction uses T and (1-x) fraction uses S   

Strategy is an Evolutionarily Stable Strategy if there exists a small positive number y such that 
- When strategy T invades S at any level x < y, organisms using S have strictly greater fitness than those using T.

### Evolutionarily Stable Strategies in the First Example.

Population where (1-x) Small strategy, and x uses the Large strategy. 

For a small beetle in this population:
- With a chance of (1-x), it meets another beetle and gains a payoff of 5.
- With a chance of x, it meets a Large beetle and gains a payoff of 1.

Small beetle expected payoff:   
6(1-x) + 1x = 5 - 4x

For the Large strategy:   
In a population, (1-x) uses the Large strategy and x uses the smal strategy.

For large beetle:
- With probability (1-x), it meets another Large beetle and gains a payoff of 3
- With probability x, it meets a Small beetle, and gains a payoff of 8

Large beetle expected payoff:   
3(1-x) + 8x = 3 + 5x

When looking at Small, for small values of x, the expected fitness of Large beetles exceeds that of Small beetles so small is not an evolutionarily stable strategy.

For large, when a small fraction(x) of the population uses smll, and the majority uses large (1-x) the expected fitness of Large beetles is still higher than that of small beetles so Large is evolutionarily stable. Large has the upper hand.

### Interpreting the Evolutionarily Stable Strategy in the Body-Size Game

Population of mostly small beetles:   
"Small" is not evolutionarily stable - a few large beetles thrive because they rarely compete with each other and get most of the food

Population of large beetles:   
"Large" is evolutionarily stable - in a population of large beetles, small beetles do poorly and can't easily invade

Reminder: **fitness** means an organism's ability to survive and reproduce in its environment

The fitness of each organism in a population of small beetles is higher than that in a population of large beetles. Sounds counterintuitive since natural selection is usually associated with increasing fitness. 

The Body-Size Game resembles a prisoner's dilema. Even though it's individually better for both types of beetles to cooperate and coexist, evolution favor the large beetles and leads to a suboptimal outcome for both. 

Natural selection usually increases fitness in a fixed environment, but in this case the environment is changing due to the shifting beetle population and leads to a decrease in fitness over time. 

The presence of more large beetles can be seen as a change in the environment that becomes more hostile for everyone, contributing to a decline in individual fitness. 

It seems that counterintuitive outcomes can arise due to the interactiono f different strategies and their long term effects. 

### Empirical Evidence for Evolutionary Arms Races

Evolutionary games in  nature often resemble Prisoner's Dilema. 

Trees can also show prisoner's dilema payoffs.
- Short trees share sunlight equally when neighbor trees are also short. 
- Tall trees share sunlight equally but invest more resources.
- One tall tree and one short, tall tree gets more sunlight.
- Trees have strategies short and tall. 

There is a certain point where payoffs only apply within a certain range because of diminishing returns as trees get taller. 

Root Systems of plants:

- Two soybean plants intermingle roots when grown together, sharing resources equally but it needs a higher root investment.

- Placing a wall with partitioned soil leads to higher reproducive success because they're not depleting energy making longer and more complex roots. 

Conserve strategy is better for everyone, but Explore is evolutionary stable. 

Virus Populations:

$\Phi \mathrm{H} 2$ benefits from $\Phi 6$ chemical products, creating a Prisoner's Dilemma scenario.
Evolutionary strategies: $\Phi 6$ and $\Phi \mathrm{H} 2$.
Conclusion: Only $\Phi \mathrm{H} 2$ is evolutionarily stable.

This resembles the exam or presentation scenario. Selfishness driven by payoffs in shared responsibilities. Evolution makes certain organisms shrink responsibilities. 

|         |       | Virus 2   |            |
|---------|-------|-----------|------------|
|         |       | $\Phi 6$  | $\Phi \mathrm{H} 2$      |
| Virus 1 |$\Phi 6$| 1.00,1.00 | 0.65,1.99  |
|         | $\Phi \mathrm{H} 2$ | 1.99,0.65 | 0.83, 0.83 |

Figure 7.2. The virus game.

|            |   | Organism 2 |     |
|------------|---|------------|-----|
|            |   | S          | T   |
| Organism 1 | S | a,a        | b,c |
|            | T | c,b        | d,d |

Figure 7.3. General symmetric game.
>>>>>>> 13533a5e161b792d772f340bef471140979bb4cd
