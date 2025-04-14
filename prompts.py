prompts = {
    'prompt0': '''You will receive the title and abstract of a scientific article. Your goal is to generate one, and just and only one, academic search string to retrieve relevant articles on the same topic. 
    One suggested approach is to take the keywords from the provided article and augment them with related words.
    I want just and only a search string. Don't give me any additional information.
    An exemple of expected output format: ("nutritional intervention" OR "dietary intervention") AND ("type 2 diabetes" OR "T2DM") AND (randomized OR "clinical trial")
    ''',
    'prompt1': '''You will receive the title and abstract of a scientific article. Your goal is to generate one, and just and only one, search string to retrieve relevant articles on the same topic. Don't give me any  additional information.
To do this, you can follow these steps:
Use the provided title and abstract of the article to identify the most important terms.
Identify words that are closely related to the central theme of the text, considering bigrams and trigrams, to select the most relevant expressions.
Group the keywords into clusters using a semantic proximity criterion.
Connect the terms within each cluster using OR.
Connect the clusters with each other using AND.
The final answer is the search string based on the reasoning. I want just and only the search string. Don't give me any additional information.
An exemple of expected format output: : ("nutritional intervention" OR "dietary intervention") AND ("type 2 diabetes" OR "T2DM") AND (randomized OR "clinical trial")
    ''',
    'prompt2': '''You will receive the title and abstract of a scientific article. Your goal is to generate one, and just and only one, search string to retrieve relevant articles on the same topic. Don't give me any  additional information.
The approach suggestion:
Use the provided title and abstract of the article to identify the most important terms.
Identify words that are closely related to the central theme of the text, considering bigrams and trigrams, to select the most relevant expressions.
Group the keywords into clusters using a semantic proximity criterion.
Ensure that the clusters contain coherently related terms, where each cluster should represent a specific topic.
Connect the terms within each cluster using OR.
Connect the clusters with each other using AND.
With that, you will have the search string. Now the approach suggestion for improve that one search string.
Imagine that the extracted terms were used to search for relevant articles and you take 10 of then. 
Generate a new list of keywords based on how the terms could be expanded to capture more relevant articles.
Build a second version of the search string, expanded with suggested terms.
Present the final search string result. I want just and only the search string. Don't give me any additional information.
An exemple of expected output format: ("nutritional intervention" OR "dietary intervention") AND ("type 2 diabetes" OR "T2DM") AND (randomized OR "clinical trial")
    '''
}

new_articles = [

    f'''title: SPL Conqueror: Toward optimization of non-functional properties in software product lines\n
        abstract: A software product line (SPL) is a family of related programs of a domain. The programs of an SPL are distinguished in terms of features, which are end-user visible characteristics of programs. Based on a selection of features, stakeholders can derive tailor-made programs that satisfy functional requirements. Besides functional requirements, different application scenarios raise the need for optimizing non-functional properties of a variant. The diversity of application scenarios leads to heterogeneous optimization goals with respect to non-functional properties (e. g., performance vs. footprint vs. energy optimized variants). Hence, an SPL has to satisfy different and sometimes contradicting requirements regarding non-functional properties. Usually, the actually required non-functional properties are not known before product derivation and can vary for each application scenario and customer. Allowing stakeholders to derive optimized variants requires us to measure non-functional properties after the SPL is developed. Unfortunately, the high variability provided by SPLs complicates measurement and optimization of non-functional properties due to a large variant space. With SPL Conqueror, we provide a holistic approach to optimize non-functional properties in SPL engineering. We show how non-functional properties can be qualitatively specified and quantitatively measured in the context of SPLs. Furthermore, we discuss the variant-derivation process in SPL Conqueror that reduces the effort of computing an optimal variant. We demonstrate the applicability of our approach by means of nine case studies of a broad range of application domains (e. g., database management and operating systems). Moreover, we show that SPL Conqueror is implementation and language independent by using SPLs that are implemented with different mechanisms, such as conditional compilation and feature-oriented programming. 
    ''',

    f'''title: Measuring non-functional properties in software product lines for product derivation\n
        abstract: A software product line (SPL) enables stakeholders to derive different software products for a domain while providing a high degree of reuse of their code units. Software products are derived in a configuration process by composing different code units. The configuration process becomes complex if SPLs contain hundreds of features. In many cases, a stakeholder is not only interested in functional but also in non-functional properties of a desired product. Because SPLs can be used in different application scenarios alternative implementations of already existing functionality are developed to meet special non-functional requirements, like restricted binary size and performance guarantees. To enable these complex configurations we discuss and present techniques to measure non-functional properties of software modules and use these values to compute SPL configurations optimized to the users needs.
    ''',

    f'''title: Machine learning techniques to predict software defect\n
        abstract: The past 10 years have seen the prediction of software defects proposed by many researchers using various metrics based on measurable aspects of source code entities (e.g. methods, classes, files or modules) and the social structure of software project in an effort to predict the software defects. However, these metrics could not predict very high accuracies in terms of sensitivity, specificity and accuracy. In this chapter, we propose the use of machine learning techniques to predict software defects. The effectiveness of all these techniques is demonstrated on ten datasets taken from literature. Based on an experiment, it is observed that PNN outperformed all other techniques in terms of accuracy and sensitivity in all the software defects datasets followed by CART and Group Method of data handling. We also performed feature selection by t-statistics based approach for selecting feature subsets across different folds for a given technique and followed by the feature subset selection. By taking the most important variables, we invoked the classifiers again and observed that PNN outperformed other classifiers in terms of sensitivity and accuracy. Moreover, the set of 'if- then rules yielded by J48 and CART can be used as an expert system for prediction of software defects. 
    ''',

    f'''title: Using machine learning to infer constraints for product lines\n
        abstract: Variability intensive systems may include several thousand features allowing for an enormous number of possible configurations, including wrong ones (e.g. the derived product does not compile). For years, engineers have been using constraints to a priori restrict the space of possible configurations, i.e. to exclude configurations that would violate these constraints. The challenge is to find the set of constraints that would be both precise (allow all correct configurations) and complete (never allow a wrong configuration with respect to some oracle). In this paper, we propose the use of a machine learning approach to infer such product-line constraints from an oracle that is able to assess whether a given product is correct. We propose to randomly generate products from the product line, keeping for each of them its resolution model. Then we classify these products according to the oracle, and use their resolution models to infer cross-tree constraints over the product-line. We validate our approach on a product-line video generator, using a simple computer vision algorithm as an oracle. We show that an interesting set of cross-tree constraint can be generated, with reasonable precision and recall.
    ''',

    f'''title: Cost-efficient sampling for performance prediction of configurable systems\n
        abstract: A key challenge of the development and maintenanceof configurable systems is to predict the performance ofindividual system variants based on the features selected. It isusually infeasible to measure the performance of all possible variants, due to feature combinatorics. Previous approaches predictperformance based on small samples of measured variants, butit is still open how to dynamically determine an ideal samplethat balances prediction accuracy and measurement effort. Inthis paper, we adapt two widely-used sampling strategies forperformance prediction to the domain of configurable systemsand evaluate them in terms of sampling cost, which considersprediction accuracy and measurement effort simultaneously. Togenerate an initial sample, we introduce a new heuristic based onfeature frequencies and compare it to a traditional method basedon t-way feature coverage. We conduct experiments on six realworldsystems and provide guidelines for stakeholders to predictperformance by sampling.
    '''
]


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
