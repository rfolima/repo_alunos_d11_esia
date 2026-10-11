1. A ideia central dos dois artigos
Os dois trabalhos tentam responder a uma pergunta parecida:
O que os LLMs realmente podem fazer dentro da Engenharia de Software, e como sabemos se estão fazendo isso de maneira correta?

A conclusão geral não é simplesmente “LLMs programam bem”.
É algo mais interessante:
LLMs podem auxiliar muitas atividades de Engenharia de Software, mas a geração do LLM não deve ser tratada como resultado confiável por si só. O valor aparece principalmente quando o LLM é combinado com mecanismos tradicionais de Engenharia de Software — testes, análise estática, validação, benchmarks, revisão humana etc.
Essa é provavelmente a ideia mais importante para você guardar dos dois textos.
2. Fan et al. — Survey and Open Problems
Versão: arXiv:2310.03533v4, 2023.
O que o artigo quer descobrir
Fan et al. fazem um grande passeio pelo ciclo de desenvolvimento de software e perguntam onde LLMs podem ser usados.
O artigo aborda áreas como:
- requisitos e design;
- geração e conclusão de código;
- testes;
- debugging;
- reparo automático;
- melhoria de performance;
- refatoração;
- documentação;
- análise de repositórios;
- processo de desenvolvimento;
- educação em Engenharia de Software.
Não é uma revisão sistemática tão formal quanto Hou. O objetivo é mapear o campo e, sobretudo, identificar problemas de pesquisa ainda não resolvidos. arXiv
3. A principal tese de Fan
Uma das ideias mais fortes aparece já na introdução.
LLMs possuem justamente uma característica que é simultaneamente sua vantagem e seu problema:
eles conseguem produzir respostas novas e plausíveis.
Isso permite gerar código, requisitos, documentação, testes e soluções. Mas também permite gerar algo falso que parece correto.
No contexto de Engenharia de Software, uma alucinação pode significar:
LLM gera código
       ↓
Código parece correto
       ↓
Compila
       ↓
MAS possui comportamento errado

Fan chama atenção para uma vantagem particular da Engenharia de Software: diferentemente de muitas tarefas de linguagem natural, frequentemente conseguimos executar o artefato produzido e verificar seu comportamento. arXiv
Esse ponto é fundamental.
Em texto comum
Se um LLM responde uma pergunta histórica incorretamente, pode ser difícil verificar automaticamente.
Mas se ele cria:
def calcular_total(...):


podemos executar testes contra essa função.
Portanto, a Engenharia de Software dispõe de uma espécie de defesa natural contra as alucinações:
testes + execução + análise automática.
4. Conceito importante: “oracle”
Fan usa bastante a ideia de test oracle.
Em testes, o oracle é aquilo que permite responder:
“Para esta entrada, qual deveria ser a saída correta?”

Imagine:
Entrada: 2 + 2
Saída esperada: 4

O teste conhece a saída correta. Logo, temos um oracle.
O problema aparece quando não sabemos automaticamente qual deveria ser o comportamento correto.
Fan chama atenção para o Oracle Problem: gerar testes não basta; é preciso saber se o resultado esperado pelo teste também está correto. arXiv
Isso se torna particularmente sério com LLMs.
Um LLM poderia gerar simultaneamente:
código errado
+
teste errado que aceita aquele código

e então o teste passa.
Logo:
“passou nos testes” só é uma evidência forte quando os próprios testes representam corretamente o requisito.

5. Aplicação importante: geração de código
Esta é provavelmente a aplicação mais simples para você selecionar na L0.
Fan discute LLMs que recebem algo como:
"Implemente uma função que faça X"

e produzem código.
O trabalho relata estudos com diferentes modelos e técnicas, mas a parte mais interessante não são os números de modelos de 2023 — eles rapidamente envelhecem.
O ponto conceitual importante é:
não basta medir se o LLM consegue gerar código; precisamos avaliar o código produzido.
Fan divide a avaliação em dimensões como:
Dimensão	Pergunta
Correctness	O código realmente faz o que deveria?
Robustness	Pequenas mudanças no prompt mudam drasticamente o resultado?
Explainability	A explicação fornecida ajuda a compreender a solução?
Determinism	Repetindo a solicitação, obtemos resultados consistentes?
Security	O código introduz vulnerabilidades?


Isso é muito mais próximo de Engenharia de Software do que simplesmente perguntar “o modelo acertou?”.
6. Problema de confiabilidade nº 1: alucinação
Uma alucinação em programação não precisa ser algo absurdo.
Na verdade, o caso perigoso é justamente:
algo tecnicamente plausível, mas incorreto.

Exemplo hipotético:
const queue = await Queue.getActiveQueue();

Parece perfeitamente razoável.
Mas talvez getActiveQueue() nem exista no framework utilizado.
Ou o LLM pode inventar:
GET /api/queue/status/current

porque aquela API “parece” uma API que deveria existir.
Fan considera a alucinação um problema estrutural dos LLMs e argumenta que ela provavelmente não será simplesmente eliminada. Por isso, os processos precisam detectar e filtrar resultados incorretos. arXiv
7. Problema de confiabilidade nº 2: não determinismo
Outra ideia muito importante:
Mesmo prompt
    ↓
LLM
    ↓
Resposta A

Mesmo prompt novamente
    ↓
LLM
    ↓
Resposta B

Isso complica avaliações científicas.
Fan cita um estudo em que mais de 60% das tarefas analisadas não produziram exatamente os mesmos resultados de teste em diferentes execuções; ao mesmo tempo, apenas 21,1% dos trabalhos analisados naquele conjunto tratavam explicitamente essa ameaça de não determinismo. arXiv
Isso significa que um experimento do tipo:
“Perguntei uma vez ao ChatGPT e funcionou.”

é uma evidência muito fraca.
Uma avaliação melhor repetiria o experimento, manteria configuração/prompt documentados e avaliaria a distribuição dos resultados.
8. O conceito mais valioso de Fan: abordagem híbrida
Talvez este seja o trecho mais importante do artigo inteiro para sua atividade.
Os autores argumentam que LLMs tendem a ser mais úteis integrados a processos tradicionais de Engenharia de Software, e não funcionando isoladamente. arXiv
Imagine:
Requisito
   ↓
  LLM
   ↓
Código candidato
   ↓
Compilação
   ↓
Análise estática
   ↓
Testes automatizados
   ↓
Security checks
   ↓
Revisão humana
   ↓
Código aceito

Esse pipeline é muito mais defensável do que:
Prompt → LLM → código → produção

Fan menciona explicitamente a perspectiva de adaptar até pipelines de Continuous Integration para incorporar LLMs com análise e pós-processamento. arXiv
9. Uma demonstração interessante: testes fracos podem enganar
Fan apresenta um caso que ajuda muito a entender avaliação.
Benchmarks de geração de código geralmente utilizam:
Pass@k
Por exemplo:
Pass@1 = porcentagem de problemas para os quais a primeira solução produzida passa nos testes.

Parece bom.
Só que existe um problema:
Código passa no teste
≠
Código necessariamente correto

Quando um estudo chamado EvalPlus adicionou testes mais rigorosos ao HumanEval, a avaliação pass@k de modelos caiu em até 15 pontos percentuais, em média sobre os problemas, segundo o survey. arXiv
Isso ensina uma lição muito importante:
Uma métrica mede tanto o sistema quanto a qualidade do mecanismo usado para avaliá-lo.

10. O que Fan quer que você saia sabendo
Eu condensaria Fan em:
LLMs são bons geradores de candidatos; Engenharia de Software precisa continuar sendo responsável por verificar os candidatos.
Ou:
LLM = geração / sugestão
SE tradicional = validação / controle

Isso explica por que os autores dão tanta importância à hibridização. arXiv
Uma observação sobre seu enunciado: Fan não possui uma seção final chamada literalmente “Conclusion” na versão v4. A síntese final está principalmente na seção XII — Crosscutting Open Research Topics, especialmente XII-C a XII-H. arXiv
11. Hou et al. — Systematic Literature Review
Aqui a abordagem muda.
Em vez de os autores simplesmente discutirem os estudos que consideram relevantes, eles realizam uma Systematic Literature Review — SLR.
Eles analisaram 395 trabalhos, publicados entre janeiro de 2017 e janeiro de 2024. arXiv
A pergunta passa a ser:
“O que a literatura como um todo está mostrando sobre LLMs em Engenharia de Software?”

12. As quatro grandes perguntas de Hou
A pesquisa é organizada em quatro questões:
RQ1 — Quais LLMs estão sendo utilizados em Engenharia de Software?
RQ2 — Que dados são utilizados e como são preparados?
RQ3 — Como os modelos são otimizados e avaliados?
RQ4 — Em quais tarefas de Engenharia de Software eles estão sendo aplicados? arXiv
Isso faz do artigo uma espécie de mapa do campo.
13. O tamanho desse mapa
Os autores identificaram 85 tarefas diferentes, distribuídas em seis grandes atividades:
Engenharia de requisitos
Design de software
Desenvolvimento
Garantia de qualidade
Manutenção
Gerenciamento de software
``` :chatgpt-content-reference{index="15"}


Entre elas aparecem tarefas como:

```text
geração de código
completar código
summarização de código
geração de testes
detecção de vulnerabilidades
localização de bugs
program repair
code review
debugging
estimativa de esforço
...

Ou seja, LLM4SE é muito maior do que “Copilot gera código”.
14. Um dado extremamente importante de Hou
Dos 395 estudos, apenas seis utilizavam datasets industriais, segundo a análise dos autores. arXiv
Esse dado merece muita atenção.
Grande parte da evidência existente vinha de:
benchmarks
GitHub
Stack Overflow
datasets públicos
problemas acadêmicos

e não necessariamente de sistemas reais de empresas.
Portanto:
um resultado muito bom em um benchmark não garante o mesmo resultado em um projeto específico.

Os próprios autores apontam possível desalinhamento entre dados acadêmicos e cenários industriais. arXiv
Isso é diretamente relevante para qualquer aplicação a um projeto como Fila Clara.
15. Hou e o problema da generalização
Imagine que um modelo consiga 90% em:
Benchmark X

Não podemos concluir automaticamente:
Fila Clara → também terá 90%

Porque mudam:
- arquitetura;
- domínio;
- convenções;
- requisitos;
- linguagem;
- dados;
- APIs;
- contexto do projeto.
Hou chama isso de problema de generalizabilidade: o desempenho pode cair ao sair do contexto em que o modelo foi estudado. arXiv
16. Como Hou organiza a avaliação
Esta é provavelmente a parte mais importante para o segundo item da sua L0.
Eles agrupam os problemas em quatro tipos:
Tipo de tarefa	Exemplos de métricas
Regressão	MAE
Classificação	Precision, Recall, F1, Accuracy
Recomendação	MRR, Precision@k, MAP@k
Geração	BLEU, Pass@k, Exact Match, CodeBLEU, ROUGE


Isso significa que a métrica precisa corresponder ao tipo de tarefa.
17. Exemplo: geração de código
Esse é um bom exemplo para sua leitura.
Hou identifica code generation como uma das áreas dominantes da literatura.
Um desenvolvedor fornece uma descrição em linguagem natural:
"Implemente uma função que retorne a posição atual do usuário na fila."

O LLM gera código.
Estudos de geração de código normalmente utilizam benchmarks como HumanEval/MBPP e frequentemente medem desempenho usando Pass@k. A própria revisão apresenta estudos de geração usando essa combinação. arXiv
Pass@k
Se:
k = 1

perguntamos:
A primeira solução gerada passou?

Se:
k = 10

perguntamos:
Entre dez soluções produzidas, pelo menos uma passou?

Consequentemente:
Pass@10 ≥ Pass@1

em condições comparáveis.
Mas atenção: isso continua dependendo dos testes usados para decidir o que significa “passar”.
18. Hou também critica as próprias métricas
Esse é um dos pontos mais sofisticados do artigo.
Os autores reconhecem que métricas como:
Accuracy
Precision
Recall
F1
BLEU
Pass@k

não capturam necessariamente tudo que interessa.
Um modelo pode ter boa accuracy média e, mesmo assim:
- falhar em casos específicos;
- ser sensível a pequenas mudanças;
- produzir código inseguro;
- ter baixa robustez;
- não generalizar;
- produzir resultados difíceis de explicar. arXiv
Então:
medir desempenho não é a mesma coisa que demonstrar confiabilidade.

Esse princípio conecta perfeitamente Hou a Fan.
19. Outros problemas que Hou identifica
Além de avaliação, Hou chama atenção para:
Dependência dos dados: a qualidade, diversidade e quantidade dos dados afetam diretamente os resultados. arXiv
Contaminação de benchmarks: partes dos dados de avaliação podem ter aparecido no treinamento do modelo, inflando o resultado. arXiv
Ambiguidade: um modelo pode produzir código sintaticamente correto, mas funcionalmente incorreto quando o requisito é ambíguo. arXiv
Generalização: resultados obtidos em um projeto/dataset podem não permanecer iguais em outro. arXiv
Interpretabilidade e confiança: não é suficiente receber um resultado; para certos usos, precisamos compreender e validar por que aquela solução foi produzida. arXiv
20. Fan × Hou: como pensar nos dois juntos
	Fan et al.	Hou et al.
Tipo	Survey + problemas em aberto	Systematic Literature Review
Foco	O que LLMs podem fazer e quais desafios permanecem	O que 395 estudos da literatura mostram
Ênfase	Confiabilidade, hallucination, testes, hibridização	Modelos, datasets, técnicas, tarefas e métricas
Aplicações	Percorre várias atividades de SE	Classifica 85 tarefas
Grande problema	Resultado plausível ≠ resultado correto	Benchmark/métrica ≠ garantia de desempenho real
Mensagem	LLM + técnicas tradicionais de SE	Avaliar cada tarefa com metodologia adequada


Eles praticamente se encaixam:
           Hou
"O que a literatura fez?"
             ↓
     tarefas + métricas
             ↓
           Fan
"Mas como tornamos isso confiável?"
             ↓
 testes + validação + processos híbridos

21. O que eu levaria para a sua L0
Sem assumir detalhes de Fila Clara que não foram fornecidos aqui, há uma combinação especialmente forte e fácil de defender.
Para Fan, eu selecionaria como aplicação geração de código assistida por LLM e, como problema de confiabilidade, alucinação/correção do código gerado. O artigo sustenta diretamente a decisão de não aceitar código produzido pelo LLM sem mecanismos externos de verificação, especialmente execução e testes. Isso aparece na Introdução (§I), Scientific Evaluation (§IV-D), Open Problems (§IV-E) e Hybridisation/Thorough Testing (§XII-C e XII-F). arXiv
Para Hou, eu também usaria code generation como tarefa, porque deixa os dois textos conectados. A tarefa aparece em §6.4 Software Development, e sua avaliação é discutida de maneira geral em §5.3 Evaluation Metrics e concretamente em §6.4 com benchmarks e Pass@k. Mais importante: Hou alerta em §8.1.3 que uma única métrica pode não capturar robustez, interpretabilidade e falhas específicas. arXiv
22. O aprendizado que realmente importa
Se você esquecer nomes de modelos, números e benchmarks, guarde esta cadeia:
LLM gera algo plausível
        ↓
Plausível não significa correto
        ↓
Precisamos de um critério verificável
        ↓
testes / execução / análise / revisão
        ↓
medimos o resultado
        ↓
repetimos para lidar com não determinismo
        ↓
validamos no contexto real do projeto

Isso resume muito bem a interseção dos dois surveys.
E há uma segunda ideia igualmente importante:
Os artigos são evidência sobre o estado da pesquisa em 2023–início de 2024, não evidência automática sobre a capacidade de um produto ou modelo específico em outubro de 2026.

O próprio escopo de Hou termina em janeiro de 2024, e Fan é de 2023. Portanto, para a L0, eles fundamentam princípios de Engenharia de Software para uso e avaliação de LLMs, não uma afirmação como “o modelo X de 2026 possui Y% de precisão”. arXiv
Se você quiser transformar isso posteriormente no fichamento de até 400 palavras, a base conceitual mais forte já está aqui: Fan → geração + alucinação + validação híbrida; Hou → geração + Pass@k/métricas + necessidade de avaliação contextualizada.