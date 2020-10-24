prompt = '''\nWrite a message and I will repeat it back
Or enter 'quit' to end the program
Your message: '''
message = input(prompt)

counter = 0
msg_list = []

while message.lower() != 'quit':
    msg_list.append(message)
    counter += 1
    message = input(prompt)
else:
    print(f"\nYou have entered {counter}-text message(s)\n\
{msg_list}\nQuitting now")
