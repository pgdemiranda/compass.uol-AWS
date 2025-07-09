# Desafio da Sprint 7

O objetivo é praticar a combinação de conhecimentos vistos no Programa, fazer um mix de tudo que já foi feito. Para essa *Sprint*, realizamos o processamento dos dados na camada **REFINED**, uma camada do data lake em que os dados estão prontos para análise e extração de *insights*, e a sua origem corresponde aos dado da camada anterior, que chamamos de **TRUSTED**.

## Entregáveis

- [] Todo o código, comentários, evidências e demais artefatos desenvolvidos para resolver o desafio;
    - Os códigos foram disponibilizados em formato `.py` e comentados neste arquivo README.md.

- [] Arquivo **README.md** com evidências imagens/prints de realização do desafio, bem como documentação de explicação de cada parte executada;
    - As evidências foram armazenadas no diretório [Evidências](../Evidências/) e as observações para resolução do desafio dessa sprint se enconta neste arquivo README.md.

- [x] Modelo de Dados da camada **REFINED** desenhado em ferramenta de modelagem;
    - Modelagem representada no arquivo [etapa1.png](./etapa-1/etapa1.png).

- [] Código desenvolvido com devidos comentários:
    - [] Arquivo contendo código Python no formato `.py` representando código *AWS Glue* para criar a camada **REFINED**;

## Sumário

- [Etapa 1 - Modelagem de Dados Camada Refined](#etapa-1---modelagem-de-dados-camada-refined)

- [Etapa 2 - Processamento Camada Refined](#etapa-2---processamento-camada-refined)

## Preparação

Não foi requisitada nenhuma preparação como nas etapas anteriores. Porém, realizamos uma série de exames para a execução das etapas dessa *Sprint*: 

- Conferimos o nosso bucket que funciona como datalake, o **pgdm-datalake**, e os diretórios das camadas **RAW** e **TRUSTED** para nos certificar que constavam lá todos os arquivos necessários;

- Através do **AWS Athena**, consultamos os dados que havíamos previamente catalogados dentro da camada **TRUSTED**, até para entendermos quais dados precisam ser limpos e quais as dimensões serão trazidas para a camada **REFINED**. 

# Desafio

Realizamos a terceira etapa do nosso Desafio Final de Filmes e Séries. Os dados devem ser persistidos na camada **REFINED**, onde os dados obtidos e processados nas etapas anteriores devem ser processados em tabelas dimensões e fatos, catalogados com *AWS Glue* para que possam ser analisados posteriormente com *AWS Athena* utilizando comandos SQL. A modelagem dos dados foi realizada pensando nossas questões originais, formuladas na primeira etapa do desafio final.

Para essa etapa, não podemos usar notebooks do Glue, os jobs precisam ser desenvolvidos com o *script editor*, e a configuração dos jobs devem atentar para esses detalhes:
    
    - Worker type: G 1x;
    
    - Requested number of workers: 2;

    - Job Timeout (minutes): 60, ou menos, se possível.

Antes de começarmos as etapas nos realizamos as preparações já mencionadas anteriormente: conferimos os arquivos que já estão em nosso datalake, o bucket **pgdm-datalake**, e os diretórios **RAW** e **TRUSTED**, além de conferir como esses dados já estão catalogados com o **AWS Athena**.

## [Etapa 1 - Modelagem de Dados Camada Refined](./etapa-1/)

Antes de mais nada, é necessário relembrar das nossas questões e das etapas anteriores. Para a camada **RAW** a ingestão dos dados aconteceram à partir de duas fontes: 

Primeiro, um arquivo `.csv` que fizemos o upload localmente para o nosso bucket com as seguintes dimensões, lembrando que apenas algumas dessas colunas nos interessa, pois a nossa análise se concentrará apenas nos títulos dos filmes:

- 'id', 
- 'tituloprincipal', 
- 'titulooriginal', 
- 'anolancamento', 
- 'tempominutos', 
- 'genero', 
- 'notamedia', 
- 'numerovotos', 
- 'generoartista', 
- 'personagem', 
- 'nomeartista', 
- 'anonascimento',
- 'anofalecimento', 
- 'profissao', 
- 'titulosmaisconhecidos';

Segundo, as requisições à API do TMDB que resultou em uma série de arquivos `.json`. As requisições foram realizadas já pensando os primeiros direcionamentos do desafio. Nossa *squad* recebeu o tema Guerra e Crime, portanto decidimos trabalhar com filmes de guerra em um determinado recorte temporal. Os filmes registrados nos arquivos `.json` já são filtrados pelo nosso temaa, países, e período de interesse: as requisições de API foram realizadas após um *join* entre o campo 'id' do `.csv` e o 'id_imdb' da API, o ano de lançamento do filme registrado em 'anolancamento' e os países produtores do filme registrados em 'paises_codigo'. Essas são as dimensões dos arquivos `.json`:

- 'id',
- 'id_imdb',
- 'lancamento',
- 'lucro',
- 'media_tmdb',
- 'orcamento',
- 'paises_codigo',
- 'paises_nome',
- 'recebimento',
- 'titulo',
- 'titulo original',
- 'votos_tmdb';

Para a etapa posterior, nós apenas padronizamos o formato dos arquivos, de `.csv` e `.json`, para `.parquet` e particionamos pela data de extração da API. Por fim, agora precisamos modelar nossos dados para responder as seguintes perguntas:

1. Nas décadas posteriores quais foram os gastos dos EUA e da ex-URSS em filmes de guerra?
2. A cada década, quem recebeu os melhores votos médios por filme?
3. Em termos de lucro, é possível mapear quem bloco lucrou mais?
4. A Rússia consegiu manter uma produção de filmes nos mesmos parâmetros de qualidade da Ex-União Soviética?
5. Quais foram os gastos realizados pela Ucrânia e Rússia, deflagrado o conflito entre eles?

Ou seja, temos claramente duas situações que precisam ser respondidas, questões referentes ao período da Guerra Fria, entre SU e US (ex-URSS e os Estados Unidos) e questões referentes ao nosso período atual entre RU e UA (Rússia e Ucrânia).

Analisamos os dados disponibilizados na camada **TRUSTED** e conseguimos modelar os dados da camada **REFINED**, uma tabela fato e quatro tabelas dimensão formando um **Esquema Tipo Estrela**, conforme a imagem abaixo:

![etapa1]()


## [Etapa 2 - Processamento Camada Refined](./etapa-2/)

