questions = ("which f1 car won 2025 cc",
             "which driver lost dc",
             "which driver won dc",""
             "youngest pole sitter of f1")
options = (("A.redbull","B.mclaren","C.minardi","D.visa rb"),
           ("A.max","B.yuki","C.lando","D.russell"),
           ("A.max","B.yuki","C.lando","D.russell"),
           ("A.kimi","B.max","C.stroll","D.alonso"))
answers = ("B","A","C","A")
guesses = []
question_num = 0
score = 0
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("enter a option (A/B/C/D): ").upper()
    guesses.append(guess)
    if(guess == answers[question_num]):
        score +=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"the correct answer is {answers[question_num]}")
    question_num+=1

print("    results    ")
print("answers: ")
for answer in answers:
    print(answer, end=" ")
print()
print("guesses: ")
for guess in guesses:
    print(guess,end=" ")
print()

score = (score/len(questions)) * 100
print(f"the percentage result is %{score}")