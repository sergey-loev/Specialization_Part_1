main_menu = '''\nГлавное меню:
		1. Открыть файл
		2. Записать файл
		3. Показать заметки
		4. Показать заметки по дате
		5. Добавить заметку
		6. Найти заметку
		7. Изменить заметку
		8. Удалить заметку           
		0. Выход\n '''

input_choice = 'Выберите пункт меню: '
load_successful = 'Заметки успешно открыты'
save_successful = 'Заметки успешно сохранены'
load_error = 'Заметок нет или они не прочитаны'
load_is_open = 'Файл заметок уже открыт'
input_new_note = 'Введите данные новой заметки: '
new_notes = {'title': 'Введите заголовок заметки: ', 'note': 'Введите текст заметки: '}
cancel_input = 'Отмена ввода'
index_del_note = 'Введите индекс заметки, которую хотите удалить: '
input_change = 'Какую заметку хотите изменить: '
input_index = 'Введите индекс заметки: '
change_note = 'Введите новые данные или оставьте поле пустым, чтобы не менять: '
input_search = 'Какую заметку хотите найти? '
input_date_search = 'За какую дату получить заметки? (dd.mm.YYYY)'

def new_note_successful(note):
	id = note['id']
	datetime = note['datetime']
	title = note['title']
	note = note['note'] 
	return f'Заметка [{id:>3} | {datetime:<20} | {title:<20} | {note:<20}] успешно добавлена!'

def del_note(title):
	return f'Заметка [{title}] успешно удалёна!'

def change_successful(note):
    
	id = note['id']
	datetime = note['datetime']
	title = note['title']
	note = note['note']    
	return f'Заметка [{id:>3} | {datetime:<20} | {title:<20} | {note:<20}] успешно изменена!'
    

def empty_search(word) -> str:
    return f'Заметки содержащие слово ["{word}"] не найдены!'