# 1155250136 ChengHaotian
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import re
import nltk
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import yfinance as yf
import matplotlib.patheffects as path_effects
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_wine
from sklearn.model_selection import learning_curve, train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from collections import Counter
from collections import defaultdict

nltk.download('stopwords')
nltk.download('punkt_tab')

# Problem 2
def problem_2(input_file, output_file="problem2.png", title="Word Cloud for problem 2", threshold=0):
    seed_number = 5731 # use this as default seed if neccessary
    # step 1: load the text from the file
    text = ""
    with open(input_file, 'r', encoding='utf-8') as file:
        text = file.read()
    
    # step 2: convert the text to frequency dictionary
    # convert all text to lower case, remove punctuations and numbers
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = text.split()
    
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1
    
    # step 3: remove all words with frequency <= threshold
    filtered_freq = {word: count for word, count in freq_dict.items() if count > threshold}
    
    # step 4: create a word cloud based on the frequencies
    wordcloud = WordCloud(
        width=800, 
        height=400, 
        background_color='black', 
        random_state=seed_number
    ).generate_from_frequencies(filtered_freq)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(title)
    
    plt.savefig(output_file, dpi=600, bbox_inches='tight')
    # do not call plt.show()
    

# Problem 3
def problem_3(input_text, output_file="problem3.png", title="Sankey Chart for Problem 3"):
    # write your logic here  
    # step 1: convert all text to lower case, remove punctuations and numbers
    # remove stop words using nltk library
    input_text = input_text.lower()
    input_text = re.sub(r'[^a-z\s]', '', input_text)
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in word_tokenize(input_text) if word not in stop_words]
    
    # step 2: convert tokens to stems
    ps = PorterStemmer()
    stems = [ps.stem(token) for token in tokens]
    
    # step 3: create Sankey data
    flow_counts = Counter(zip(tokens, stems))
    
    stem_to_tokens = defaultdict(list)
    for t, s in set(zip(tokens, stems)):
        stem_to_tokens[s].append(t)
    
    sorted_stems = sorted(stem_to_tokens.keys())
    
    token_y = {}
    stem_y = {}
    current_y = 0
    
    for s in sorted_stems:

        associated_tokens = sorted(stem_to_tokens[s])
        
        # Assign y-positions to tokens
        group_token_y = []
        for t in associated_tokens:
            token_y[t] = current_y
            group_token_y.append(current_y)
            current_y += 1
        
        # Place the stem at the center of its tokens
        stem_y[s] = sum(group_token_y) / len(group_token_y)
        # Add a small gap between different stem groups
        current_y += 0.5
    
    max_rows = current_y
    
    # step 4: create Sankey chart
    plt.figure(figsize=(12, 12))
    
    # 绘制流向线条 (Sigmoid 曲线)
    for (token, stem), count in flow_counts.items():
        y1, y2 = token_y[token], stem_y[stem]
        x = np.linspace(0, 1, 100)
        y = y1 + (y2 - y1) * (1 / (1 + np.exp(-10 * (x - 0.5))))
        plt.plot(x, y, alpha=0.3, linewidth=count * 2, color='skyblue')
    
    # 添加标签和列标题
    for t, y in token_y.items(): plt.text(-0.02, y, t, ha='right', va='center', fontsize=8)
    for s, y in stem_y.items(): plt.text(1.02, y, s, ha='left', va='center', fontsize=8)
    
    plt.text(0, max_rows, "Original Tokens", ha='center', va='bottom', fontsize=12, fontweight='bold')
    plt.text(1, max_rows, "Stems", ha='center', va='bottom', fontsize=12, fontweight='bold')
    
    plt.title(title, pad=40, fontsize=14)
    plt.xlim(-0.3, 1.3)
    plt.axis('off')
    plt.savefig(output_file)
    # do not call plt.show()
    

# Problem 4
def problem_4(tickers, start_date, end_date, output_file="problem4.png", title="Stock Price Comparison for Problem 4"):
    # download data
    #data = pd.read_csv('problem4_data.csv')
    data = yf.download(tickers, start=start_date, end=end_date)['Close']
    # write your logic here  
    plt.figure(figsize=(12, 6))
 
    mid_idx = len(data) // 2
    offset_step = (len(data) // 3) // len(tickers)
    
    for i, ticker in enumerate(tickers):
 
        line, = plt.plot(data.index, data[ticker], label=ticker, linewidth=2)
        color = line.get_color()
        
        label_idx = mid_idx + i * offset_step
        label_idx = min(len(data) - 1, label_idx) 
        
        x_pos = data.index[label_idx]
        y_pos = data[ticker].iloc[label_idx]
        

        txt = plt.text(x_pos, y_pos, ticker, color=color, 
                       fontweight='bold', fontsize=10,
                       ha='center', va='bottom')
        
        txt.set_path_effects([
            path_effects.withStroke(linewidth=3, foreground='white')
        ])
    
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Stock Price (USD)")
    plt.grid(True, linestyle='--', alpha=0.7)

    
    plt.savefig(output_file)
    # do not call plt.show()


# Problem 5
def problem_5(data, group_names, output_file="problem5.png", titles=["Subplot Exercise for Problem 5", "Box plot", "Mean values"]):
    # write your logic here
    means = [np.mean(d) for d in data]
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    
    fig.suptitle(titles[0], fontsize=16)
    colors = ['red', 'yellow', 'green']
    # a. Left subplot: Box plot 
    bp = ax1.boxplot(data, tick_labels=group_names, patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    ax1.set_title(titles[1])
    ax1.set_ylabel("Value")
    
    # b. Right subplot: Horizontal bar chart
    bars = ax2.barh(group_names, means, color=colors)
    for bar in bars:
        width = bar.get_width()
        ax2.text(width + (max(means)*0.01), bar.get_y() + bar.get_height()/2, f'{width:.2f}', 
                 ha='left', va='center', fontweight='bold', fontsize=10)
    ax2.set_title(titles[2])
    ax2.set_xlabel("Mean Value")
    ax2.set_xlim(0, max(means) * 1.15)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    plt.savefig(output_file)
    # do not call plt.show()


# Problem 6
def problem_6(X, y, output_file="problem6.png", title="Learning Curve for Problem 6"):
    seed_number = 5731
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed_number)
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # write your logic here
    train_sizes = [1, 10, 20, 50, 100, 113]
    
    rf = RandomForestClassifier(random_state=seed_number)
    train_sizes_abs, train_scores, test_scores = learning_curve(
        rf, X_train_scaled, y_train, train_sizes=train_sizes, cv=5, scoring='accuracy', random_state=seed_number
    )
    
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    
    plt.figure(figsize=(12, 6))
    plt.plot(train_sizes_abs, train_scores_mean, 'o-', color="b", label="Training score")
    plt.plot(train_sizes_abs, test_scores_mean, 'o-', color="r", label="Cross-validation score")
    
    plt.fill_between(train_sizes_abs, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1, color="b")
    plt.fill_between(train_sizes_abs, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="r")
    
    plt.text(train_sizes_abs[-1], train_scores_mean[-1] + 0.01, f'Final Train: {train_scores_mean[-1]:.3f}', 
             va='bottom', ha='left', color='b', fontweight='bold')
    plt.text(train_sizes_abs[-1], test_scores_mean[-1] - 0.01, f'Final CV: {test_scores_mean[-1]:.3f}', 
             va='top', ha='left', color='r', fontweight='bold')
    
    plt.title(title)
    plt.xlabel("Training Set Size")
    plt.ylabel("Accuracy Score")
    plt.legend(loc="best")
    plt.grid(True)
    
    plt.savefig(output_file)
    # do not call plt.show()


if __name__ == "__main__":
    # Testing: Problem 2
    problem_2("problem2.txt", "problem2.png", threshold=3)


    # Testing: Problem 3
    text = ""
    with open("problem3.txt", 'r', encoding='utf-8') as file:
        text = file.read()
    problem_3(text, output_file="problem3.png")
   

    # Testing: Problem 4
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]
    start_date = "2020-01-01"
    end_date = "2025-01-01"
    problem_4(tickers, start_date, end_date)


    # Testing: Problem 5
    np.random.seed(5731)
    # create sample data for three groups
    data1 = np.random.normal(100, 15, 300)  # Group A
    data2 = np.random.normal(110, 12, 200)  # Group B
    data3 = np.random.normal(95, 18, 400)   # Group C
    # combine data for subplots
    data = [data1, data2, data3]
    group_names = ['Group A', 'Group B', 'Group C']
    problem_5(data, group_names)
    
    
    # Testing: Problem 6
    wine = load_wine()
    X, y = wine.data, wine.target
    problem_6(X, y)
