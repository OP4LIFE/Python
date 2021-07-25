# If you have a question, the following function will answer it.
# It has a built-in list of answers and returns a random one.
def answer():
    answers = \
        [
        'It is certain.',
        'It is decidedly so.',
        'Yes',
        'Reply hazy later.',
        'Ask again later.',
        'Concentrate and ask again.',
        'My reply is no.',
        'Outlook not so good.',
        'Very doubtful.'
        ]
    # Returns a random one.
    import random
    return random.choice(answers)
    # return answers[random.randint(0, len(answers) - 1)]

print(answer())