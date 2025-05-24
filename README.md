<h1> Soil Classification using CNN Feature Extraction + Random Forest</h1>

<p>
  This project was developed as part of the Hackathon and Internship opportunity organized by IIT Ropar and Annam.ai. It focuses on classifying soil types (Alluvial, Black, Clay, Red) from images using deep learning techniques to support AI-driven sustainable agriculture.
</p>

<h2>🗂️ Dataset Structure</h2>

<pre><code>soil_classification-2025/
├── train/
│   ├── 0001.jpg
│   └── ...
├── test/
│   ├── 2001.jpg
│   └── ...
├── train_labels.csv   # image_id, soil_type
└── test_ids.csv       # image_id
</code></pre>

<h2>🧠 Methodology</h2>

<h3>🔍 Feature Extraction</h3>
<ul>
  <li><strong>Model:</strong> Pretrained <code>ResNet-18</code> (ImageNet)</li>
  <li><strong>Modification:</strong> Replace <code>fc</code> layer with <code>Identity()</code> to extract 512-D features</li>
  <li><strong>Transform:</strong> Resize (224×224), convert to tensor</li>
</ul>

<h3>🎯 Classification</h3>
<ul>
  <li><strong>Model:</strong> Random Forest Classifier</li>
  <li><strong>Validation:</strong> Stratified 5-Fold Cross-Validation</li>
  <li><strong>Metric:</strong> Macro F1-Score</li>
</ul>

<h2>🏁 How to Run</h2>

<h3>✅ Requirements</h3>
<pre><code>pip install torch torchvision scikit-learn pandas numpy tqdm pillow</code></pre>

<h3>▶️ Run Pipeline</h3>
<ol>
  <li>Clone the repo:
    <pre><code>git clone https://github.com/saikoushiknalubola/anndata_annam.git
cd anndata_annam</code></pre>
  </li>
  <li>Place the <code>soil_classification-2025</code> folder in the project root.</li>
  <li>Run the script:
    <pre><code>python training.ipynb</code></pre>
  </li>
</ol>

<h2>📊 Performance</h2>

<h3>🧪 Fold-wise F1 Scores</h3>
<table>
  <tr><th>Fold</th><th>Macro F1 Score</th></tr>
  <tr><td>1</td><td>0.94</td></tr>
  <tr><td>2</td><td>0.94</td></tr>
  <tr><td>3</td><td>0.95</td></tr>
  <tr><td>4</td><td>0.95</td></tr>
  <tr><td>5</td><td>0.99</td></tr>
  <tr><td><strong>Avg</strong></td><td><strong>0.955</strong></td></tr>
</table>

<div class="highlight">
✅ <strong>Public Leaderboard Score:</strong> 1.0000<br/>
</div>

<h2>📁 Output</h2>
<ul>
  <li><code>submission.csv</code>: Final test set predictions</li>
  <li>Console: Fold-wise classification reports and average F1</li>
</ul>

<h2>📌 Notes</h2>
<ul>
  <li>ResNet weights loaded manually </li>
  <li>End-to-end CNN fine-tuning can be explored for large datasets</li>
</ul>

<h2>🤝 Acknowledgements</h2>
<ul>
  <li>Dataset provided by competition organizers</li>
  <li>ResNet model from PyTorch Model Zoo</li>
</ul>

<h2>👨‍💻 Author</h2>
<p><strong>Saikoushik Nalubola</strong><br/>
</p>

<h2>📬 Contact</h2>
<ul>
  <li>Email: <code>saikoushiknalubola@gmail.com</code></li>
</ul>

<h2>⚖️ License</h2>
<p>This project is licensed under the <a href="#">MIT License</a>.</p>

</body>
</html>
