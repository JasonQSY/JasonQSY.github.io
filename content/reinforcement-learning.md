Title: Key Ideas in Typical Reinforcement Learning
Category: Machine Learning
Date: 2017-4-20
Modified: 2017-4-20

This post is learning notes of reinforcement learning.

## Basic Ideas

### Agent and Environment

First, we need clarify and define some basic ideas. In the reinforcement learning problem, the core relationship is that between **agent** and **environment**. According to Sutton and Barto (S&B),

> The learner and decision-maker is called the agent. The thing it interacts with, comprising everything outside the agent, is called the environment.

### States and Actions

Within the interaction, the agent need take actions according to the environment. For states and actions,

> actions can be any decisions we want to learn how to make, and the states can be anything we can know that might be useful in making them.

We use action space to decribe the set of actions. It can be discrete or continuous. Similar for state space.

### Policy

Under a state, the agent need decide the action taken. It is called a policy.

> the agent implements a mapping from states to probabilities of selecting each possible action. This mapping is called the agent’s policy and is denoted $\pi_t$ , where $\pi_t (a|s)$ is the probability that $A_t = a$ if $S_t = s$.

Policy $\pi$ is a mapping from the state space to the action space. It is unnecessary to be fixed. Random policy is a policy.

### Goal

Now it comes out what is the goal of a policy.

> Informally, the agent’s goal is to maximize the total amount of reward it receives.

The goal is to maximize the total reward in the long run.

### Discount Rate

When measure the so called "total reward", we use a discount rate $\gamma$ to show the weight of future reward.

$$G_t = R_{t+1} + \gamma R_{t+2} + \gamma^2 R_{t+3} + \cdots= \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}$$

Whether the number of items is finite of infinite depends on the problem. If the problem has a terminal state, it would be finite.

### Transition Probability

It is not guaranteed that an action under a specific state always has the same result since the environment can be very complicated. Hence, we use $s'$ to show the next state after taking action $a$ under state $s$. The transition probability is defined as

$$P(s' | s, a) = P\{ S_{t+1} = s' | S_t = s, A_t = a \}$$

### Reward

After taking an action, the environment needs give reward back to show the action is "good" or "bad". Losing a game is a negative reward, while winning a game is a positive reward. Reward is defined as

$$r(s, a, s') = E\{R_{t+1} | S_t = s, A_t = a, S_{t+1} = s'\}$$

Note that it is just a singal. It is unnecessary that actions should have a reward (actually, $r=0$ if no reward). It is unnecessay that $r<0$ if the agent loses the game.

### Value Function

How to evaluate a policy? It comes out the value function. Under specfic policy $\pi$,

$$V_{\pi} (s) = \mathbb{E}_{\pi}[G_t | S_t = S]$$

is the value function for a state. However, the value function for a state-action pair is sometimes more useful. It is defined as

$$q_{\pi}(s, a) = \mathbb{E}_{\pi} [G_t | S_t = s, A_t = a]$$

### Bellman Equation

Currently, even if we know everything of the environment, it seems very complicated to calculate the value function for a specfic policy. Bellman Equation solves the problem.

$$V_{\pi}(s) = \sum_{a} \pi(a | s) \sum_{s'} p(s' | s, a) \left[ r(s,a,s') + \gamma V_{\pi}(s') \right]$$

$$q_{\pi}(s, a) =  \sum_{s'} p(s' | s, a) \left[ r(s,a,s') + \gamma V_{\pi}(s') \right]$$

Obviously,

$$V_{\pi}(s) = \sum_{a} \pi(a | s) q_{\pi} (s,a)$$

### Optimal Policy

Now we can evaluate a policy. However, it is still impossible for us to improve a policy. We need to define **optimal policy $\pi'$**

$$\forall_{\pi} V_{\pi'}(s) \ge V_{\pi}(s)$$

And update the value function according to

$$V_{t+1}(s) = \sum_{a} \pi(a | s) \sum_{s'} p(s' | s, a) \left[ r(s,a,s') + \gamma V_{t}(s') \right]$$

It can be proved that the value function will converge finally. According to such a value function, the policy is the optimal policy (choose action with the maximal q-value).

### Related Reading

Some ideas are not shown in detail and we ignore the mathematical proof. For the details, have a look at Chapter 3 of the S&B.

## Typical Methods

Based on basic ideas, it is possible for us to solve simple problems now.

### Dynamic Programming

Just follow

$$V_{t+1}(s) = \sum_{a} \pi(a | s) \sum_{s'} p(s' | s, a) \left[ r(s,a,s') + \gamma V_{t}(s') \right]$$

A sample implementaion is shown here.

```python
# constants
iterations = 100
discount = 0.9

# variables
values = {}

# abstract class. Terminal state if len(mdp.get_possible_actions) = 0
class mdp:
    # return a list of states
    get_states(self):
        pass
        
    # return a list of actions
    get_possible_actions(self, state):
        pass
        
    # return [('state', 0.9), ...]
    get_transition_states_and_probs(self, state, action):
     	pass
    
    # return a number
    get_reward(self, state, action, next_state):
        pass
       
# compute q(s, a) = sum p(s'|s,a)[r(s,a,s') + gamma * v_old(s')]
def compute_qvalue_from_values(state, action):
    next_states = mdp.get_transition_states_and_probs(state, action)
    q_value = 0
    for next_state in next_states:
        prob = next_state[1]
        reward = mdp.get_reward(state, action, next_state[0])
        value = values[next_state[0]]
        q_value += prob * (reward + discount * value)
        
    return q_value
    
# return action with max q(s, a)
def choose_action_from_values(state):
    actions = mdp.get_possible_actions(state)
    max_q = float('-Inf')
    action_index = ''
    for action in actions:
        q_value = compute_qvalue_from_values(state, action)
        if q_value > max_q:
            action_index = action
            max_q = q_value
            
    return action_index
        
# main

# initialize v(s) = 0
states = mdp.getStates()
for state in states:
    self.values[state] = 0
    
# keep iterations
for _ in range(iterations):
    temp = values[:]
    for state in states:
        actions = mdp.get_possible_actions(state)
        greedy_action = choose_action_from_values(state)
        for action in actions:
            q_value = compute_qvalue_from_values(state, action)
            if action == greedy_action:
                temp[state] = q_value
                break
                
    values = temp[:]
        
```



### Monte Carlo Methods

Calculating value functions according to dynamic programming relies on the fact that you know everything of the environment. However, if we do not know the model exactly, how could we do? The answer is abandon the model and to learn from experience directly. This is called model-free algorithm

For Monte Carlo methods, we put a sample robot and let it go. After it arrives at the terminal state, we have $G$ for every step and now we update the value function, i.e.

$$V_{new}(s) = V_{old}(s) + \alpha \left [ G_t - V_{old}(s) \right ]$$

## Advanced Topics

I do not want to cover td-learning and q-learning in detail here. It will be topics of the next post. Here I just talk about the motivation and show the formula.

### TD Learning

TD learning is a combination of monte carlo methods and dynamic programming. It adds bootstraping into Monto Carlo methods, i.e.

$$V_{t+1}(s) = V_{t}(s) + \alpha (R(s, a, s') + \gamma V_{t} (s') - V_{t}(s))$$

where $\alpha$ is the learning rate.

### Q Learning

After talking about TD learing, it is natural to think if it is possible to update q value instead of V. This is Q learning.

$$Q_{t+1}(s, a) = Q_{t} (s, a) + \alpha \left ( R(s, a, s') + \gamma \max_{a'} Q_{t}(s', a') - Q_{t}(s, a)\right)$$

where $\alpha$ is the learning rate.

## Reference

- [Sutton and Barto, Reinforcement Learning: An Introduction](https://mitpress.mit.edu/books/reinforcement-learning)
- [CSE 573 - Introduction to Artificial Intelligence, University of Washington](https://courses.cs.washington.edu/courses/cse573/12au/)
- [CS 181: Intro to AI, UC Berkeley](http://inst.eecs.berkeley.edu/~cs188/pacman/home.html)

