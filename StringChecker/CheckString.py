import random 
import string as single_letters



class CheckString():
	
	
	def __init__(self):
		self.words_list = []
		self.choosed_word = ''
		self.letter_list = []
		self.warn_message = "Your word was close!"
		self.char = single_letters.ascii_lowercase + single_letters.punctuation
		self.original_word = ''
		

	'''
	Chooses a random line in a txt file.
	Input is the name of the file.
	Output is a list[original line, cleaned line]
	'''
	def wordPicker(self, file = ''):
		word_list = open(file, 'r')
		for words in word_list:
			single_line = words.strip()
			line_list = single_line.split()
			self.words_list.append(line_list)
		random_word = random.choice(self.words_list)
		self.original_word = ' '.join(random_word)
		self.choosed_word = ''.join(random_word).lower()
		return self.original_word, self.choosed_word
		
	
	def _checkerTF(self, insert = [], rightone = ''):
		joined_word = ''.join(insert)
		if joined_word == rightone:
			return True
		else:
			return False
	
			
	'''
	Checks if your inserted word == the looked after word.
	If it dosnt match, itll check wheather the word misses one char, has one too much, or if a char got mixed up. It then returns a string depending on the outcome.
	'''
	def checkNow(self, insert = '', expected = ''):
		insert = insert.lower()
		insert = insert.replace(' ', '')
		expected = expected.lower()

		for x in insert:
			self.letter_list.append(x)
		backup_letter_list = tuple(self.letter_list)
		length_of_word_index = len(self.letter_list) - 1
		checker = CheckString()
		counter = 0
		
#Direct hit. returns 'True'
		if insert == expected:
			return 'True'
		else:

#One Letter too much. returns 'close:much'			
			for x in backup_letter_list:
				self.letter_list = list(backup_letter_list)
				self.letter_list.pop(counter)
				counter += 1
				if checker._checkerTF(self.letter_list, expected) is True:
					return 'close:much'
				else:
					continue
			counter = 0
			
#One mixed up letter. returns 'close:mixed'
			for x in backup_letter_list:
				self.letter_list = list(backup_letter_list)
				for j in self.char:
					self.letter_list[counter] = j
					if checker._checkerTF(self.letter_list, expected) is True:
						return 'close:mixed'
				counter += 1
			counter = 0
				
#One letter less. returns 'close:less'
			for x in range(0, len(backup_letter_list) + 1):
				for j in self.char:
					self.letter_list = list(backup_letter_list)
					self.letter_list.insert(x, j)
					if checker._checkerTF(self.letter_list, expected) is True:
						return 'close:less'
					else:
						continue
		
#Complete miss. returns 'False'
		return 'False'
		
		
	def hit(self, hite):
		if hite == 'True':
			print("Direct hit!")
		elif hite == 'False':
			print("Complete miss!")
		elif hite == 'close:less':
			print(self.warn_message, 'Your word misses one letter!')
		elif hite == 'close:mixed':
			print(self.warn_message, 'You mixed a letter up!')
		else:
			print(self.warn_message, 'One letter too much!')
			
				
				
if __name__ == '__main__':
	string_test = CheckString()
	both_words = string_test.wordPicker('words.txt')
	print(both_words)
	hit = string_test.checkNow(str(input('your word ')), ''.join(both_words[1]))
	string_test.hit(str(hit))
