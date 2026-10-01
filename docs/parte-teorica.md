# Parte Teórica – Análise e Discussão

**Projeto:** Meu Sistema Operacional Pessoal: Utilizando IA para Gerenciar Tempo, Comunicação e Produtividade
**Disciplina:** Produtividade e Gestão do Tempo – UniFECAF, 2º semestre
**Aluno:** Kennedy Pereira

**Links do projeto:**

- Vídeo pitch: https://youtu.be/X9Nvlp9Ii6c
- Repositório (GitHub): https://github.com/Kenny-Barra/sistema-operacional-pessoal
- Painel (dashboard): https://claude.ai/artifact/JZHFT2irWLy7iPYgsBy9dC
- Base no Airtable: https://airtable.com/appcEBvt6c792Oi5F/shrqILXXOTvyHHImJ

---

## 1. Diagnóstico da rotina atual

Trabalho como **analista de IA e Automação**, em regime **presencial, das 09h às 18h**, e curso **IA e Automação na UniFECAF** a distância. Antes deste projeto, meu dia típico seguia esta sequência:

| Horário aproximado | Atividade |
|---|---|
| Manhã | Acordar e ir para o trabalho |
| 09h – 18h | Expediente presencial |
| Depois do trabalho | Academia |
| Noite | Voltar para casa, estudar "quando dava", banho e dormir |

A rotina tinha uma única âncora fixa: a **academia**, que funciona bem e que eu mantenho com regularidade. Todo o resto era feito "de cabeça". Eu **não usava nenhuma ferramenta de organização**: as tarefas da faculdade, do trabalho e da vida pessoal ficavam na memória ou espalhadas em conversas de WhatsApp e e-mails.

Ao montar o diagnóstico, percebi três pontos importantes:

1. **Eu não sabia quantas horas estudava por semana.** Sem medição, não havia como saber se o tempo de estudo era suficiente nem como melhorá-lo.
2. **O estudo ficava com a "sobra" do dia.** Ele acontecia depois do trabalho e da academia, no momento de menor energia, sem horário definido e sem um objetivo claro para a sessão.
3. **Prazos eram lembrados tarde.** Sem uma lista central, o trabalho da faculdade só ganhava atenção quando o prazo já estava próximo, o que gerava acúmulo e pressão.

## 2. Principais desafios de produtividade identificados

| Desafio | Como aparece na rotina | Consequência |
|---|---|---|
| **Procrastinação** | Adiar o estudo e os trabalhos da faculdade, principalmente à noite | Acúmulo de tarefas perto do prazo |
| **Cansaço** | Chegar ao momento de estudo depois de 9h de trabalho e da academia | Pouca concentração e sessões que não começam |
| **Falta de sistema** | Nenhuma ferramenta; tudo na memória | Esquecimento, sensação de "estar devendo algo" o tempo todo |
| **Interrupções digitais** | Celular e redes sociais durante o estudo | Foco fragmentado |
| **Saúde mental** | Ansiedade e estresse, com fases de desânimo | Energia baixa, mais procrastinação, ciclo que se retroalimenta |

O ponto central do diagnóstico é que **procrastinação, cansaço e ansiedade formam um ciclo**: o cansaço faz adiar; o adiamento gera acúmulo; o acúmulo aumenta a ansiedade; a ansiedade piora o sono e a energia; e com menos energia, adia-se ainda mais. Por isso o sistema não poderia ser só uma lista de tarefas. Ele precisava **reduzir o esforço de começar**, **proteger a energia** e **tirar a carga mental da cabeça**.

Sobre comunicação, o desafio é menor, mas existe: no trabalho, mensagens chegam o dia inteiro por vários canais, e responder tudo na hora interrompe o trabalho profundo.

## 3. Métodos utilizados

O sistema combina quatro métodos, cada um escolhido para atacar um desafio específico do diagnóstico:

### 3.1 GTD – Getting Things Done (David Allen)

**Problema que resolve:** tudo na memória.
O GTD parte da ideia de que a mente serve para ter ideias, não para guardá-las. Apliquei três etapas do método:

- **Capturar:** toda tarefa nova entra na tabela *Tarefas* com status *Caixa de entrada*.
- **Esclarecer e organizar:** cada tarefa recebe área, prazo, estimativa e um **próximo passo concreto**.
- **Revisar:** todo domingo às 19h faço a **Revisão Semanal**, registrada numa tabela própria.

### 3.2 Matriz de Eisenhower

**Problema que resolve:** decidir o que fazer primeiro sem gastar energia com isso.
Cada tarefa é marcada como *Urgente* e/ou *Importante*, e uma fórmula no Airtable calcula o quadrante automaticamente:

| | Urgente | Não urgente |
|---|---|---|
| **Importante** | 1. Fazer agora | 2. Agendar |
| **Não importante** | 3. Delegar / limitar | 4. Eliminar |

O objetivo é deslocar o tempo para o **quadrante 2** (importante e não urgente), onde estão o trabalho com prazo em 15/10, as aulas, a saúde e o sono. Quando essas tarefas são feitas com antecedência, elas não viram urgências no quadrante 1.

### 3.3 Técnica Pomodoro (Francesco Cirillo)

**Problema que resolve:** cansaço e procrastinação na hora de estudar.
Ciclos de **25 minutos de foco e 5 de pausa**, com pausa longa de 15 minutos a cada 4 ciclos. A decisão mais importante foi definir uma **meta mínima pequena: 2 Pomodoros por noite**. Começar 25 minutos, mesmo cansado, é muito mais fácil do que "estudar a noite toda". Cada tarefa é estimada em Pomodoros, o que também mede o tempo de estudo, resolvendo o problema de "não saber quanto estudo".

### 3.4 Time blocking (blocos de tempo)

**Problema que resolve:** estudo sem horário.
Os compromissos fixos viraram blocos na agenda semanal: trabalho, academia, um bloco de **descompressão sem tela** antes do estudo, estudo de segunda a quinta às 20h30, estudo longo no sábado de manhã, revisão semanal no domingo e **horário de desligar as telas** às 22h30. Sexta à noite fica livre de propósito: descanso também é planejado.

### 3.5 Regra dos 2 minutos

Complementa o GTD: toda tarefa tem um campo **"Próximo passo (2 min)"**, uma ação tão pequena que pode ser feita imediatamente (por exemplo, "abrir o AVA e dar play na primeira aula pendente"). A procrastinação costuma estar no início da tarefa, não nela inteira.

## 4. Ferramentas escolhidas e justificativa

| Ferramenta | Papel no sistema | Justificativa |
|---|---|---|
| **Airtable** | Núcleo do sistema: tarefas, agenda, check-in diário, revisão semanal e biblioteca de prompts | Já uso a ferramenta (projeto da ONG Vida Plena); funciona como banco de dados, com fórmulas (quadrante automático), visualizações e **automações nativas**. É mais estruturado que o Trello e permite medir dados ao longo do tempo |
| **Google Agenda** | Lembretes dos blocos de tempo no celular | Já uso no dia a dia; os blocos da tabela *Agenda* foram exportados por script para um arquivo `.ics`, que entra no Google Agenda de uma vez, com alerta 10 minutos antes de cada bloco |
| **Claude (IA)** | Planejamento, priorização, quebra de tarefas, comunicação e revisão | Trabalho com IA; o Claude entende contexto longo e responde em português com tabelas, o que facilita levar o resultado para o Airtable |
| **Painel POS (dashboard web)** | Visão consolidada: indicadores, Matriz de Eisenhower, Pomodoro, agenda semanal e evolução de energia e humor | O Airtable é ótimo para registrar, mas o painel mostra a semana numa tela só e inclui um timer de Pomodoro ligado às tarefas |

O Trello foi considerado, mas descartado: ele é ótimo para fluxo visual (kanban), mas não mede hábitos, energia e Pomodoros com a mesma facilidade, e eu queria **dados** para acompanhar a evolução.

## 5. Como a IA foi utilizada para apoiar a organização

A IA entrou em cinco pontos do sistema. Os prompts estão salvos na tabela *Prompts de IA* do Airtable e na pasta `prompts/` do projeto, para serem reutilizados sem precisar escrever do zero:

1. **Planejamento semanal:** no domingo, envio ao Claude as tarefas da caixa de entrada com prazos e estimativas. Ele classifica na Matriz de Eisenhower, distribui as tarefas nos blocos de estudo **sem passar da capacidade real da semana** e sugere um Top 3.
2. **Classificação rápida:** para tarefas novas no meio da semana, um prompt curto devolve "urgente/importante" com uma justificativa de uma frase.
3. **Combate à procrastinação:** quando travo numa tarefa, o prompt "Destravar" quebra a tarefa em até 5 passos de 1 Pomodoro, com o primeiro passo executável em 2 minutos. Os textos do campo *Próximo passo* das tarefas foram gerados assim.
4. **Comunicação profissional:** reescrita de mensagens com contexto, pedido claro, prazo e próximo passo, em versão para WhatsApp e para e-mail.
5. **Revisão semanal e estudo:** o Claude lê os check-ins diários e as tarefas da semana, resume a semana, aponta padrões (por exemplo, a relação entre sono e foco) e sugere no máximo dois ajustes. Também faz fichamentos de 1 página das aulas.

A IA também foi usada para **construir** o sistema: o Claude me ajudou a modelar as tabelas, escrever a fórmula do quadrante, gerar o arquivo da agenda e montar o painel.

**Uso consciente.** A IA **sugere** e eu **decido**. Os prompts pedem respostas curtas e práticas, e eu reviso cada classificação antes de aceitar. Não envio dados sensíveis de terceiros nem informações confidenciais do trabalho; para tarefas do trabalho, uso descrições genéricas.

### Automação

Além do uso direto da IA, o Airtable tem uma **automação semanal**: todo domingo às 19h ela cria o registro da revisão semanal com status *Planejada*. Assim, o ritual de revisão não depende de eu lembrar.

## 6. Estratégias para melhorar comunicação, reduzir procrastinação e preservar a saúde mental

### 6.1 Comunicação

- **Janelas de mensagens:** responder mensagens e e-mails em três janelas fixas (09h15, 13h30 e 17h15), com notificações silenciadas fora delas. Isso reduz interrupções sem deixar ninguém sem resposta.
- **Mensagens completas:** usar o prompt "Mensagem profissional" para que cada mensagem tenha contexto, pedido, prazo e próximo passo, o que reduz idas e vindas.
- **Reuniões com pauta:** pedir pauta antes ou resolver por mensagem quando a reunião não for necessária.

### 6.2 Procrastinação

- **Começar pequeno:** meta mínima de 2 Pomodoros e "próximo passo de 2 minutos" em cada tarefa.
- **Remover a decisão:** o horário de estudo já está na agenda e a tarefa da noite já foi escolhida no domingo. À noite eu só executo.
- **Reduzir gatilhos:** apps de redes sociais fora da tela inicial do celular durante o bloco de estudo.
- **Quebrar entregas grandes:** o trabalho com prazo em 15/10 foi dividido em três tarefas com prazos semanais, para não acumular na última semana.

### 6.3 Saúde mental e bem-estar

Este é o ponto mais sensível do diagnóstico. Tenho lidado com ansiedade e estresse, e entendi que **produtividade sem cuidado com a saúde não se sustenta**. As estratégias adotadas foram:

- **Proteger a academia** como compromisso inegociável, por ser o principal regulador de estresse da minha rotina.
- **Proteger o sono:** telas desligadas às 22h30 e celular fora do quarto, com meta de 7 horas.
- **Pausas sem tela:** bloco de descompressão entre a academia e o estudo, e pausas do Pomodoro longe do celular.
- **Check-in diário de 1 minuto:** registrar energia, humor, sono e hábitos. Isso torna visível o que antes era só sensação e ajuda a perceber padrões cedo.
- **Descanso planejado:** sexta à noite e parte do fim de semana livres.
- **Buscar apoio profissional:** incluí no próprio sistema a tarefa de buscar acompanhamento psicológico (plano de saúde, SUS ou serviço da faculdade), no quadrante "importante". Ferramentas organizam a rotina, mas não substituem o cuidado com a saúde mental.

## 7. Resultados iniciais e próximos passos

O sistema começou a ser usado em **30/09/2026**. Os dias 28 e 29/09 foram registrados como **linha de base**, com valores estimados a partir da rotina anterior. No primeiro dia de uso, o trabalho desta disciplina foi feito em **5 Pomodoros**, sem procrastinação e com mais clareza do que precisava ser entregue.

Os ganhos percebidos até aqui são:

- **Clareza:** todas as tarefas estão em um lugar só, com prioridade definida. A sensação de "estar esquecendo algo" diminuiu.
- **Medição:** pela primeira vez sei quanto estudo, em Pomodoros.
- **Início mais fácil:** com o próximo passo já escrito, começar exige menos energia.
- **Equilíbrio:** saúde, sono e descanso entraram na agenda com o mesmo peso dos compromissos de trabalho e estudo.

Para as próximas semanas, os indicadores a acompanhar no painel são: **Pomodoros de estudo por semana** (meta: 12), **dias sem procrastinação**, **média de energia e humor** e **horas de sono**. A Revisão Semanal com o Claude vai usar esses dados para ajustar o sistema, que deve evoluir com a rotina.

## 8. Conclusão

O principal aprendizado deste projeto é que meu problema não era falta de tempo nem de conhecimento técnico, e sim **falta de um sistema** e de **energia no momento certo**. Ao juntar métodos clássicos (GTD, Eisenhower, Pomodoro e time blocking), ferramentas simples (Airtable e Google Agenda) e a IA como assistente de planejamento e comunicação, a organização deixou de depender da memória e da força de vontade. A tecnologia, usada com consciência, serviu para **reduzir a carga mental** e abrir espaço para o que importa: aprender, trabalhar bem e cuidar da saúde.

## Referências

- ALLEN, David. *A arte de fazer acontecer: o método GTD – Getting Things Done*. Rio de Janeiro: Sextante, 2016.
- CIRILLO, Francesco. *The Pomodoro Technique*. Berlim: FC Garage, 2006.
- COVEY, Stephen R. *Os 7 hábitos das pessoas altamente eficazes*. Rio de Janeiro: BestSeller, 2017 (Matriz do tempo / Eisenhower).
- AIRTABLE. *Airtable Support: Automations e Formula field reference*. Disponível em: https://support.airtable.com.
- NOTION. *Notion Guides*. Disponível em: https://www.notion.so/help.
- TRELLO. *Trello Guide*. Disponível em: https://trello.com/guide.
- ASANA. *Asana Academy*. Disponível em: https://academy.asana.com.
- UNIFECAF. *Disciplina Produtividade e Gestão do Tempo*: conteúdos sobre Gestão do Tempo, Comunicação, Saúde Mental e Bem-Estar no Trabalho.
