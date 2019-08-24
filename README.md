#                                          **Instalando virtualenv e virtualenvwrapper**
                                            
O virtualenv e virtualenvwrapper nos dá um ambiente dedicado para cada projeto Django que você criar. Enquanto isso não é obrigatório, é considerado a melhor prática e irá lhe economizar tempo no futuro quando estiver pronto para implantar seu sistema. Simplesmente digite:

> **pip install virtualenvwrapper-win**

Então crie um ambiente virtual para seu projeto:

> **mkvirtualenv myproject**

O ambiente virtual será ativado automaticamente e você irá ver “(myproject)” próximo ao “prompt” na linha de comando que indica isso. Se você iniciar uma nova linha de comando, você irá precisar ativar o ambiente novamente usando:

> **workon myproject**
