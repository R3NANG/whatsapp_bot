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
+ Linha 12: Altere para o sufixo que você costuma salvar seus contatos. Ex: cliente, loja, etc.
+ Linha 14: Altere para a mensagem que deseja enviar para os contatos. Ex: Bom dia! Estou com um novo produto que possa ser do seu interesse!
+ Agende um contato com um nome que faça com que ele seja o último da sua lista, eu usei como exemplo "Zfinal Teste" em um contato que bloqueei. É importante que ele também tenha o sufixo que você determinou nos outros contatos. Este contato serve como ponto de parada de execução do programa.
+ Linha 32: Altere o title para o nome do último contato da sua lista, deve ser o nome exato.
