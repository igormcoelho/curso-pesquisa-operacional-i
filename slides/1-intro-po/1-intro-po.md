---
author: Igor M. Coelho
title: Pesquisa Operacional
date: 18 de Junho de 2020
transition: page
fontsize: 10
header-includes:
- <link rel="stylesheet" type="text/css" href="general.css">
- <link rel="stylesheet" type="text/css" href="reveal-beamer.css">
---


# Introdução à Pesquisa Operacional

-----

## Sobre esse material

Esses slides foram preparados com base em diversos materiais da literatura, em especial:

- [1] Profa. Maristela Oliveira dos Santos (ICMC/USP): "Introdução à Pesquisa Operacional - Otimização Linear", 2010.
- [2] Tutorial ilectures (https://igormcoelho.github.io/ilectures-pandoc/)


# O que é Pesquisa Operacional?


-----

## O que é pesquisa operacional?

**Pesquisa Operacional - PO** (pt-br), Investigação Operacional (pt), Operational Research (en-gb), Operations Research (en), Investigación Operativa (es), Recherche Opérationnelle (fr), ...

Da [Wikipedia](https://pt.wikipedia.org/wiki/Investiga%C3%A7%C3%A3o_operacional):

> "Ramo interdisciplinar da matemática aplicada que faz uso de modelos matemáticos, estatísticos e de algoritmos na ajuda à tomada de decisões".

-----

## Associações de PO no Brasil e no Mundo

- IFORS - International Federation of Operacional Research
Societies
- EURO - The Association of European Operational Research
Societes
- APDIO - Associação Portuguesa de Investigação Operacional.
- SOBRAPO - Sociedade Brasileira de Pesquisa Operacional

-----

## INFORMS Journals

Alguns journals do *Institute for Operations Research and the Management Sciences* (INFORMS): 

- Decision Analysis
- Information Systems Research
- INFORMS Journal on Computing
- INFORMS Transactions on Education
- Management Science
- Manufacturing & Service Operations Management
- Marketing Science
- Mathematics of Operations Research
- Operations Research
- Organization Science
- Service Science
- Transportation Science

-----

## Onde pode ser aplicada?

- Pode ser aplicada a problemas onde é necessário especificar, de forma quantitativa, a condução e a coordenação das operações ou atividades dentro de uma organização.
- A natureza da organização pode ser financeira, industrial, militar, governamental, etc.

-----

## Tomada de decisões (escopo)

- (Em uma estrada) Qual o melhor caminho a tomar?
- (Na bolsa de valores) Em que companhias investir?
- (Em uma indústria) O que e em que ordem produzir?
- (Em um trabalho em grupo) Que pessoas alocar a que tarefas?
- (Em uma companhia de distribuição) Que rede (elétrica, de
gás, etc.) instalar?

# Um breve histórico da PO

------

## Um breve histórico da PO

- **1939-1945:** Durante a 2ª Guerra Mundial, as gerências
militares britânica e americana empregaram uma abordagem
científica para tratamento de problemas de gerenciamento de
recursos escassos (radares, tropas, munição, remédios etc.), de forma eficaz.
- **1936:** *British Military Applications* utilizaram o termo "operational research" (*en-gb*).
- **Problema:** Como usar radares? (Como aumentar a eficiência da informação fornecida por radares)

------

## Um breve histórico da PO

- Segunda Guerra Mundial: Problema: Tamanho dos comboios!
- O que é melhor usar ?
- vários comboios pequenos (mais rápidos)?
- poucos comboios grandes (mais protegidos)?

------

## II Guerra Mundial

- Melhoria das operações utilizadas:
- Operations research - Pesquisa Operacional


------

## Um breve histórico da PO

- 1947: Início do interesse das indústrias na utilização das técnicas desenvolvidas na área militar, para auxiliar no planejamento e controle da produção.
- A maioria desses problemas é formulada através de modelos
matemáticos lineares.

------

## Um breve histórico da PO


::::::::::::: {.columns}

::::: {.column width=40%}

![George Dantzig (1914-2005) - "pai da programação linear"](./img/dantzig.jpg "Dantzig"){width=80%}

:::::

::::: {.column width=60%}


- 1949: George B. Dantzig apresenta o Método Simplex para
resolver problemas de otimização linear (equações e (ou)
inequações lineares).
- George B. Dantzig - propõe o Método Simplex enquanto
trabalhava como Consultor em Matemática no controle da
força aérea americana.
- mais datas( http://www.lionhrtpub.com/orms/orms-10-
02/frhistorysb1.html)


:::::


:::::::::::::

# Modelagem em PO

------

## Diagrama de um projeto de PO

![Modelo vs Mundo Real. *Retirado de [1]*](2020-06-22-22-54-18.png){width=80%}


------

## Construindo um modelo matemático

- **Passo Fundamental:** Ouvir aquele que lida com o problema real.
- **Passo 1:** Descobrir o que deve ser determinado (variáveis do problema).
- **Passo 2:** Descobrir o que está disponível (dados do problema).
- **Passo 3:** Reproduzir os caminhos que levam a uma solução (equações/formulações)


# Conceitos de Otimização

-----

## Problema de Otimização

- A busca de uma *solução mais adequada* entre diversas *soluções alternativas* traz consigo os elementos de um **Problema de Otimização**
- Um critério de avaliação das soluções alternativas, o qual nos
permite dizer que uma solução é “melhor” que outra (objetivo ou subjetivo).
- A este critério de avaliação chamamos de **função objetivo**, que buscamos otimizar, ou seja, *maximizar* ou *minimizar*.
- Por outro lado, as soluções alternativas devem ser passíveis de execução indicando a presença de restrições que devem ser respeitadas.


------

## Problema de Otimização

- De outra forma: temos uma função $z$, chamada função objetivo, definida no conjunto de soluções alternativas (viáveis), digamos $\mathcal{S}_f$, tipicamente mapeada nos reais: $z : \mathcal{S}_f \mapsto \mathbb{R}$
- Um problema de otimização (de *minimização*) é definido por:

$$min\; z(s)$$
$$sujeito\;a: \; s \in \mathcal{S}_f$$


------

## Problema de Otimização

Dependendo do comportamento de $z(s)$ e de como o conjunto $\mathcal{S}_f$ é descrito, temos diferentes classes de problemas de otimização, para os quais uma variedade de métodos de solução tem sido desenvolvida:

- Otimização linear.
- Otimização não linear.
- Otimização Inteira.
- Controle ótimo.


# Aplicações de PO

------

## Algumas aplicações

- indústria de petróleo: extração, refinamento, mistura e distribuição.
- indústria de alimentos: ração animal (problema da mistura).
- planejamento da produção: dimensionamento de lotes (o que, quando e quanto produzir?).
- indústria siderúrgica: ligas metálicas (problema da mistura).
- indústria de papel: otimização do processo de cortagem de bobinas.
- indústrias de móveis: otimização do processo de cortagem de placas retangulares.
- aplicações financeiras: otimização do fluxo de caixa, análise de carteiras de investimento.


--------

## Níveis de planejamento

Quando se fala em planejamento, se consideram três tipos, de acordo com a duração:

- Estratégico (longo prazo)
- Tático (médio prazo)
- Operacional (curto prazo)

Mais detalhes serão discutidos para cada problema abordado no curso.


# Tarefa

-----

## Tarefa 1

Escrevam um texto resumido com explicando alguns problemas inspiradores e personalidades da PO.

- Falar sobre o problema do caminho mínimo
- Falar sobre o problema de fluxo máximo
- Falar sobre George Dantzig
- Falar sobre John von Neumann

-----

## Tarefa 2

- Visitar o site das agremiações de PO, nacionais e internacionais.

- Visitar os sites do Simpósio Brasileiro de Pesquisa Operacional (SBPO) e procurar dentre os trabalhos publicados nos Anais dos eventos **TRÊS trabalhos** interessantes (pelo título e resumo)

Dica: link dos anais do sbpo 2017 - http://www.sbpo2017.iltc.br/trabalhos-completos.html

---------

## Reprodução do material

Esses slides foram escritos utilizando pandoc, segundo o tutorial ilectures:

- https://igormcoelho.github.io/ilectures-pandoc/

Licença: Creative Commons 2020

Igor Machado Coelho
