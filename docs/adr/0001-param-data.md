# ADR 0001: Resolução determinística de períodos de data

## Status
Aceito

## Contexto
O agente precisa converter expressões em linguagem natural ("mês atual",
"mês passado") em datas concretas (`data_inicio`, `data_fim`) para alimentar
as tools de consulta (faturamento, metas). LLMs não têm acesso confiável ao
relógio e são propensos a erro em aritmética de calendário.

## Decisão
Datas relativas nunca são calculadas pelo modelo. O modelo apenas classifica
a expressão do usuário em um rótulo conhecido (`mes_atual`, `mes_passado`,
`ano_atual`, etc.) e chama a tool `resolver_periodo`, que calcula as datas
em Python puro, de forma determinística.

## Consequências
- Elimina erro de aritmética de data vindo do LLM.
- Adiciona uma tool extra e uma etapa a mais no fluxo do agente.
- Novos rótulos de período (ex: "trimestre atual") exigem atualizar
  `resolver_periodo`, não o prompt do modelo.