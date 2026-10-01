# Parte Teórica: Análise e Discussão

**Projeto:** Meu Sistema Operacional Pessoal: Utilizando IA para Gerenciar Tempo, Comunicação e Produtividade
**Disciplina:** Produtividade e Gestão do Tempo, UniFECAF, 2º semestre
**Aluno:** Kennedy Pereira

**Links do projeto:**

- Vídeo pitch: https://youtu.be/X9Nvlp9Ii6c
- Repositório (GitHub): https://github.com/Kenny-Barra/sistema-operacional-pessoal
- Painel (dashboard): https://claude.ai/artifact/JZHFT2irWLy7iPYgsBy9dC
- Base no Airtable: https://airtable.com/appcEBvt6c792Oi5F/shrqILXXOTvyHHImJ

---

## 1. Diagnóstico da minha rotina

Trabalho como analista de IA e Automação, de forma presencial, das 9h às 18h. Também curso IA e Automação na UniFECAF, a distância. Antes deste trabalho, meu dia era mais ou menos assim:

| Horário | O que eu fazia |
|---|---|
| Manhã | Acordar e ir para o trabalho |
| 9h às 18h | Expediente presencial |
| Depois do trabalho | Academia |
| À noite | Voltar para casa, estudar quando dava, tomar banho e dormir |

O único compromisso fixo que eu tinha era a academia, e ela sempre funcionou bem. O resto ficava na cabeça. Eu não usava nenhuma ferramenta para me organizar, então as coisas da faculdade, do trabalho e da vida pessoal ficavam na memória ou perdidas em conversas de WhatsApp e e-mail.

Quando parei para fazer esse diagnóstico, percebi três coisas. A primeira é que eu não sabia quantas horas estudava por semana, então não tinha como saber se era pouco ou muito. A segunda é que o estudo sempre ficava com o que sobrava do dia, depois do trabalho e da academia, quando eu já estava sem energia, sem horário certo e sem saber direito o que ia estudar. A terceira é que eu lembrava dos prazos tarde. Sem uma lista, os trabalhos da faculdade só ganhavam atenção perto da data de entrega.

## 2. Principais desafios de produtividade

| Desafio | Como aparece no dia a dia | O que causa |
|---|---|---|
| Procrastinação | Deixar o estudo e os trabalhos para depois, principalmente à noite | Tarefas acumulando perto do prazo |
| Cansaço | Chegar na hora de estudar depois de 9 horas de trabalho e da academia | Pouca concentração, e às vezes o estudo nem começa |
| Falta de organização | Nenhuma ferramenta, tudo na memória | Esquecimentos e a sensação de estar sempre devendo alguma coisa |
| Celular | Redes sociais e notificações durante o estudo | Foco quebrado |
| Saúde mental | Ansiedade e estresse | Menos energia e mais procrastinação |

Olhando a tabela, percebi que esses problemas estão ligados. Quando estou cansado, eu adio. As tarefas acumulam, a ansiedade aumenta, durmo pior e no dia seguinte tenho menos energia ainda. Por isso eu sabia que uma lista de tarefas sozinha não ia resolver. O sistema precisava facilitar o começo das tarefas, cuidar da minha energia e tirar as coisas da minha cabeça.

Sobre comunicação, não tenho grandes problemas, mas no trabalho as mensagens chegam o dia todo por vários canais. Responder tudo na hora atrapalha quando preciso me concentrar.

## 3. Métodos utilizados

Usei quatro métodos, e cada um foi escolhido por causa de um problema do diagnóstico.

### 3.1 GTD (Getting Things Done)

O GTD, de David Allen, parte da ideia de que a cabeça serve para ter ideias e não para guardar tarefas. Era exatamente o meu problema. Usei três partes do método. Toda tarefa nova é anotada no Airtable com o status "Caixa de entrada" (captura). Depois cada uma recebe área, prazo, estimativa de tempo e um próximo passo concreto (organização). E todo domingo às 19h faço uma revisão da semana, que fica registrada numa tabela própria (revisão).

### 3.2 Matriz de Eisenhower

Para decidir o que fazer primeiro, marco cada tarefa como urgente, importante, as duas coisas ou nenhuma. Uma fórmula no Airtable coloca a tarefa no quadrante certo automaticamente:

| | Urgente | Não urgente |
|---|---|---|
| Importante | 1. Fazer agora | 2. Agendar |
| Não importante | 3. Delegar ou limitar | 4. Eliminar |

A ideia é passar mais tempo no quadrante 2, das coisas importantes que ainda não são urgentes. É onde estão o trabalho da faculdade com prazo em 15/10, as aulas, a academia e o sono. Se eu faço essas tarefas com antecedência, elas não viram correria depois.

### 3.3 Técnica Pomodoro

O Pomodoro, criado por Francesco Cirillo, divide o trabalho em blocos de 25 minutos de foco com 5 minutos de pausa, e uma pausa maior de 15 minutos a cada 4 blocos. Escolhi essa técnica por causa do cansaço. Coloquei uma meta pequena de propósito: 2 Pomodoros por noite. Começar 25 minutos cansado é bem mais fácil do que pensar em "estudar a noite toda". Também passei a estimar as tarefas em Pomodoros, e assim consigo medir quanto estudo, coisa que eu não sabia antes.

### 3.4 Blocos de tempo (time blocking)

Coloquei os compromissos fixos na agenda da semana: trabalho, academia, um intervalo sem tela antes de estudar, estudo de segunda a quinta às 20h30, um estudo mais longo no sábado de manhã, a revisão de domingo e o horário de desligar as telas às 22h30. A sexta à noite ficou livre de propósito, porque descanso também precisa estar planejado.

### 3.5 Regra dos 2 minutos

Junto com o GTD, cada tarefa tem um campo chamado "Próximo passo (2 min)". É uma ação tão pequena que dá para fazer na hora, como "abrir o AVA e dar play na primeira aula pendente". Percebi que o mais difícil para mim é começar, e depois que começo eu geralmente continuo.

## 4. Ferramentas escolhidas e por quê

| Ferramenta | Para que uso | Por que escolhi |
|---|---|---|
| Airtable | Centro do sistema: tarefas, agenda, check-in diário, revisão semanal e biblioteca de prompts | Já usei em outro trabalho da faculdade (ONG Vida Plena). Ele funciona como um banco de dados, tem fórmulas e automações e guarda os números do dia a dia para eu acompanhar a evolução |
| Google Agenda | Lembretes dos blocos de tempo no celular | Já uso no dia a dia. Os blocos da tabela Agenda foram exportados por um script para um arquivo .ics, que pode ser importado de uma vez, com aviso 10 minutos antes de cada bloco |
| Claude (IA) | Planejar, priorizar, quebrar tarefas grandes, escrever mensagens e revisar a semana | Trabalho com IA e já tenho familiaridade. Ele entende bem o contexto e responde em português, inclusive em tabela, o que facilita passar para o Airtable |
| Painel POS | Ver a semana numa tela só: indicadores, matriz, Pomodoro, agenda e evolução de energia e humor | O Airtable é bom para registrar, mas o painel junta tudo e tem um timer de Pomodoro ligado às tarefas |

Pensei em usar o Trello, que é muito bom para ver as tarefas em colunas (kanban). Mas ele não guarda com a mesma facilidade dados como energia, sono e quantidade de Pomodoros, e eu queria acompanhar esses números ao longo das semanas.

## 5. Como a IA ajudou na organização

Usei o Claude em cinco momentos. Os prompts ficam salvos na tabela "Prompts de IA" do Airtable e na pasta `prompts/` do projeto, assim não preciso escrever tudo de novo toda vez.

1. **Planejamento da semana.** No domingo, mando para o Claude a lista de tarefas com prazos e estimativas. Ele classifica na Matriz de Eisenhower, distribui as tarefas nos horários de estudo sem passar do tempo que eu realmente tenho e sugere as 3 prioridades da semana.
2. **Classificação rápida.** Quando aparece uma tarefa nova no meio da semana, um prompt curto me diz se ela é urgente e/ou importante, com uma frase explicando.
3. **Quando eu travo.** Peço para o Claude dividir a tarefa em até 5 passos de um Pomodoro cada, sendo que o primeiro precisa caber em 2 minutos. Os textos do campo "Próximo passo" das tarefas foram feitos assim.
4. **Mensagens de trabalho.** Uso um prompt que reescreve a mensagem com contexto, pedido, prazo e próximo passo, numa versão para WhatsApp e outra para e-mail.
5. **Revisão da semana e estudo.** O Claude lê meus check-ins e as tarefas da semana, resume como foi, mostra padrões (por exemplo, a relação entre sono e foco) e sugere no máximo dois ajustes. Também uso para fazer resumos de uma página das aulas.

Também usei a IA para montar o próprio sistema. Ela me ajudou a pensar nas tabelas, a escrever a fórmula da matriz, a gerar o arquivo da agenda e a criar o painel.

Tomo alguns cuidados nesse uso. A IA sugere, mas quem decide sou eu, e reviso as classificações antes de aceitar. Também não coloco informações confidenciais da empresa nem dados de outras pessoas. Para tarefas do trabalho, uso descrições genéricas.

Além da IA, configurei uma automação no Airtable: todo domingo às 19h ela cria o registro da revisão semanal. Assim a revisão não depende de eu lembrar.

## 6. Estratégias para comunicação, procrastinação e saúde mental

### 6.1 Comunicação

- Responder mensagens e e-mails em três horários fixos (9h15, 13h30 e 17h15), com as notificações silenciadas no resto do tempo. Assim ninguém fica sem resposta e eu não sou interrompido o dia todo.
- Usar o prompt de mensagem profissional para que cada mensagem já tenha contexto, pedido e prazo, evitando várias idas e vindas.
- Pedir a pauta antes das reuniões ou resolver por mensagem quando a reunião não for necessária.

### 6.2 Procrastinação

- Começar pequeno, com a meta mínima de 2 Pomodoros e o próximo passo de 2 minutos em cada tarefa.
- Não precisar decidir na hora. O horário de estudo já está na agenda e a tarefa da noite foi escolhida no domingo, então à noite eu só executo.
- Deixar os aplicativos de redes sociais fora da tela inicial do celular durante o estudo.
- Dividir entregas grandes. O trabalho com prazo em 15/10 foi separado em três partes, uma por semana, para não ficar tudo para os últimos dias.

### 6.3 Saúde mental e bem-estar

Essa foi a parte mais difícil de escrever. Tenho lidado com ansiedade e estresse, e entendi que não adianta ser produtivo se a saúde não acompanha. O que coloquei no sistema:

- A academia virou compromisso que não sai da agenda, porque é o que mais me ajuda a aliviar o estresse.
- Telas desligadas às 22h30 e celular fora do quarto, com meta de 7 horas de sono.
- Um intervalo sem tela entre a academia e o estudo, e as pausas do Pomodoro longe do celular.
- Um check-in de 1 minuto por dia, anotando energia, humor, sono e hábitos. Assim consigo ver no papel o que antes era só sensação e perceber quando a semana está pesada.
- Sexta à noite e parte do fim de semana livres.
- Coloquei no próprio sistema a tarefa de procurar acompanhamento psicológico, pelo plano de saúde, pelo SUS ou pela faculdade. Ferramenta ajuda a organizar a rotina, mas não substitui esse cuidado.

## 7. Primeiros resultados e próximos passos

Comecei a usar o sistema em 30/09/2026. Os dias 28 e 29/09 entraram como ponto de partida, com valores que estimei a partir da rotina que eu tinha antes. No primeiro dia de uso fiz este trabalho em 5 Pomodoros, sem procrastinar, sabendo exatamente o que precisava entregar.

O que já percebi de diferença:

- Tudo está num lugar só e com prioridade definida. Aquela sensação de estar esquecendo alguma coisa diminuiu bastante.
- Pela primeira vez consigo medir quanto estudo, contando os Pomodoros.
- Com o próximo passo já escrito, fica mais fácil começar mesmo cansado.
- Saúde, sono e descanso entraram na agenda junto com trabalho e estudo.

Nas próximas semanas vou acompanhar no painel a quantidade de Pomodoros de estudo (meta de 12 por semana), os dias sem procrastinar, a média de energia e humor e as horas de sono. A revisão de domingo com o Claude vai usar esses dados para ir ajustando o sistema conforme a rotina mudar.

## 8. Conclusão

Com este trabalho percebi que o que me faltava não era tempo nem conhecimento técnico. Faltava um sistema, e faltava energia na hora em que eu deixava para estudar. Juntando métodos conhecidos (GTD, Eisenhower, Pomodoro e blocos de tempo), ferramentas simples (Airtable e Google Agenda) e a IA como apoio no planejamento e na comunicação, minha organização parou de depender só da memória e da força de vontade. Usada com cuidado, a tecnologia tirou peso da minha cabeça e deixou mais espaço para estudar, trabalhar bem e cuidar da saúde.

## Referências

ALLEN, David. *A arte de fazer acontecer: o método GTD (Getting Things Done)*. Rio de Janeiro: Sextante, 2016.

AIRTABLE. *Airtable Support*. Disponível em: https://support.airtable.com. Acesso em: 30 set. 2026.

ASANA. *Asana Academy*. Disponível em: https://academy.asana.com. Acesso em: 30 set. 2026.

CIRILLO, Francesco. *The Pomodoro Technique*. Berlim: FC Garage, 2006.

COVEY, Stephen R. *Os 7 hábitos das pessoas altamente eficazes*. Rio de Janeiro: BestSeller, 2017.

NOTION. *Notion Guides*. Disponível em: https://www.notion.so/help. Acesso em: 30 set. 2026.

TRELLO. *Trello Guide*. Disponível em: https://trello.com/guide. Acesso em: 30 set. 2026.

UNIFECAF. *Produtividade e Gestão do Tempo*: conteúdos sobre gestão do tempo, comunicação, saúde mental e bem-estar no trabalho. Material da disciplina, 2026.
