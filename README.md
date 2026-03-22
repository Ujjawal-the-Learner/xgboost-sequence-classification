# xgboost-sequence-classification 
Greetings !! thanks for coming to my repository, I hope you will be smiling if not I just reminded you to, I want you all to go through this readme in detail, I have used my newly learned techstack in biological domain, anybody can understand this as i have kept the language friendly and tried to explain my AIM and FUTURE prospect like a story, so do give it a read, I am trying to create an ML based solution for Antibiotic resistance (bacteria are learning the antibiotics and getting resistant to them), so there are already short peptides present that can be used to kill bacteria but they cannot be used in their natural form, so we need to modify them, as proteins made of amino acids and  there are 20 of them, there can be huge permutations and combinations so why do it experimentally!! lets help researchers finding 2-3 effective sample peptide(predicted based on features and optimized using RL system) for them to experiment on.



Machine Learning Pipeline for Sequence Classification Using XGBoost:- This project implements a machine learning pipeline for binary sequence classification using 3 features that are biologically relevant for peptide(short length protein) and an XGBoost classifier.

The objective is to evaluate the effectiveness of feature-based representations of sequences for classification tasks.


Workflow:-
Sequence preprocessing


Feature extraction using Amino Acid Composition (AAC)

Model training using XGBoost

Model evaluation using classification metrics

Performance Metrics

Metric	Score        


Accuracy             -   0.91


Precision	         - label 0 - 0.92              label 1 - 0.90


Recall	           - label 0 - 0.93              label 1 - 0.89


F1 Score	         - label 0 - 0.92               label 1 - 0.89

Confusion Matrix     - TN - 674  FP - 52
                       FN - 62   TP - 480 

                       
Tools:- Python, Pandas, NumPy, Scikit-learn, XGBoost


References


Dataset:- Roy, Kuldeep (2020), “antimicrobial peptides”, Mendeley Data, V1, doi: 10.17632/37gbg3p3nr.1


T. Singh, P. Choudhary, and S. Singh, ‘Antimicrobial Peptides: Mechanism of Action’, Insights on Antimicrobial Peptides. IntechOpen, Jul. 06, 2022. doi: 10.5772/intechopen.99190.


Bhangu, S. K., Welch, N., Lewis, M., Li, F., Gardner, B., Thissen, H., & Kowalczyk, W. (2025). Machine Learning-Assisted Prediction and Generation of Antimicrobial Peptides. Small Science, 5(6), 2400579. https://doi.org/10.1002/smsc.202400579


Important Instructions:-

I have created a pkl file and a predict.py file

Anyone who wants to make a prediction can use this repository by making sure you have everything in same folder

Open your command terminal or powershell in that exact same folder and run 'python predict.py'
a dialogue 'Enter sequence', appears which will give output 1(AMP) or 0(non-AMP)





FUTURE WORKS 

As my aim is to optimize the peptide sequence, I will incorporate intelligent reinforced backed learning the plan is like using the probablity of being good peptide(antimicrobial peptide) as a reward to which the RL agent will try to increase till convergence by creating mutations in sequence by the policy of (i,j) for example- KDEKL(short sequence) at position i amino acid j will be replaced example- KDRKL. i position 3rd and new acid R, among 20 amino acids which will move the agent towards maximum reward, will be kept as mutation and this mutation is guided by classifier's score that is trained on appropriate features that are biologically in significance such as length(to be shorter),charge(to be positive),20 AAC(amino acid composition) this the composition which tell classifier what amino acids are present in good peptide(antimicrobial peptide). I will soon update the repository with proposed set of work.


Created by:- Ujjawal Shukla (National Institute of Technology,Warangal)
