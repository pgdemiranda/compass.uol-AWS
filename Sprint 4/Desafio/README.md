# Desafio da Sprint 2 - Análise de Dados

## Entregáveis

- [x] Dois arquivos no formato `.ipynb`(Jupyter Notebook) contendo o código usado para a execução de cada etapa correspondente do problema;
    - [etapa-1.ipynb](./etapa-1/etapa-1.ipynb)
    - [etapa-2.ipynb](./etapa-2/etapa-2.ipynb)

- [] Arquivo **README.md** com as análises completas escolhidas;

- [] Imagens evidenciando a execução completa e correta das etapas;
    - imagens encontradas na pasta [Evidências](../Evidências/) e renderizadas na explicação do Desafio.

- [x] Arquivos **JSON** ou **CSV** baixado e resultante.
    - baixado: [anuario-2024-dados_abertos-tabela2-19.csv](./data/anuario-2024-dados_abertos-tabela2-19.csv)
    - resultante: [dataset.csv](./data/dataset.csv)

## Sumário

- [Preparação](#preparação)
    - [Dicionário de Dados](#dicionário-de-dados)
- [Desafio](#desafio)
    - [Etapa 1 - Upload do Dataset](#etapa-1---upload-do-dataset)
    - [Etapa 2 - Análises](#etapa-2---análises)
    - [Etapa 3 - Salvar Arquivos no Bucket](#etapa-3---salvar-arquivos-no-bucket)

## Preparação

Foi requisitado que procurássemos um arquivo JSON ou CSV no portal de dados públicos do Governo Brasileiro, na URL http://dados.gov.br e garantir que o arquivo fosse o único na turma. 

Utilizamos um conjunto de dados originado do **Anuário Estatístico Brasileiro do Petróleo, Gás Natural e Biocombustível 2024**, e segundo as informações do repositório: "O Anuário Estatístico Brasileiro do Petróleo, Gás Natural e Biocombustíveis 2024 consolida os dados referentes ao desempenho da indústria do petróleo, gás natural e biocombustíveis e do sistema de abastecimento nacionais no período 2014-2023. Estão disponíveis para consulta e download as tabelas integrantes do Anuário 2024 representadas em metadados e no formato CSV."

Utilizamos a **"Tabela 2.19 - Distribuição de royalties sobre a produção de petróleo e de gás natural, segundo beneficiários - 2014-2023"**, disponibilizada em formato "CSV" e um dicionário de dados em formato "DOCX" (no site apontado consta como PDF, mas o link do dicionário abre um arquivo em `.docx`) e que podem ser acessados na URL https://dados.gov.br/dados/conjuntos-dados/anuario-estatistico-2024, e, adicionalmente, em modo local seguindo os links abaixo:

- [Dicionário dos Dados](./dicionario/anuario-abertos-metadados-tabela2-19.docx)

- [Conjunto de Dados](./data/anuario-2024-dados_abertos-tabela2-19.csv)

### Dicionário de Dados

| NOME DA COLUNA                           | DESCRIÇÃO                                                                 | TIPO DO DADO     |
|:----------------------------------------:|--------------------------------------------------------------------------|:----------------:|
| **BENEFICIÁRIO**                         | Estados;<br>Municípios;<br>Depósitos Judiciais;<br>Fundo Especial;<br>Educação e Saúde;<br>União - Comando da Marinha;<br>União - Ministério da Ciência e Tecnologia;<br>União - Fundo Social. | `Texto`          |
| **ANO**                                  | Ano                                                                      | `Número inteiro` |
| **DISTRIBUIÇÃO DE ROYALTIES**<br>(sobre a produção de petróleo e gás natural) | Distribuição de royalties segundo beneficiários.                          | `Número real`    |

# Desafio

O objetivo para essa sprint é a prática utilizando serviços da AWS. Aqui o desafio foi separado em três etapas: 

Na **primeira etapa** deve se analisar o conjunto de dados escolhido localmente no editor de texto da nossa preferência para conhecer os dados e o que pode ser analisado. 3 questionamentos ou análises que pretendemos trazer com os dados escolhidos precisam ser definidos. Por fim, deve-se utilizar a biblioteca **boto3** para carregar o arquivo para um bucket à partir de um script Python.

Na **segunda etapa**, em um outro script Python e, **a partir do arquivo que está dentro do S3**, se deve criar um dataframe com pandas ou com polars e executar as análises definidas na etapa anterior. **As análises devem ser baseadas nas seguintes manipulações (obrigatoriamente uma por análise no mínimo)**:

- Uma cláusula que filtra dados usando ao menos dois operadores lógicos;

- Uma função de agregação;

- Uma função condicional;

- Uma função de conversão;

- Uma função de data;

- Uma função de string.

Na **terceira etapa**, após finalizar a análise e realizar as manipulações, deve-se salvar o(s) arquivo(s) resultantes no mesmo bucket criado para o desafio e no formato de entrada deles.

## [Etapa 1 - Upload do Dataset](./etapa-1/)

- Foi feito o download do arquivo csv e armazenado dentro da pasta [data](./data/) no nome original, que é [anuario-2024-dados_abertos-tabela2-19.csv](./data/anuario-2024-dados_abertos-tabela2-19.csv).

- Criamos um Jupyter notebook, o [etapa-1.ipynb](./etapa-1/etapa-1.ipynb) para explorar os dados e realizar o upload do dataset no bucket com **boto3**. Importamos os dados, realizamos uma exploração simples para conferir:
    - Dimensão dos dados;
    - Tipos dos dados;
    - Dados faltantes;
    - Dados duplicados.

- No notebook formulamos as seguintes questões que serão exploraradas na próxima etapa:

    1. Qual a diferença total (somando todos os anos) no recebimento dos royalties entre cada estado e os seus municípios?

    2. Que região do Brasil recebeu mais royalties e que região recebeu menos?

    3. Qual foi a evolução de royalties para beneficiários que não os estados ou os municípios desses estados?

- O conjunto de dados é pequeno, não há dados faltantes e nem duplicados, os tipos dos dados podem ser modificados se necessário nos questionamentos, de modo que **as únicas limpezas ou ajustes nos dados** foi transformar as colunas em *snake case*, retirar acentuações e cedilhas e modificar o nome de uma das colunas para algo menor que possa ajudar na hora da manipulação.

- Para não termos problemas de vazamento das nossas credenciais, foram criados dois arquivos: um arquivo **.gitignore** e um arquivo **.env**. O **.gitignore** impede que nossas credenciais armazenadas no arquivo **.env**, que, por sua vez, é acessado na execução do código e fornece essas credenciais como variáveis para que o **boto3** possa enviar os arquivos para o nosso bucket.

- **Apesar de não ter sido requisitado**, o processo também foi armazenado em um script python, [etapa-1.py](./etapa-1/etapa-1.py).

- O upload para o bucket com boto3 foi feito com o código abaixo. No início do notebook, havíamos importado as bibliotecas **os** (nativa do Python), **pandas**, **dotenv**, **unidecode** e **boto3**. Carregamos as variáveis de ambiente com a biblioteca dotenv utilizando o comando `load_dotenv()` (como as variáveis de ambiente são as mesmas para esse Desafio, podemos usar um arquivo **.env** compartilhado, de modo que não foi necessário passar o *path* do arquivo). Com a biblioteca **os** definimos as variáveis de ambiente, e listamos quais variáveis poderiam estar faltando ou que não foi detectada. O cliente s3 foi definido com nossas variáveis e a região **us-east-1**. Para ter certeza que o arquivo nomeado **dataset.csv** foi enviado para o bucket, implementamos dois prints que confirmam essa operação: um que avisa que o Bucket foi encontrado, **importante porque se nossas credenciais não for autorizado para ler e escrever no bucket**, ele simplesmente não será encontrado, e outro que informa que o upload realizado. Caso haja algo de errado, o erro é capturado pelo `except`.

```Python
load_dotenv()

access_key = env.get('AWS_ACCESS_KEY_ID')
secret_key = env.get('AWS_SECRET_ACCESS_KEY')
bucket_name = env.get('BUCKET_NAME')

if not all([access_key, secret_key, bucket_name]):
    missing = [name for name, value in [
        ('AWS_ACCESS_KEY_ID', access_key),
        ('AWS_SECRET_ACCESS_KEY', secret_key),
        ('BUCKET_NAME', bucket_name)
    ] if not value]
    raise ValueError(f"Variáveis de ambiente faltando: {', '.join(missing)}")

s3 = boto3.client(
    's3',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='us-east-1',
)

try:
    s3.head_bucket(Bucket=bucket_name)
    print(f'Bucket encontrado')

    df.to_csv(
        f's3://{bucket_name}/dataset.csv',
        storage_options={
            'key': access_key,
            'secret': secret_key
        },
        index=False
    )
    print('Upload realizado')

except Exception as e:
    print('Erro:', e)
```

## [Etapa 2 - Análises](./etapa-2/)

### Questão 1: qual a diferença total (somando todos os anos) no recebimento dos royalties entre cada estado e os seus municípios?

### Questão 2: Que região do Brasil recebeu mais royalties e que região recebeu menos?

### Questão 3: Qual foi a evolução de royalties para beneficiários que não os estados ou os municípios desses estados?

## Etapa 3 - Salvar Arquivos no Bucket