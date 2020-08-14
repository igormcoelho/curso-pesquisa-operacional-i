---
author: Igor M. Coelho
title: Exemplo Tableau Simplex
date: 02 de Agosto de 2020
transition: page
fontsize: 10
header-includes:
- <link rel="stylesheet" type="text/css" href="general.css">
- <link rel="stylesheet" type="text/css" href="reveal-beamer.css">
---

## Exemplo Tableau Simplex

$$ maximize \; 40x1 + 35x2 $$
$$ x1 + x2 \leq 24$$
$$ 3x1 + 2x2 \leq 60$$
$$ x1,x2 \geq 0$$

Problema na forma padrão:

$$ maximize \; 40x1 + 35x2 + 0x3 + 0x4 $$
$$ x1 + x2  + 1x3 + 0x4 = 24$$
$$ 3x1 + 2x2 + 0x3 + 1x4 = 60$$
$$ x1,x2,x3,x4 \geq 0$$

### Passo 1 - Base x3, x4

Ponto A: x1=0 x2=0 x3=24 x4=35

|L | VB    |  x1   | x2     | x3    | x4    | *     |
|:-| :---- | :---- | :----  | :---- | :---- | :---- |
|L1| x3    | 1     |  1     | 1     | 0     | 24    |
|L2| x4    | 3     |  2     | 0     | 1     | 60    |
|L3| *     | 40    |  35    | 0     | 0     | z     |

x1 entra na base, x4 sai da base (60/3=20 < 24/1=24)

$$L1 \leftarrow L1 -1/3 L2$$
$$L3 \leftarrow L3 -40/3 L2$$
$$L2 \leftarrow L2/3$$

### Passo 2 - Base x3, x1

Ponto B: x1=20 x2=0 x3=4 x4=20

|L | VB    |  x1   | x2     | x3    | x4    | *     |
|:-| :---- | :---- | :----  | :---- | :---- | :---- |
|L1| x3    | 0     |  1/3   | 1     | -1/3  | 4     |
|L2| x1    | 1     |  2/3   | 0     | 1/3   | 20    |
|L3| *     | 0     |  25/3  | 0     | -40/3 | z - 800 |

x2 entra na base, x3 sai da base (4/(1/3)=12 < 24/1=24)

$$L2 \leftarrow L2 -2 L1$$
$$L3 \leftarrow L3 -25 L1$$
$$L2 \leftarrow L2/(1/3)$$

### Passo 3 - Base x2, x1

Ponto C: x1=12 x2=12 x3=0 x4=0

|L | VB    |  x1   | x2     | x3    | x4    | *     |
|:-| :---- | :---- | :----  | :---- | :---- | :---- |
|L1| x2    | 0     |  1     | 3     | -1    | 12    |
|L2| x1    | 1     |  0     | -2    | -1    | 12    |
|L3| *     | 0     |  0     | -25   | -15/3 | z - 900 |

Solução ótima! $z^* = 900$.
