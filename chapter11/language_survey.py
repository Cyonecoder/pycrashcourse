from survey import AnonymousSurvey

question = "what language did you learn first to speak?"

my_survey = AnonymousSurvey(question=question)


my_survey.show_question()

print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == "q":
        break

    my_survey.store_response(response)

print("\nThank you to everyone who praticipated in the survey!")
my_survey.show_results()
