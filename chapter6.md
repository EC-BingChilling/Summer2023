# Chapter 6 Games
The connectedness of a complex system like a social group, nature, or technology means that different parts of the system are liked together. At the same time, the actions of individuals in the system depend on each other so the outcome for one person is influenced by what another person does. Graph theory is mentioned to discuss the structure of the connections. 

TLDR; things in a system affects other things in the system. 

## 6.1 What is a game?

### Example:
Assignments due tomorrow:  
- Presentation
- Exam 

Assumptions:
1. Choose 1 to do
2. The grade estimates are accurate based on what you choose
3. The presentation is to be worked on with a partner

Possible Outcomes:  
![alt text](ch6_exam_or_presentation.png)

### Basic Ingredients of a Game

Players: set of participants  
```python
# Python
players = {"You","Your partner"}
```

For each player, they have options on how to behave (strategies)
```mermaid
graph TD;
    player--> Prepare_for_presentation;
    player--> Study_for_exam;
```

**For each choice of strategies, each player recieves a payoff that can depend on the strategies selected by everyone**
###### a less brain intensive way to look at the 2x2 table (for me at least), also chapter had these numbers p141:

Results of both studying for the exam or both preparing the presentation:
```mermaid
graph LR;
    You -.-> Prepare_for_presentation.;
    You -.-> Study_for_exam.;
    Partner --> Prepare_for_presentation;
    Partner --> Study_for_exam;
    Prepare_for_presentation. -.->Presentation:100
    Prepare_for_presentation -->Presentation:100
    Prepare_for_presentation. -.-> Exam:80
    Prepare_for_presentation -->Exam:80
    Exam:80 -->|you_+_partner| Average:90
    Presentation:100 -->|you_+_partner| Average:90

    Study_for_exam --> Exam:92
    Study_for_exam. -.-> Exam:92
    Study_for_exam --> Presentation:84
    Study_for_exam. -.-> Presentation:84
    Exam:92 -->|you_+_partner| Average:88
    Presentation:84 -->|you_+_partner| Average:88
```

One person studies for the exam while the other prepares for the presentation:
```mermaid
graph LR;
    You -.-> Prepare_for_presentation;
    Prepare_for_presentation -->|you_+_partner| Presentation:92
    You -.-> Exam:80
    Presentation:92 -.-> You_Average:86
    Exam:80 -.-> You_Average:86
    Partner -->|you_+_partner| Presentation:92
    Partner --> Study_for_exam --> Exam:92
    Presentation:92 --> Partner_Average:92
    Exam:92 --> Partner_Average:92
```
In this case, this person benefits from the fact that one of the two of you prepared it.