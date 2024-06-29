## Shine Kun Bot - Telegram Bot

<img src ="https://github.com/ShineKunBot/MyBot/img/shinekunbot.png">

1) Goals : 
1- [*] - be simple and easy to read
2- [x] - Implement a Markov chain
3- [x] - Implement automatic translation of bot responses
4- [ ] - Add a sticker creation library
5- [ ] - implement a neural network

Shine Kun Bot is a multitasking bot for Telegram written in Python, I added a markov chain to play with! This bot automatically captures messages from the groups it is in to train the markov chain. The training data will not be made available for privacy reasons and the token will not be made available either. All codes are licensed under the gpl 3 open source license and there are some conditions for using the code, you can download and modify the code and use your modification, but you will have to make the modified code available on an Open Source platform!

A Markov chain, is a mathematical model that describes a sequence of events where the probability of each future event depends only on the current state of the chain. In other words, it is a stochastic process in which the probability of transitioning to the next state depends only on the current state, not the path that led to that state. So don't expect coherence in the Markov chain's responses!

## Contributors

This project exists thanks to all the people who contribute. 

<a href="https://github.com/ShineKunBot/MyBot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ShineKunBot/MyBot&max=24" />
</a>

## Project tree

```
Projeto/
│
├── requirements.txt
├── mensagens.txt
├── main.py
│
├── api/
│   ├── shineMainApi.py
│   ├── secret.key
│   └── encrypted_api_key.bin
│
├── markovchain/
│   └── MarkovC.py
│
└── handlers/
    ├── mainHandlers.py
    ├── markovHandlers.py
    ├── languageHandlers.py
    └── admHandlers.py
```
