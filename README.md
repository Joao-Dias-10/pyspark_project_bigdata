# 🚀 PySpark Big Data Pipeline

Projeto estruturado em PySpark, com foco em boas práticas, orientação a objetos e escalabilidade para tratamento de grandes volumes de dados. A pipeline inclui carregamento, transformação, limpeza, inserções otimizadas em bancos relacionais como PostgreSQL e testes unitários.

---

### 🎯 Objetivo do Código

Automatizar uma pipeline de ingestão, processamento e carregamento de dados, capaz de tratar e inserir **mais de 3.9 milhões de registros** com eficiência, estabilidade e organização.

Essa solução foi construída com foco em **boas práticas de engenharia de dados**, utilizando:

* `PySpark` para **processamento distribuído eficiente**
* `.parquet` como formato de **armazenamento colunar compacto**
* `SQLAlchemy` para **modelagem e criação de tabelas**
* `PostgreSQL` como **destino relacional confiável**
* Estruturação do código em **POO** e módulos reutilizáveis para garantir **manutenibilidade, clareza e escalabilidade**
* `pytest` utilizado para **testes unitários**, garantindo a **confiabilidade das transformações e manutenção**

O pipeline automatiza todo o fluxo: baixa o dado bruto, trata e transforma os registros, salva de forma otimizada e insere no banco com escrita em lote — tudo controlado por logs e encerramento adequado dos recursos.

---

## ⚙️ Tecnologias utilizadas

* Python 3.10+
* PySpark
* PostgreSQL
* Pytest (para testes unitários)
* SQLAlchemy (para modelagem ORM)
* notebooks (para testes e verificações rápidas)
* Dotenv (para gerenciamento de variáveis)
* Logging (para rastreamento de execução)

---

## 🧱 Estrutura do projeto

```
├── config/           # Arquivos de configuração (.yaml, .env, etc.)
├── data/             # Dados brutos e processados
│   ├── raw/
│   └── processed/
├── logs/             # Logs de execução
├── notebooks/        # Cadernos Jupyter para testes manuais e EDA
├── src/              # Código-fonte principal
│   ├── automation/   # Scripts de automação 
│   ├── db/           # Lógica de banco de dados
│   │   ├── init_db.py
│   │   ├── models.py
│   │   └── queries.py
│   ├── preprocessing/ # Pré-processamento e transformação de dados
│   └── utils/        # Funções utilitárias
├── tests/            # Testes unitários e de integração
├── .gitignore        # Padrões de arquivos ignorados pelo Git
├── main.py           # Ponto de entrada do projeto
├── requirements.txt
```

---

### ▶️ Rodando o pipeline

```bash
python main.py
```

---

