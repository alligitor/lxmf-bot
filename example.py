from lxmfbot import LXMFBot
import socket

def read_file_to_array(file_path):
    lines = []  # Initialize an empty list
    try:
        with open(file_path, 'r') as file:
            # Read each line and append it to the list
            for line in file:
                lines.append(line.strip())  # Using strip() to remove any leading/trailing whitespace
        return lines
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return []
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Main
hostname = socket.gethostname()

print(hostname)

#bot = LXMFBot("testbot")
bot = LXMFBot(hostname)

@bot.received
def echo_msg(msg):
    print(f"Message {msg}")
    msg.reply(msg.content)

bot._announce()


#if there is a file with destinations, send them a message with our host name
destinations = read_file_to_array("initial_message.txt")

for dest in destinations:
    print("Sending message to " + dest)
    bot.send(dest, hostname)

bot.run()
