# Entrega individual — AV2

**Estudante:** Rafael Farias de Oliveira Lima · **Data:** 02/10/2026 · **Via:** inspeção e execução isolada
**Limites:** análise até duas páginas; anexo técnico até duas páginas. O estudante confirmou no chat a conferência da versão atualizada dentro desses limites em 02/10/2026. [Enunciado](README.md).

## Análise

**1. Recorte e requisito.** Avaliar a função isolada `pode_visualizar_proposta(chamado, departamento)` e a documentação candidata. A manutenção usa a análise para decidir o aceite; o retorno indica se a pessoa do departamento solicitante pode visualizar o chamado. Entradas válidas e sintéticas: departamentos Oficina/Laboratório, estados aberto/em andamento/fechado e impacto/urgência de 1 a 3. Não há autenticação real, API, persistência ou validação de entradas externas no escopo.

**Critério de aceite definido antes da verificação:** conforme R3, retornar `True` se os departamentos forem iguais e `False` se forem diferentes, independentemente de estado ou prioridade. R4 exige documentação coerente com essa mesma regra. O estudante confirmou no chat a decisão de respeitar R3; a mudança hipotética de C3 da aula 1 não é requisito desta avaliação.

**2. Estratégia.** Cruzar igualdade/diferença de departamento com aberto/fechado, usando V-01–V-04 e solicitante `Oficina`. Manter o solicitante fixo e usar os campos fornecidos, sem modificar os dados. Os quatro casos cobrem todas as combinações exigidas e contrastam a permissão em chamados abertos e fechados. Dentro de cada par de departamento, impacto e urgência permanecem iguais, isolando o efeito do estado.

**Caso decisivo:** T2, mesmo departamento e fechado: R3 exige `True`, mas o candidato resulta em `False`. **Controle:** T1, mesmo departamento e aberto: esperado e candidato são `True`. T3/T4 também conferem a negativa para outro departamento. A matriz não cobre `em_andamento`, o solicitante Laboratório ou todas as combinações de impacto/urgência.

**3. Evidência e interpretação.** A matriz T1–T4 do anexo mostra concordância em T1/T3/T4 e divergência em T2. Pelo percurso de E2, a condição adicional de estado impede visualizar um chamado fechado do próprio departamento. Isso viola E1/R3; três casos conformes não anulam o contraexemplo.

Em E3, a documentação afirma que “chamados fechados ficam indisponíveis”: descreve o candidato, mas contradiz R3. Código e texto concordarem entre si não demonstra conformidade com o requisito. As afirmações sobre impedir acesso de outros departamentos e sobre impacto/urgência não interferirem são compatíveis com R3, mas não corrigem a restrição indevida de estado.

**4. Decisão comparada.** **Código: rejeitar a versão atual**, pela divergência T2. **Documentação: rejeitar a versão atual**, pela restrição a chamados ativos. Não se propõe mudar o contrato para justificar o candidato.

**Alternativa:** remover o filtro de estado e revisar o texto para explicitar acesso ao próprio departamento em qualquer estado. Manter a versão atual evita edição imediata, mas continua descumprindo o critério; ajustá-la preserva R3 e exige nova revisão do código, dos casos e da documentação. Não há evidência de ganho de produtividade.

**Ajuste e revalidação:** A1 e A2, no anexo, apresentam código/texto ajustados. Após a inspeção, o assistente executou as duas versões e o estudante executou a ajustada, compartilhando a saída: T1–T4 coincidem com R3. O estudante também confirmou a coerência de A2, inclusive para chamados fechados. Isso sustenta **aceite condicionado da versão ajustada**, sujeito ao aceite da pessoa responsável pela manutenção, não autorização de produção.

**Responsável e revisão:** a pessoa revisora da manutenção deve registrar o aceite da versão ajustada contra R3/R4 e revisar novamente se houver divergência ou mudança de versão. Casos adicionais de `em_andamento`/solicitante Laboratório podem complementar os quatro casos executados. Alterar o requisito exigiria aprovação formal separada; não é a alternativa escolhida.

**5. Procedência e limites.** Contrato, candidato, documentação e V-01–V-04 são artefatos didáticos de [insumos.md](insumos.md), não saídas observadas de modelo real. Esperados foram definidos por R3 antes da comparação. Retornos foram inicialmente inferidos por inspeção e depois observados em execução isolada: original pelo assistente, ajustada pelo assistente e pelo estudante, com saída compartilhada no chat. Aceite pela manutenção e casos adicionais continuam propostos; o kit não foi alterado.

A cobertura limitada não demonstra execução correta de uma implementação integrada, segurança de um sistema real ou produtividade de IA. A divergência concreta basta para rejeitar a versão atual, enquanto o aceite da alternativa permanece dependente de revisão humana da versão efetivamente apresentada.

**IA:** GitHub Copilot, GPT-6.1 Sol (`gpt-6.1-sol`), em 02/10/2026, apoiou matriz, percurso lógico, confronto documental, ajuste, teste isolado e redação. O estudante confirmou R3 e a rejeição dos originais, executou a ajustada, conferiu A2 e confirmou os limites da conclusão. A revisão pessoal dos pontos de decisão, documentação e evidência e a conferência de paginação foram confirmadas pelo estudante no chat. Metadados de modelo das propostas didáticas, tokens, custo e latência: não informados.

## Anexo técnico — trechos essenciais

**Dados e condições comuns:** seção “Dados disponíveis para construir a matriz” de [insumos.md](insumos.md). Usam-se todos os campos dos registros V-01–V-04, sem alteração; solicitante `Oficina`. V-01/V-02: departamento Oficina, impacto 1, urgência 1; V-03/V-04: Laboratório, impacto 3, urgência 3. Estados conforme tabela abaixo.

| Caso | Entrada/referência + solicitante | Relação / estado | Esperado por R3 | Retorno do candidato | Status | Interpretação |
|---|---|---|---|---|---|---|
| T1 | V-01 / Oficina | Igual / aberto | `True` | `True` | Observado pelo assistente | Conforme; controle positivo. |
| T2 | V-02 / Oficina | Igual / fechado | `True` | `False` | Observado pelo assistente | Divergência: bloqueia próprio departamento. |
| T3 | V-03 / Oficina | Diferente / aberto | `False` | `False` | Observado pelo assistente | Conforme; bloqueia outro departamento. |
| T4 | V-04 / Oficina | Diferente / fechado | `False` | `False` | Observado pelo assistente | Conforme; departamento diferente já impede acesso. |

**E1 — contrato e localização:** [caso/regras.md](../../caso/regras.md), tabela “Regra / Comportamento esperado”, R3: “permite acesso somente à pessoa do mesmo departamento do chamado, independentemente de estado ou prioridade”. R4: “A documentação descreve essas mesmas regras.”

**E2 — código e localização:** [insumos.md](insumos.md), seção “Candidato de código”:

```python
def pode_visualizar_proposta(chamado, departamento):
    return (
        chamado["departamento"] == departamento
        and chamado["estado"] != "fechado"
    )
```

**Percurso decisivo T2:** `Oficina == Oficina` → `True`; `fechado != fechado` → `False`; `True and False` → `False`. R3 exige `True`.
**Percurso de controle T1:** `Oficina == Oficina` → `True`; `aberto != fechado` → `True`; `True and True` → `True`, conforme R3.

**E3 — documentação e confronto:** [insumos.md](insumos.md), seção “Documentação candidata — texto fictício”:

> A função permite que uma pessoa visualize chamados ativos de seu próprio departamento. Chamados abertos ou em andamento ficam disponíveis para o departamento correspondente; chamados fechados ficam indisponíveis. Chamados de outros departamentos não são exibidos. Impacto e urgência não alteram essa decisão.

“Ativos” e “fechados ficam indisponíveis” correspondem ao filtro do candidato, mas violam R3 em T2. Exclusão de outros departamentos e independência de impacto/urgência são coerentes com contrato e código.

**Execução — ambiente/comando/saída:** Windows/PowerShell, Python e biblioteca padrão; versão do Python não registrada. Script separado [verificacao_av2.py](verificacao_av2.py), com funções `proposta_original` e `proposta_ajustada` equivalentes aos trechos E2/A1. Um método de teste contém quatro subcasos, com esperados explícitos derivados de R3.

Na raiz desta sessão, o assistente executou `python -B .\avaliacoes\av2\verificacao_av2.py --original`:

```text
V-01: esperado=True, retorno=True
V-02: esperado=True, retorno=False
V-03: esperado=False, retorno=False
V-04: esperado=False, retorno=False
FAILED (failures=1)
```

O estudante executou `python -B $teste`, com `$teste` apontando para o script desta sessão, e compartilhou:

```text
V-01: esperado=True, retorno=True
V-02: esperado=True, retorno=True
V-03: esperado=False, retorno=False
V-04: esperado=False, retorno=False
Ran 1 test in 0.001s
OK
```

Para repetir a execução ajustada na raiz da sessão: `python -B .\avaliacoes\av2\verificacao_av2.py`. A execução anterior de C3 da aula 1 não integra esta evidência.

**A1 — alternativa de código, isolada, sem alteração do kit:**

```python
def pode_visualizar_ajustada(chamado, departamento):
    return chamado["departamento"] == departamento
```

**A2 — documentação ajustada:** “A função permite visualizar um chamado quando o departamento solicitante é igual ao departamento do chamado. Chamados de outro departamento não são permitidos. Estado, impacto e urgência não alteram essa decisão.”

**Revalidação da alternativa:** mesmas entradas e solicitante de T1–T4; a condição remanescente é apenas igualdade de departamento.

| Caso | Esperado por R3 | Retorno ajustado | Status | Confronto com A2 |
|---|---|---|---|---|
| T1 | `True` | `True` | Observado pelo estudante | Mesmo departamento permite aberto. |
| T2 | `True` | `True` | Observado pelo estudante | Mesmo departamento permite fechado. |
| T3 | `False` | `False` | Observado pelo estudante | Outro departamento impede aberto. |
| T4 | `False` | `False` | Observado pelo estudante | Outro departamento impede fechado. |

**Conclusão pessoal confirmada no chat:** rejeitar código/documentação originais e encaminhar o ajuste à revisão da manutenção. A execução dos quatro casos e a conferência do texto sustentam conformidade com R3/R4 nesse recorte, mas não comprovam todas as entradas, integração ou segurança de um sistema real. A revisão acadêmica do estudante não substitui o aceite formal pela manutenção.

**Checklist de conteúdo:** [x] quatro combinações; [x] critério prévio; [x] código e texto; [x] status; [x] alternativa/revalidação; [x] limites/IA; [x] revisão pessoal final; [x] paginação 2+2 páginas.
