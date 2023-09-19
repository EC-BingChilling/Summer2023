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