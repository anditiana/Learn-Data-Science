word = "excelent"
print(word)
#change to uppercase
word = word.upper()
print(word)

#change to lowercase
word = word.lower()
print(word)

#how to delete whitespace or other char or word
#if whitescape on right use .rstrip()
#if whitespace on left use .lstrip()
#if want to delete on both side use strip()
#if want to delete a char or word use variable.strip('word wan to delete') this only work if the word only in start
#or end of line.
greeting = "good morning folks 123"
#i want to delete 123 from greeting
print(greeting.strip(" 123 "))


#join string
print(' '.join(['Hello','World','Happy','Holiyay']))

#to split string
print('Hello world happy fasting'.split())
#this method split string into some string and save into list

#to change specific char or word
word3 = "burger, i burger like sandwich and burger"
print(word3.replace("burger", "Pizza"))