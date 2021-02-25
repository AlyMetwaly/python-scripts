def sort_words(phrase):
	#split the words
	words = phrase.split()
	print(words)
	#append a lowercase version of the word for each word
	words = [w.lower() + w for w in words]
	print(words)
	words.sort()
	words = [w[len(w)/2:] for w in words]
	print(words)
	return ' '.join(words)

if __name__ == '__main__':
	print(sort_words('cat dog RABBIT'))