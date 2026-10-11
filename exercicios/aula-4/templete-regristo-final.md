# Registro individual — AV1.4

**Estudante:** Rafael Farias de Oliveira Lima — **Data:** 11/10/2026
**Limite:** uma página; paginação conferida manualmente pelo estudante.
**Critério de aceite por R2:** incluir `aberto` e `em_andamento`, excluir `fechado` e preservar a ordem relativa da entrada, conforme o [contrato](../../caso/regras.md).

| Entrada / contraexemplo | IDs esperados por R2 | IDs do candidato | Status | Mecanismo/trecho essencial |
| --- | --- | --- | --- | --- |
| TR-41, TR-42, TR-43, TR-44 | TR-41, TR-42, TR-44 | TR-42, TR-44, TR-41 | Inferido por inspeção | `sorted(ativos, key=lambda c: c["impacto"] + c["urgencia"], reverse=True)` ordena os escores 6, 4, 2. |

**Divergência:** o candidato seleciona os estados corretamente, mas move TR-41 de primeiro para último entre os ativos. Retornar os mesmos IDs não basta: R2 também exige a mesma sequência relativa.

**Teste entregue — alcance e evidência:** sua entrada é `[TR-42, TR-44, TR-41, TR-43]`; a única asserção exige `["TR-42", "TR-44", "TR-41"]`. Os ativos já aparecem em ordem decrescente de escore. Tanto preservar a entrada quanto ordenar por escore satisfariam essa asserção, por leitura. O teste verifica os estados nessa amostra, mas não distingue as duas estratégias. Não foi fornecido resultado de execução.

**Decisão e motivo:** rejeitar o candidato atual e preservar R2, conforme decisão do estudante no chat. O contraexemplo acima demonstra a violação; o teste favorável não a elimina.

**Comparação entre manter e ajustar / responsável:** manter a ordenação exigiria mudança formal de requisito, não autorizada neste cenário. Remover a ordenação conserva o contrato e o filtro correto. A pessoa revisora da manutenção deve aprovar a versão ajustada após conferir código e resultados.

**Ajuste proposto, isolado, sem alterar o kit:**

```python
def listar_ativos_proposta(chamados):
    return [c for c in chamados if c["estado"] in ("aberto", "em_andamento")]
```

**Revalidação por inspeção:** a compreensão percorre a entrada na ordem recebida e apenas exclui os registros fechados. Os campos completos são os da tabela do [enunciado](README.md).

| Caso para conferir o ajuste: entrada e ordem | IDs esperados | Resultado previsto / status |
| --- | --- | --- |
| TR-41, TR-42, TR-43, TR-44 | TR-41, TR-42, TR-44 | TR-41, TR-42, TR-44 / inferido por inspeção |
| TR-42, TR-44, TR-41, TR-43 | TR-42, TR-44, TR-41 | TR-42, TR-44, TR-41 / inferido por inspeção |

**Revisão do teste proposta:** manter a asserção existente e acrescentar comparação da lista completa de IDs para a entrada do contraexemplo. Assim, a versão ordenada indevidamente falharia nesse novo caso.

**Limite remanescente e condição para rever o parecer:** não houve execução nem verificação de integração; duas entradas não cobrem todas as listas válidas. Rever o aceite da versão ajustada se ela divergir dos esperados; uma alteração formal de R2 exigiria novos critérios e nova análise.

**Origem e método:** candidato, teste e entradas são simulações didáticas do enunciado, não saída observada de modelo real. Comparação e revalidação por leitura, com assistência de IA; execução não realizada.

**Uso de IA:** GitHub Copilot, GPT-6.1 Sol (`gpt-6.1-sol`), apoiou comparação, explicação do teste, ajuste e redação. Em 11/10/2026, o estudante solicitou esclarecimento sobre a ordem e confirmou preservar R2, citando a divergência e o contraexemplo. Revisão pessoal final do texto e paginação concluídas manualmente pelo estudante.

**Revisão de conteúdo:** [x] comparação com R2; [x] alcance do teste; [x] ajuste/revalidação; [x] status; [x] revisão pessoal final; [x] paginação até uma página.
