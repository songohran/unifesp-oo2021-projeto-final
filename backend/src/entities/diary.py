from __future__ import annotations
from datetime import date
from typing import List


class Diary:
    def __init__(self, user_cpf: str, entries: List[DiaryEntry]) -> None:
        self.user_cpf = user_cpf
        self.entries = entries

    def __str__(self) -> str:
        return f'''Diary (
            \r\tuser_cpf: "{self.user_cpf}",
            \r\tentries: "{self.entries}"
        \r)'''

    def __repr__(self) -> str:
        return f'''Diary (
            \r\tuser_cpf: "{self.user_cpf}",
            \r\tentries: "{self.entries}"
        \r)'''

    def from_list(diaries_list: list) -> List[Diary]:
        '''
        Função que transforma uma lista genérica em uma lista da classe Diary
        '''
        diaries = []

        for diary in diaries_list:
            try:
                diaries.append(Diary.from_dict(diary))
            except:
                pass

        return diaries

    def to_list(diaries: List[Diary]) -> list:
        '''
        Função que transforma um lista da classe Diary em uma lista genérica
        '''
        diaries_list = []

        for diary in diaries:
            try:
                diaries_list.append(Diary.to_dict(diary))
            except:
                pass

        return diaries_list

    def from_dict(diary: dict) -> Diary:
        '''
        Função que transforma um dicionário genérico em um objeto da classe Diary
        '''
        return Diary(diary['user_cpf'], DiaryEntry.from_list(diary['entries']))

    def to_dict(self) -> dict:
        '''
        Função que transforma um objeto da classe Diary em um dicionário genérico
        '''
        return {
            'user_cpf': self.user_cpf,
            'entries': DiaryEntry.to_list(self.entries),
        }


class DiaryEntry:
    def __init__(self, date: date, content: str) -> None:
        self.date = date
        self.content = content

    def __str__(self) -> str:
        return f'''DiaryEntry (
            \r\tdate: "{self.date}",
            \r\tcontent: "{self.content}"
        \r)'''

    def __repr__(self) -> str:
        return f'''DiaryEntry (
            \r\tdate: "{self.date}",
            \r\tcontent: "{self.content}"
        \r)'''

    def from_list(entries_list: list) -> List[DiaryEntry]:
        '''
        Função que transforma uma lista genérica em uma lista da classe DiaryEntry
        '''
        entries = []

        for entry in entries_list:
            try:
                entries.append(DiaryEntry.from_dict(entry))
            except:
                pass

        return entries

    def to_list(entries: List[DiaryEntry]) -> list:
        '''
        Função que transforma um lista da classe DiaryEntry em uma lista genérica
        '''
        entries_list = []

        for entry in entries:
            try:
                entries_list.append(
                    DiaryEntry.to_dict(entry, date_to_str=True)
                )
            except:
                pass

        return entries_list

    def from_dict(entry: dict) -> DiaryEntry:
        '''
        Função que transforma um dicionário genérico em um objeto da classe DiaryEntry
        '''
        _date = str(entry['date'])
        _date = date.fromisoformat(_date)

        return DiaryEntry(_date, entry['content'])

    def to_dict(self, date_to_str: bool) -> dict:
        '''
        Função que transforma um objeto da classe DiaryEntry em um dicionário genérico
        '''
        date = str(self.date) if date_to_str else self.date

        return {
            'date': date,
            'content': self.content,
        }
