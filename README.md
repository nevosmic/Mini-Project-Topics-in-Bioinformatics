# Mini Project - Topics in Bioinformatics:

**Project Objective**: Identify distinguishing patterns between two classes of bacteria

*In this project we examined related Problem in Data Mining that is more general than genomics: Distinguishing Frequent Itemset Mining
We translated and changed this general problem so that it would serve our purpose.*

### Project goals:

**Data-mining goal**: Given a set of bacterial genomes, “spelled” by genes (COGs) and annotated with binary
labels (e.g. pathogenic or non-pathogenic), identify genomic patterns (sets of COGs) that distinguish between
the two classes.

• In our experiment, a pattern is a “bag of genes (COGs)” – also called “Gene Teams”.

• The statistical measure we used to measure how “distinguishing” a pattern is called “Information
Gain”.

• The data structure we used to enumerate the groups of genes (COGs) is the **FP-Tree**. This data
structure, together with an **algorithm called FP-Growth**, combines pattern enumeration and database search
for pattern occurrence.

• The paper we have read proposes an algorithm to efficiently traverse the FP-Tree while employing a “branch
and bound” search pruning subtrees that will not yield a “good enough” Information Gain score.

• We where given bacterial genomic datasets with habitat annotation, we selected two habitats we would like to
distinguish, and identified and interpreted high-scoring distinguishing patterns between the two habitat classes.

• **The last and most important and “creative” step in the project is our proposal and implementaion of our own ideas on how
to either further speed up the search or improve the biological model or both.**


### Reading material on which the project is based :
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

### our idea:
The two habitats we chose to explore are marine and animal.
in this part we decided to filter the data in order to speed up the search and obtain more meaningful results. 
We sorted the data by certain enzymes, we decided to focus on lipid transport and metabolism. we analyzed the transactions that contain cogs that relate to lipid transport and metabolism and ignored the cogs that are note related to the lipid transport and metabolism process. 

We found out that enzymes that participant in the lipid transport and metabolism process are much more common in marine bacteria compare to animal bacteria.  

In conclusion, it can be seen that the algorithm of our final step is faster and more importantly, return more informative results .The results show that groups of enzymes that related to the lipid transport and metabolism process’s are much more common in marine environment bacteria. 

### our final report is attached 

**Credits**:
This project was done with my class mate Adi Nechemia.




