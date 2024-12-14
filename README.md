# English
# Website Data Scraper

This project demonstrates how to fetch data from an API, process it, and save it to a CSV file using Python.

## Requirements

- Python 3.x
- `requests` library for HTTP requests
- `pandas` library for data manipulation

## Installation

To install the necessary dependencies, you can use pip:
pip install requests pandas

## Usage

1. Replace `api_url` with the actual API endpoint from which you want to fetch data.
2. The script will fetch the data from the API, process it, and save it into a CSV file (`data.csv` by default).

### Example Code

```python
api_url = 'https://api.example.com/data'  # API endpoint URL
data = fetch_data(api_url)  # Fetching data from the API
if data:
    process_and_save_data(data, 'data.csv')  # Processing and saving the data to a CSV file
else:
    print("Failed to fetch data from the API.")  # Printing error message if data is not fetched
```
# Português ![Bandeira do Brasil](https://upload.wikimedia.org/wikipedia/commons/0/05/Flag_of_Brazil.svg)

# **Raspador de Dados de Website**

Este projeto demonstra como buscar dados de uma API, processá-los e salvá-los em um arquivo CSV usando Python.

## Requisitos

- Python 3.x
- Biblioteca `requests` para requisições HTTP
- Biblioteca `pandas` para manipulação de dados

## Instalação

Para instalar as dependências necessárias, você pode usar o pip:
```bash
pip install requests pandas
```

## Uso

1. Substitua `api_url` pelo endpoint real da API de onde você deseja buscar os dados.
2. O script buscará os dados da API, processará e salvará em um arquivo CSV (`data.csv` por padrão).

### Exemplo de Código

```python
api_url = 'https://api.example.com/data'  # URL do endpoint da API
data = fetch_data(api_url)  # Buscando os dados da API
if data:
    process_and_save_data(data, 'data.csv')  # Processando e salvando os dados em um arquivo CSV
else:
    print("Falha ao buscar dados da API.")  # Imprimindo mensagem de erro caso não consiga buscar os dados
```
