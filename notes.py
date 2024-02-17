from contextlib import suppress
from datetime import datetime
import os

class Notes:

    def __init__(self):
        self.notes: list[dict[str, str]] = []
        self.path = os.path.dirname(__file__) + "\\" + "data_file_notes.csv"
        self.is_open = False

    def load_notes(self):
        if(not self.is_open):
            with suppress(Exception):
                with open(self.path, 'r', encoding='UTF-8') as file:
                    data = file.readlines()
                    for note in data:
                        note = note.strip().split(';')
                        self.notes.append({'id': note[0], 'datetime': note[1], 'title': note[2], 'note': note[3]})
                    self.is_open = True
            return 0
        else:
            return -1
                        

    def save_notes(self):
        data = []
        for note in self.notes:
            data.append(';'.join([value for value in note.values()]))
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(data))

    def get_notes(self) -> list[dict[str, str]]:
        return self.notes

    def get_max_id(self) -> int:
        if self.notes:
            max_id = max(int(value['id']) for value in self.notes)+1
        else:
            max_id = 1
        return max_id

    def add_note(self, note: dict[str, str]):
        self.notes.append(note)

    def del_note(self, index: int):
        return self.notes.pop(index-1).get('title')

    def search_notes(self, word: str) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for note in self.notes:
            for field in note.values():
                if word.lower().strip() in field.lower().strip():
                    result.append(note)
                    break
        return result

    def search_notes_by_date(self, date) -> list[dict[str, str]]:
        result: list[dict[str, str]] = []
        for note in self.notes:
            date_note = datetime.strptime(note['datetime'], '%d-%m-%Y %H:%M:%S').date()       
            if date_note == date:
               result.append(note)
        return result

    def change_notes(self, note: dict[str, str], index: int):
      with suppress(Exception):
        if len(note['title']) > 0:
            self.notes[index-1]['title'] = note['title']
      with suppress(Exception):
        if len(note['note']) > 0:
            self.notes[index-1]['note'] = note['note']
      with suppress(Exception):
        self.notes[index-1]['datetime'] = note['datetime']
