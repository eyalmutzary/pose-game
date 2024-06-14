import joblib
from typing import Dict, List
import numpy as np
from config.constants import FEATURE_ORDER, PREDICTION_THRESHOLD

class PoseClassifier:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PoseClassifier, cls).__new__(cls)
            cls._instance.__initialize()
        return cls._instance

    def __initialize(self):
        self.model = joblib.load('pose_classifier.pkl')
    
    def classify_pose(self, features: Dict[str, float]) -> str | None:
        features_array = PoseClassifier._parse_features_array(features)
        probabilities: np.ndarray = self.model.predict_proba(features_array)[0]
        classes = self.model.classes_
        max_prob = max(probabilities)
        max_prob_index = list(probabilities).index(max_prob)
        max_prob_pose = classes[max_prob_index]
        return max_prob_pose if max_prob > PREDICTION_THRESHOLD else None
    
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
    
    def get_all_poses_names(self) -> List[str]:
        return list(self.model.classes_)
    
    @staticmethod
    def _parse_features_array(features: Dict[str, float]) -> np.ndarray:
        features_list = [features.get(col, 0) for col in FEATURE_ORDER]
        return np.array(features_list).reshape(1, -1)
    
    @staticmethod
    def _get_max_value_index(probabilities: List[float]) -> int:
        max_value = max(probabilities)
        return probabilities.index(max_value)