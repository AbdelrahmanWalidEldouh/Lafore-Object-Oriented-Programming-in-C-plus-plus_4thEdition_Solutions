names = ["Yousef", "Mohamed", "Moaaz"]

message1 = "Hi " + names[0] + " i invite you to dinner"
message2 = "Hi " + names[1] + " i invite you to dinner"
message3 = "Hi " + names[-1] + " i invite you to dinner"

print(message1 + "\n" + message2 + "\n" + message3)

print(names[1] + " can't make it.")

print("******************")

names[1] = "Ali"
message2 = "Hi " + names[1] + " i invite you to dinner"
print(message1 + "\n" + message2 + "\n" + message3)

print("******************")

names.insert(0, "Naser")
names.insert(2, "Ahmed")
names.append("Ibrahim")

message1 = "Hi " + names[0] + " i invite you to dinner"
message2 = "Hi " + names[1] + " i invite you to dinner"
message3 = "Hi " + names[2] + " i invite you to dinner"
message4 = "Hi " + names[3] + " i invite you to dinner"
message5 = "Hi " + names[4] + " i invite you to dinner"
message6 = "Hi " + names[-1] + " i invite you to dinner"
print(
    message1
    + "\n"
    + message2
    + "\n"
    + message3
    + "\n"
    + message4
    + "\n"
    + message5
    + "\n"
    + message6
)
