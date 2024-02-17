import messages
import view
import notes

my_notes = notes.Notes()

def start():
	while True:
		choice = view.main_menu() 
		match choice:
			case 1: 
				result = my_notes.load_notes()
				if(result != -1):
					view.print_message(messages.load_successful)
				elif(result == -1):
					view.print_message(messages.load_is_open)
			case 2: 
				my_notes.save_notes()
				view.print_message(messages.save_successful)
			case 3: 
				notes = my_notes.get_notes()
				view.print_notes(notes, messages.load_error)
			case 4:
				date = view.input_date(messages.input_date_search)
				notes = my_notes.search_notes_by_date(date)
				view.print_notes(notes, messages.load_error)
			case 5: 
				note = view.input_notes(my_notes.get_max_id(), messages.input_new_note, messages.cancel_input)
				my_notes.add_note(note)
				view.print_message(messages.new_note_successful(note)) 
			case 6: 
				word = view.input_search(messages.input_search)
				result = my_notes.search_notes(word, messages.load_error)
				view.print_notes(result, messages.empty_search(word))
			case 7: 
				notes = my_notes.get_notes()
				index = view.input_index(messages.input_index, notes, messages.load_error)
				if(index != -1):	
					note = view.input_notes(index, messages.input_new_note, messages.cancel_input)
					result = my_notes.change_notes(note, index)
					view.print_message(messages.change_successful(note))
			case 8: 
				notes = my_notes.get_notes()
				index = view.input_index(messages.index_del_note, notes, messages.load_error)
				if(index != -1):	
					title = my_notes.del_note(index)
					view.print_message(messages.del_note(title)) 
			case 0:
				break