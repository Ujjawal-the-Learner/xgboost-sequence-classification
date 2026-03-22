import pickle

amino_acids = "ARNDCQEGHILKMFPSTWYV"

def compute_aac(Sequence):
    length = len(Sequence)
    aac_values = []
    for aa in amino_acids:
        count = Sequence.count(aa)
        freq = count/length
        aac_values.append(freq)
    return aac_values

# load model
model=pickle.load(open('Classifier.pkl','rb'))

# input
Sequence = input("Enter sequence: ").upper()

# AAC
aac_values = compute_aac(Sequence)

# charge
positive_charge = aac_values[amino_acids.index('K')] + aac_values[amino_acids.index('R')]
negative_charge = aac_values[amino_acids.index('D')] + aac_values[amino_acids.index('E')]
net_charge = positive_charge - negative_charge

# length
length = len(Sequence)

# final features
features = aac_values + [length, net_charge]

# prediction
prediction = model.predict([features])

print(prediction[0])