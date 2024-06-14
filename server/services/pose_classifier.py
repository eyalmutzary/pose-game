import joblib
from typing import Dict
import numpy as np
from config.constants import FEATURE_ORDER

class PoseClassifier:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PoseClassifier, cls).__new__(cls)
            cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        self.model = joblib.load('pose_classifier.pkl')
    
    def classify_pose(self, features: Dict[str, float]) -> str:
        features_array = PoseClassifier._parse_features_array(features)
        pose_name = self.model.predict(features_array)[0]
        return pose_name
    
    def get_pose_probability(self, features: Dict[str, float], pose_to_check: str) -> float:
        features_array = PoseClassifier._parse_features_array(features)
        probabilities = self.model.predict_proba(features_array)[0]
        classes = self.model.classes_
        if pose_to_check in classes:
            pose_index = list(classes).index(pose_to_check)
            pose_probability = probabilities[pose_index] * 100  # Convert to percentage
        else:
            pose_probability = 0
        return pose_probability
    
    @staticmethod
    def _parse_features_array(features: Dict[str, float]) -> np.ndarray:
        features_list = [features.get(col, 0) for col in FEATURE_ORDER]
        return np.array(features_list).reshape(1, -1)