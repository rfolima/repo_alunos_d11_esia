# Fichamento L0 — LLMs para Engenharia de Software

Fan et al. (2023) e Hou et al. (2024)

## 1. Fan et al. — Large Language Models for Software Engineering: Survey and Open Problems

**Argumento do artigo.** LLMs podem apoiar tarefas como geração de código, testes e manutenção, mas sua capacidade de produzir saídas plausíveis também introduz risco de alucinação e código funcionalmente incorreto. Os autores defendem a combinação de LLMs com mecanismos tradicionais de Engenharia de Software, como execução, testes, análise e revisão, em vez de confiar diretamente na saída do modelo. Localização: Introdução (§I), Scientific Evaluation (§IV-D), Open Problems (§IV-E) e Hybridisation/Thorough Testing (§XII-C e §XII-F).

**Limitação para o Fila Clara.** Os resultados discutidos no survey não demonstram que um modelo específico de 2026 produzirá código correto no contexto, arquitetura e regras do Fila Clara.

**Inferência/decisão.** Usar o LLM como gerador de candidatos, nunca como fonte final de verdade. Código gerado deve passar por testes automatizados, validações do projeto e revisão humana antes de ser aceito.

## 2. Hou et al. — Large Language Models for Software Engineering: A Systematic Literature Review

**Argumento do artigo.** A revisão sistemática mostra que geração de código é uma das principais aplicações de LLMs em Engenharia de Software e que métricas como Pass@k são usadas para avaliar se soluções geradas passam em testes. Entretanto, os autores destacam que uma única métrica não representa toda a confiabilidade: robustez, generalização e adequação ao cenário real também precisam ser consideradas. Localização: Evaluation Metrics (§5.3), Software Development / Code Generation (§6.4) e discussão de limitações de avaliação (§8.1.3).

**Limitação para o Fila Clara.** Desempenho em benchmarks públicos, medido por Pass@k, não garante o mesmo resultado em um sistema real com requisitos e dados próprios.

**Inferência/decisão.** Avaliar LLMs no próprio contexto do Fila Clara, usando casos representativos, testes definidos a partir dos requisitos e mais de um critério de qualidade; Pass@k pode ser um indicador, mas não deve ser a única evidência.

**Referências.** FAN, A. et al. Large Language Models for Software Engineering: Survey and Open Problems. arXiv:2310.03533v4, 2023. HOU, X. et al. Large Language Models for Software Engineering: A Systematic Literature Review. arXiv:2308.10620v6, 2024.
