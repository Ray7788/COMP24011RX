
Bag of n-grams
--------
1-grams: Absolutely, wonderful, silky, and, sexy, and, comfortable  
2-grams: Absolutely wonderful, wonderful silky, silky and, and sexy, sexy and, and comfortable  
3-grams: Absolutely wonderful silky, wonderful silky and, silky and sexy, and sexy and, sexy and comfortable


DF, TF, IDF  
https://medium.com/nlplanet/two-minutes-nlp-learn-tf-idf-with-easy-examples-7c15957b4cb3  
https://www.mygreatlearning.com/blog/bag-of-words/#what-is-tf-idf-term-frequency-inverse-document-frequency

PageRank(including examples)  
https://www.softwarepundit.com/seo/google-pagerank

我们假设页面 A 有页面 T1...Tn 指向它（即引用​​）。参数d是一个阻尼因子，可以在0到1之间设置。我们通常将d设置为0.85。下一节中有关于 d 的更多详细信息。此外，C(A) 定义为离开页面 A 的链接数。页面 A 的 PageRank 如下：

PR(A) = (1-d) + d (PR(T1)/C(T1 ) + ... + PR(Tn)/C(Tn))

请注意，PageRanks 在网页上形成概率分布，因此所有网页的 PageRanks 之和将为 1。

PageRank 或 PR(A) 可以使用简单的迭代算法计算，并且对应于网络规范化链接矩阵的主要特征向量。此外，在中等规模的工作站上，可以在几个小时内计算出 2600 万个网页的 PageRank。还有许多其他细节超出了本文的范围。
