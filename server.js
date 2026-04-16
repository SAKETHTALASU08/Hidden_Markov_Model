const express = require("express");
const bodyParser = require("body-parser");

const app = express();
app.use(bodyParser.json());
app.use(express.static("public"));

// HMM Model
const states = ["DET", "NOUN", "VERB"];

const pi = [0.6, 0.3, 0.1];

const A = [
    [0.1, 0.8, 0.1],
    [0.1, 0.2, 0.7],
    [0.2, 0.3, 0.5]
];

const B = {
    "The": [0.9, 0.1, 0.0],
    "dog": [0.1, 0.8, 0.1],
    "barks": [0.0, 0.2, 0.8]
};

// Viterbi Algorithm
function viterbi(obs) {
    let T = obs.length;
    let n = states.length;

    let dp = Array.from({length: n}, () => Array(T).fill(0));
    let path = Array.from({length: n}, () => Array(T).fill(0));

    for (let i = 0; i < n; i++) {
        dp[i][0] = pi[i] * (B[obs[0]] ? B[obs[0]][i] : 0.01);
    }

    for (let t = 1; t < T; t++) {
        for (let j = 0; j < n; j++) {
            let maxProb = 0, maxState = 0;

            for (let i = 0; i < n; i++) {
                let emission = B[obs[t]] ? B[obs[t]][j] : 0.01;
                let prob = dp[i][t-1] * A[i][j] * emission;

                if (prob > maxProb) {
                    maxProb = prob;
                    maxState = i;
                }
            }

            dp[j][t] = maxProb;
            path[j][t] = maxState;
        }
    }

    let bestPath = Array(T);
    bestPath[T-1] = dp.map(row => row[T-1]).indexOf(Math.max(...dp.map(row => row[T-1])));

    for (let t = T-2; t >= 0; t--) {
        bestPath[t] = path[bestPath[t+1]][t+1];
    }

    return bestPath.map(i => states[i]);
}

// API route
app.post("/predict", (req, res) => {
    let sentence = req.body.sentence.split(" ");
    let result = viterbi(sentence);
    res.json({ tags: result });
});

app.listen(3000, () => {
    console.log("Server running at http://localhost:3000");
});