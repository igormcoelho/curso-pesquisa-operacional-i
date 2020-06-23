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


# Introdução ao Curso

-------

## Boas vindas

Bem-vind@s ao curso de Pesquisa Operacional!

Curso:

- Pesquisa Operacional - `TCC00318` - C.H. 64
- Site: https://igormcoelho.github.io/curso-pesquisa-operacional-i

Links úteis:

- http://www.ic.uff.br/index.php/pt/curriculo-e-disciplinas/disciplinas-obrigatorias
- https://app.uff.br/graduacao/quadrodehorarios
- Instituto de Computação (IC/UFF) - www.ic.uff.br
- Universidade Federal Fluminense (UFF) - www.uff.br

--------

## Sobre mim


::::::::::::: {.columns}

::::: {.column width=40%}

![Prof. Igor M. Coelho](./img/igor-lattes.jpeg "Pesquisa Operacional"){width=50%}

imcoelho at ic.uff.br (preferência)

igor.machado at gmail.com (emergência)

:::::

::::: {.column width=60%}

Me chamo Igor, e é um prazer apresentar esse curso para vocês! Sou professor e pesquisador da UFF, apaixonado pela área de pesquisa operacional, em especial, técnicas de otimização e meta-heurísticas (*ao final desse curso vocês também saberão bem o que é isso!*). Podem me contactar pelos emails ao lado (*substituam o 'at' por '@'*).
Esse curso está disponível no meu site pessoal no github: igormcoelho.github.io/curso-pesquisa-operacional-i


:::::


:::::::::::::

--------

## Sobre vocês

Gostaria que se apresentassem também (*nas aulas síncronas*) para nos conhecermos melhor! 

Ninguém aprende 100% do que o professor ensina, e nem o professor consegue ensinar 100% de um conteúdo, então cabe aos alunos: *ler*, *estudar* e *questionar* (muito!). **Juntos** podemos trabalhar para transmitir esse conhecimento valioso para cada um de vocês.

Sempre que tiverem uma dúvida ou curiosidade, perguntem! Toda pergunta é valiosa, e o conhecimento é construído em pequenas porções.

-------

## Acordo Aluno-Professor

*Para esse curso funcionar: tenham dedicação!*

É fundamental: 

- Não atrasar entrega de trabalho, mas caso precisem de uma extensão, solicitem antes do prazo! (*atrasos podem reduzir ou até zerar notas*)
- Buscar ao máximo não perder nenhuma aula (síncrona), e caso percam, busquem o quanto antes suprir esse conteúdo
- Nunca, em hipótese alguma, copiem um trabalho pronto! Além dos efeitos práticos (como perda de nota ou demais sanções previstas nas normas), não se enganem: quem mais perde é o aluno. Conhecimento é o bem mais valioso!
- Sempre citem as fontes, especialmente para trechos de textos. Sempre que possivel, indique a licença de uso de imagens e códigos (os buscadores permitem buscas com licença livre).


--------


## Contexto ACE

Atividades Acadêmicas Emergenciais (ACE)

- Definição de plano de trabalho: 26/06/2020

- Período: 29/06/2020 (segunda-feira) - 31/08/2020 (segunda-feira)

- Lançamento de notas: 31/08/2020

Teremos aulas síncronas no horários regulares, e devido ao período mais curto, teremos outras diversas atividades assíncronas complementares (vídeos, textos, trabalhos, ...) para suprir toda a carga horária.

---------

## Ementa

1. INTRODUÇÃO AOS CONCEITOS DE PESQUISA OPERACIONAL: ORIGEM, DESENVOLVIMENTO E ESTADO DA
ARTE;
2. PRINCIPAIS ÁREAS DA PESQUISA OPERACIONAL (PO);
3. CONCEITOS DE PROGRAMAÇÃO LINEAR, MODELAGEM, MÉTODOS;
4. CONCEITOS DE PROGRAMAÇÃO LINEAR INTEIRA, APLICAÇÕES;
5. ALGORITMOS HEURÍSTICOS E META-HEURÍSTICOS PARA PROBLEMAS DE OTIMIZAÇÃO COMBINATÓRIA;
6. SOFTWARES DE OTIMIZAÇÃO COMBINATÓRIA (CPLEX, XPRESS, ETC);
7. OUTROS TÓPICOS DE PESQUISA OPERACIONAL E SUAS APLICAÇÕES

--------

## Avaliação

Toda semana haverá atividades avaliativas assícronas (A), como listas de exercícios e resumos de textos/vídeos. Além disso, haverá uma prova escrita (E) e dois trabalhos de implementação (I), com apresentação.

A nota do curso será:

T = 30%A + 70%I

N = (E + T)/2

De acordo com as normas regulares da UFF, a nota mínima para aprovação é 6.

--------

## Cronograma

- Período: 29/06/2020 - 31/08/2020 

Tipo = Sinc./Assinc.

| Data       | Atividade                       | Tipo   |
| :---       |   :----                         | :---   |
| 29/06/2020 |  Introdução a PO e Modelagem    |  Sinc. |
| 06/07/2020 |  Conceitos Otimização Comb.     |  Sinc. |
| 13/07/2020 |  Programação Linear e Inteira   |  Sinc. |
| 20/07/2020 |  *                              |  Sinc. |
| 27/07/2020 |  Prática                        |  Sinc. |
| 03/08/2020 |  Prova Escrita (E)              |  Sinc. |
| 10/08/2020 |  (Meta-)Heurísticas             |  Sinc. |
| 17/08/2020 |  *                              |  Sinc. |
| 24/08/2020 |  Apresentação (I)               |  Sinc. |
| 31/08/2020 |  Lançamento Notas               |  Sinc. |


-------

## Ferramentas Necessárias

Para o andamento do curso e reprodução dos exemplos oferecidos, serão necessários alguns softwares, como:

- Python3 (preferência pela Anaconda3 com todos pacotes)
   * pacote `python-mip`: pip3 install python-mip
- Compilador C++ com suporte C++20 (GCC-10.1 ou clang-11)

No GNU/Linux, em especial família Debian/Ubuntu, a instalação é direta utilizando o sistema de pacotes `apt` ou executáveis providos nos respectivos sites dos projetos. No Windows é recomendado instalar versões nativas. Ou opção para utilizar os mesmos pacotes Linux no Windows, é utilizar o WSL para simular um terminal Ubuntu:

- Tutorial WSL (cortesia Anderson Zudio):
https://docs.google.com/document/d/1eHT19VPVyY3VlPT-820Ztf_rhZ4DORxaQDOZFdlDaus/edit?usp=sharing



--------

## Bibliografia Recomendada

::::::::::::: {.columns}

::::: {.column width=40%}

![Livro Referência](./img/livro.jpeg "Pesquisa Operacional"){width=50%}

:::::

::::: {.column width=60%}

Buscaremos suprir o conteúdo especialmente através de materiais com licença livre (slides, apostilas, vídeos, textos, ...). Como livro texto, recomendamos o livro: *"Arenales M.,  Armentano V., Morabito R., Yanasse H. Pesquisa Operacional. Rio de Janeiro: Editora Campus. (2007)"*.

:::::


::::::::::::: 


# Agradecimentos

-----

## Software

Esse material de curso só é possível graças aos inúmeros projetos de código-aberto que são necessários a ele, incluindo:

- pandoc
- LaTeX
- GNU/Linux
- git
- markdown-preview-enhanced (github)
- visual studio code
- atom
- revealjs
- ...

-----

## Empresas

Agradecimento especial a empresas que suportam projetos livres envolvidos nesse curso:

- github
- gitlab
- microsoft
- google
- ...

-----

## Pessoas

Em especial, agradeço a colaboradores que tornaram esse material possível (em ordem alfabética):

- Anderson Zudio (tutorial)
- Haroldo Gambini (python-mip)
- Luiz Satoru Ochi (slides)
- Marcone Jamilson Freitas Souza (slides)
- Vitor Nazário Coelho (site)
- ...

-----

## Reprodução do material

Esses slides foram escritos utilizando pandoc, segundo o tutorial ilectures:

- https://igormcoelho.github.io/ilectures-pandoc/

Licença: Creative Commons 2020

Igor Machado Coelho