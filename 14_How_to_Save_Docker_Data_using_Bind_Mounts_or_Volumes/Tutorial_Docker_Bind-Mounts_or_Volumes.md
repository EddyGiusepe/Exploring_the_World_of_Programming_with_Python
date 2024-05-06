<h1 align="center"><font color="pink">Como salvar permanentemente o banco de dados dentro do Docker</font></h1>


<font color="yellow">Data Scientist.: Dr. Eddy Giusepe Chirinos Isidro</font>


# <font color="gree">Contextualizando</font>
Por padrão, o Docker não mantém os dados criados por você dentro de um contêiner. Se você parar o contêiner ou iniciar ele, os dados no seu banco de dados ainda estarão lá. Mas se você remover um contêiner ou quiser recriá-lo, os dados desaparecerão.

<font color="red">E se você quiser manter os dados?</font> 

Felizmente, isso pode ser feito. No `Docker`, existem dois métodos para manter os dados de forma mais permanente.  

# <font color="gree">Volume ou Bind Mount</font>
O primeiro é chamado de `volume` e o segundo é chamado de `montagem vinculada`. 

Então, quais são as diferenças. 

* Um `volume` no Docker é essencialmente um diretório dentro do Docker. Ele pode ser acessado por contêineres e é mantido quando você remove um contêiner.

* Uma `montagem vinculada` no Docker é onde você vincula um diretório dentro do Docker a um diretório em sua máquina host, também conhecido como fora do Docker ou em seu computador.

<font color="red">Pré-requisitos:</font> 

* Docker em teu computador

* Imagem Docker com Database

Aqui, usaremos uma imagem `MySQL`, mas os conceitos funcionarão com qualquer imagem de banco de dados que você queira usar.

# <font color="gree">Vamos na prática</font>

## <font color="pink">Criando um `Volume`</font>

Começamos criando um volume:
```
docker volume create mysqlvol 
```
Você pode verificar a criação do volume usando os seguintes comandos: `docker volume ls` ou `docker volume list`.

Usando `MySQL`, assim:

* Sem usar o volume:
```
docker run -d --name mysql-wvol -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=multiple_regression mysql:latest
```

* Usando o volume:
```
docker run -d --name mysql-wvol -p 3306:3306 -e MYSQL_ROOT_PASSWORD=123456 -e MYSQL_DATABASE=multiple_regression --mount source=mysqlvol,target=/var/lib/mysql mysql:latest
```















Thanks God 🤗!