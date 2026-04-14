# 1155250136 Cheng Haotian
### **a.**  Two main objectives
- Deliver fast, accurate self‑service resolution for common inquiries
- Improve user satisfaction and provide personalized solutions

### **b.**  Two main differences
- **Scope:** LLMs are specific large neural models for language generation/understanding; NLP is the broader field covering all language-processing tasks, methods, datasets, and evaluations (including non-LLM approaches).
- **Methodology/Scale:** LLMs are pretrained on massive corpora and excel at general, zero-/few-shot tasks; traditional NLP relies more on task-specific pipelines, supervised models, and feature engineering with smaller data and compute.

### **c.**  What are Word Embeddings?
- Word embeddings are dense vector representation of words
- A type of distributed representation of words
- Word embeddings can be obtained by training a neural network on a large corpus of text data
- Training samples are generated from the corpus usually using a sliding window to define contexts

#### How can Word Embeddings be used in NLP?
1.  **Input for Deep Learning Models**: They serve as the foundational input layer for neural networks (like RNNs, LSTMs, CNNs, and Transformers) in tasks such as sentiment analysis, text classification, and named entity recognition, allowing models to process text mathematically.
2.  **Semantic Similarity**: Because embeddings capture semantic relationships (e.g., `King - Man + Woman = Queen`), they are used to compute the similarity between words, sentences, or documents for tasks like search engines, recommendation systems, and plagiarism detection.
3.  **Dimensionality Reduction**: They provide a dense, low-dimensional representation of words compared to high-dimensional sparse representations like one-hot encoding or TF-IDF, making computation more efficient.
4.  **Transfer Learning**: Pre-trained embeddings (like Word2Vec, GloVe, BERT embeddings) allow models to leverage knowledge learned from massive datasets, improving performance on specific tasks with limited data.

### **d.** Three types of word embedding tools and their construction principles
- **Count-based embedding: scikit-learn TfidfVectorizer**
  - Constructs a sparse vector per word/document from raw counts; weights by TF-IDF (term frequency × inverse document frequency). Optionally applies SVD (LSA) to reduce dimensionality.

- **Dense embedding: Gensim Word2Vec**
  - Learns low-dimensional dense vectors by training neural objectives (CBOW/Skip-gram) to predict a word from its context or vice versa, using techniques like negative sampling.

- **Pretrained embedding: Hugging Face Transformers (e.g., BERT)**
  - Provides embeddings learned from large-scale pretraining with language modeling (masked/next-token). Outputs contextual vectors where a word’s embedding depends on the entire sentence.

### **e.** Content downloaded simultaneously
- **Tokenizer and vocabulary files** (e.g., vocab.txt, merges.json/vocab.json, spiece.model, tokenizer_config.json, special_tokens_map.json) to convert text to IDs consistently with pretraining.
- **Model configuration** (config.json) describing architecture/hyperparameters so the weights load into the correct network structure.
- **Model weight files** (model.safetensors) storing the parameters learned during pre-training is the core of a model's language capabilities.

### **f.** Why Multiple Layers
- **Hierarchical representations:** early layers capture local patterns (tokens, syntax), middle layers model longer-range semantics, later layers align to task objectives; one layer cannot build this compositional hierarchy.
- **Iterative refinement:** each layer re-attends and transforms features, correcting and sharpening alignments; depth enables multi-hop reasoning and complex dependency resolution.
- **Capacity and expressivity:** stacking attention+feed-forward blocks increases model capacity to approximate complex functions; a single layer with the same width is less expressive.
- **Larger effective receptive field:** successive self-attention layers propagate information across the sequence, enabling global context integration beyond what one pass provides.
- **Optimization stability:** residual connections, layer norms, and depth allow smoother gradient flow and better training dynamics; shallow models often underfit or fail to converge on hard tasks.
- **Empirical scaling:** deeper encoder–decoder stacks consistently reduce perplexity and improve accuracy in translation, summarization, and generation compared with single-layer counterparts.

### **g.** Decoder-only (GPT-style)
- Prefer decoder-only (GPT-style) for customer-service chatbots because it natively supports auto-regressive generation, streaming responses, and instruction/Chat fine-tuning, yielding fluent, coherent replies with simple deployment.
- It scales well to long contexts and tool-use (function calling/RAG), and has mature production tooling for safety, moderation, and RLHF alignment.
- Encoder-only models (such as BERT) are only good at "language understanding" (such as classification and question answering) and cannot directly generate responses.
- Transformer models are more suitable for "input → output" tasks (such as translation and summarization), and the fluency and coherence of dialogue generation are not as good as decoder-only models.


### **h.** Fine-tuning in the context of LLMs
- Fine-tuning is training a pretrained LLM further on curated, task- or domain-specific data to adapt behavior, improve accuracy, and align style or safety, starting from the model’s existing weights rather than training from scratch. 
- Fine-tuning is a key step in the “pre-training → transfer learning” process: Based on a large-scale pre-trained LLM, a small-scale labeled data for a specific task (such as a Taobao customer service dialogue dataset) is used to further train the model while fine-tuning some or all of the underlying parameters, so that the model can be adapted to the specific task (such as customer service dialogue generation) and retain the general language ability learned in the pre-training stage.



### **i.** Three metrics
- **Customer Satisfaction (CSAT):** Percentage of positive post‑chat ratings from users (e.g., 4–5 on a 5‑point scale). Measures perceived helpfulness and tone. Collected via short surveys at session end. Also an important metric for measuring user retention.

- **Resolution Rate:** The percentage of conversations where a user's core needs are successfully resolved out of all conversations. Directly reflects whether the robot has achieved the goal of "reducing human workload and improving user efficiency." For example, if a user inquires about "how to change their shipping address," and the robot provides accurate steps that are adopted by the user, this is counted in the resolution rate.

- **First Response Time (FRT) / Turn Latency:** Time to the bot’s first reply and average latency per turn. Lower is better; track p50/p95 to catch tail delays and reduce abandonment.

### Written Part Problem 6
- **CNN AutoEncoder**
- **Encoder:** Use 3-layer Conv2d+BatchNorm+ReLU+MaxPool2d to gradually compress the features of the input (250, 2, 32, 391).
- **Latent Space:** After flattening, it is mapped to a 256 dimensional vector through a fully connected layer.
- **Decoder:** Use 3-layer ConvTranspose2d for upsampling, and combine it with output padding to ensure that the output size is accurately restored to (250, 2, 32, 391). Removing the Sigmoid activation function from the last layer of the Decoder allows the model to more accurately fit the true dB values

- **output:**
- Epoch 1/20, Loss: 2194.127075
- Epoch 2/20, Loss: 2155.372498
- Epoch 3/20, Loss: 2131.896936
- Epoch 4/20, Loss: 2112.076807
- Epoch 5/20, Loss: 2086.701501
- Epoch 6/20, Loss: 2059.565320
- Epoch 7/20, Loss: 2030.774280
- Epoch 8/20, Loss: 2007.065869
- Epoch 9/20, Loss: 1975.502844
- Epoch 10/20, Loss: 1947.279089
- Epoch 11/20, Loss: 1919.478113
- Epoch 12/20, Loss: 1889.284253
- Epoch 13/20, Loss: 1861.822095
- Epoch 14/20, Loss: 1833.034619
- Epoch 15/20, Loss: 1806.721655
- Epoch 16/20, Loss: 1773.277783
- Epoch 17/20, Loss: 1744.296179
- Epoch 18/20, Loss: 1712.333130
- Epoch 19/20, Loss: 1676.291357
- Epoch 20/20, Loss: 1646.173511