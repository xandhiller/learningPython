import random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
   'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island':
   'Providence','South Carolina': 'Columbia', 'South Dakota': 'Pierre',
   'Tennessee':'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City',
   'Vermont':'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
   'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files
for quizNum in range(3):
    # Create the quiz and answer key files
    quizFile = open('capitalsQuiz%s.txt' % (quizNum + 1), 'w')
    answerFile = open('capitalsQuizAnswerFile%s.txt' % (quizNum + 1), 'w')

    # Write out the header
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + 'State Capitals Quiz (Form %s)' % (quizNum + 1) )
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())
    random.shuffle(states)   # random.shuffle reorders the value of any list.

    # Loop through all 50 states and write a question for each
    for questionNum in range(50):

       # Get right and wrong answers
       correctAnswer = capitals[states[questionNum]]
       wrongAnswers = list(capitals.values()) # Duplicates all capitals into list
       del wrongAnswers[wrongAnswers.index(correctAnswer)] # Deletes correct answer
       # nb: wrongAnswers.index('string') will return int value of the index of 'string'
       wrongAnswers = random.sample(wrongAnswers, 3)
       answerOptions = wrongAnswers + [correctAnswer]
       random.shuffle(answerOptions)

       # Write the question and answer keys to the quiz file
       quizFile.write('%s. What is the capital of %s\n' % (questionNum+1,
       states[questionNum]))
       for i in range(4):
           quizFile.write('    %s. %s\n' % ('ABCD'[i], answerOptions[i]))
       quizFile.write('\n')

       # Write the answer key to a file
       answerFile.write('%s. %s\n' % (questionNum +1,
       'ABCD'[answerOptions.index(correctAnswer)]))

quizFile.close()
answerFile.close()
