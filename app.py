from flask import Flask, render_template, request
from collections import defaultdict

app = Flask(__name__)

# Load corpus
corpus = open(r"C:\Users\udayb\OneDrive\Desktop\nlp\hmm\corpus.txt").read().strip().split("\n")

transition = defaultdict(lambda: defaultdict(int))
emission = defaultdict(lambda: defaultdict(int))
start = defaultdict(int)
states = set()

# Training
for line in corpus:
    words = line.split()
    prev_tag = None

    for i, wt in enumerate(words):
        word, tag = wt.split("/")
        states.add(tag)

        emission[tag][word] += 1

        if i == 0:
            start[tag] += 1
        else:
            transition[prev_tag][tag] += 1

        prev_tag = tag

# Normalize
def normalize(d):
    total = sum(d.values())
    if total == 0:
        return
    for k in d:
        d[k] /= total

for tag in emission:
    normalize(emission[tag])

for tag in transition:
    normalize(transition[tag])

normalize(start)

states = list(states)

# Viterbi (Top 2 paths)
def viterbi(sentence):
    words = sentence.split()
    T = len(words)

    dp = {s: [(0, [])] for s in states}

    # Initialization
    for s in states:
        prob = start.get(s, 0.01) * emission[s].get(words[0], 0.01)
        dp[s] = [(prob, [s])]

    # Recursion
    for t in range(1, T):
        new_dp = {s: [] for s in states}

        for curr in states:
            candidates = []

            for prev in states:
                for prob, path in dp[prev]:
                    new_prob = prob * \
                               transition[prev].get(curr, 0.01) * \
                               emission[curr].get(words[t], 0.01)

                    candidates.append((new_prob, path + [curr]))

            candidates.sort(key=lambda x: x[0], reverse=True)
            new_dp[curr] = candidates[:2]

        dp = new_dp

    all_paths = []
    for s in states:
        all_paths.extend(dp[s])

    all_paths.sort(key=lambda x: x[0], reverse=True)

    return all_paths[:2]


@app.route("/", methods=["GET", "POST"])
def index():
    best_pairs = []
    comparisons = []

    if request.method == "POST":
        sentence = request.form["sentence"]
        paths = viterbi(sentence)

        words = sentence.split()

        # Best path
        best_prob, best_tags = paths[0]
        best_pairs = list(zip(words, best_tags))

        # Comparison list
        for i, (prob, tags) in enumerate(paths):
            comparisons.append({
                "path": i + 1,
                "prob": "{:.2e}".format(prob),
                "best": (i == 0)
            })

    return render_template("index.html",
                           best_pairs=best_pairs,
                           comparisons=comparisons)


if __name__ == "__main__":
    app.run(debug=True)