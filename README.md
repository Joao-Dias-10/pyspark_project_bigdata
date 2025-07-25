# 🚀 PySpark Big Data Pipeline

Projeto estruturado em PySpark, com foco em boas práticas, orientação a objetos e escalabilidade para tratamento de grandes volumes de dados. A pipeline inclui carregamento, transformação, limpeza e inserções otimizadas em bancos relacionais como PostgreSQL.

---

### 🧪 Visão Geral

* **Processamento distribuído de grandes volumes de dados** com PySpark e arquivos `.parquet`
* **Download automático** de arquivos `.parquet` via URL
* **Leitura, limpeza e tratamento** de dados com PySpark
* **Conversão de tipos**, tratamento de nulos e criação de colunas derivadas
* **Salvamento otimizado** em formato `.parquet` com `coalesce` (1 único arquivo)
  **`.parquet`** é um formato colunar, compacto e eficiente para leitura em escala
* **Modelagem ORM com SQLAlchemy**
* **Inserção eficiente no PostgreSQL** via escrita em lote com PySpark
* **Boas práticas de engenharia de dados** com POO e estrutura modular
* ✅ **Desempenho real**:
  `.parquet` com **3.970.553 linhas** processado e inserido no PostgreSQL 

---

## ⚙️ Tecnologias utilizadas

* Python 3.10+
* PySpark
* PostgreSQL
* Pytest
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

