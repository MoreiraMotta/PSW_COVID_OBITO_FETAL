import pandas as pd
import matplotlib.pyplot as plt

df_interesse = pd.read_csv('./resultados/check_leitos_vs_nascimentos/df_interesse.csv')

df_correlacoes_mun_menor_500 = pd.read_csv('./resultados/check_leitos_vs_nascimentos/df_correlacoes_municipios_menor_500.csv')

aa=df_correlacoes_mun_menor_500[(df_correlacoes_mun_menor_500['correlacao_QTLEIT'] >= 0.5) | (df_correlacoes_mun_menor_500['correlacao_QTINST'] >= 0.5) |
              (df_correlacoes_mun_menor_500['correlacao_TP_UNID_5'] >= 0.5) | (df_correlacoes_mun_menor_500['correlacao_TP_UNID_7'] >= 0.5) |
              (df_correlacoes_mun_menor_500['correlacao_TP_UNID_15'] >= 0.5) | (df_correlacoes_mun_menor_500['correlacao_TP_UNID_36'] >= 0.5)]

# Criar gráficos de dispersão

ufs = pd.unique(df_interesse['evento_SIGLA_UF'])
for uf in ufs:
   subset = df_interesse[df_interesse['evento_SIGLA_UF'] == uf]
   corr = round(df_correlacoes_mun_menor_500.loc[df_correlacoes_mun_menor_500['evento_SIGLA_UF'] == uf, 'correlacao_QTLEIT'], 2)
   plt.figure(figsize=(10, 6))
   plt.scatter(subset['var_QTLEIT'], subset['var_QTD_NASCIMENTOS'], alpha=0.5)
   plt.title(f'Leitos VS Nasc corr {corr.reset_index(drop=True)[0]} municipio {uf} ')
   plt.xlabel('Variação QTDLEIT)')
   plt.ylabel('Variação QTDNASC')
   plt.grid(True)
   plt.savefig(f'resultados/check_leitos_vs_nascimentos/graficos/dispersao_var_leitos_vs_var_nasc_{uf}.png', format='png', dpi=300)
   plt.clf()
   # plt.show()


for uf in ufs:
   subset = df_interesse[df_interesse['evento_SIGLA_UF'] == uf]
   corr = round(df_correlacoes_mun_menor_500.loc[df_correlacoes_mun_menor_500['evento_SIGLA_UF'] == uf, 'correlacao_QTINST'], 2)
   plt.figure(figsize=(10, 6))
   plt.scatter(subset['var_QTINST'], subset['var_QTD_NASCIMENTOS'], alpha=0.5)
   plt.title(f'Inst VS Nasc corr {corr.reset_index(drop=True)[0]} municipio {uf} ')
   plt.xlabel('Variação QTINST')
   plt.ylabel('Variação QTDNASC')
   plt.grid(True)
   plt.savefig(f'resultados/check_leitos_vs_nascimentos/graficos/dispersao_var_inst_vs_var_nasc_{uf}.png', format='png', dpi=300)
   plt.clf()

for uf in ufs:
   subset = df_interesse[df_interesse['evento_SIGLA_UF'] == uf]
   corr = round(df_correlacoes_mun_menor_500.loc[df_correlacoes_mun_menor_500['evento_SIGLA_UF'] == uf, 'correlacao_TP_UNID_5'], 2)
   plt.figure(figsize=(10, 6))
   plt.scatter(subset['var_TP_UNID_5'], subset['var_QTD_NASCIMENTOS'], alpha=0.5)
   plt.title(f'TP_UNID_5 VS Nasc corr {corr.reset_index(drop=True)[0]} municipio {uf} ')
   plt.xlabel('Variação TP_UNID_5')
   plt.ylabel('Variação QTDNASC')
   plt.grid(True)
   plt.savefig(f'resultados/check_leitos_vs_nascimentos/graficos/dispersao_var_inst_vs_var_nasc_{uf}.png', format='png', dpi=300)
   plt.clf()