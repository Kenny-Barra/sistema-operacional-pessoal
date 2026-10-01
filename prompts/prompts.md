# Biblioteca de prompts (Claude)

Os mesmos prompts estão na tabela **Prompts de IA** do Airtable e no painel (botão *Copiar prompt*). Troque o texto entre colchetes antes de enviar.

| Prompt | Quando usar | Método que apoia |
|---|---|---|
| Planejamento semanal | Domingo, 19h | GTD + Eisenhower + time blocking |
| Classificar tarefa | Ao capturar uma tarefa nova | Eisenhower |
| Destravar: próximo passo de 2 minutos | Ao travar numa tarefa | Regra dos 2 minutos + Pomodoro |
| Mensagem profissional clara | Antes de enviar mensagem/e-mail importante | Comunicação |
| Fichamento de aula | Depois de assistir a uma aula | Estudo |
| Revisão semanal | Domingo, 19h | GTD (revisão) + bem-estar |

---

## 1. Planejamento semanal

```
Você é meu assistente de planejamento. Minha rotina fixa: trabalho presencial 09h-18h (seg-sex), academia 18h30-19h30, estudo 20h30-21h25 (seg-qui, 2 Pomodoros) e sábado 09h30-11h30 (4 Pomodoros). Abaixo estão minhas tarefas com prazo e estimativa em Pomodoros. 1) Classifique cada uma na Matriz de Eisenhower. 2) Distribua as tarefas dos quadrantes 1 e 2 nos blocos da semana sem passar da capacidade. 3) Liste o que deve ser eliminado ou adiado. 4) Escolha um Top 3 da semana. Responda em tabela.

TAREFAS:
[colar a exportação da view 'Caixa de entrada' do Airtable]
```

## 2. Classificar tarefa na Matriz de Eisenhower

```
Classifique a tarefa abaixo na Matriz de Eisenhower (urgente? importante?) considerando que meus objetivos são: entregar bem no trabalho, concluir a faculdade e cuidar da minha saúde. Responda só com: Urgente (sim/não), Importante (sim/não), Quadrante e uma frase de justificativa.

TAREFA: [descrever]
```

## 3. Destravar: próximo passo de 2 minutos

```
Estou procrastinando a tarefa abaixo e estou cansado. Quebre em no máximo 5 passos, cada um cabendo em 1 Pomodoro (25 min). O primeiro passo precisa ser tão pequeno que eu consiga fazer em 2 minutos agora. Seja direto e sem julgamentos.

TAREFA: [descrever]
```

## 4. Mensagem profissional clara

```
Reescreva a mensagem abaixo para o contexto profissional: tom cordial e direto, contexto em 1 frase, pedido claro, prazo e próximo passo. Máximo de 6 linhas. Me dê uma versão para WhatsApp e outra para e-mail.

MENSAGEM: [colar rascunho]
```

## 5. Fichamento de aula

```
Com base nas anotações/transcrição abaixo, faça um fichamento de 1 página: 5 ideias principais, 3 conceitos com definição curta, 1 exemplo prático ligado a IA e automação e 3 perguntas de revisão.

ANOTAÇÕES: [colar]
```

## 6. Revisão semanal

```
Abaixo estão meus check-ins diários (energia, humor, sono, academia, Pomodoros, procrastinação) e as tarefas concluídas e pendentes da semana. 1) Resuma a semana em 3 frases. 2) Aponte 1 padrão que liga energia/sono ao foco. 3) Sugira no máximo 2 ajustes para a próxima semana. 4) Se a carga estiver alta, diga o que cortar. Seja gentil e prático.

CHECK-INS: [colar]
TAREFAS: [colar]
```

## Exemplo real de uso

**Entrada (Destravar):** "Assistir às aulas da semana no AVA" (estimativa: 4 Pomodoros).

**Saída usada no Airtable:**
1. *(2 min)* Abrir o AVA e dar play na primeira aula pendente.
2. *(Pomodoro 1)* Assistir à primeira aula anotando 3 ideias.
3. *(Pomodoro 2)* Segunda aula, mesmo formato.
4. *(Pomodoro 3)* Terceira aula.
5. *(Pomodoro 4)* Colar as anotações no prompt "Fichamento de aula".

O passo 1 virou o campo **Próximo passo (2 min)** da tarefa.
