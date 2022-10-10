<h1 align="center">Análise de caso AdviceHealth</h1>

<p align="center">
 <a href="#sobre">Sobre</a> •
 <a href="#features">Features</a> • 
 <a href="#prereq">Pré-requisitos</a> • 
 <a href="#play">Rodando a aplicação</a> • 
 <a href="#testes">Testes</a>
</p>


<div id="sobre">
<h3>Sobre</h3>
<p>Repositório criado para realização do teste de análise de caso da Advice Health.</p>
</div>

<h3 id="features">Features</h3>

- [x] Cadastro de pessoa
- [x] Cadastro de carro relacionado a pessoa


<h3 id="prereq">Pré-requisitos</h3>

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[Git](https://git-scm.com), [Docker](https://www.docker.com/). 
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

<h3 id="play">Rodando o Projeto</h3>

```bash
# Clone este repositório
$ git clone https://github.com/deusdeditvilar/advicehealth

# Acesse a pasta do projeto no terminal/cmd
$ cd advicehealth

# Inicie a aplicação com docker
$ docker-compose up -d --build

# Realize o migrate do banco de dados do Django
$ docker-compose exec web python manage.py migrate --noinput
```

O projeto estará rodando no endereço http://localhost:1337

<h3 id="testes">Visualizando testes</h3>

Caso queira visualizar os testes rodados na aplicação navegue até a pasta ``` carford ``` dentro do projeto e abra o arquivo ``` tests.py ```

E caso queira rodar os testes:
```bash
# Cole o seguinte comando no cmd
$ docker-compose exec web python manage.py test
```