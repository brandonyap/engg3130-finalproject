# Final Project
## Ideas
- Gym OpenAI game modeling (https://gym.openai.com)
- Genetic Algorithm for Path Finding


### Balancing Algorithm
- https://gym.openai.com/envs/CartPole-v1/
- Algorithms: 
  - Brute force
    - "if going to the right, push to the left"
  - reinforcement learning
    - Neuroevolution
      - This can be easily implemented with tf.layers
    - Q learning
      - Would be much harder to implement but would be a good learning experience
    - Policy Gradient
  - digital negative feedback loop (like what would be in control theory)


1) Make base program for interacting with the cartpole environment
2) Make all of the algorithms that will interface with the cartpole algorithm
3) compare and contrast the algorithms
  - how long the pole balances
  - maximum angle that the pole reaches (smaller better) stability
  - 
4) Graph all of the performance results
5) include a GIF of each of the balancing algorithms

## Git Tutorial

- "I want to have this code on my local machine"
`git clone https://github.com/brandonyap/engg3130-finalproject.git`
- "I want the latest code in my repository"
`git pull`
- "I want to push my code up into the shared repo"
`git add .`
`git commit -m "<commit_message>"`
`git push`
- "I made a mistake in a file and I don't want it anymore"
`git checkout <files>`
- "I want to switch to a different branch"
`git checkout <branch_name>`

