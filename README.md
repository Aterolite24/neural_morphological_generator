# Neural Morphological Generator (NMG)

The **Neural Morphological Generator (NMG)** is a deep learning project designed to generate morphological transformations of Hindi words using sequence-to-sequence learning. By incorporating BiLSTM-based encoders and decoders with an attention mechanism, the model predicts transformed words based on linguistic attributes such as tense, gender, number, and aspect.

---

#### **Features**
- **BiLSTM Encoder**: Captures bidirectional context for input sequences, improving feature representation.
- **Attention Mechanism**: Dynamically focuses on relevant parts of the input sequence for accurate decoding.
- **Feature Inputs**: Integrates morphological attributes (e.g., POS, person, tense) for enhanced predictions.
- **Decoder**: Generates transformed words sequentially by attending to the encoded context.

---

#### **Dataset**
Source: [unimorph/hin](https://github.com/unimorph/hin)
The dataset contains:
- **Base Words**: Input words in their root form.
- **Transformed Words**: Target morphological forms.
- **Features**: Attributes such as POS, person, number, tense, aspect, and gender, one-hot encoded for processing.

---

#### **Model Architecture**
The architecture includes:
- **BiLSTM Encoder**: Encodes input sequences bidirectionally.
- **Attention Layer**: Helps the decoder focus on relevant parts of the encoder's output.
- **Decoder**: Generates output sequences step by step.
- **Feature Integration**: Merges linguistic features with the encoder's output for improved predictions.

---

#### **Performance**
The model achieves high accuracy and BLEU scores, demonstrating its ability to learn complex morphological patterns. Metrics include:
- **BLEU Score**: 0.6911
- **Accuracy**: 97.19%
- **Precision**: 97.87%
- **Recall**: 97.19%
- **F1-Score**: 97.51%

---

#### **Training Insights**
The training process shows steady improvement in accuracy, with minimal fluctuations, indicating effective learning of morphological transformations. Visualizations such as attention maps highlight how the model prioritizes relevant parts of the input sequence.

---

#### **How to Run**
1. Clone the repository and navigate to the project directory.
2. Prepare the dataset in the specified format (`Base Word`, `Transformed Word`, and features).
3. Train the model using the provided script or pre-trained weights.
4. Evaluate the model on test data for performance metrics and visualizations.

---

#### **Author**
**Achal Gawande**  
**Computer Science and Engineering**  
**Indian Institute of Technology (Banaras Hindu University), Varanasi**  
Email: [achal.gawande.cse22@itbhu.ac.in](mailto:achal.gawande.cse22@itbhu.ac.in)

GitHub: [Aterolite24](https://github.com/Aterolite24)  
LinkedIn: [Achal Gawande](https://www.linkedin.com/in/achal-gawande-33615b250/)  

---

Feel free to contribute or reach out for collaboration! 🚀
