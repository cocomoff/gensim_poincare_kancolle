import dill

relations = []
with open("./data/dataset_kuchiku.txt", "r") as f:
  for line in f:
    line = line.strip()
    if line[0] == '#':
      continue

    relation = line.split()
    relations.append(relation)

with open('./data/relations_kuchiku.dill', 'wb') as f:
  dill.dump(relations, f)