# Automação de Envio de Mensagens no WhatsApp

Adaptado de um vídeo do canal Dev Aprender\
https://www.youtube.com/watch?v=_ZDBVeqyK6g

Ojetivo:
Enviar mensagem definida pelo usuário para todos os contatos que estão com determinado sufixo salvo no nome do contato.\
Como exemplo no programa, será enviado mensagem para todos os contatos que estão com o sufixo "Teste" salvo no nome:

Diego Teste\
Davi Teste\
Takeshi Teste\
... Teste

Por que usar este bot?\
Listas de transmissão são eficientes quando os contatos tem o seu número salvo, caso o contrário, não receberão as mensagens enviadas pela lista.\
Criar um grupo com os contatos é algo incoveniente. Além disso, você pode alcançar mais pessoas do que o máximo permitido em grupos (256 pessoas).

Para o funcionamento do seu caso:
+ Preencha todos os campos solicitados na interface gráfica (o campo contador serve para caso voce pare o programa durante a execucao, voce pode voltar de onde parou).
+ Agende um contato com um nome que faça com que ele seja o último da sua lista, eu usei como exemplo "Zfinal Teste" em um contato que bloqueei. É importante que ele também tenha o sufixo que você determinou nos outros contatos. Este contato serve como ponto de parada de execução do programa.
+ Linha 55: Altere o title para o nome do último contato da sua lista, deve ser o nome exato.
+ Após clicar em Iniciar, clique rapidamente na aba do chrome em que o bot irá funcionar, caso o contrário, os comandos do PyAutoGUI não serão reconhecidos e o bot não funcionará.
+ Não use este bot com contatos que usam a função de "mensagens temporárias", ao chegar em um contato com essa função, o bot da erro e não consegue prosseguir com a lista.
