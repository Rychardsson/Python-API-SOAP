# Python-API-SOAP

Este projeto serve para criar um servidor SOAP usando Python. Esse servidor pode receber solicitações (requests) via o protocolo SOAP, processar essas solicitações e retornar respostas (responses) apropriadas. SOAP (Simple Object Access Protocol) é um protocolo baseado em XML usado para troca de informações estruturadas na implementação de serviços web.

## Funcionalidade Específica do Código

O código define um serviço de calculadora com quatro operações básicas:

- **Soma (`add`)**: Recebe dois números inteiros e retorna a soma deles.
- **Subtração (`subtract`)**: Recebe dois números inteiros e retorna a diferença entre o primeiro e o segundo número.
- **Multiplicação (`multiply`)**: Recebe dois números inteiros e retorna o produto deles.
- **Divisão (`divide`)**: Recebe dois números inteiros e retorna o quociente do primeiro número pelo segundo. Se o segundo número for zero, ele gera um erro, pois a divisão por zero não é permitida.

## Como Utilizar

1. **Execução**: Ao executar o código, você cria um servidor que escuta as requisições SOAP em `http://127.0.0.1:8000`.

2. **Interação**: Clientes (ou seja, outros programas ou sistemas) podem enviar mensagens SOAP para esse servidor. As mensagens devem especificar qual operação desejam realizar (por exemplo, soma, subtração) e fornecer os números para a operação.

3. **Resposta**: O servidor processa a solicitação, executa a operação matemática solicitada e retorna o resultado ao cliente em formato XML.

