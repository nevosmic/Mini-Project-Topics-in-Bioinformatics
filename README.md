# Mini Project - Topics in Bioinformatics:

**Project Objective**: Identify distinguishing patterns between two classes of bacteria

###Project goals:

**Data-mining goal**: Given a set of bacterial genomes, “spelled” by genes (COGs) and annotated with binary
labels (e.g. pathogenic or non-pathogenic), identify genomic patterns (sets of COGs) that distinguish between
the two classes.


• In our experiment, a pattern is a “bag of genes (COGs)” – also called “Gene Teams”
• The statistical measure we used to measure how “distinguishing” a pattern is called “Information
Gain”.
• The data structure we used to enumerate the groups of genes (COGs) is the **FP-Tree**. This data
structure, together with an **algorithm called FP-Growth**, combines pattern enumeration and database search
for pattern occurrence.
• The paper we red proposes an algorithm to efficiently traverse the FP-Tree while employing a “branch
and bound” search pruning subtrees that will not yield a “good enough” Information Gain score.
• We where given bacterial genomic datasets with habitat annotation, we selected two habitats we would like to
distinguish, and identified and interpreted high-scoring distinguishing patterns between the two habitat classes.

• **The last and most important and “creative” step in the project is our proposal and implementaion of our own ideas on how
to either further speed up the search or improve the biological model or both.**


### Reading material:
(1) Chapter 12 in the machine learning book, the FP-tree data structure and the FP-growth
algorithm for mining frequent itemsets.

![pictures](https://images-na.ssl-images-amazon.com/images/I/41VTWhdpIlL._SX397_BO1,204,203,200_.jpg)

(2) The main paper to implement:
Cheng, Hong, et al. "Direct discriminative pattern mining for effective classification." 2008
IEEE 24th International Conference on Data Engineering. IEEE, 2008.

(3) In order to understand the pruning heuristic (Information Gain upper bound) it is
recommended to look into a previous paper by the authors:
Cheng, Hong, et al. "Discriminative frequent pattern analysis for effective classification." 2007
IEEE 23rd international conference on data engineering. IEEE, 2007.

 propose some other creative way to either speed up the search or to obtain more
meaningful biological results (or both).


