# votAluno

## Sobre o projeto

Este é um sistema desenvolvido para ser entregue como TCC no curso Tecnólogo em Análise e Desenvolvimento de Sistemas ofertado pelo Instituto Federal de Rondônia - IFRO campus Vilhena.

### O que é?

O votAluno é um sistema de votação voltado para agilizar a realização dos conselhos de classe, automatizando os lançamentos dos votos e possuindo função de realizar avaliações bimestrais dos alunos, tornando as realizações dos conselhos mais fáceis e simples para os servidores das instituições.

### Funcionalidades

 - Gerenciar os perfis dos usuários;
 - Gerenciar os cadastros de  Disciplinas, Cursos, Turmas e Alunos;
 - Gerenciar as Avaliações realizadas pelos usuários;
 - Gerenciar as Votações e Votos dos conselhos;

### Sobre o desenvolvimento

Para o desenvolvimento do votAluno foi utilizado o framework Django e o deploy na plataforma Heroku.

## Getting Started

### Clonando o projeto

> git clone https://github.com/JeanSchnorr/votaluno.git

### Executando o projeto

Antes de tudo configure seu ambiente Django com a plataforma Heroku, para isso siga este tutorial [**aqui**](https://devcenter.heroku.com/articles/deploying-python).

Após isso logue-se faça a criação de um usuário administrador para o sistema:

>```heroku run python manage.py createsuperuser```

Em seguida faça o deploy e pronto

> ```git add . ```

> ```git commit -m "realizando deploy"```

> ```git push -f heroku master```

## Licença

A licença de uso escolhida para o projeto foi a MIT e pode ser encontrada [**aqui**](https://github.com/JeanSchnorr/votaluno/blob/master/LICENSE).
