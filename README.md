## Pesquisa Operacional I

_Curso de **Pesquisa Operacional I** do [Prof. Igor Machado Coelho](https://igormcoelho.github.io), oferecido pelo [Instituto de Computação (IC) da Universidade Federal Fluminense (UFF)](http://www.ic.uff.br)._ **versão online:** [igormcoelho.github.io/curso-pesquisa-operacional-i/](https://igormcoelho.github.io/curso-pesquisa-operacional-i/)

[Código-fonte no GitHub](https://github.com/igormcoelho/curso-pesquisa-operacional-i)
![Estrelas](https://img.shields.io/github/stars/igormcoelho/curso-pesquisa-operacional-i)
![Licença](https://img.shields.io/github/license/igormcoelho/curso-pesquisa-operacional-i)

_**Última atualização:** Julho/2020 (Período ACE 2020.1)_

### Tópicos do Curso

0. [Introdução ao curso](slides/0-intro-curso/0-intro-curso.md): [PDF](slides/0-intro-curso/0-intro-curso.pdf) [Online](https://igormcoelho.github.io/curso-pesquisa-operacional-i/slides/0-intro-curso/index.html)
1. [Introdução a PO](slides/1-intro-po/1-intro-po.md): [PDF](slides/1-intro-curso/1-intro-po.pdf) [Online](https://igormcoelho.github.io/curso-pesquisa-operacional-i/slides/1-intro-po/index.html)
2. [Modelagem](slides/2-modelagem/2-modelagem.md): [PDF](slides/2-modelagem/2-modelagem.pdf) [Online](https://igormcoelho.github.io/curso-pesquisa-operacional-i/slides/2-modelagem/index.html)
   * Material complementar: [Slides Prof. Marcone (Modelagem-P2)](./slides/thirdparty/Marcone-Modelagem-Parte-2.pdf)
3. [Simplex](slides/3-simplex/3-simplex.md): [PDF](slides/3-simplex/3-simplex.pdf) [Online](https://igormcoelho.github.io/curso-pesquisa-operacional-i/slides/3-simplex/index.html)
   * Material complementar: [Slides Prof. Marcone (Tab.Simplex)](./slides/thirdparty/Marcone-SIMPLEX.pdf)
4. [Programação Linear Inteira](slides/4-mip/4-mip.md): [PDF](slides/4-mip/4-mip.pdf) [Online](https://igormcoelho.github.io/curso-pesquisa-operacional-i/slides/4-mip/index.html)
   * Material complementar: [Slides Prof. Marcone (B&B)](./slides/thirdparty/Marcone-Branch-and-Bound.ppt)
5. Fundamentos de Otimização
6. Meta-heurísticas
   * Artigo de Kenneth Sörensen (2013): [_Metaheuristics -- the Metaphor Exposed_](https://doi.org/10.1111/itor.12001) - [PDF](https://www.researchgate.net/publication/237009138_Metaheuristics_--_the_metaphor_exposed)
   * Artigo co-autorado com Gustavo Semaan et al (2020): _A Brief History of Heuristics, from Bounded Rationality to Intractability_, **IEEE Latin America Transactions** (to appear).
   * Materiais do Prof. Marcone:
      - [Introdução PDF](slides/thirdparty/marcone-meta/Introducao.pdf)
      - [Heurísticas Construtivas PPT](slides/thirdparty/marcone-meta/Ico-construtivas.ppt)
      - [Heurísticas de Refinamento PPT](slides/thirdparty/marcone-meta/Ico-refinamento.ppt)
      - [Algoritmos Genéticos PPT](slides/thirdparty/marcone-meta/AGs.ppt)
      - [Busca em Vizinhança Variável PPT](slides/thirdparty/marcone-meta/VNS.ppt)
      - [BRKGA PDF](slides/thirdparty/marcone-meta/brkga.pdf)
      - [Busca Tabu PPT](slides/thirdparty/marcone-meta/Ico-BT.ppt)
      - [PSO PPT](slides/thirdparty/marcone-meta/PSO.ppt)
      - [Simulated Annealing PPT](slides/thirdparty/marcone-meta/SA.PPT)

- Avaliações:
   * [Prova 1 - 2020.1 ACE](./slides/avaliacoes/ace-20201-prova.pdf)
      - [Solução Questão 1](./slides/avaliacoes/1-ex_prova_tv.py)
      - [Solução Questão 2](./slides/avaliacoes/2-ex_prova_cam.py)
      - [Solução Questão 3](./slides/avaliacoes/3-ex_tableau.md)
      - Solução Questão 4

- Materiais Complementares do Curso:
   * Apostila Otimização Combinatória: [Apostila Prof. Marcone (Apost. Otim.)](./slides/thirdparty/Marcone-Apostila-Otimizacao.pdf)
   * Manual Python-MIP: [QuickStart](https://python-mip.readthedocs.io/en/latest/quickstart.html)
   * Examples-MIP:
      - [knapsack.py](./slides/examples-mip/knapsack.py)
      - [ex1_marcone.py](./slides/examples-mip/ex1_marcone.py)
   * Exemplo Simulated Annealing para Mochila (com OptFrame FCore):
      - [FCore-KP-SA.zip](./exemplo-optframe/FCore-KP-SA.zip)
   * Documentação do OptFrame no [readthedocs](https://optframe.readthedocs.io/en/latest)

- Algumas Personalidades da Área (em construção):
    * [Brian Wilson Kernighan](https://en.wikipedia.org/wiki/Brian_Kernighan)
      - [Kernighan-Lin algorithm for VLSI](https://en.wikipedia.org/wiki/Kernighan%E2%80%93Lin_algorithm)
    * [Christos Papadimitriou](https://engineering.columbia.edu/faculty/christos-papadimitriou)
    * George Dantzig
    * Nelson Maculan
    * Shen Lin
      - [Lin-Kernighan heuristic for TSP](https://en.wikipedia.org/wiki/Lin%E2%80%93Kernighan_heuristic)
    * ...

- Curiosidades:
    * [Pedra, Papel e Tesoura em LP](https://www.youtube.com/watch?v=I_vBhNf5x9Y): contribuição [Rodolfo Araujo](https://github.com/rodoufu)
    * Genético para Caminhadas (gaits): https://www.youtube.com/watch?v=pgaEE27nsQw

- Livros interessantes:
    * In Pursuit of the Traveling Salesman - William J. Cook

...

### Como esses slides foram feitos?

Estes slides foram feitos em `markdown` e `pandoc` (super fácil!) de acordo com o tutorial [ilectures-pandoc](https://github.com/igormcoelho/ilectures-pandoc).

Basicamente, é necessário instalar o pandoc e, opcionalmente, copiar alguns filtros úteis do tutorial (dois arquivos python). Então, é possível gerar, a partir do `markdown`, uma versão PDF LaTeX+Beamer, e outra web utilizando RevealJS. O tutorial explica tudo em detalhes.

O mais legal é que a edição do slide tem uma visualização em tempo real, com plugins disponíveis para editores populares como Atom e VSCode.
Uma demonstração foi colocada no site do ilectures: [https://github.com/igormcoelho/ilectures-pandoc#demonstrations](https://github.com/igormcoelho/ilectures-pandoc#demonstrations).


### Licença CC-BY 4.0

Você pode: (Share) copiar e redistribuir esse material em qualquer formato; (Adapt) adaptar esse material, mesmo que para uso comercial.

Você deve: (Attribution) dar crédito apropriado, bem como um link para o original e a indicação das mudanças que você fez.

Veja licença original [CreativeCommons CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)

```
curso-pesquisa-operacional-i (c) by Igor M. Coelho

curso-pesquisa-operacional-i is licensed under a
Creative Commons Attribution 4.0 International License.

You should have received a copy of the license along with this
work. If not, see <http://creativecommons.org/licenses/by/4.0/>.
```


Copyleft 2020
