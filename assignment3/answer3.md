### 1155250136 Cheng Haotian

### a. Reinforcement Learning
**Reinforcement learning (RL):** Machine learning through interactions in simulation. A computational approach to learning whereby an agent tries to maximize the total amount of reward it receives while interacting with a complex and uncertain environment. The agent performs actions based on the state of the environment, and the environment provides rewards. The core objective of the agent is to maximize long-term cumulative rewards, rather than relying on labeled supervised data; it is an unsupervised/semi-supervised learning paradigm.

### b. Why for game agents?
RL is well-suited for game agents because games are complex environments with uncertain outcomes. In game, the agent learns to make decisions based on the current state of the game and the rewards it receives. The agent iteratively improves its strategy through trial and error, gradually learning the optimal actions to maximize the cumulative reward.

### c. How can we categorize RL algorithms?
#### Model-Based RL vs Model-Free RL vs Hybrid RL
- **Model-based** algorithms learns a model of the environment's dynamics.
- **Model-free** algorithms does not learn a model of the environment. It learns a policy and/or value function directly from the interactions with the environment.
- **Hybrid** algorithms combine elements of both model-based and model-free approaches.
#### Value-Based RL vs Policy-Based RL vs Actor-Critic RL
- **Value-based** algorithms learn the value function of each state or state-action pair, and use it to select actions. 
- **Policy-based** algorithms directly learn the optimal policy, mapping states to actions.
- **Actor-critic** algorithms combine elements of both value-based and policy-based approaches. The actor learns the policy, and the critic learns the value function.

### d. Chinese Chess Game
**State**: The current board configuration, including the positions of all pieces. And which side is making the move at the moment?

### e. Chinese Chess Game
**Action**: A valid move by a piece on the board. It includes the piece to be moved, the starting position, and the ending position. Chess piece specific movement rules: such as the horse moves in an "日" shape, the elephant moves in a "田" shape, the chariot moves in a straight line, the cannon moves in a straight line to jump over other pieces, the general/king only moves one step in the palace, and the pawn/soldier moves horizontally before crossing the river/after crossing the river, etc.

### f. Chinese Chess Game
**Value-Based Reward**: 
- **Final reward**: Win +100, Loss -100, Draw +0.
- **Instant reward**: Capturing an opponent's piece grants the following bonuses: Rook: +10; Horse/Cannon: +5; Advisor/Elephant: +3; Pawn/Soldier: +2 (Pawns that cross the river receive +4, as their value increases after crossing the river). Violation: -10.

### g. Chinese Chess Game
**Policy-Based Reward**: Assign high cumulative rewards to paths leading to victory, thus strengthening the strategies associated with those paths. For example, "checkmate by sacrifice." Assign low/zero cumulative rewards to paths leading to defeat or a draw, thus weakening the strategies associated with those paths. For example, "greedy move resulting in failure" or "conservative move leading to a draw."

### h. Always learn a better game stategy?
**No**, in some cases, the agent may learn a suboptimal strategy. This is because the agent is learning from a set of examples, and some of the examples may not be representative of the optimal strategy. And overfitting to limited opponents makes the agent’s strategy ineffective in general scenarios.  

### i. Do we set the goal as training a super skillful and perfect game agent?
**No**, the goal of RL is to learn a good strategy that maximizes the cumulative reward. It does not aim to create a super skillful and perfect agent. If the AI ​​agent is too powerful, human players will have no gaming experience and the game will lose its fun. Therefore, the strength needs to be adjusted to suit different players.
