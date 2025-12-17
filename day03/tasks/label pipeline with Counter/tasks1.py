from collections import Counter

def label_pipeline(labels, k):
    counts=Counter(labels)
    counts2=sorted(counts.items(),key=lambda item:item[1],reverse=True)
    top_k=counts2[:k]
    labels_id={x:i for i, (x,_) in enumerate(top_k)}
    return counts, top_k, labels_id


labels = ["cat","dog","cat","bird","dog","dog"]
print(label_pipeline(labels, 2),end="\n")