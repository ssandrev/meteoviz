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

