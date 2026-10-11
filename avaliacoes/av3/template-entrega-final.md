# Entrega individual — AV3

**Estudante:** Rafael Farias de Oliveira Lima · **Data:** 11/10/2026
**Caso/recorte:** assistência de IA para sugerir testes e documentação na manutenção de Fila Clara.
**Limites:** parecer até três páginas; evidências/referências até duas páginas. Revisão pessoal final e paginação confirmadas pelo estudante. [Enunciado](README.md).

## Parecer

### 1. Recomendação e problema

Recomendo **adoção condicionada**, restrita à preparação de um piloto com dados sintéticos, ferramenta autorizada e revisão humana. Enquanto essas condições não forem atendidas, manter o processo manual. Não autorizar envio de chamados/logs internos, implantação automática ou produção.

A manutenção é a beneficiária; o resultado esperado é obter propostas de testes e documentação conformes a R1–R4, com evidências auditáveis. O objeto de adoção é a assistência à equipe, não o sistema de chamados. As restrições são governança externa ainda não confirmada, ausência de piloto executado e necessidade de revisão das sugestões. Não há ganho de produtividade demonstrado.

| Alternativa | Processo e recursos | Benefício esperado / pressuposto | Limite e esforço de verificação |
|---|---|---|---|
| A — sem IA | Manutenção lê o contrato, prepara casos e documentação e revisa os resultados. | Pode começar agora com o kit sintético, sem envio externo. | Exige trabalho humano e não elimina erros; comparar estados, departamentos e ordem com o contrato. |
| B — assistência condicionada | IA sugere casos/texto em ferramenta autorizada; manutenção deriva os esperados e revisa antes de uso. | Pode ampliar sugestões; utilidade ainda precisa ser avaliada. | Acrescenta autorização e revisão; aparência correta ou teste verde não bastam. |

**Comparação:** A é a alternativa imediatamente viável. B merece avaliação limitada, não substituição automática de A: os artefatos e verificações permitem investigar utilidade, mas ainda não comprovam vantagem. A recomendação mantém A disponível e condiciona B a evidências e controles, evitando aceitar risco sem autorização ou presumir economia de tempo.

### 2. Autonomia e responsabilidade

Delegar somente rascunhos de testes e documentação. Requisitos, saídas esperadas, revisão e aceite permanecem humanos. A pessoa revisora da manutenção compara cada proposta com R1–R4 e registra entrada, esperado, encontrado e método. Para estados/departamentos/ordem, incluir contrastes que possam revelar erros, não só exemplos favoráveis.

Segurança verifica ferramenta, condições e dados; a gestora decide o uso autorizado e designa a revisão. Autorizar envio é diferente de aprovar uma resposta. Diante de divergência, recusar o artefato, manter a versão anterior e revalidar a correção. Exceções exigem decisão registrada; urgência não libera envio nem dispensa revisão. Sugestões permanecem isoladas, sem alteração automática do kit ou de produção.

### 3. Verificação e contraponto

**E1 — AV2:** V-02 é um chamado fechado da Oficina, solicitado por Oficina. R3 exige `True`; o candidato original retorna `False` por acrescentar filtro de estado. A divergência foi inferida por leitura e observada em execução pelo assistente. Após retirar o filtro, o estudante executou os quatro casos: todos coincidiram com R3, e conferiu a documentação ajustada. Isso favorece um processo de sugestão seguido de verificação contra critério independente.

**E2 — contraponto AV1.4:** um teste cuja entrada já esteja ordenada por escore aceita tanto o filtro correto quanto o candidato que altera a sequência. O contraexemplo TR-41/TR-42/TR-43/TR-44 revela a violação de R2 por inspeção. Logo, passar em um caso favorável não basta; é necessário avaliar o próprio teste.

Os candidatos de E1/E2 são simulações didáticas, não saídas de consultas reais a modelos. Não permitem medir taxa de erro de IA ou afirmar que ela causou os defeitos. O `OK` de AV2 cobre quatro casos de uma função isolada, não integração, segurança ou benefício operacional. Evidência de inadequação persistente ou descumprimento dos controles levaria a suspender a assistência e manter A.

### 4. Riscos e mecanismos

| Risco / consequência | Mecanismo | Responsável | Evidência e conferência | Exceção / interrupção |
|---|---|---|---|---|
| Exposição de identificação/acessos em envio externo. | Bloquear dados internos; autorizar ferramenta e escopo antes de eventual uso sintético. | Segurança emite parecer; gestora decide; solicitante confere conteúdo. | Decisão e checklist datados, vinculados à versão e às condições consultadas; comparar conteúdo com escopo autorizado. | Pendência mantém bloqueio; envio indevido suspende uso e aciona segurança. |
| Teste/texto incorreto aceito por plausibilidade. | Derivar esperados de R1–R4, revisar contrastes, registrar divergências e revalidar. | Pessoa revisora da manutenção. | Matriz e versão revisada; conferir ordem, estados/departamentos e texto, distinguindo inspeção de execução. | Recusar saída inadequada; uso sem revisão ou divergência não resolvida exige suspensão. |

Registros são controles futuros propostos por AV1.5, não autorizações já emitidas. Marcar checklist sem responsável, versão e evidência não comprova controle. Evidências sensíveis devem permanecer protegidas, com referências em vez de cópias em documentos de acesso amplo.

### 5. Maturidade e próximo passo

O estágio é **protótipo**: M1 apresenta artefato demonstrável. Exploração seria insuficiente; piloto exige execução limitada acompanhada, ausente em M5. M2–M4 mostram responsável, revisão e planejamento, não execução. M6 indica ausência de série de qualidade, retrabalho, tempo e incidentes. Uso sustentado exige operação recorrente e evidências ao longo do tempo. A execução didática da AV2 não altera esses fatos do dossiê.

Proponho piloto de duas semanas com duas pessoas da manutenção, dados sintéticos e ferramenta previamente autorizada, sob acompanhamento do responsável designado. Definir quantidade de tarefas antes do início; comparar tarefas equivalentes manuais e assistidas, alternando ordem e mantendo critérios R1–R4. Registrar tarefa, participante, modalidade, versão, revisão e correções.

**Qualidade inicial (%)** = 100 × propostas conformes na primeira revisão / propostas revisadas, calculada separadamente por modalidade. Informar contagens; denominador zero impede taxa e comparação. Contar também execuções e revisões e registrar conformidade final e incidentes. A referência é o processo manual, não um benchmark externo.

Amostra pequena, julgamento humano e aprendizagem limitam a comparação; contagens não comprovam qualidade, e a taxa não mede produtividade. Não usar essa taxa como equivalente a Pass@k. Não estabelecer conclusão de economia sem medir tempo total, incluindo revisão e retrabalho.

**Avanço proposto:** gestora autoriza avaliar uso recorrente somente com dados nas duas modalidades, taxa inicial assistida pelo menos igual à manual, todos os artefatos usados conformes após revisão final e nenhum incidente de dados. **Interrupção:** responsável suspende diante de envio indevido, uso sem revisão ou divergência não resolvida. Resultado inferior ou comparação insuficiente impede ampliar; gestora decide ajustar, repetir ou encerrar.

Essas metas não são resultados. Execução limitada acompanhada justificaria piloto; sucesso permitiria avaliar continuidade, não declarar imediatamente uso sustentado.

### 6. Fundamentação aplicada

**F1 — Fan et al.:** a introdução (§I) discute artefatos plausíveis porém incorretos e o papel da execução e dos testes. Isso fundamenta a fronteira de autonomia da seção 2. **Inferência para o caso:** usar IA como geradora de candidatos, com esperados derivados do contrato e revisão independente; E1/E2 mostram por que o critério importa. A fonte não prova desempenho de um produto de 2026 nem torna testes uma garantia universal.

**F2 — Hou et al.:** §5.3 discute métricas por tarefa; §6.4 aborda geração de código; §8.1.3 alerta que métricas usuais podem omitir falhas específicas e aspectos qualitativos. Isso fundamenta a seção 5: combinar qualidade inicial, conformidade final, realização e incidentes, com contraponto manual. **Inferência para o caso:** um indicador favorável deve ser confrontado com falhas e condições de uso. A revisão não fornece meta de aceite para Fila Clara nem garante transferência de benchmarks.

A tensão é permitir sugestões sem transformar potencial em garantia: F1 sustenta verificação dos artefatos; F2 limita o alcance dos indicadores. A adoção condicionada trata ambos, conservando o processo manual como alternativa e referência.

## Anexo — evidências, referências e procedência

### E1 — AV2: visibilidade

Origem: [insumos AV2](../av2/insumos.md); análise e evidências em [template-entrega-final.md](../av2/template-entrega-final.md); teste isolado [verificacao_av2.py](../av2/verificacao_av2.py).

Solicitante: `Oficina`. V-01/V-02: Oficina, impacto/urgência 1/1; V-03/V-04: Laboratório, impacto/urgência 3/3.

| Caso / estado | Esperado R3 | Original: observado pelo assistente | Ajustado: observado pelo estudante |
|---|---|---|---|
| V-01 / aberto | `True` | `True` | `True` |
| V-02 / fechado | `True` | `False` | `True` |
| V-03 / aberto | `False` | `False` | `False` |
| V-04 / fechado | `False` | `False` | `False` |

Trecho original: `departamento_igual and estado != "fechado"`; ajuste: somente `departamento_igual`. Os termos resumem as comparações dos campos no código.

Execução em Windows/PowerShell com Python, versão não registrada. Original: assistente executou `python -B .\avaliacoes\av2\verificacao_av2.py --original`, na raiz da sessão, obtendo `FAILED (failures=1)` em V-02. Ajustada: estudante executou `python -B $teste`, apontando para o mesmo script, e compartilhou `Ran 1 test in 0.001s` e `OK` em 02/10/2026. Um método contém quatro subcasos. Documentação ajustada conferida pelo estudante: próprio departamento em qualquer estado; outro departamento impedido.

### E2 — AV1.4: ordem e limite do teste

Origem: [enunciado AV1.4](../../exercicios/aula-4/README.md) e [registro](../../exercicios/aula-4/templete-regristo-final.md).

Entrada: TR-41/TR-42/TR-43/TR-44; R2 exige TR-41/TR-42/TR-44. Candidato ordena escores 6/4/2 e retorna TR-42/TR-44/TR-41. Status: inferido por inspeção, sem execução. O teste entregue usa entrada TR-42/TR-44/TR-41/TR-43 e exige TR-42/TR-44/TR-41: não distingue preservar ordem de ordenar por escore.

### Apoio à governança e maturidade

[AV1.5](../../exercicios/aula-5/templete-regristo-final.md): ferramenta/condições não confirmadas; bloqueio do envio interno e controles propostos. [AV1.6](../../exercicios/aula-6/templete-regristo-final.md): M1–M6, protótipo e piloto proposto. Responsável/revisão/plano constam do cenário; execução com usuários e série de resultados não ocorreram no dossiê.

### F1/F2 — referências L0

**F1:** FAN, A. et al. *Large Language Models for Software Engineering: Survey and Open Problems*. 2023, arXiv:2310.03533v4. Localizações informadas no [fichamento L0](fichamento-l0.md): §I, §IV-D, §IV-E, §XII-C e §XII-F; aplicação central deste parecer: §I. [Versão consultada](https://arxiv.org/abs/2310.03533v4).

**F2:** HOU, X. et al. *Large Language Models for Software Engineering: A Systematic Literature Review*. 2024, arXiv:2308.10620v6. Localizações: §5.3, §6.4 e §8.1.3, conforme fichamento. [Versão consultada](https://arxiv.org/abs/2308.10620v6).

### Procedência e assistência

O estudante informou ter realizado as leituras e forneceu o fichamento; as [notas extensas](notas-leitura-fornecidas.md) são apoio, não evidência empírica adicional. O assistente conferiu diretamente a introdução de Fan e as discussões de geração, métricas e limitações de Hou para a redação. Não se extrapolam resultados antigos para modelos de 2026.

Dados, candidatos e M1–M6 são didáticos; execução própria compartilhada: versão ajustada de AV2. Diagnóstico e comparação são inferências; piloto, metas, registros e autorizações são propostas. Não houve envio de dados internos nem implantação realizada nesta atividade.

**IA:** GitHub Copilot, GPT-6.1 Sol (`gpt-6.1-sol`), apoiou análise, testes isolados de AV2, organização do fichamento fornecido e redação do parecer. Em 11/10/2026, o estudante confirmou preservar R2, bloquear envio interno, os controles de AV1.5, o piloto/métricas de AV1.6 e a adoção condicionada da AV3. **Declaração do estudante:** “Revisei o parecer e confirmo as decisões, evidências e limites registrados.” Metadados indisponíveis: não informado.

**Checklist:** [x] alternativas; [x] autonomia; [x] evidência/contraponto; [x] dois riscos; [x] maturidade/métrica; [x] duas fontes aplicadas; [x] procedência; [x] revisão pessoal final; [x] paginação 3+2 páginas.
