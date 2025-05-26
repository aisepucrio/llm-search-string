prompts = {
    'prompt0': '''You will receive the **title** and **abstract** of a scientific article. Your goal is to generate one, and only one, **comprehensive Boolean search string** to retrieve **relevant articles on the same topic**.

To do this, extract the **key concepts** from the text and identify **related terms**, including synonyms, abbreviations, variations, and associated expressions, in order to **broaden the scope** and increase recall. Focus on the underlying meaning of the topic, not just keywords that appear literally in the text.

The final output must be a single, logically structured search string using Boolean operators:
- Use OR to connect similar terms within a concept.
- Use AND to connect distinct concepts.

Do not provide any explanation or additional information. Return **only** the complete search string.

Expected output format:
("machine learning" OR "ML" OR "supervised learning" OR "unsupervised learning") AND ("software product line" OR "SPL" OR "product line engineering" OR "variability management")''',

    'prompt1': '''You will receive the **title** and **abstract** of a scientific article. Your task is to generate one, and only one, **search string** to retrieve articles on the same general topic. The search string must be **semantically rich and contextually expanded** to improve retrieval of **relevant scientific literature**.

To build it, follow these steps:
1. Identify the **main topics and concepts** from the title and abstract.
2. For each concept, include **related expressions**, such as synonyms, abbreviations, technical variations, or common usage forms.
3. Group semantically related terms using OR.
4. Combine different conceptual groups using AND.
5. Avoid overly specific expressions that might reduce the number of retrieved articles. You need to **broaden the scope**, thinking about what more general terms could relate to those.

Return only the final Boolean search string. Do not include explanations or intermediate steps.

Expected format:
("machine learning" OR "ML" OR "supervised learning" OR "unsupervised learning") AND ("software product line" OR "SPL" OR "product line engineering" OR "variability management")''',

    'prompt2': '''You will receive the **title** and **abstract** of a scientific article. Your task is to generate one, and only one, **expanded Boolean search string** to retrieve relevant literature on the same topic. The goal is not to narrow the topic, but to ensure **broad yet relevant** retrieval of literature.

Use the following approach:
1. Extract the main concepts from the title and abstract.
2. Expand each concept by identifying semantically related terms (e.g., synonyms, expressions, domain-specific variations, acronyms, plural/singular forms).
3. Organize terms into **clusters**, where each cluster represents a coherent subtopic.
4. Use OR to join terms within a cluster and AND to connect different clusters.

Then, simulate a refinement step: imagine that the initial string was used to retrieve articles. Based on the retrieved set, expand the query by including additional terms that would likely improve recall while maintaining topic relevance.

You have to avoid overly specific expressions that might reduce the number of retrieved articles. You need to **broaden the scope**, thinking about what more general terms could relate to those.

Return only the **final version** of the enriched Boolean search string, incorporating both the initial and the expanded terms. Do not include reasoning or commentary.

Expected format:
("machine learning" OR "ML" OR "supervised learning" OR "unsupervised learning") AND ("software product line" OR "SPL" OR "product line engineering" OR "variability management")
'''
}



prompts_antigos = {
    'prompt0': '''You will receive the title and abstract of a scientific article. Your goal is to generate one, and just and only one, Boolean search string to retrieve other scientific articles that address the same general research theme or area.
    One suggested approach is to take the keywords from the provided article and augment them with related words.
    I want just and only a search string. Don't give me any additional information.
    An exemple of expected output format: ("nutritional intervention" OR "dietary intervention") AND ("type 2 diabetes" OR "T2DM") AND (randomized OR "clinical trial")
    ''',
    'prompt1': '''You will receive the title and abstract of a scientific article. Your goal is to generate one, and just and only one, search string to retrieve other scientific articles that address the same general research theme or area.. Don't give me any  additional information.
To do this, you can follow these steps:
Use the provided title and abstract of the article to identify the most important terms.
Identify words that are closely related to the central theme of the text, considering bigrams and trigrams, to select the most relevant expressions.
Group the keywords into clusters using a semantic proximity criterion.
Connect the terms within each cluster using OR.
Connect the clusters with each other using AND.
The final answer is the search string based on the reasoning. I want just and only the search string. Don't give me any additional information.
An exemple of expected format output: : ("nutritional intervention" OR "dietary intervention") AND ("type 2 diabetes" OR "T2DM") AND (randomized OR "clinical trial")
    ''',
    'prompt2': '''You will receive the title and abstract of a scientific article. Your goal is to generate one, and just and only one, search string to retrieve other scientific articles that address the same general research theme or area.. Don't give me any  additional information.
The approach suggestion:
Use the provided title and abstract of the article to identify the most important terms.
Identify words that are closely related to the central theme of the text, considering bigrams and trigrams, to select the most relevant expressions.
Group the keywords into clusters using a semantic proximity criterion.
Ensure that the clusters contain coherently related terms, where each cluster should represent a specific topic.
Connect the terms within each cluster using OR.
Connect the clusters with each other using AND.
With that, you will have the search string. Now the approach suggestion for improve that one search string.
Imagine that the extracted terms were used to search for relevant articles and you take 10 of then. 
Generate a new list of keywords based on how the terms could be expanded to capture other scientific articles that address the same general research theme or area..
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

