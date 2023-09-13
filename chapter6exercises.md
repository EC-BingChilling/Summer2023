# 6.11 Exercises
1. Say whether the following claim is true or false, and provide a brief (one to three sentence) explanation for your answer.

Claim: If player A in a two-person game has a dominant strategy
_s_<sub>A</sub>, then there is a pure-strategy Nash equilibrium in which player A
plays _s_<sub>A</sub> and player B plays a best response to _s_<sub>A</sub>.

**Answer:** True because there is no incentive for player A to switch which means player B would have to choose the best strategy to combat player A.

2. Consider the following statement:

In a Nash equilibrium of a two-player game, each player is playing
an optimal strategy, so the two players’ strategies are social-welfare
maximizing.

Is this statement correct or incorrect? If you think it is correct, give a brief (one- to
three-sentence) explanation why. If you think it is incorrect, give an example of a
game discussed in Chapter 6 that shows it to be incorrect (you do not have to spell
out all the details of the game, provided you make it clear what you are referring
to), together with a brief (one- to three-sentence) explanation.

**Answer:** False, an example is the prisoner's dilema game where both people could get the higher payoff but the nash equilibrium is one with a lower payoff than the result both players actually want.

3. Find all pure-strategy Nash equilibria in the game that follows. In the payoff matrix of
Figure 6.28, the rows correspond to player A’s strategies and the columns correspond
to player B’s strategies. The first entry in each box is player A’s payoff and the second
entry is player B’s payoff.

|          |   | Player B |     |
|----------|---|----------|-----|
|          |   | L        | R   |
| Player A | U | 1,**2**      | **3**,**2** |
|          | D | **2**,**4**      | 0,2 |

Figure 6.28. A two-player game for Exercise 3.

**Answer:** As we can see, there are two pure strategy nash equilibria here which is D,L and U,R. 

4. Consider the two-player game with players, strategies, and payoffs described in the
game matrix of Figure 6.29.

|          |   |     | Player B |     |
|----------|---|-----|----------|-----|
|          |   | L   | M        | R   |
|          | t | 0,**3** | **6**,2      | 1,1 |
| Player A | m | 2,**3** | 0,1      | **7**,0 |
|          | b | **5**,**3** | 4,2      | 3,1 |

Figure 6.29. A two player game for Exercise 4.

Best strategies are bolded. 

(a) Does either player have a dominant strategy? Explain briefly (one to three
sentences).  

**Answer:** Yes, it is always better for player B to choose L.

(b) Find all pure-strategy Nash equilibria for this game.

**Answer:** 5,3 (L,b)

5. Consider the two-player game in Figure 6.30 in which each player has three strategies.

|          |   |      | Player B |     |
|----------|---|------|----------|-----|
|          |   | L    | M        | R   |
|          | U | 1,1  | 2,3      | 1,**6** |
| Player A | M | **3**,4  | **5**,**5**      | **2**,2 |
|          | D | 1,**10** | 4,7      | 0,4 |

Figure 6.30. A two-player game for Exercise 5. 

Find all the pure strategy Nash equilibria for this game.

**Answer:** 5,5 (M,M)

6. In this question we consider several two-player games. In each payoff matrix that
follows, the rows correspond to player A’s strategies and the columns correspond to
player B’s strategies. The first entry in each box is player A’s payoff and the second
entry is player B’s payoff.

(a) Find all pure-strategy (nonrandomized) Nash equilibria for the game described in the payoff matrix of Figure 6.31:

|          |   | Player B |      |
|----------|---|----------|------|
|          |   | L        | R    |
| Player A | U | 2,15     | 4,**20** |
|          | D | **6**,6      | **10**,**8** |

Figure 6.31. A two-player game for Exercise 6(a).

**Answer:** (D,R) 10,8

(b) Find all pure-strategy Nash equilibria for the game described in the payoff
matrix of Figure 6.32:

|          |   | Player B |     |
|----------|---|----------|-----|
|          |   | L        | R   |
| Player A | U | **3**,**5**      | **4**,3 |
|          | D | 2,1      | 1,**6** |

Figure 6.32. A two player game for Exercise 6(b).

**Answer:** (U,L) 3,5

(c) Find all Nash equilibria for the game described in the payoff matrix of
Figure 6.33:

|          |     |   | Player B |     |
|----------|-----|---|----------|-----|
|          |     |   | q        | 1-q |
|          |     |   | L        | R   |
| Player A | p   | U | 1,1      | 4,2 |
|          | 1-p | D | 3,3      | 2,2 |

Figure 6.33. A two player game for Exercise 6(c).

**Answer:** p = 1/2, q = 1/2

Explanation: 

Player 1's choice of p is to make player 2 indifferent between left and right. 

Payoff to player 2 of going right:

p1 goes right or left  * player 2 payoff if player 1 goes right or left

p*1 + (1-p)(3) = p + 3 - 3p = 3-2p

Payoff to player 2 going left:

p*2 + (1-p)(2) = 2p + 2 - 2p

player 2 is indifferent when:  
3-2p = 2
p = 1/2

Player 2's choice of q: make player 1 indifferent between r or L

Player 2 R or L * p1 payoff if p2 r or L

Payoff p1 left:
q(3) + (1-q)(2) = 3q + 2 - 2q = 2+q

Payoff of p1 right:
q(1) + (1-q)(4) = 1 + 4 - 4q = 4-3q

P1 is indifferent when:
2+q = 4-3q
2 + 4q = 4
4q = 2
q = 1/2
