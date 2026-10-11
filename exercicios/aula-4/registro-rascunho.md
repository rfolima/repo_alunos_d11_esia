# Registro individual — AV1.4 — rascunho para revisão

**Estudante:** Rafael Farias de Oliveira Lima · **Data do registro:** 11/10/2026. Limite: uma página, a conferir na exportação.
**Critério R2:** incluir aberto/em andamento, excluir fechado e preservar a ordem de entrada.

| Entrada | IDs esperados por R2 | IDs do candidato | Status | Mecanismo |
|---|---|---|---|---|
| TR-41, TR-42, TR-43, TR-44 | TR-41, TR-42, TR-44 | TR-42, TR-44, TR-41 | Inferido por inspeção | `sorted(ativos, key=lambda c: c["impacto"] + c["urgencia"], reverse=True)` ordena os escores 6, 4, 2. |

**Alcance do teste:** entrada `[TR-42, TR-44, TR-41, TR-43]`; única asserção: IDs iguais a `["TR-42", "TR-44", "TR-41"]`. Nessa entrada, os ativos já estão em ordem decrescente de escore. Tanto o filtro que preserva ordem quanto o candidato ordenado satisfariam a asserção, por inspeção. O teste confere inclusão/exclusão nessa amostra, mas não distingue preservação de ordem de ordenação por prioridade; não há execução fornecida.

**Decisão confirmada pelo estudante:** preservar R2 e rejeitar a versão atual por alterar a ordem. Registrar explicitamente a divergência e o contraexemplo `[TR-41, TR-42, TR-43, TR-44]`: R2 exige `[TR-41, TR-42, TR-44]`, mas o candidato produz `[TR-42, TR-44, TR-41]`, por inspeção. O teste favorável não elimina esse contraexemplo.

**Comparação e responsável:** manter a ordenação só seria admissível com mudança aprovada do requisito, inexistente no cenário. Remover a ordenação atende ao contrato vigente e evita alterar a expectativa do usuário. Aceite da versão ajustada cabe à pessoa revisora da manutenção, após nova verificação.

**Ajuste proposto, isolado, sem alterar o kit:**

```python
def listar_ativos_proposta(chamados):
    return [c for c in chamados if c["estado"] in ("aberto", "em_andamento")]
```

| Revalidação por leitura: entrada e ordem | Esperado | Resultado previsto / status |
|---|---|---|
| TR-41, TR-42, TR-43, TR-44 | TR-41, TR-42, TR-44 | TR-41, TR-42, TR-44; inferido: compreensão percorre a entrada e só remove TR-43. |
| TR-42, TR-44, TR-41, TR-43 | TR-42, TR-44, TR-41 | TR-42, TR-44, TR-41; inferido, preserva também o caso do teste original. |

**Limite e revisão:** inspeção não comprova execução ou integração; amostras não cobrem todas as listas válidas. Rever o parecer se uma versão ajustada divergir dos esperados ou se houver alteração formal de R2; para aceite executável, propor asserção adicional usando a entrada que expõe a inversão.

**Procedência:** candidato, teste e dados simulados do [enunciado](README.md); referência [R2](../../caso/regras.md). Execução não realizada.
**Assistência efetiva:** GitHub Copilot, GPT-6.1 Sol (`gpt-6.1-sol`), elaborou comparação, ajuste e revalidação por inspeção. Em 11/10/2026, após esclarecimento sobre ordem e alcance do teste, o estudante confirmou preservar R2 e explicitar a divergência e o contraexemplo. Revisão final do texto e paginação ainda pendentes; execução não realizada.
