# model_training.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import matplotlib.pyplot as plt
import seaborn as sns
import os


class CropRecommendationModel:
    def __init__(self):
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        # Kaggle dataset features
        self.feature_names = ['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']

    def load_data(self, filepath='data/Crop_recommendation.csv'):
        """Load the Kaggle crop dataset"""
        print(f"Loading data from {filepath}...")

        if not os.path.exists(filepath):
            print(f"❌ File not found: {filepath}")
            print("Please download from: https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset")
            return None

        df = pd.read_csv(filepath)
        print(f"✓ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

        # Display column names to verify
        print(f"✓ Columns: {list(df.columns)}")

        return df

    def prepare_data(self, df):
        """Split features and target"""
        # Kaggle dataset uses 'label' as target column
        X = df[self.feature_names]
        y = df['label']

        print(f"✓ Features prepared: {X.shape}")
        print(f"✓ Target prepared: {y.shape}")
        print(f"✓ Number of crops: {y.nunique()}")
        print(f"✓ Crops: {sorted(y.unique())}")

        return X, y

    def train(self, X, y, test_size=0.2, random_state=42):
        """Train the Random Forest model"""
        print("\n" + "=" * 60)
        print("TRAINING MODEL")
        print("=" * 60)

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state, stratify=y
        )

        print(f"Training set: {X_train.shape[0]} samples")
        print(f"Test set: {X_test.shape[0]} samples")

        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)

        # Train Random Forest
        print("\nTraining Random Forest Classifier...")
        self.model = RandomForestClassifier(
            n_estimators=100,
            random_state=random_state,
            max_depth=15,
            min_samples_split=5,
            n_jobs=-1
        )

        self.model.fit(X_train_scaled, y_train)
        print("✓ Model trained successfully!")

        # Evaluate
        y_pred = self.model.predict(X_test_scaled)
        accuracy = accuracy_score(y_test, y_pred)

        print("\n" + "=" * 60)
        print("MODEL EVALUATION")
        print("=" * 60)
        print(f"Accuracy: {accuracy * 100:.2f}%")
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))

        # Plot confusion matrix
        self.plot_confusion_matrix(y_test, y_pred)

        # Feature importance
        self.plot_feature_importance()

        return accuracy

    def plot_confusion_matrix(self, y_test, y_pred):
        """Plot confusion matrix"""
        cm = confusion_matrix(y_test, y_pred)

        plt.figure(figsize=(14, 12))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=sorted(self.model.classes_),
                    yticklabels=sorted(self.model.classes_),
                    cbar_kws={'label': 'Count'})
        plt.title('Confusion Matrix - Crop Prediction', fontsize=16, fontweight='bold', pad=20)
        plt.ylabel('Actual Crop', fontsize=12)
        plt.xlabel('Predicted Crop', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.yticks(rotation=0)
        plt.tight_layout()
        plt.savefig('static/confusion_matrix.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Confusion matrix saved to: static/confusion_matrix.png")

    def plot_feature_importance(self):
        """Plot feature importance"""
        importances = self.model.feature_importances_
        indices = np.argsort(importances)[::-1]

        plt.figure(figsize=(10, 6))
        colors = plt.cm.viridis(np.linspace(0, 1, len(importances)))
        plt.title("Feature Importances in Crop Prediction", fontsize=16, fontweight='bold', pad=20)
        bars = plt.bar(range(len(importances)), importances[indices], color=colors)
        plt.xticks(range(len(importances)),
                   [self.feature_names[i] for i in indices],
                   rotation=45, ha='right')
        plt.ylabel('Importance Score', fontsize=12)
        plt.xlabel('Features', fontsize=12)
        plt.grid(axis='y', alpha=0.3)

        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2., height,
                     f'{height:.3f}',
                     ha='center', va='bottom', fontsize=9)

        plt.tight_layout()
        plt.savefig('static/feature_importance.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✓ Feature importance saved to: static/feature_importance.png")

    def predict(self, input_data):
        """
        Predict crop for given input
        input_data: dict with keys N, P, K, temperature, humidity, ph, rainfall
        """
        # Convert to DataFrame
        input_df = pd.DataFrame([input_data])

        # Scale features
        input_scaled = self.scaler.transform(input_df[self.feature_names])

        # Predict
        prediction = self.model.predict(input_scaled)[0]
        probabilities = self.model.predict_proba(input_scaled)[0]

        # Get all crops with probabilities
        crops_proba = list(zip(self.model.classes_, probabilities))
        crops_proba.sort(key=lambda x: x[1], reverse=True)

        return prediction, crops_proba

    def save_model(self, model_path='models/crop_model.pkl',
                   scaler_path='models/scaler.pkl'):
        """Save trained model and scaler"""
        # Create models directory if doesn't exist
        os.makedirs('models', exist_ok=True)

        with open(model_path, 'wb') as f:
            pickle.dump(self.model, f)

        with open(scaler_path, 'wb') as f:
            pickle.dump(self.scaler, f)

        print(f"\n✓ Model saved to: {model_path}")
        print(f"✓ Scaler saved to: {scaler_path}")

    def load_model(self, model_path='models/crop_model.pkl',
                   scaler_path='models/scaler.pkl'):
        """Load trained model and scaler"""
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)

        with open(scaler_path, 'rb') as f:
            self.scaler = pickle.load(f)

        print("✓ Model loaded successfully!")


# Train the model
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("CROP RECOMMENDATION MODEL TRAINING")
    print("Using Kaggle Dataset")
    print("=" * 60 + "\n")

    # Create static directory for plots
    os.makedirs('static', exist_ok=True)

    # Initialize model
    model = CropRecommendationModel()

    # Load data
    df = model.load_data()

    if df is not None:
        # Display dataset info
        print("\n" + "=" * 60)
        print("DATASET INFORMATION")
        print("=" * 60)
        print(f"\nDataset shape: {df.shape}")
        print(f"\nCrop distribution:")
        print(df['label'].value_counts())
        print(f"\nDataset summary:")
        print(df.describe().round(2))

        # Prepare data
        X, y = model.prepare_data(df)

        # Train model
        accuracy = model.train(X, y)

        # Save model
        model.save_model()

        # Test prediction
        print("\n" + "=" * 60)
        print("TESTING PREDICTION")
        print("=" * 60)

        test_input = {
            'N': 90,
            'P': 42,
            'K': 43,
            'temperature': 20.87,
            'humidity': 82.00,
            'ph': 6.50,
            'rainfall': 202.93
        }

        print("\nTest Input:")
        for key, value in test_input.items():
            print(f"  {key}: {value}")

        prediction, probabilities = model.predict(test_input)

        print(f"\n🌾 Recommended Crop: {prediction}")
        print("\nTop 5 Recommendations with Confidence:")
        for i, (crop, prob) in enumerate(probabilities[:5], 1):
            print(f"  {i}. {crop}: {prob * 100:.2f}%")

        print("\n" + "=" * 60)
        print("✓ MODEL TRAINING COMPLETE!")
        print("=" * 60)
    else:
        print("\n❌ Dataset not found! Please download it from Kaggle.")