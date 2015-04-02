def concept_html(e, sub_lesson):
	concept_title = e[0]
	concept_description = e[1]
	sub_lesson_print = str(sub_lesson)
	return generate_concept_html(concept_title, concept_description, sub_lesson_print)


def generate_concept_html(concept_title, concept_description, sub_lesson_print):
	concept_html_1 = '''
	<div id="lesson-''' + lesson + "-" + sub_lesson_print + '''">
		<h3>
	 		''' + concept_title
	concept_html_2 = '''
		</h3>
		<p>
	 		''' + concept_description
	concept_html_3 = '''
		</p>
	</div>'''
	full_concept_html = concept_html_1 + concept_html_2 + concept_html_3
	return full_concept_html


def lesson_html(input, lesson):
	full_html='''
<div class = "lesson-''' + lesson + '''">'''
	sub_lesson = 0
	for e in input:
		sub_lesson = sub_lesson + 1
		add_html = concept_html(e, sub_lesson)
		full_html = full_html + add_html
	full_html = full_html + '''
</div>'''
	return full_html


lesson = '4'
input=[['Programming','Programming is a core of computer science<br>A toaster is designed to do only one thing. A computer can be programmed to do anything. It is a universal machine.<br>A computer uses a precise series of steps. It can execute billions of steps in a second.'],['Python','Python is an interpreter. It takes what you input and translates is for a computer.'],['Why use programming languages?','In natural languages like English there is too much ambiguity. A computer cannot interpret this.<br>Natural languages are verbose.'],['Python expressions','Expressions are legal statements in Python.']]
print lesson_html(input, lesson)
lesson = '5'
input=[['Variables','Variables are names given to values. For example, you could assign "35" to the variable "my_age". The next time the variable "my_age" is mentioned, the computer knows that it equals 35.'],['Strings', 'Strings are specific lines of text. They are assigned to variables, just like numbers are. For example, a variable could contain the text "This is an example of a string." Strings can be assigned by putting the text into either single or double quotation marks.']]
print lesson_html(input, lesson)
lesson = '6'
input = [['What are functions (procedures)?','Functions/procedures take input and then do something with the input to produce output. For example, if you want the function to add two numbers together, you would input the two numbers and then the function would work its magic to output the sum of the numbers.'],['Using paramaters to define the output of a function','To make a function that simply adds two numbers together and outputs the sum, you could do this:<br>def sum(x,y): <br><span class="indent">answer = x + y</span> <br><span class="indent">return answer</span><br>This returns (outputs) x + y. You could also just code it like this:<br>def sum(x,y): <br><span class="indent">return x + y</span><br>That would also return (output) x + y.<br>You must use a return statement. Otherwise, the function will not define an output.']]
print lesson_html(input, lesson)
lesson = '7'
input = [['Boolean values','There are two boolean values: True and False. A computer program often has to decide the boolean value of a statement.'],['Types of procedures','If procedures. This one returns the absolute value of a number by changing the sign of the number only if it is negative.<br>Else procedures. With these, if the first statement is False, the computer will perform the second instruction.<br>Or procedures. The value comes back True if either one of the two things is True.<br>Loops. The cycle will keep looking until the value does not meet the statement.<br>Breaks. This is a way to stop the loop even when the test condition is true.']]
print lesson_html(input, lesson)
lesson = '8'
input = [['Lists','A list is a sequence of anything, unlike strings which can only be a sequence of characters. The sequence could be characters, numbers, strings or other lists.'],['Changing lists','Mutation. This would change the item indexed at list position 0 and leave the rest of the list items as they are.<br>Aliasing is referring to the same thing by two different names. For example, if you made p=q, then p and q would become the same. If you later changed the value of one, it would change the value of both.<br>Appending items to lists:<br>A single command that adds an item to the end of a list']]
print lesson_html(input, lesson)
