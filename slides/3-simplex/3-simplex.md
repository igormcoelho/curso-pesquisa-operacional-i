---
author: Igor M. Coelho
title: Pesquisa Operacional
date: 6 de Julho de 2020
transition: page
fontsize: 10
header-includes:
- <link rel="stylesheet" type="text/css" href="general.css">
- <link rel="stylesheet" type="text/css" href="reveal-beamer.css">
---


# Método Simplex

-----

## Sobre esse material

Esses slides foram possíveis devido a contribuições de diversas pessoas/materiais, em especial:

- Notas do prof. Marcone Jamilson Freitas Souza
- Livro Nelson Maculan e Marcia Fampa
- Livro-texto do curso
- [2] Tutorial ilectures (https://igormcoelho.github.io/ilectures-pandoc/)
- Minha esposa Cristiane Tavares pelas valiosas dicas na elaboração desse material

-----

## Fundamentos Necessários

Caso não se sintam confiantes nos tópicos abaixo, façam uma revisão antes de aprofundar neste material:

- Álgebra Linear e Geometria Analítica
   * Equação da Reta
   * Operações Vetoriais
   * Operações com Matrizes
- Métodos Numéricos
   * Método da Eliminação de Gauss
- Cálculo
   * Gradientes e Otimização



# História do Simplex

------

## Breve história

De acordo com Maculan&Fampa (2006)[^1], as primeiras ideias de como otimizar um sistema de desigualdades lineares foi explorado por Fourier[^2] em 1880, porém somente George Dantzig[^3] em 1947 que de fato propôs o método de resolução _simplex_.

O simplex é um algoritmo reconhecidamente bem-sucedido, tendo sido implementado em diversos _solvers_ de computador altamente eficientes, como CPLEX, Gurobi, CBC (_open-source_), etc.

[^1]: N. Maculan e M. Fampa. _Otimização Linear_. Editora UnB, 2006.
[^2]: Fourier, J.B.J. _Oeuvres_. "Second Extrait", G. Darboux, Gauthiers-Villars, p. 325-328, 1880.
[^3]: Dantzig, George B. Maximization of a linear function of variables subject to linear inequalities. _Activity Analysis of Production and Allocation_. In: KOOPMANS, C. (Ed.). New York: Wiley, p. 359-373, 1951.

-------

## Aplicações no planejamento da produção e outros métodos

Em 1939, L. Kantorovich[^4] modelou e resolveu matematicamente problemas de planejamento da produção na União Soviética, ganhando o prêmio Nobel de Economia em 1975. 

Outros métodos para resolução: Métodos Elipsoidais de L. Khachian[^5] em 1978; Métodos de Pontos Interiores de N. Karmarkar[^6] em 1984; embora elegantes (com garantia de tempo polinomial), são tipicamente menos eficientes _na prática_ que o simplex.


[^4]: Kantorovich, L. _Métodos Matemáticos na Organização e no Planejamento da Produção_ (em russo). Leningrado: Editora da Univ. Estatal de Leningrado, 1939 (tradução inglesa: _Management Science_, v.6, p. 366-422, 1960).
[^5]: Khachian, L. A polynomial algorithm for linear programming. Doklady Academiia Nauk SSSR, v.244, p.191-194 (em russo. Tradução em inglês: _Soviet Mathematics Doklady_, v.20, p.191-194, 1979.).
[^6]: Karmarkar, N. A new polynomial algorithm for linear programming. _Combinatorica_, v.4, p.373-395, 1984.


# Fundamentos do Simplex

------

## Um Problema de Programação Linear

Considere o seguinte problema de programação linear:

$$maximizar \; f(x) = \sum_{j=1}^p c_j x_j$$
Sujeito a:
$$\sum_{j=1}^p a_{ij}x_j \leq b_i, \; i=1,2,...,q$$
$$x_j \geq 0, \; j=1,2,...,p$$

onde: $c_j$, $a_{ij}$ e $b_i$ são dados (números reais) e $x_j$ representa as variáveis de decisão (não-negativas).
Consideramos, neste caso, uma função objetivo $f(x)$ de maximização, e restrições do tipo $\leq$.

------

## Variáveis de Folga

Restrições do tipo $\leq$ (ou $\geq$) podem ser facilmente transformadas em igualdades, com a introdução de novas variáveis (não-negativas) de folga/falta (do inglês, _slack_/_surplus_):

$$\sum_{j=1}^p a_{ij}x_j \leq b_i \iff 
\begin{cases} 
\sum_{j=1}^p a_{ij}x_j + x_{p+1} = b_i,\\
x_{p+i} \geq 0
\end{cases} $$

$$\sum_{j=1}^p a_{ij}x_j \geq b_i \iff 
\begin{cases} 
\sum_{j=1}^p a_{ij}x_j - x_{p+1} = b_i,\\
x_{p+i} \geq 0
\end{cases} $$

------

## Variáveis de Folga (exemplo)

Um exemplo de transformação de $\leq$ em igualdade (introduzindo variável de folga $x_3$):

$$2x_1 + 3x_2 \leq 5 \Rightarrow 2x_1 + 3x_2 + \underbrace{x_3}_{x_3 \geq 0} = 5$$

O mesmo para restrições $\geq$ (introduzindo variável $x_4$):

$$x_1 + 6x_2 \geq 7 \Rightarrow x_1 + 6x_2 - \underbrace{x_4}_{x_4 \geq 0} = 7$$

------

## Outras conversões à forma padrão

Demais técnicas de conversão de variáveis/restrições:

- Existe $b_i < 0$:
   * **Solução:** multiplique a restrição $i$ por $-1$

- Existem variáveis não positivas (seja $x_k \leq 0$):
   * **Solução:** Substituir por variável $x_k' \geq 0$ tal que $x_k' = -x_k$

- Existem variáveis livres (seja $x_k \in \mathbb{R}$): 
   * **Solução:** substituir $x_k$ por $x_k' - x_k''$, tal que $x_k' \geq 0$ e $x_k'' \geq 0$

- Um problema de minimização pode ser convertido em maximização (vice-versa):
   $$ maximizar \; f(x) = - minimizar \; \{ - f(x) \} $$

-------

## Problema de Programação Linear Padrão

Sempre poderemos escrever um **problema de programação linear na forma padrão** (PPL):

$$(PPL):\; maximizar \; f(x) = \sum_{j=1}^n c_j x_j$$
$$\sum_{j=1}^n a_{ij} x_j = b_i, \; i=1,2,...,m$$
$$x_j \geq 0, \; j=1,2,...,n$$

tendo assim, $n$ variáveis e $m$ restrições.

--------

## Problema de Programação Linear Padrão (vetores)

De forma equivalente, podemos representar o PPL na forma vetorial:
$$(PPL):\; maximizar \; z = cx$$
$$\mathcal{A}x = b$$
$$x \geq 0$$

onde $c=(c_1\;c_2\;...\;c_n)$, $x^T = (x_1\;x_2\;...\;x_n)$, $b^T = (b_1\;b_2\;...\;b_m)$, $\mathcal{A}=(a_1\;a_2\;...\;a_n)$ e $a_j^T = (a_{1j} \; a_{2j} \; ... a_{mj})$, isto é, $c^T \in \mathbb{R}^n$, $x \in \mathbb{R}^n$, $b \in \mathbb{R}^m$, $\mathcal{A} \in \mathbb{R}^{m\times n}$ e $a_j \in \mathbb{R}^m$.



Definição 2.1 (Maculan&Fampa)
: Seja $X=\{x \in \mathbb{R}^n|\mathcal{A}x=b, x\geq 0 \}$ a **região viável** do PPL, e $x \in X$ uma **solução viável** do PPL. Se $x^* \in X$ tal que $cx^* \geq cx, \forall x\in X$, $x^*$ é uma **solução ótima**.

-------

## Exemplo de PPL

$$
\begin{matrix}
max & x_1 & +2x_2 \\
    & x_1 &       & \leq 2\\
    &     &  x_2  & \leq 2\\
    & x_1 & +x_2  & \leq 3\\
    & x_1,&  x_2  & \geq 0\\ 
\end{matrix}
\;
\Rightarrow
\;
\begin{matrix}
max & x_1 & +2x_2 & +0x_3 & +0x_4 & +0x_5\\
    & x_1 &       & +x_3  &       &       & = 2\\
    &     &  x_2  &       &  +x_4 &       & = 2\\
    & x_1 &  +x_2 &       &       & +x_5  & = 3\\
    & x_1,& x_2,  & x_3,  & x_4,  & x_5   & \geq 0\\
\end{matrix}
$$
$$
\underbrace
{
\begin{bmatrix}
1 & 0 & 1 & 0 & 0\\
0 & 1 & 0 & 1 & 0\\
1 & 1 & 0 & 0 & 1\\
\end{bmatrix}
}_{\mathcal{A}}
\underbrace
{
\begin{bmatrix}
x_1\\
x_2\\
x_3\\
x_4\\
x_5\\
\end{bmatrix}
}_{x}
=
\underbrace
{
\begin{bmatrix}
b_1\\
b_2\\
b_3\\
\end{bmatrix}
}_{b}
$$

(Vide slides prof. Marcone para visualização gráfica)

------

## Matriz básica e não-básica

A matriz $\mathcal{A}_{m \times n}$ pode ser particionada da seguinte maneira (supondo $posto(\mathcal{A})=m$, com $m$ colunas independentes): 

$$\mathcal{A} = ( \mathcal{B} \; \mathcal{N} )$$

onde $\mathcal{B}_{m \times m}$, chamada de matriz básica, é inversível; e $\mathcal{N}_{m \times (n-m)}$ é chamada de não-básica.
Analogamente, particionamos $x$ e $c$, tal que: $x^T = (x_B^T \; x_N^T)$, $c = (c_B \; c_N)$. Vetores $x_B$ e $c_B$ possuem $m$ componentes associadas à matriz $\mathcal{B}$.
Reescrevemos o PPL:

$$(PPL): \; maximizar \; z = c_B x_B + c_N x_N$$
$$\mathcal{B}x_B + \mathcal{N}x_N$$
$$x_B\geq 0, x_N \geq 0$$

-------

## Solução básica e não-básica

Explicitamos $x_B$ em função de $x_N$ (Eq. 2.10 em Maculan&Fampa):

$$x_B = \mathcal{B}^{-1}b - \mathcal{B}^{-1}\mathcal{N}x_N$$

Faremos $x_N=0$ e $\bar{x}_B = \mathcal{B}^{-1}b$.


Definição 2.2 (Maculan&Fampa)
: $\bar{x}$ é uma **solução básica**, se $\bar{x}^T = (\bar{x}_B^T \; 0)$. 

Quando $\bar{x}_B \geq 0$, será uma **solução básica viável**.

Sejam $I_B$ o conjunto dos índices das colunas de $\mathcal{A}$ pertencendo à matriz $\mathcal{B}$, e $I_N$ os demais índices de $\mathcal{A}$, tal que: $I_B \cap I_N = \varnothing$ e $I_B \cup I_N = \{ 1,2, ..., n\}$.

------

## PPL com matriz básica

$$(PPL): \; maximizar \; z = c_B\mathcal{B}^{-1}b - (c_B\mathcal{B}^{-1}\mathcal{N} - c_N)x_N$$
Sujeito a:
$$x_B=\mathcal{B}^{-1}b - \mathcal{B}^{-1}\mathcal{N}x_N$$
$$x_B \geq 0, x_N \geq 0$$

--------

## PPL com notação aprimorada

De acordo com Maculan&Fampa, definiremos:

- $\lambda = c_B\mathcal{B}^{-1}$, $\lambda^T \in \mathbb{R}^m$
- $\bar{x}_B = \mathcal{B}^{-1}b$, $\bar{x}_B \in \mathbb{R}^m$
- $z_j = \lambda a_j$, $(j \in I_B \cup I_N)$, $z_j \in \mathbb{R}$
- $y_j = \mathcal{B}^{-1} a_j$,  $(j \in I_B \cup I_N)$,  $y_j \in \mathbb{R}^m$
- $\bar{z} = c_B\mathcal{B}^{-1}b = \lambda b = c_B\bar{x}_B$.

Então teremos um novo PPL aprimorado:

$$(PPL): \; maximizar \; z = \bar{z} - \sum_{j \in I_N}(z_j - c_j)x_j$$
sujeito a:
$$ x_B=\bar{x}_B - \sum_{j \in I_N} y_j x_j$$
$$x_B \geq 0, x_j \geq 0, j \in I_N$$

------

## Otimalidade no PPL

Proposição 2.1 (de Maculan&Fampa)
: Se $\bar{x}_B \geq 0$ e $z_j - c_j \geq 0$, $\forall j \in I_N$, então o vetor $x^* \in \mathbb{R}^n$, onde $x^*_{B(i)} = \bar{x}_{B(i)}$, $i=1,2,...,m$ e $x^*_j=0$, $j \in I_N$, será uma solução ótima do (PPL).

Focaremos agora na versão do Simplex por tabelas, após apresentar um pseudo-código do algoritmo (com base no livro-texto de Arenales).

# Detalhamento do Simplex

-----

## Simplex para problemas de $\leq$ 

O Simplex consiste de duas fases, onde a primeira consiste em encontrar uma base $\mathcal{B}$.

Para problemas com restrições $\leq$, as variáveis de folga introduzidas no modelo irão naturalmente formar uma matriz identidade $\mathcal{I}_m$. 

Assim, escolheremos essas variáveis de folga como _variáveis básicas_, atribuindo valor zero a todas as demais _variáveis não-básicas_ (originais do modelo).
Teremos assim uma base inversível $\mathcal{B} = \mathcal{I}_m$.
Neste caso, a primeira fase do Simplex já é naturalmente efetuada.

------

## Pseudo-código do Simplex (Fase II) livro-texto

1. Passo 1: cálculo da solução básica
$$
\begin{cases}
\bar{x}_B = \mathcal{B}^{-1}b\\
\bar{x}_N = 0
\end{cases}
$$
2. Passo 2: cálculo dos custos relativos
   1. Vetor multiplicador simplex
      - $\lambda^T = c_B^T\mathcal{B}^{-1}$
   1. Custos relativos
      - $\hat{c}_{N(j)}=c_{N(j)} - \lambda^T a_{N(j)}, \; j=1,2,...,n-m$
   1. Determinação de variável a entrar na base 
      - $\hat{c}_{N(k)} = min\{\hat{c}_{N(j)}, j=1,...,n-m\}$ (a variável $x_{N(k)}$ entra na base)
3. Passo 3: teste de otimalidade (minimização)
   - Se $\hat{c}_{N(k)} \geq 0$, então: _pare_ (solução atual é ótima!).

--------

## Pseudo-código do Simplex (Fase II) livro-texto

4. Passo 4: Cálculo da direção Simplex
   - $y = \mathcal{B}^{-1} a_{N(k)}$
5. Passo 5: Determinação do passo e variável a sair da base
   - Se $y \leq 0$, então: _pare_ (não existe solução ótima finita: $f(x) \rightarrow -\infty$)
   - Caso contrário, determine a variável a sair da base pela razão mínima:
   $$\hat{\varepsilon}=\frac{\hat{x}_{B(\ell)}}{y_\ell} = min\left\{ \frac{\hat{x}_{B(i)}}{y_i}: y_i > 0, i = 1, ..., m \right\}$$ (variável $x_{B(\ell)}$ sai da base)
6. Passo 6: atualização
   - matriz básica: $\mathcal{B}=(a_{B(1)}\;...\;a_{B(\ell-1)}\;a_{N(k)}\;a_{B(\ell+1)}\;...\;a_{B(m)})$
   - não-básica: $\mathcal{N}=(a_{N(1)}\;...\;a_{N(k-1)}\;a_{B(\ell)}\;a_{N(k+1)}\;...\;a_{N(n-m)})$
   - incrementa iteração e volte ao Passo 1


# Tableau Simplex

------

## Simplex por Tabelas

Uma versão prática do Simplex pode ser feita com tabelas (_tableau simplex_). 

No caso de não haver apenas restrições $\leq$, é necessário criar _variáveis artificiais_, bem como um novo problema de otimização que busca _minimizar_ o valor delas (a zero!). Nesse PPL estendido, o peso inicial é $0$ para as variáveis do PPL original, e $1$ para as artificiais.
Quando a otimalidade é atingida nesse modelo (e as variáveis artificiais saem da base), podemos cortar as variáveis artificiais, e retornar ao modelo original (fase 2).

Os slides do prof. Marcone detalham o passo-a-passo dessa abordagem: [Slides SIMPLEX (pdf)](../thirdparty/Marcone-SIMPLEX.pdf).

------

## Lista de Exercícios

A lista de exercícios está disponibilizada no site.
