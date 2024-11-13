# Skin Disease Detection and Classification 🩺🌟

### A Project by:
- **Karakattil Dilrose Reji**
- **Sharma Akshat Devendra**
- **Sneha Mary Bency**

### Supervised by:
- **Mr. Mritunjay Ojha**, Department of Computer Engineering, Fr. Conceicao Rodrigues Institute of Technology

---

## 📚 Overview
This project addresses a significant need for early, accurate detection and classification of skin diseases. With skin diseases being the fourth leading cause of non-fatal disease burden globally, timely diagnosis is critical. Our approach leverages deep learning to develop a web-based solution that helps users analyze dermoscopic images for potential skin diseases, ensuring swift action and preventive care.

---

## 🧠 Motivation
Skin diseases, often underestimated due to their low mortality rate, can have severe implications if left undiagnosed. Many individuals delay consulting a dermatologist, believing skin issues to be minor. Our project aims to bridge this gap by providing a tool that can identify skin abnormalities through images, enabling early intervention.

---

## 🎯 Aim and Objective
- **Primary Goal**: To create an automated system capable of classifying dermoscopic images into different diagnostic categories and providing users with a probable disease percentage.
- **Secondary Features**: Offer users information on nearby dermatologists for professional follow-up care.

---

## 📂 Dataset
The project utilizes images sourced from **Dermnet**, the largest online dermatology resource, comprising:
- **Total Images**: Approximately 19,500 images
- **Format**: JPEG
- **Categories**: 23 skin disease types (project focus on 4 main categories)

---

## 🔧 Methodology
### 1. **Data Preprocessing and Augmentation**
   - Applied techniques such as horizontal/vertical flips, random rotations, and rescaling to enhance dataset diversity and model robustness.

### 2. **Model Training**
   - **Traditional Approach**: Utilized a Convolutional Neural Network (CNN) with moderate results (training accuracy of 42.8%).
   - **Transfer Learning Approach**: Implemented **MobileNet** for improved accuracy, achieving a training accuracy of 89.9% and a validation accuracy of 73.8%.

### 3. **Model Implementation**
   - The system architecture integrates preprocessing, training, and user-facing result generation, ensuring a seamless experience for end-users.

---

## 📈 Results
- **CNN Classifier**: Limited performance, highlighted by fluctuating training and validation accuracies.
- **MobileNet Classifier**: Demonstrated significantly better performance with high reliability, making it the preferred model for deployment.

### Sample Outcomes:
| Disease Type          | CNN Accuracy | MobileNet Accuracy |
|-----------------------|--------------|---------------------|
| Acne and Rosacea      | 0.23         | 0.94                |
| Melanoma Skin Cancer  | 0.29         | 0.99                |
| Psoriasis             | 0.13         | 0.97                |
| Vasculitis            | 0.019        | 0.99                |

---

## 💡 Conclusion and Future Scope
The project successfully demonstrates the potential of AI-driven diagnosis for skin diseases using MobileNet. Future enhancements may include:
- Expanding the system to detect additional types of skin diseases.
- Integrating features like appointment booking and personalized skin care recommendations.

---

## 📜 References
Key literature and prior works consulted for this project include studies on CNN efficiency, transfer learning, and various data mining techniques for skin disease classification.

---

**Thank you for exploring our project! Your feedback and suggestions are welcome.**
