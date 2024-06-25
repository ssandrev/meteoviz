# MeteoViz

O MeteoViz é uma ferramenta interativa que permite aos usuários explorar e analisar variáveis meteorológicas. As principais funções do programa incluem:

- Upload de dados meteorológicos em formatos CSV e Excel.
- Criação de gráficos de séries temporais, mapas espaciais, gráficos de dispersão e histogramas.
- Ferramentas de análise estatística para calcular estatísticas descritivas, correlações, tendências e anomalias nos dados.

Este programa foi concebido para atender principalmente pesquisadores especializados em meteorologia, climatologia e áreas relacionadas, bem como estudantes e professores dessas disciplinas. É uma ferramenta utilitária que pode ser utilizada tanto para fins educacionais quanto de pesquisa. Até o atual momento é necessário conhecimento de programação para iniciar o projeto.

## Visão de Projeto

Esta seção contém cenários que orientam o projeto, uso e evolução do software, garantindo que ele atenda às necessidades dos usuários e possa ser mantido e melhorado ao longo do tempo.

### Cenário Positivo 1
João é um pesquisador interessado em estudar padrões climáticos e suas variações ao longo do tempo. Ele utiliza o MeteoViz para carregar um conjunto de dados meteorológicos de um ano inteiro. João seleciona a opção de gráfico de séries temporais e escolhe visualizar a variação da pressão atmosferica máxima ao longo do ano. Com a ferramenta de análise estatística João consegue calcular a média, mediana e desvio padrão de todos os dados do arquivo enviado. Satisfeito com os resultados, João exporta os gráficos e as estatísticas para utilizá-los em sua próxima apresentação.

### Cenário Positivo 2
Maria, uma professora de geografia, usa o MeteoViz em suas aulas para ensinar seus alunos sobre a importância dos dados meteorológicos. Ela pede aos alunos que façam o upload de arquivos CSV contendo dados da localização de sensores de dados metereológicos de diferentes regiões. Maria utiliza a opção de mapas para visualizar a distribuição dos sensores no estado.

### Cenário Negativo 1
Carlos, um estudante de climatologia, tenta usar o MeteoViz para carregar um arquivo de dados meteorológicos. No entanto, ele acidentalmente faz o upload de um arquivo de texto que não está no formato CSV ou Excel. O programa não exibe uma mensagem de erro indicando que o formato do arquivo não é suportado, mas ao tentar utilizar os mapas não é encontrado nenhuma opção de escolha para o X e Y. Carlos então converte o arquivo para CSV e consegue carregar os dados corretamente.

### Cenário Negativo 2
Ana, uma pesquisadora, ao analisar dados de temperatura e umidade de várias estações meteorológicas. Ela faz o upload de um arquivo CSV com a localização dos sensores, mas percebe que as colunas latitude e longitude estão faltando ou estão corrompidos. Realizando a falha na demonstração do mapa devido aos valores ausentes. Ana compreende que precisa renomear as colunas que representam a latitude e longitude para o formato necessário antes de realizar a análise e usa outra ferramenta para corrigir os dados antes de tentar novamente.

## Documentação Técnica do Projeto

### Especificação de Requisitos Funcionais e Não-Funcionais
- **Requisitos Funcionais**:
  - Upload de arquivos CSV e Excel.
  - Criação de gráficos interativos (séries temporais, mapas espaciais, dispersão, histogramas).
  - Ferramentas de análise estatística (estatísticas descritivas, correlações).
  - Exportação de gráficos e resultados estatísticos.

- **Requisitos Não-Funcionais**:
  - Interface amigável e responsiva.
  - Suporte para grandes volumes de dados.
  - Mensagens de erro claras e informativas.
  - Desempenho eficiente nas operações de análise.

### Arquitetura do Software
O MeteoViz é construído utilizando a framework Dash com componentes Bootstrap para a interface do usuário. Ele utiliza bibliotecas como pandas para manipulação de dados e plotly para visualização gráfica.

### Descrição Funcional do Software
O software permite aos usuários fazer upload de arquivos de dados meteorológicos, selecionar variáveis para análise e gerar visualizações interativas. Ele também fornece ferramentas para análise estatística dos dados carregados.

### Sobre o Código
- **Linguagem**: Python
- **Framework**: Dash, Plotly, Pandas
- **Diretivas de Compilação**: Não aplicável (interpretação direta em Python).

## Manual de Utilização para Usuários Contemplados

### Guia de Instruções:
**Cenário 1**:
1. Faça o upload de um arquivo CSV ou Excel clicando em "Select a CSV or Excel File".
2. Após carregar os dados, selecione "Temporal Series" no menu dropdown.
3. Escolha a variável de interesse para o eixo X (e.g., data).
4. Escolha uma ou mais variáveis para o eixo Y (e.g., temperatura).
5. Clique na camera no grafico para exporta-lo como png
6. Nas abas de estatistica e matrix de correlação clique no botão de export para exporta como csv.

**Para Criar Mapas Espaciais**:
1. Após carregar os dados, selecione "Map" no menu dropdown.
2. Certifique-se de que os dados tenham colunas de latitude e longitude.
3. Selecione o Toggle axis selection e selecione qualquer valor para o X e Y
4. O mapa será gerado automaticamente com marcadores nas coordenadas especificadas (latitude e longitude,, independente dos selecionados).

**Para Criar e Renomear Abas**:
1. Escreve o nome da nova aba e em seguida clique no botão "Add Tab".
2. Selecione a aba que deseja renomear.
3. Escreva o novo nome e em seguida clique no botão "Rename Tab".

### Exceções ou Potenciais Problemas:
**Se o Formato do Arquivo Não for Suportado**:
- O programa exibirá uma mensagem de erro. Converta o arquivo para CSV ou Excel e tente novamente.

**Se Houver Dados Ausentes ou Corrompidos**:
- Mensagens de erro podem ser exibidas durante a análise estatística. Verifique e limpe os dados antes de tentar novamente.

## Como Iniciar a Aplicação

### Passo a Passo para Iniciar o MeteoViz

1. **Baixar e Instalar Python**:
    - Acesse o site oficial do Python: [python.org](https://www.python.org/)
    - Faça o download da versão mais recente do Python.
    - Siga as instruções de instalação conforme seu sistema operacional (Windows, macOS, Linux).

2. **Clonar o Repositório do Projeto**:
    - Abra o terminal (ou prompt de comando) e navegue até o diretório onde deseja clonar o repositório.
    - Execute o comando:
      ```sh
      git clone <URL_do_repositorio>
      ```
    - Substitua `<URL_do_repositorio>` pelo URL real do repositório MeteoViz.

3. **Instalar Dependências**:
    - Navegue até o diretório do projeto clonado:
      ```sh
      cd MeteoViz
      ```
    - Instale as dependências necessárias:
      ```sh
      pip install -r requirements.txt
      ```

4. **Iniciar o Aplicativo**:
    - Execute o comando para iniciar o servidor Dash:
      ```sh
      python app.py
      ```
    - O servidor será iniciado e você verá uma mensagem indicando que o aplicativo está rodando em um endereço local (por exemplo, `http://127.0.0.1:8050`).

5. **Acessar a Interface HTML**:
    - Abra um navegador web e digite o endereço fornecido no terminal (por exemplo, `http://127.0.0.1:8050`).
    - Você verá a interface do MeteoViz onde pode começar a carregar dados e gerar visualizações.

