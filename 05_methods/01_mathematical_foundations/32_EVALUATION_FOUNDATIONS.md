# 32. Evaluation foundations

For binary predictions against a specified reference, TP is true positives, FP false positives, TN true negatives and FN false negatives. “True” here means agreement with that reference, whose biological validity must be examined. [Official metric definitions](SOURCES.md#metrics)

| Metric | Formula | Main qualification |
|---|---|---|
| Accuracy | $(TP+TN)/(TP+TN+FP+FN)$ | Can conceal poor minority-class detection |
| Precision | $TP/(TP+FP)$ | Fraction of predicted positives that match reference |
| Recall/sensitivity | $TP/(TP+FN)$ | Fraction of reference positives recovered |
| Specificity | $TN/(TN+FP)$ | Fraction of reference negatives rejected |
| F1 | $2TP/(2TP+FP+FN)$ | Harmonic mean of precision/recall; ignores TN |

Zero denominators need a reported convention or “undefined”; silently selecting a replacement can distort comparisons. For TP=3, FP=1, TN=4, FN=2, accuracy is 0.7, precision 0.75, recall 0.6, specificity 0.8, and F1 $6/9=2/3$. In multiclass work, macro averaging treats classes equally, micro aggregates counts, and support weighting gives large classes more influence.

Clustering introduces different questions. Within-cluster similarity asks how close members are in a chosen space; between-cluster separation asks how far groups are apart. ARI and NMI compare two partitions of the same observations and are invariant to arbitrary label renaming. Silhouette uses a partition and distances, requiring no external label set. None proves cell identity or mechanism. [Clustering metrics](SOURCES.md#cluster-metrics)

Future evaluation must declare observation unit, label hierarchy/provenance, preprocessing, metric, held-out design and handling of missing labels. Region labels are not interchangeable with cell-type labels. Reusing labels to select features and then scoring against them is circular. These are definitions and a synthetic confusion table; there are no predictions or clusters fitted to project data.
