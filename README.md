[![Standard](https://github.com/ZyamHunter/pytest-bdd-selenium/actions/workflows/standard.yaml/badge.svg)](https://github.com/ZyamHunter/pytest-bdd-selenium/actions/workflows/standard.yaml)

# pytest-bdd-selenium
Repositório de testes dedicados ao uso da biblioteca Pytest BDD para executar testes e2e com Selenium

# Configuração do Ambiente

## 1. Instalar Python 3.10

Certifique-se de ter o Python 3.10 instalado em seu sistema. Você pode baixá-lo no [site oficial do Python](https://www.python.org/).

## 2. Instalar Conda para gerenciamento de projeto
Acesse o site e para o seu dispositivo: https://docs.conda.io/projects/conda/en/latest/
- https://www.anaconda.com/installation-success?source=installer
- https://conda.io/projects/conda/en/latest/user-guide/getting-started.html

## 3. Criar um ambiente virtual:
- conda create -n pytest-bdd-selenium

## 4. Se você estiver usando o PowerShell e encontrar problemas para executar scripts, talvez precise alterar a política de execução temporariamente para permitir a execução de scripts:
- Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

## 5. Ativar o ambiente virtual:
- conda init nome-do-shell
- conda activate pytest-bdd-selenium

## 6. Remover cache do pip
- pip cache remove *

## 7. Rodar os testes
- pytest --html=report.html

## 8. Desativar ambiente virtual
- conda deactivate

## 9. Instalar dependências
> Primeiro ative o ambiente virtual para evitar erros de versão com outras bibliotecas instaladas
- pip install -r requirements.txt

## 10. Formatar código
- autopep8 --in-place --recursive .

<br/>

### ---- Diferenciais no projeto ----
<br/>

- Page Object
- RPA Framework
- Behave
- WebDriver Manager
- Massa de Dados
- Report dos testes

<br/>
