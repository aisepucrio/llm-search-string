prompts = {
    'prompt0': '''You will receive the title and abstract of a scientific article. Your goal is to generate one, and just and only one, academic search string to retrieve relevant articles on the same topic. I want just and only a search string. Don't give me any additional information.
    ''',
    'prompt1': '''You will receive the title and abstract of a scientific article. Your goal is to generate one, and just and only one, search string to retrieve relevant articles on the same topic. Don't give me any  additional information.
To do this, follow these steps:
Use the provided title and abstract of the article to identify the most important terms.
Keyword Identification:
Identify words that are closely related to the central theme of the text, considering bigrams and trigrams, to select the most relevant expressions.
Clustering:
Group the keywords into clusters using a semantic proximity criterion.
Ensure that the clusters contain coherently related terms, where each cluster should represent a specific topic.
Search String Assembly:
Connect the terms within each cluster using OR.
Connect the clusters with each other using AND.
Expected Output: Generate the final search string based on the reasoning. I want just and only the search string. Don't give me any additional information.
    ''',
    'prompt2': '''You will receive the title and abstract of a scientific article. Your goal is to generate one, and just and only one, search string to retrieve relevant articles on the same topic. Don't give me any  additional information.
To ensure a fair comparison, follow the same process as a traditional Machine Learning-based method, which involves the following steps:
Use the provided title and abstract of the article to identify the most important terms.
Keyword Identification:
Identify words that are closely related to the central theme of the text, considering bigrams and trigrams, to select the most relevant expressions.
Clustering reasoning:
Group the keywords into clusters using a semantic proximity criterion.
Ensure that the clusters contain coherently related terms, where each cluster should represent a specific topic.
Search String Assembly:
Connect the terms within each cluster using OR.
Connect the clusters with each other using AND.
Simulated Refinement. Here there is the steps of the suggested reasoning:
Imagine that the extracted terms were used to search for relevant articles.
Generate a new list of keywords based on how the terms could be expanded to capture more relevant articles.
Build a second version of the search string, expanded with suggested terms.
Final Adjustment:
Present the generated string and the identified clusters.
Expected Output:
Present the final search string in boolean format. I want just and only the search string. Don't give me any additional information.
    '''
}

articles = [
    f'''
    title: Input Sample Selection for RBF Neural Network
    Classification Problems Using Sensitivity Measure
    abstract: Large data sets containing irrelevant or
    redundant input samples reduce the performance af
    leaming and increases storage and labeling casts. This
    work compares several sample selection and active
    reaming techniques and proposes a novel sample
    selection method based on the stochastic radial basis
    firnction neural network sensitiviry measure (Sw. The
    experimental results for the UCI IRlS data set show that
    we can remove 99% of data while keeping 92% of
    classifcation accuracy when applying both sensitivity
    based feature and sample selection methods. We propose
    a single and consistent method, which is robust enough to
    handle both feature and sample selection for a supervised
    RBFNN classifcation system. by using the same neural
    network architecture for both selection and classifreation
    tasks. 
    ''',

    f'''
    title: Analysis of Machine Learning Techniques for Context Extraction
    abstract: "’Context is key’ conveys the importance of capturing the
    digital environment of a knowledge worker. Knowing the
    user’s context offers various possibilities for support, like
    for example enhancing information delivery or providing
    work guidance. Hence, user interactions have to be aggregated and mapped to predefined task categories. Without
    machine learning tools, such an assignment has to be done
    manually. The identification of suitable machine learning
    algorithms is necessary in order to ensure accurate and
    timely classification of the user’s context without inducing
    additional workload.
    This paper provides a methodology for recording user interactions and an analysis of supervised classification models, feature types and feature selection for automatically detecting the current task and context of a user. Our analysis
    is based on a real world data set and shows the applicability
    of machine learning techniques."
    ''',

    f'''
    title: Selecting Discrete and Continuous Features Based on Neighborhood Decision Error Minimization
    abstract: —Feature selection plays an important role in pattern recognition and machine learning. Feature evaluation and classification complexity estimation arise as key issues in the construction of selection algorithms. To estimate classification complexity in different feature subspaces, a novel feature evaluation measure, called the neighborhood decision error rate (NDER), is proposed, which is applicable to both categorical and numerical features. We first introduce a neighborhood rough-set model to divide the sample set into decision positive regions and decision boundary regions. Then, the samples that fall within decision boundary regions are further grouped into recognizable and misclassified subsets based on class probabilities that occur in neighborhoods. The percentage of misclassified samples is viewed as the estimate of classification complexity of the corresponding feature subspaces. We present a forward greedy strategy for searching the feature subset, which minimizes the NDER and, correspondingly, minimizes the classification complexity of the selected feature subset. Both theoretical and experimental comparison with other feature selection algorithms shows that the proposed algorithm is effective for discrete and continuous features, as well as their mixture.
    ''',
    
    f'''
    title: Comprehensive Analysis of Network Traffic Data
    abstract: With the large volume of network traffic flow, it is necessary to preprocess raw data before classification to gain the accurate results speedily. Feature selection is an essential approach in preprocessing phase. The Principal Component Analysis (PCA) is recognized as an effective and efficient method. In this paper, we classify network traffic by using the PCA technique together with six machine learning algorithms — Naive Bayes, Decision Tree, 1-Nearest Neighbor (NN), Random Forest, Support Vector Machine (SVM) and H2O. We analyze the impact of PCA through classifying the data set by each algorithm with and without PCA. Experiments are set out by varying the size of input data sets, and the performances are measured from two metrics including overall accuracy and Fmeasure. The computational time is also considered in analysis phase. Our results show that Random Forest and NN are the top two algorithms among the six. Specifically, both of them behave well in classification under the most cases of input sets regardless of applying PCA. Lastly, PCA significantly boosts NN algorithms in terms of classification accuracy and shortens the classification time for Random Forest.
    ''',

    f'''
    title: "An extensible framework for software configuration optimization on
    heterogeneous computing systems: Time and energy case study"
    abstract: Context: Application of component based software engineering methods to heterogeneous computing (HC) enables different software configurations to realize the same function with different non–functional properties (NFP). Finding the best software configuration with respect to multiple NFPs is a non–trivial task. Objective: We propose a Software Component Allocation Framework (SCAF) with the goal to acquire a (sub–) optimal software configuration with respect to multiple NFPs, thus providing performance prediction of a software configuration in its early design phase. We focus on the software configuration optimization for the average energy consumption and average execution time. Method: We validated SCAF through its instantiation on a real–world demonstrator and a simulation. Firstly, we verified the correctness of our model through comparing the performance prediction of six software configurations to the actual performance, obtained through extensive measurements with a confidence interval of 95%. Secondly, to demonstrate how SCAF scales up, we performed software configuration optimization on 55 generated use–cases (with solution spaces ranging from 1030 to 3070) and benchmark the results against best performing random configurations. Results: The performance of a configuration as predicted by our framework matched the configuration implemented and measured on a real–world platform. Furthermore, by applying the genetic algorithm and simulated annealing to the weight function given in SCAF, we obtain sub–optimal software configurations differing in performance at most 7% and 13% from the optimal configuration (respectfully). Conclusion: SCAF is capable of correctly describing a HC platform and reliably predict the performance of software configuration in the early design phase. Automated in the form of an Eclipse plugin, SCAF allows software architects to model architectural constraints and preferences, acting as a multi–criterion software architecture decision support system. In addition to said, we also point out several interesting research directions, to further investigate and improve our approach.
    '''
]
