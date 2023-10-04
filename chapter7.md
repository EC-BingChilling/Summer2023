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

## 7.3 A General Description of Evolutionarily Stable Strategies
|            |   | Organism 2 |     |
|------------|---|------------|-----|
|            |   | S          | T   |
| Organism 1 | S | a,a        | b,c |
|            | T | c,b        | d,d |

Figure 7.3. General symmetric game.

There is a game with two players, where each player can choose between strategies "S" and "T" which represent different behaviors. 
- Same roles

Payoff for S: a(1-x)+bx where 
- 1-x = Probability of meeting another player of S
- recieving a payoff of a
- x = probability it meets a player of T
- recieving a payoff of b

|          |   | Hunter 2 |     |
|----------|---|----------|-----|
|          |   | S        | T   |
| Hunter 1 | S | 4,4      | 0,3 |
|          | T | 3,0      | 3,3 |
Figure 7.4. Stag Hunt game

For "S" to be considered evolutionarily stable, it must meet a condition, which is expressed as an inequality: "a(1-x) + bx > c(1-x) + dx," where a, b, c, and d are values from the payoff matrix, and x represents the fraction of the population using strategy "T."

The payoff for using strategy "S" against others of "S" is greater than the payoff for using "T" against others of "S", which means "S" is stable. It makes sense because if "S" does better when interacting with other "S" players, it is less likely to be replaced with strategy "T". 

Payoffs for "S" vs "S" and "T" vs "S" are equal (a=c) but the payoff for "S" vs "T" is better than "T" vs "T" (b>d) then "S" can also be stable. "S" does better against "T" players than "T" players against each other. 

How can a strategy be evolutionarily stable? (satisfy one of these conditions)
- does better against it's own kind than the alternate strategy
- does equally well against its own kind but better against the alternative strategy

It's less likely to die out or be replaced by another strategy in a population over time. 

tldr;

Playing S:  
a(1-x)+bx

Playing T:  
e(1-x)+dx


S is evolutionarily stable if for all sufficient small values of x>0, the inequality   
a(1-x) + bx > c(1-x)+dx holds

As x goes to 0, the left hand side becomes a and the right hand side becomes c if a>c then the left hand is larger once x is sufficiently small

if a = c then the left hand side is larger when b>d

We can express the condition that S is evolutionarily stable in a two player two strategy game 
1. a > c
2. a = c and b > d

The set of Nash equilibria is bigger than the set of evolutionarily stable strategies. 

Some notes from
[Lecture 47: Evolutionary Stable Strategy (ESS) - Beetles’ World Example and Analysis](https://youtu.be/wDCagl37nb8?si=YnJBXZtG3_dUDkJ0) for clarity.

Strategy T invades a strategy S at level x (for small x) if:
- x fraction of population uses T (Large)
- 1-x fraction of population uses S (Small)

Strategy S is evolutionarily stable if there is some number y such that:
- When any other strategy T invades S at any level x < y, the fitness of an organism playing S is strictly greater than the fitness of an organism playing T

|          |       | Beetle 2 |       |
|----------|-------|----------|-------|
|          |       | Small    | Large |
| Beetle 1 | Small | 6,6      | 1,10   |
|          | Large | 10,1      | 4,4   |

Modified beetle game

Is Small an evolutionarily stable strategy?
- Suppose for some small number x, a 1-x fraction of the population uses Small and x uses Large
- In other words, a small population of Large beetles (x) invades the population of small beetles. 