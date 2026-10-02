# Registro individual — AV1.1

**Estudante:** Rafael Farias de Oliveira Lima — **Data:** 02/10/2026
**Limite:** uma página, incluindo evidências; paginação a conferir na exportação.
**Origem:** cartões C1–C3 do [enunciado](README.md), [contrato R2/R3](../../caso/regras.md) e [chamados sintéticos](../../caso/chamados.json).

| Cartão | Como faria sem IA / entrada e resultado | Modalidade e justificativa | O que conferir para aprovar | Responsável humano |
|---|---|---|---|---|
| C1 | Ler R2 e escrever critérios de estados e ordem. Para FC-001 a FC-006, esperar `[FC-001, FC-002, FC-004, FC-005]`. | Com assistência para rascunhar critérios: regra aprovada, dados controlados e revisão humana. | Incluir `aberto`/`em_andamento`, excluir `fechado` e preservar a sequência de entrada. | Pessoa revisora da manutenção. |
| C2 | Cruzar manualmente os departamentos solicitantes com os três estados; derivar de R3 a tabela abaixo. | Com assistência para sugerir casos, mas esperado definido pelo contrato, não pelo código proposto. | Mesmo departamento: `True`; diferente: `False`, independentemente de estado/impacto/urgência. | Pessoa revisora da manutenção. |
| C3 | Suspender implantação e solicitar nova regra aprovada, dados afetados, verificações e aprovador. Resultado: não autorizar nas condições atuais. | Sem delegar a decisão. IA pode sugerir uma alternativa isolada, mas urgência e “facilitar acesso” não autorizam produção. | Aprovação formal da mudança, análise de impacto, verificações registradas e documentação atualizada; simulação não basta. | Gestão responsável pela mudança, após revisão técnica. |

**Exemplo que sustenta a decisão — C2:** a tabela aplica R3 aos seis registros. FC-003, fechado e da Oficina, deve retornar `True` para Oficina e `False` para Laboratório; fechamento não impede acesso ao próprio departamento. Impacto/urgência são os do JSON e não interferem.

**Proposta hipotética para C3:** manter acesso ao próprio departamento em qualquer estado e permitir acesso entre departamentos somente a chamados ativos. Implementação isolada:

```python
def pode_visualizar_proposta(chamado, departamento):
    return (chamado["departamento"] == departamento
            or chamado["estado"] in ("aberto", "em_andamento"))
```

| ID / estado | C2: esperado R3 — Oficina / Laboratório | C3: proposta executada — Oficina / Laboratório |
|---|---|---|
| FC-001 / aberto | `True` / `False` | `True` / `True` |
| FC-002 / em_andamento | `False` / `True` | `True` / `True` |
| FC-003 / fechado | `True` / `False` | `True` / `False` |
| FC-004 / aberto | `False` / `True` | `True` / `True` |
| FC-005 / em_andamento | `True` / `False` | `True` / `True` |
| FC-006 / fechado | `False` / `True` | `False` / `True` |

**Método e decisão C3:** C1/C2 são resultados esperados por leitura, não execução. C3 foi executado pelo assistente em Python (`python -B -`), lendo o JSON e chamando a função para ambos os departamentos, sem alterar o kit. A proposta amplia acesso em quatro registros e contradiz R3 vigente nesses acessos. A implantação continua suspensa: comportamento demonstrado não equivale a requisito aprovado ou autorização.

**Alternativa para C1:** manutenção escreve os critérios sem IA. **Comparação:** como R2 é curta, redação manual pode custar menos que revisar sugestões; não há medição de ganho de produtividade.

**Limite da delegação e condição para rever a escolha:** IA sugere, humanos aprovam. Preferir processo manual se houver omissões ou retrabalho. Rever C3 somente após aprovação da nova regra, confirmação dos impactos e revalidação; dados sintéticos não demonstram segurança real.

**Uso de IA:** GitHub Copilot, GPT-6.1 Sol (`gpt-6.1-sol`), apoiou redação, tabelas, proposta e execução isolada. Intervenção registrada: o estudante identificou a lista ativa de C1 e pediu comparação e simulação de C3; o assistente conferiu o contrato e corrigiu o último ID repetido para FC-006. Revisão pessoal final do documento pelo estudante ainda pendente.

**Revisão de conteúdo:** [x] três decisões; [x] exemplo explicado; [x] alternativa e limite; [ ] paginação até uma página.
