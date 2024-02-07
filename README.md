# calculadora_inteli

Ponderada semana 1

Aplicação: Calculadora simples. Recebe dois números inteiros e uma operação (soma, subtração, multiplicação, divisão ou potenciação). Retorna um número como resultado no terminal. Caso seja uma operação inválida, retorna uma mensagem de erro no terminal.

Commits (ordem cronoólica):

1. feat: ask for two numbers and a operation - Adicionar três inputs a fim de receber do usuário o primeiro número, o segundo número e a operação desejada;
2. feat: add functions 'sum', 'sub', 'multp', 'div' - Adicionar as funções de somar, subtrair, multiplicar e dividir;
3. feat: add a condicional structure to 'operation' variable - Adicionar uma estrutura de condicionais para a variável 'operation';
4. style: add message on error - Adicionar uma mensagem de 'shut down' quando operação não reconhecida;
5. refactor: change the condicional structure - Refatoração da estrutura de condicionais. Adiciona um dicionário de operações com {número_da_operação: função}
6. feat: add a main function to reset after an operation - Adicionar uma função 'main' para que seja chamada após cada operação bem sucedida (para reiniciar a calculadora). Caso operação não reconhecida, calculadora não se reinicia;

Criação da branch 'potenciacao': 7. feat: add new operation (potentiation) - Adiciona potenciação ao dicionário de operações.

Merge de 'potenciacao' na 'main'

8. docs: add READ.me - Descreve o projeto e todos os commits
