---
author: Igor M. Coelho
title: Fundamentos de Otimização
date: 29 de Julho de 2020
transition: page
fontsize: 10
header-includes:
- <link rel="stylesheet" type="text/css" href="general.css">
- <link rel="stylesheet" type="text/css" href="reveal-beamer.css">
---


# Pesquisa Operacional

-----

## Sobre esse material

Esses slides foram possíveis devido a contribuições de diversas pessoas/materiais, em especial:

- Notas do prof. Marcone Jamilson Freitas Souza
- Livro Nelson Maculan e Marcia Fampa
- Livro-texto do curso
- [2] Tutorial ilectures (https://igormcoelho.github.io/ilectures-pandoc/)
- Vitor Nazário Coelho e Haroldo Gambini pelas dicas no Python-MIP e Gurobi


-----

## Fundamentos Necessários

Caso não se sintam confiantes nos tópicos abaixo, façam uma revisão antes de aprofundar neste material:

- Simplex e Programação Linear



# Fundamentos de Otimização

------

## Introdução

Problemas de otimização podem ser definidos da seguinte maneira:

...

------

## Classes P e NP

...

------

## Fortemente NP-Difícil

Um problema é **fortemente NP-Completo** se todos seus parâmetros numéricos são limitados a um polinômio no tamanho da entrada.

Um problema é **fortemente NP-Difícil**, se algum problema fortemente NP-Completo se reduz a ele.

- Bin Packing é fortemente NP-Completo
- Mochila 0-1 é fracamente NP-Completa

------

## Problemas Clássicos

Consideraremos dois problemas fundamentais:

- Problema de Mochila
- Problema do Caixeiro Viajante

------

## Caixeiro Viajante

O Problema do Caixeiro Viajante é um dos problemas clássicos de otimização, que busca minimizar o trajeto de um caixeiro ao visitar um conjunto de $n$ cidades.

Em especial, consideraremos algumas variantes do PCV:

- PCV Simétrico e Assimétrico
- PCV Métrico (desigualdade triangular)
- PCV Euclideano

Aparentemente, o PCV Euclideano tende a ser "um pouco mais fácil", com maiores níveis de aproximabilidade.

-------

## Dúvidas em NP

Em geral, é considerado que a versão de decisão do PCV é NP-Completa (_"existe rota de tamanho $k$?"_). Porém, ainda não se sabe[^1] se o PCV Euclideano (decisão) pertence a NP!

A razão é que comparar somas de raizes não é trivial (_sum of square roots problem_)... vide sequências abaixo somadas de 1.000.000 (e tirando raiz):

```
1 25 31 84 87  134 158 182 198
2 18 42 66 113 116 169 175 199
```

```
9000.4499835688397309490268288613590291912
9000.4499835688397309490268288613590291915
```

Uma diferença é encontrada somente na 37ª casa decimal! (e não se conhece um algoritmo polinomial para isso)... Porém, basta arredondar para o inteiro mais próximo e o problema claramente pertence a NP.

[^1]: _William J. Cook - In Pursuit of the Traveling Salesman_ Mathematics at the Limits of Computation -Princeton University Press (2011)_

------

## NPO

Um problem `NPO` (NP Optimization) se:

- O tamanho de cada solução viável $s \in \mathcal{S}(\pi)$ é limitada polinomialmente ao tamanho da instância $\pi$
- As linguagens $\pi \in \mathcal{I}$ e $(\pi, s)$ podem ser reconhecidas em tempo polinomial
- $z$ é computável em tempo polinomial

Isto implica que o problema de decisão correspondente está em NP[^2].


[^2]: _Hromkovic, Juraj (2002), Algorithmics for Hard Problems, Texts in Theoretical Computer Science (2nd ed.), Springer, ISBN 978-3-540-44134-2_

------

## NPO e Aproximabilidade

Algumas subclasses de NPO podem ser formadas de acordo com a aproximabilidade:

- NPO(I): FPTAS (Mochila)
- NPO(II): PTAS (Makespan Scheduling Problem)
- NPO(III): Aproximação limitada a $c$ (MAX-SAT e PCV Métrico)
- NPO(IV): Aproximação a uma fração polinomial no logaritmo do tamanho da entrada (set cover)
- NPO(V): Alguma aproximação com fração limitada a alguma função de $n$ (PCV e Max Clique).

Vide livro de Hromkovic[^2].

------

## Limites Atuais

- Mochila pode ser resolvida por programação dinâmica em tempo pseudo-polinomial
- Caixeiro Viajante pode ser aproximado com fator 1,5, porém existem limites de não-aproximabilidade acima de 1 (a não ser que P=NP).
Ainda existe um grande intervalo a ser explorado...
- Algoritmo de Programação Dinâmica Held-Karp nunca melhorado desde 1962 (tempo $O(n^2 2^n)$)
- Heurística $Lin-Kernighan$ dominante para o PCV (vide trabalhos de $Helsgaun$)

------

## Exemplo Metah


```{.latex .exec .hide hide=true void=true cmd='codes/run_latex.sh' args='figs/pseudo2.svg' output_label=''}
\documentclass{standalone}
\usepackage[ruled,vlined,linesnumbered]{algorithm2e}
%
%\renewcommand{\thealgorithm}{}
\renewcommand{\thealgocf}{}  % no number on algorithm2e
%
\begin{document}
\pagestyle{empty}
%
\begin{algorithm}[H]
\DontPrintSemicolon
\SetAlgoLined
\KwResult{Write here the result}
\SetKwInOut{Input}{Input}\SetKwInOut{Output}{Output}
\Input{Write here the input}
\Output{Write here the output}
\BlankLine
\While{While condition}{
    instructions\;
    \eIf{condition}{
        instructions1\;
        instructions2\;
    }{
        instructions3\;
    }
}
\caption{While loop with If/Else condition}
\end{algorithm} 
\end{document}
```

![Algoritmo de Teste](./figs/pseudo2.svg){width=100%}

------

## Lista de Exercícios

A lista de exercícios está disponibilizada no site.
