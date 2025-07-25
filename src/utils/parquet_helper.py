import os

class ParquetHelper:
    @staticmethod
    def localizar_arquivo_parquet(diretorio_saida: str) -> str:
        """
        Busca o arquivo .parquet real dentro de um diretório gerado pelo Spark com coalesce(1).
        Retorna o caminho completo do arquivo.
        """
        arquivos = os.listdir(diretorio_saida)
        arquivo = next((f for f in arquivos if f.endswith(".parquet")), None)

        if not arquivo:
            raise FileNotFoundError(f"Nenhum arquivo .parquet encontrado em {diretorio_saida}")

        return os.path.join(diretorio_saida, arquivo)
