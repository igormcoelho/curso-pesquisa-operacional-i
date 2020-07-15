## Pesquisa Operacional I

_Curso de **Pesquisa Operacional I** do [Prof. Igor Machado Coelho](https://igormcoelho.github.io), oferecido pelo [Instituto de Computação (IC) da Universidade Federal Fluminense (UFF)](http://www.ic.uff.br)._

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
   * Artigo de Kenneth Sörensen (2013): _Metaheuristics -- the Metaphor Exposed_.
   [DOI](https://doi.org/10.1111/itor.12001) - [PDF](https://www.researchgate.net/publication/237009138_Metaheuristics_--_the_metaphor_exposed)

- Extras:
   * Material complementar: [Apostila Prof. Marcone (Apost. Otim.)](./slides/thirdparty/Marcone-Apostila-Otimizacao.pdf)
   * Manual Python-MIP: [QuickStart](https://python-mip.readthedocs.io/en/latest/quickstart.html)
   * Examples-MIP:
      - [knapsack.py](./slides/examples-mip/knapsack.py)
      - [ex1_marcone.py](./slides/examples-mip/ex1_marcone.py)


...

### Como esses slides foram feitos?

Estes slides foram feitos em `markdown` e `pandoc` (super fácil!) de acordo com o tutorial [ilectures-pandoc](https://github.com/igormcoelho/ilectures-pandoc).

Basicamente, é necessário instalar o pandoc e, opcionalmente, copiar alguns filtros úteis do tutorial (dois arquivos python). Então, é possível gerar, a partir do `markdown`, uma versão PDF LaTeX+Beamer, e outra web utilizando RevealJS. O tutorial explica tudo em detalhes.

O mais legal é que a edição do slide tem uma visualização em tempo real, com plugins disponíveis para editores populares como Atom e VSCode.
Uma demonstração foi colocada no site do ilectures: [https://github.com/igormcoelho/ilectures-pandoc#demonstrations](https://github.com/igormcoelho/ilectures-pandoc#demonstrations).
