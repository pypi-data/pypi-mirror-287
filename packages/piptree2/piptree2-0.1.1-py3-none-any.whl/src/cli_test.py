import inquirer


if __name__ == '__main__':
    questions = [
        inquirer.Text('name', message="What's your name"),
        inquirer.List('size',
                      message="What size do you need?",
                      choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'],
                      ),
        inquirer.List('color',
                      message="What color do you need?",
                      choices=['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet'],
                      default='Blue',
                      ),
    ]

    answers = inquirer.prompt(questions)
    print(answers['name'])
    print(answers['size'])
    print(answers['color'])
