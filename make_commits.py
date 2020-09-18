import random
import os

# zalgoification stolen from a code golf example, could I format this better? yes. will I? no.
q=lambda z:''.join([v,v+''.join(random.choice(list(map(chr,range(768,815))))for i in range(int(random.normalvariate(10,5))))][v.isalpha()]for v in z)

# these messages taken from a list of most common commit messages
messages=[
	"initial commit",
	"update readme.md",
	"update",
	"first commit",
	"dummy",
	"updated readme",
	"pi push",
	"create readme.md",
	"fix",
	"cleanup",
	"test",
	"typo",
	"fuck",
	"wip",
	"bump version",
	"updates",
	"ah dammit, forgot this",
	"if I write it correctly the first time, I should get an award",
	"when does code exist? WHY does it exist?",
	"Do you think Zalgo willl forgive mine sins?",
	"Ain't no party like a empty space party",
	"HEAD empty, no commmits",
	"sometimes I wonder if computers fear us, I certainly fear them",
	"if you press the button, you receive candy",
	"If everybody's green, nobody's green",
	"http://gph.is/2jAdoZw",
	"Someone said gif commit messages were unprofessional, I don't like that Someone",
	"A scrub is a guy that thinks he's fly and is also known as a buster",
	"I miss when songs would introduce the concepts they talked about",
	"Last commit *insert Final Countdown music*"
]

# I couldn't get the bash for loop to run in the github action, so... here we are.
for n in range(random.randint(1, 10)):
	message = q(random.choice(messages))
	os.system(f'git commit -m "{message}" --allow-empty')
