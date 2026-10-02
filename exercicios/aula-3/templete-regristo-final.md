# Registro individual — AV1.3

**Estudante:** Rafael Farias de Oliveira Lima — **Data:** 02/10/2026
**Limite:** uma página; paginação a conferir na exportação.

**O que listagem/documentação precisam cumprir:** [R2/R4](../../caso/regras.md) exigem incluir `aberto` e `em_andamento`, excluir `fechado`, preservar a ordem relativa da entrada e documentar o mesmo comportamento.

| Caso / estado | Entrada (IDs e ordem) | IDs esperados na ordem | Obrigação de R2 e como verificar |
|---|---|---|---|
| 1 / aberto | `[TR-33]` | `[TR-33]` | Incluir aberto; comparar a lista de IDs com a esperada. |
| 2 / em_andamento | `[TR-31]` | `[TR-31]` | Incluir em andamento; comparar a lista de IDs com a esperada. |
| 3 / fechado | `[TR-32]` | `[]` | Excluir fechado mesmo com impacto/urgência altos; conferir lista vazia. |

**Entrada combinada TR-31, TR-32, TR-33 → IDs esperados:** `[TR-31, TR-33]`. Os campos completos são os fornecidos na tabela do [enunciado](README.md).

**Como conferir a ordem:** TR-31 está na posição 1 e TR-33 na 3 da entrada; após retirar TR-32, TR-31 deve permanecer antes de TR-33. Comparar a sequência, não apenas o conjunto: `[TR-33, TR-31]` contém os mesmos IDs, mas viola R2.

**Complemento do chat:** para os seis registros de [chamados.json](../../caso/chamados.json), o esperado é `[FC-001, FC-002, FC-004, FC-005]`; FC-003/FC-006 são excluídos. Esse exemplo não substitui os casos TR exigidos. Listar ativos (R2) é diferente de permitir visualização (R3); a proposta hipotética de C3 da aula 1 não altera R2/R4.

**Documentação proposta:** “`listar_ativos` retorna os chamados nos estados `aberto` e `em_andamento` e exclui os chamados `fechado`. A saída preserva a ordem relativa dos registros na entrada. Departamento, impacto e urgência não alteram esse filtro.”

**Etapa em que admitiria IA / tarefa / responsável:** preparação de verificações e documentação; IA sugere casos e rascunha o texto, com aceite da pessoa revisora da manutenção. Não define requisitos nem autoriza uso automático.

**O que verificar antes de aprovar:** derivar esperados do contrato, conferir os três estados e a sequência combinada e comparar cada frase com R4. Se avaliar código posteriormente, confrontar retornos com esses esperados. Planejar casos não comprova execução.

**Alternativa sem IA e comparação:** manutenção escreve manualmente os casos e a documentação a partir de R2. A regra curta pode tornar essa opção menos trabalhosa que revisar sugestões; não há medição que comprove economia com IA.

**Limite e condição para rever a aprovação:** não houve verificação executada da implementação, nem cobertura de todas as listas válidas. Recusar proposta que omita `em_andamento`, inclua `fechado` ou ordene por prioridade; reconsiderar após correção e nova conferência dos casos e do texto.

**Origem dos dados e método:** entradas fictícias TR do enunciado e FC fornecidas no chat; saídas esperadas calculadas por R2, com leitura apoiada pelo assistente. Execução nesta atividade: não realizada; a execução anterior de C3 tratava outra função e outro requisito proposto.

**Uso de IA:** GitHub Copilot, GPT-6.1 Sol (`gpt-6.1-sol`), elaborou tabela, documentação e decisão proposta e conferiu estados/ordem com R2/R4. O estudante identificou a lista ativa FC no chat e pediu revisão; o assistente manteve os casos TR e distinguiu listagem de visibilidade. Revisão pessoal final pelo estudante ainda pendente.

**Revisão de conteúdo:** [x] três estados; [x] ordem; [x] texto; [x] aceite/limite; [ ] paginação até uma página.
