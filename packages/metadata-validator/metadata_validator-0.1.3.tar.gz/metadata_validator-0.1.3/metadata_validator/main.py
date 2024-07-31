from .metadata_main import descriptive_metadata_upload

def outside_bil_check():
    choices = ['ingest_1', 'ingest_2', 'ingest_3', 'ingest_4', 'ingest_5']
    file_path = input("What is the absolute path to the spreadsheet file? ")
    question = "Which Ingest method will be used?"
    print(question)
    for i, choice in enumerate(choices, 1):
        print(f"{i}. {choice}")

    while True:
        try:
            user_input = int(input("Please enter the number of your choice: "))
            if 1 <= user_input <= len(choices):
                user_choice = choices[user_input - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(choices)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")  

    descriptive_metadata_upload(file_path, user_choice)