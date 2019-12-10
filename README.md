# **Bem Vindo ao votAluno!**
Nesta sessão você poderá entender o que está por trás deste sistema.

# **Banco de Dados**
Como banco de dados foi escolhido o SQLite, pois é o mais versátil para se utilizar com o framework Django. Mas Também é possível migrá-lo para outros tipos de banco, como o PostgreSQL.

# **Criando uma nova virtualenv**

O processo de criação de uma virtualenv é bastante simples e pode ser feito utilizando um único comando, como podemos ver abaixo:

> **virtualenv nome_da_virtualenv**

O mais comum é criar a virtualenv na raiz do projeto que ela irá pertencer. Isso permite uma organização maior das virtualenvs que possuímos em nosso computador:

Com isso, criamos a virtualenv do projeto chamada “venv”. É ela quem vai comportar todos os pacotes necessários para a execução do projeto.

# **Ativando uma virtualenv**
Após criar uma virtualenv, precisamos ativá-la para que possamos instalar os pacotes necessários do projeto. Para isso, utilizamos o seguinte comando:

> **source nome_da_virtualenv/bin/activate** (Linux ou macOS)

ou

> **nome_da_virtualenv\Scripts\activate** (Windows)

O comando acima irá ativar a virutalenv e teremos um retorno similar ao ilustrado abaixo:


Note que o nome da virtualenv, agora, é exibido antes do caminho do diretório em que estamos. Isso indica que a virtualenv foi ativada com sucesso.

# **Desativando uma virtualenv**
Para desativar uma virtualenv utilizamos o comando **_desactivate_**.

# **Instalando pacotes**
Com a virtualenv ativada, podemos instalar os pacotes necessários do projeto utilizando o próprio PIP.
Agora, instalamos o pacote Django, em sua versão mais atual, na virtualenv do projeto “projeto_python”.
Agora, se precisarmos instalar uma outra versão do Django em outro projeto, bastaria criar uma nova virtualenv e realizar o mesmo processo.

### Essas e outras dicas eu encontrei no site [**_TreinaWeb_**](https://www.treinaweb.com.br/blog/criando-ambientes-virtuais-para-projetos-python-com-o-virtualenv/)

### [Aprendendo Django](https://data-flair.training/blogs/django-architecture/)
