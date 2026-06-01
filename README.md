# Miniprojeto Análise de Dados com Python T1
**Aluna:** Ana Cristina Otoni Lopes  
**Turma:** Análise de Dados T1  
**Módulo:** 1 - Semana 07  

---

## Sobre o Projeto
Análise Exploratória de Dados (AED) aplicada a uma base de varejo
com 830.000 registros reais de compras. O objetivo foi transformar
dados brutos em informações úteis, identificando padrões de consumo
e problemas de qualidade nos dados.

---

## Reflexão Teórica: ETL e Qualidade de Dados

**ETL** significa Extração, Transformação e Carga (Extract, Transform, Load).
É o processo de coletar dados brutos, limpá-los e prepará-los para análise.

Neste projeto aplicamos cada etapa:
- **Extração:** carregamento do CSV com pandas
- **Transformação:** limpeza de duplicatas, conversão de tipos e tratamento de valores inválidos
- **Carga:** geração do arquivo df_limpo.csv pronto para uso

**Qualidade de dados** significa garantir que os dados sejam:
- **Completos:** sem valores nulos relevantes
- **Consistentes:** sem duplicatas e com tipos corretos
- **Confiáveis:** com problemas documentados e tratados

Dados de baixa qualidade geram análises incorretas e decisões ruins.
Por isso a limpeza e documentação do processo são etapas essenciais.

---

## Principais Insights

1. A base original tinha 830.000 registros — após limpeza ficaram 733.447 (remoção de 11,6% de duplicatas)
2. Mulheres realizaram 52% das compras (382.427 vs 351.020 dos homens)
3. ALIMENTOS é a categoria mais vendida com 384.197 compras (52% do total)
4. A maioria dos clientes não tem filhos (moda e mediana = 0)
5. 3.228 registros com categoria inválida (#N/D) foram tratados como "Sem Categoria"
6. Nas categorias BEBIDAS, PET e ACESSORIOS a diferença entre gêneros é pequena — recomenda-se campanhas direcionadas ao público masculino nessas categorias

---

## Problemas Remanescentes
- 3.228 registros classificados como "Sem Categoria" precisam de investigação
- A origem do valor "#N/D" pode indicar falha no sistema de origem dos dados