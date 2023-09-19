<h1>PADRÕES DE PROJETOS</h1>
<h2>Composit</h2>
<p>O padrao de projeto composite tem como o intuito de simular uma "arvore" onde cada nó interno da arvore sera representado como o composit e cada no externo sera representado como uma leaf.</p>

![Exemplo da arvore](https://github.com/Tkl02/padroes_de_projeto/assets/84601712/a3f762c2-f572-4d99-bc07-70dc19d77a3b)

<p>No exemplo aseguir sera usado a compra de peças de computadores, onde cada peça e uma leaf e cada caixa e um composit</p>

![Exemplo composit da compra de peça de um PC](https://github.com/Tkl02/padroes_de_projeto/assets/84601712/96f2d5da-1523-4abb-b653-5d2d4567a5d8)

<p>Suponhamos que ultilizaremos a operação "getprice" nos poderiamos obter os preços não so apenas de cada leaf(peças) como tambem de seus composit(caixas), ou seja esta operação sera aplicada no composit definido e em todas as suas dependencias</p>
