import markovify

# Get raw text as string.
with open("turrets.txt") as f:
    text = f.read()

# Build the model.
text_model_turrets = markovify.Text(text, state_size = 2)
f.close()

with open("units.txt") as f:
    text = f.read()
text_model_units = markovify.Text(text, state_size = 2)

model_combo = markovify.combine([ text_model_turrets, text_model_units ], [ 1, 1 ])

for i in range(5):
    a  = model_combo.make_sentence()
    print(a.replace(' ', ''))
