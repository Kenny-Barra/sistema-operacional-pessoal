# -*- coding: utf-8 -*-
"""Gera agenda-pos.ics com os blocos fixos do Sistema Operacional Pessoal.

Importar no Google Agenda: Configurações > Importar e exportar > Importar.
"""
from datetime import datetime, timezone
from pathlib import Path

TZ = "America/Sao_Paulo"
INICIO = "20261001"  # primeira semana de uso completo

# (título, descrição, dias RRULE, hora início, hora fim)
BLOCOS = [
    ("Expediente (presencial)", "Mensagens em 3 janelas: 09:15, 13:30 e 17:15.", "MO,TU,WE,TH,FR", "0900", "1800"),
    ("Academia", "Compromisso fixo: principal regulador de estresse e ansiedade.", "MO,TU,WE,TH,FR", "1830", "1930"),
    ("Jantar e descompressão (sem tela)", "Transição antes do estudo.", "MO,TU,WE,TH,FR", "1945", "2030"),
    ("Estudo: 2 Pomodoros", "2 x (25 min foco + 5 min pausa). Comece pelo 'próximo passo de 2 min' da tarefa.", "MO,TU,WE,TH", "2030", "2125"),
    ("Estudo longo: 4 Pomodoros", "Aulas atrasadas e trabalhos da faculdade.", "SA", "0930", "1130"),
    ("Revisão semanal + planejamento com IA", "Revisão GTD no Airtable + prompts 'Revisão semanal' e 'Planejamento semanal' no Claude.", "SU", "1900", "1930"),
    ("Desligar telas e check-in diário", "Check-in de 1 minuto no Airtable e celular fora do quarto.", "MO,TU,WE,TH,FR,SA,SU", "2230", "2300"),
]
UNICOS = [
    ("ENTREGA: trabalho da faculdade (prazo 15/10)", "20261015"),
]

DIA_SEMANA = {"MO": 0, "TU": 1, "WE": 2, "TH": 3, "FR": 4, "SA": 5, "SU": 6}


def primeira_data(dias: str) -> str:
    """Primeira data >= INICIO que cai num dos dias da regra (o Google exige DTSTART coerente)."""
    d0 = datetime.strptime(INICIO, "%Y%m%d")
    alvo = {DIA_SEMANA[d] for d in dias.split(",")}
    from datetime import timedelta
    for i in range(7):
        d = d0 + timedelta(days=i)
        if d.weekday() in alvo:
            return d.strftime("%Y%m%d")
    return INICIO


def main() -> None:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    linhas = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//POS Kennedy//Sistema Operacional Pessoal//PT-BR",
              "CALSCALE:GREGORIAN", "X-WR-CALNAME:POS - Sistema Operacional Pessoal", f"X-WR-TIMEZONE:{TZ}"]
    for n, (titulo, desc, dias, ini, fim) in enumerate(BLOCOS, 1):
        data = primeira_data(dias)
        linhas += ["BEGIN:VEVENT", f"UID:pos-bloco-{n}@kennedy-pos", f"DTSTAMP:{stamp}",
                   f"DTSTART;TZID={TZ}:{data}T{ini}00", f"DTEND;TZID={TZ}:{data}T{fim}00",
                   f"RRULE:FREQ=WEEKLY;BYDAY={dias}", f"SUMMARY:{titulo}", f"DESCRIPTION:{desc}",
                   "BEGIN:VALARM", "TRIGGER:-PT10M", "ACTION:DISPLAY", f"DESCRIPTION:{titulo}", "END:VALARM",
                   "END:VEVENT"]
    for n, (titulo, data) in enumerate(UNICOS, 1):
        linhas += ["BEGIN:VEVENT", f"UID:pos-entrega-{n}@kennedy-pos", f"DTSTAMP:{stamp}",
                   f"DTSTART;VALUE=DATE:{data}", f"SUMMARY:{titulo}",
                   "BEGIN:VALARM", "TRIGGER:-P3D", "ACTION:DISPLAY", f"DESCRIPTION:{titulo}", "END:VALARM",
                   "END:VEVENT"]
    linhas.append("END:VCALENDAR")
    saida = Path(__file__).with_name("agenda-pos.ics")
    saida.write_text("\r\n".join(linhas) + "\r\n", encoding="utf-8")
    print("Gerado:", saida, "-", len(BLOCOS) + len(UNICOS), "eventos")


if __name__ == "__main__":
    main()
