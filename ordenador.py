import pandas as pd
import numpy as np

df_tabela = pd.read_csv('dados_cursos_2023/dados_.csv')
colunas =   ('classificacao_negros',
            'classificacao_publica_rendamenor_autodeclara',
            'classificacao_publica_rendamenor_autodeclara_pcd',
            'classificacao_publica_rendamenor_naoautodeclara',
            'classificacao_publica_rendamenor_naoautodeclara_pcd',
            'classificacao_publica_rendamaior_autodeclara',
            'classificacao_publica_rendamaior_autodeclara_pcd',
            'classificacao_publica_rendamaior_naoautodeclara',
            'classificacao_publica_rendamaior_naoautodeclara_pcd')

df_tabela = df_tabela.replace('-', np.nan)

for coluna in colunas:
    # Apenas classificacao universal
    df_tabela = df_tabela.loc[df_tabela[coluna].isna()]

df_tabela = df_tabela[[ 'inscricao',
                        'nome',
                        'nf_selecao',
                        'classificacao_su']
                        ].sort_values(
                        by=['classificacao_su'])

print(df_tabela.head(50))