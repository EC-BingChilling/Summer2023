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