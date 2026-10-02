# Registro individual — AV1.2

**Estudante:** Rafael Farias de Oliveira Lima — **Data:** 02/10/2026
**Limite:** uma página; paginação a conferir na exportação.

**Critérios antes da análise:** [R1](../../caso/regras.md) exige somar impacto e urgência: escore ≥ 5 dá `alta`, 3–4 dá `media` e < 3 dá `baixa`. Para avaliar outras entradas/repetições, exigir registros reais com modelo, versão, configuração e contexto identificados, entradas variadas e comparação com o contrato. Uma amostra finita não prova correção universal.

| Entrada de A (impacto, urgência) | Cálculo e esperado por R1 | Trecho da resposta A | Conclusão por inspeção |
|---|---|---|---|
| (2, 3) | 2 + 3 = 5 → `alta` | “é media” | Incorreto: considera apenas impacto e ignora urgência. |
| (3, 1) | 3 + 1 = 4 → `media` | “é alta” | Incorreto: considera apenas impacto e ignora urgência. |

**Ligação com o chat:** FC-002 e FC-006 de [chamados.json](../../caso/chamados.json) têm, respectivamente, esses pares e prioridades esperadas `alta` e `media`. São exemplos complementares, não resultados de modelo; prioridade é calculada, não armazenada no JSON.

**B — trecho analisado:** “As três saídas foram ‘alta’. Isso prova que o modelo é determinístico e sempre entrega a classificação correta, inclusive em outros chamados.”

**O que posso concluir sobre o par citado:** para (2, 3), `alta` está de acordo com R1. As três repetições são apenas parte da narrativa simulada; não foram observadas nesta atividade.

**Afirmação geral de B: o que falta:** registros reais, identificação do modelo/configuração/contexto e resultados para outras entradas. Mesmo repetições reais iguais demonstrariam somente estabilidade na amostra, não determinismo universal nem acerto em qualquer chamado.

**Condição não coberta:** (3, 1) exige `media` e (1, 1) exige `baixa`; B não informa resultados desses pares. Isso é ausência de cobertura, não falha observada de B.

**Decisão A + motivo:** rejeitar a regra e ambas as classificações porque contradizem R1.
**Decisão B + motivo:** aceitar parcialmente a classificação do par (2, 3); rejeitar a generalização de determinismo e correção universal.

**Alternativa de verificação e condição para rever uma decisão:** montar a tabela dos nove pares válidos com esperados derivados de R1 e comparar uma versão corrigida de A. Rever a rejeição dessa versão se aplicar a soma e coincidir com todos os pares. Essa verificação é proposta, não executada. Para repetibilidade, propor coleta real em condições identificadas, sem reproduzir agora a narrativa B; restringir qualquer conclusão à amostra, nunca ao “sempre”.

**Origem dos dados e método:** A/B são simulações didáticas do [enunciado](README.md), não consultas reais. Cálculos e leitura elaborados com o assistente; execução real nesta atividade: não realizada. Tokens, custo, latência, configuração e modelo das respostas simuladas: não informados.

**IA na produção do registro:** GitHub Copilot, GPT-6.1 Sol (`gpt-6.1-sol`), elaborou tabela, análise e decisões propostas, conferindo somas com R1. O estudante forneceu os dados FC no chat e solicitou revisão; o assistente aproveitou FC-002/FC-006 como exemplos. Revisão pessoal final pelo estudante ainda pendente; não se declara verificação própria já concluída.

**Revisão de conteúdo:** [x] critérios; [x] dois pares; [x] análise de B; [x] decisões/limites; [ ] paginação até uma página.
