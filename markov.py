import markovify

# Get raw text as string.
with open("name of text file.txt") as f:
    text = f.read()

# How many words it looks ahead to decide next word.
complexity = 2
    
    
# Build the model.
text_model = markovify.Text(text, state_size = complexity)
f.close()

for i in range(5):
    a  = model_combo.make_sentence()
    print(a)
