# Trabalho feito para a disciplina de Linguagem de Programação Script

## Passos para reproduzir

1. **Ter Python instalado na sua máquina**
   - Certifique-se de ter o Python 3.6 ou superior instalado. Você pode verificar a versão do Python com o comando:
     ```bash
     python --version
     ```

2. **Criar um ambiente virtual**
   - No terminal, navegue até o diretório do projeto e crie um ambiente virtual com o comando:
     ```bash
     python -m venv venv
     ```

3. **Ativar o ambiente virtual**
   - No Linux/macOS:
     ```bash
     source venv/bin/activate
     ```
   - No Windows:
     ```bash
     .\venv\Scripts\activate
     ```

4. **Instalar as dependências**
   - Com o ambiente virtual ativado, instale as dependências necessárias com o comando:
     ```bash
     pip install -r requirements.txt
     ```

5. **Executar a aplicação**
   - Com todas as dependências instaladas, execute a aplicação com o comando:
     ```bash
     python main.py
     ```

6. **Acessar a aplicação**
   - Abra o navegador e acesse `http://127.0.0.1:5000/` para ver a aplicação em execução.

## Estrutura do Projeto

- [main.py](http://_vscodecontentref_/1): Arquivo principal que inicia a aplicação Flask.
- [blueprint.py](http://_vscodecontentref_/2): Define as rotas e lógica da aplicação.
- [utils.py](http://_vscodecontentref_/3): Contém funções utilitárias usadas na aplicação.
- [requirements.txt](http://_vscodecontentref_/4): Lista de dependências necessárias para a aplicação.
- [templates](http://_vscodecontentref_/5): Diretório que contém os arquivos HTML.

## Observações

- Certifique-se de que todos os arquivos mencionados acima estão presentes no diretório do projeto.
- Se encontrar algum problema, verifique se todas as dependências foram instaladas corretamente e se o ambiente virtual está ativado.