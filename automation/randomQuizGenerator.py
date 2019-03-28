#! python 3
# randomQuizGenerator.py - Creates quizzes with questions and
# answers in random order ,along with the answer key

import random

# The quiz  data.keys are states and Values are their capitals.
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
	' Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
	' Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
	' Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
	' Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
	' Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
	' Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
	' Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
	' Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
	' Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New \
	 Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
	' North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
	' Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
	' South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
	' Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
	' Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
	 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quizNum in range(35):
    # Create the quiz and answer key files.
    quizfile = open('capitalsquiz%s.txt' % (quizNum + 1),'w')
    answerKeyfile = open('capitalsquiz_answers%s.txt' % (quizNum + 1),'w')

    # Write the header for the quiz
    quizfile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizfile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1 ))
    quizfile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)

    # loop through all 50 states , making a question for each.
    for questionNum in range(50):
        # Get right and wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the questions and the answer options to the quiz file.
        quizfile.write('%s. What is the capital of %s?\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizfile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
        quizfile.write('\n')

        # Write the answer key to a file.
        answerKeyfile.write('%s. %s\n' % (questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
        quizfile.close()
        answerKeyfile.close()
    