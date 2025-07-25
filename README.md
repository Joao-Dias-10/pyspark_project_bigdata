# 🚀 PySpark Big Data Pipeline

Projeto estruturado em PySpark, com foco em boas práticas, orientação a objetos e escalabilidade para tratamento de grandes volumes de dados. A pipeline inclui carregamento, transformação, limpeza e inserções otimizadas em bancos relacionais como PostgreSQL.

---

## 📌 Objet ivos

- Processar grandes volumes de dados de forma distribuída com PySpark e aquivos .parquet
- Utilizar orientação a objetos (POO) para organização e reuso de código
- Aplicar boas práticas de engenharia de dados
- Realizar inserções eficientes em bancos relacionais (ex: PostgreSQL)
- Demonstrar o potencial do Apache Spark em ambientes de Big Data

---

## ⚙️ Tecnologias utilizadas

- Python 3.10+
- PySpark
- PostgreSQL
- Pytest
- SQLAlchemy (para modelagem ORM)
- notebooks (para testes e verificações rápidas)
- Dotenv (para gerenciamento de variáveis)
- Logging (para rastreamento de execução)


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
│   │   ├── init\_db.py
│   │   ├── models.py
│   │   └── queries.py
│   ├── preprocessing/ # Pré-processamento e transformação de dados
│   └── utils/        # Funções utilitárias
├── tests/            # Testes unitários e de integração
├── .gitignore        # Padrões de arquivos ignorados pelo Git
├── main.py           # Ponto de entrada do projeto
├── requirements.txt   
````

---

### ▶️ Rodando o pipeline

```bash
python main.py
```

---

## 🧪 Funcionalidades principais

* SQLAlchemy (para modelagem ORM)
* Download automático de arquivos .parquet via URL
* Leitura, limpeza e tratativa de dados com PySpark
* Conversões de tipo, tratamento de nulos e colunas derivadas
* Salvamento em formato Parquet (com coalesce para gerar arquivo único)

  > *Parquet é um formato colunar, altamente eficiente para leitura e compressão, ideal para grandes volumes de dados e processamento distribuído.*
* Inserção estruturada em PostgreSQL utilizando PySpark para escrita em lote

---
