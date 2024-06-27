# MeteoViz

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
      git clone https://github.com/ssandrev/meteoviz.git
      ```

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

## Arquivos de Teste

### Arquivos Disponíveis na Release do Projeto

Para facilitar o teste e validação da aplicação MeteoViz, foram disponibilizados alguns arquivos de exemplo na seção de releases do nosso projeto no GitHub. Esses arquivos incluem dados meteorológicos e de localização de sensores que podem ser carregados na aplicação para gerar visualizações. Siga os passos abaixo para acessar e usar esses arquivos:

1. **Acesse a Seção de Releases**:
    - Vá para a página do repositório MeteoViz no GitHub.
    - Clique na aba "Releases" para ver todas as versões disponíveis.

2. **Baixe os Arquivos de Teste**:
    - Na última release, você encontrará um conjunto de arquivos para teste.
    - Baixe os arquivos desejados para o seu computador.

3. **Carregue os Arquivos na Aplicação**:
    - Na interface do MeteoViz, você pode usar a opção de upload para carregar os arquivos de teste baixados.
    - Siga as instruções na interface para visualizar e analisar os dados.

Esses arquivos de teste são fornecidos para garantir que você possa explorar todas as funcionalidades do MeteoViz sem precisar de dados próprios inicialmente.
