import pandas as pd
import numpy as np

gdas = []
with open("out/RE/cooc_FINAL.befree") as f:
    for line in f:
        items = line.split('\t')
        gdas.append([items[0], items[7], items[9], items[13], items[15]])
        
gdas_befree = pd.DataFrame(np.array(gdas), columns=['pmid', 'geneId', 'gene_name', 'diseaseId', 'disease_name'])

predicted_positive = gdas_befree.drop_duplicates(['pmid', 'geneId', 'diseaseId'])

actual_positive = pd.read_csv('out/test_labels.csv')

actual_positive.geneId = actual_positive.geneId.astype(str)

actual_positive.pmid = actual_positive.pmid.astype(str)

true_positives = pd.merge(actual_positive, predicted_positive, how="inner")

precision = true_positives.shape[0] / float(predicted_positive.shape[0])

recall = true_positives.shape[0] / float(actual_positive.shape[0])

Fscore = 2 * precision * recall /(precision + recall)

print "precision:{}  recall:{}  F-score:{}".format(precision, recall, Fscore)