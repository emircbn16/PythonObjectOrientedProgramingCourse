# Question
class Question:
    def __init__(self,text,choices,answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer

# Quiz
class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f'Soru {self.questionIndex + 1}: {question.text}')

        for q in question.choices:
            print('-'+q)
        
        answer = input('Cevap: ')
        self.guess(answer)
        self.loadQuestion()

    def guess(self, answer):
        question = self.getQuestion()

        if question.checkAnswer(answer):
            self.score += 1
        self.questionIndex += 1

    def loadQuestion(self):
        if len (self.questions) == self.questionIndex:
            self.showScore()
        
        else:
            self.displayProgress()
            self.displayQuestion()

    def showScore(self):
        print('Score: ', self.score)

    def displayProgress(self):
        totalQuestion = len(self.questions)
        questionNumber = self.questionIndex + 1

        if questionNumber > totalQuestion:
            print('Quiz Bitti.')
        else:
            print(f'Question {questionNumber} of {totalQuestion}'.center(35,'*'))

q1 = Question('En İyi Programlama Dili Hangisidir ?', ['C#','Python','JavaScript','Java'], 'Python')
q2 = Question('En Popüler Programlama Dili Hangisidir ?', ['Python','C#','JavaScript','Java'], 'Python')
q3 = Question('En Çok Kazandıran Programlama Dili Hangisidir ?', ['JavaScript','C#','Python','Java'], 'Python')
q4 = Question('En SevilenProgramlama Dili Hangisidir ?', ['Java','JavaScript','C#','Python'], 'Python')
q5 = Question('En Kolay Programlama Dili Hangisidir ?', ['JavaScript','C#','Python','Java'], 'Python')

questions = [q1,q2,q3,q4,q5]


quiz = Quiz(questions)

quiz.loadQuestion()
