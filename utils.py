import numpy as np

def assign_sets():
    '''
    Questa funzione legge dalla cartella i seguenti file:
    - test_assignment.txt
    - train_assignment.txt
    - val_assignment.txt
    Poi ritorna tre array di valori
    '''
    test_set = []
    train_set = []
    val_set = []
    # leggo prima Train
    with open('train_assignment.txt', 'r') as f:
        for row in f:
            row = row.strip()
            train_set.append(row)
    # poi test
    with open('test_assignment.txt', 'r') as f:
        for row in f:
            row = row.strip()
            test_set.append(row)
    # infine validation
    with open('val_assignment.txt', 'r') as f:
        for row in f:
            row = row.strip()
            val_set.append(row)
    
    print(f'Train set: {len(train_set)}')
    print(f'Test set: {len(test_set)}')
    print(f'Val set: {len(val_set)}')
    return train_set, test_set, val_set


def extract_boundary_box(valore, annotations):
    '''
    Questa funzione prende un valore in input
    ed estrae le boundary box della classe 1 relative a quel valore
    '''
    path_file = 'Annotations/' + valore + '.jpg.txt'
    print(path_file)
    rows = []
    if path_file[12:] in annotations:
        # il file è presente
        with open(path_file, 'r') as f:
            for row in f:
                row = row.strip()
                rows.append(row)
        rows = rows[1:] # faccio slicings
        bboxes = []
        for row in rows:
            row = row.split(' ')
            target,x,y,w,h = row
            if int(target) == 1:
                box = [x,y,w,h]
                bboxes.append(box)
        # print(f'Ho trovato {len(bboxes)} boundary boxes')
        return bboxes
    return None




train, test, val = assign_sets()
file_0 = train[0]

import os

directory = 'Annotations'

annotations = []
for root,dirs,files in os.walk(directory):
    for file in files:
        annotations.append(str(file))


bboxes_train = []
for i in range(len(train)):
    bboxes = extract_boundary_box(train[i], annotations)
    if bboxes:
        bboxes_train.append(bboxes)

bboxes_test = []
for i in range(len(test)):
    bboxes = extract_boundary_box(test[i], annotations)
    if bboxes:
        bboxes_test.append(bboxes)

bboxes_val = []
for i in range(len(val)):
    bboxes = extract_boundary_box(val[i], annotations)
    if bboxes:
        bboxes_val.append(bboxes)


print(f'Ci sono in totale {len(bboxes_train)} file di annotazioni per il train')
print(f'Ci sono in totale {len(bboxes_test)} file di annotazioni per il test')
print(f'Ci sono in totale {len(bboxes_val)} file di annotazioni per il validation')


directory = 'Images_Positive'

images = []
for root,dirs,files in os.walk(directory):
    for file in files:
        images.append(str(file))

print(f'Ci sono {len(annotations)} annotazioni per le boundary box')
print(f'Ci sono {len(images)} immagini')