<h1 align="center">Python Threading Exercises</h1>

<p>Exercícios:</p>

<p>
    <strong>1)</strong> Fazer uma aplicação que rode 5 Threads que cada uma delas receba um inteiro chamado id como parâmetro e imprima no console o texto "Thread #" + id.
    Antes de imprimir o valor, deve-se fazer um sleep de 0.5 segundos.
</p>

<p>
    <strong>2)</strong> Fazer uma aplicação que, na main, inicialize uma variável id, inteira e inicialize 5 variáveis inteiras para valores, crie um vetor de parâmetros,
    com o id como primeiro parâmetro e um vetor com os 5 valores recebidos.

    As variáveis que recebem os valores devem receber, cada uma delas, um valor aleatório de 1 a 100.

    Esses parâmetros devem ser preenchidos para 3 chamadas de Threads.

    Faça 3 chamadas de Threads, passando os parâmetros e, cada Thread, deve calcular a soma de cada linha.

    Cada iteração do laço para a soma deve ser seguida por um sleep de 0.2 segundos.

    Ao final, deve-se imprimir a identificação da linha e o resultado da soma.
</p>

<p>
    <strong>3)</strong> Fazer uma aplicação de uma corrida de sapos, com 5 Threads, cada Thread controlando 1 sapo.

    Deve haver um tamanho máximo para cada pulo do sapo (em centímetros) e a distância máxima para que os sapos percorram.

    A cada salto, um sapo pode dar um salto de 0 até o tamanho máximo do salto (valor aleatório entre 1 e 5 cm).

    Após dar um salto, a Thread, para cada sapo, deve mostrar no console:
</p>

<ul>
    <li>Qual foi o tamanho do salto;</li>
    <li>Quanto o sapo percorreu.</li>
</ul>

<p>
    Assim que o sapo percorrer a distância máxima, a Thread deve apresentar que o sapo chegou.
</p>

<p>
    <strong>Dica:</strong> O exercício deve ser resolvido todo em console, ou seja, como se estivesse sendo narrado.
</p>

<p>
    <strong>4)</strong> No Sistema Operacional Linux, o comando para realizar uma operação de ping com 10 iterações é:
</p>

<pre><code>ping -4 -c 10 &lt;servidor&gt;</code></pre>

<p>
    No Sistema Operacional Windows, o comando para a mesma função é:
</p>

<pre><code>ping -4 -n 10 &lt;servidor&gt;</code></pre>

<p>
    Fazer uma aplicação Python que rode 3 Threads, sendo que a Thread deve identificar o SO para rodar o comando certo,
    fazendo operação de ping para os servidores:
</p>

<ul>
    <li>UOL (www.uol.com.br)</li>
    <li>Terra (www.terra.com.br)</li>
    <li>Google (www.google.com.br)</li>
</ul>

<p>
    Cada Thread deve ler a saída do ping imprimindo, a cada iteração:
</p>

<ul>
    <li>O nome do servidor (usar fixo: UOL, Terra ou Google);</li>
    <li>O tempo daquela iteração.</li>
</ul>

<p>
    Ao fim, deve-se exibir:
</p>

<ul>
    <li>O nome do servidor;</li>
    <li>O tempo médio obtido pela operação.</li>
</ul>

<p>
    Outros Sistemas Operacionais devem ser descartados.
</p>
