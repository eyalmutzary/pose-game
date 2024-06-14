
import cv2
import mediapipe as mp
import numpy as np
from typing import Dict

from config.constants import ANGLE_JOINTS, DISTANCE_PAIRS, GAPS_PAIRS, POSE_LANDMARKS 
mp_pose = mp.solutions.pose


class FeaturesAnalyzer:
    def __init__(self):

        self.keypoints: Dict[str, Dict[str, float]] = {}
    
    def get_features(self, frame) -> Dict[str, float]:
        with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # Make detection
            results = pose.process(image)
            
            if results.pose_landmarks:
                self.keypoints = FeaturesAnalyzer._extract_keypoints(results)
                angles = self._calculate_angle_features()
                distances = self._calculate_distance_features()
                gaps = self._calculate_gaps()
            
            features_dict = {**angles, **distances, **gaps}
            return features_dict

    
    def _calculate_gaps(self) -> Dict[str, float]:
        """
            Calculate the gaps between body parts to detect misalignment in the pose
        """
        gaps = {}
        for a_name, b_name in GAPS_PAIRS:
            if a_name in self.keypoints and b_name in self.keypoints:
                a = self.keypoints[a_name]
                b = self.keypoints[b_name]
                x_diff = a['x'] - b['x']
                y_diff = a['y'] - b['y']
                gaps[f"{a_name}_{b_name}_x_gap"] = x_diff
                gaps[f"{a_name}_{b_name}_y_gap"] = y_diff
        return gaps
    
    def _calculate_angle_features(self) -> Dict[str, float]:
        angles = {}
        for a_name, b_name, c_name in ANGLE_JOINTS:
            if a_name in self.keypoints and b_name in self.keypoints and c_name in self.keypoints:
                a = self.keypoints[a_name]
                b = self.keypoints[b_name]
                c = self.keypoints[c_name]
                angle = FeaturesAnalyzer._calculate_angle(a, b, c)
                angles[f"{b_name}_angle"] = angle

        # Add angles to the keypoints dictionary
        self.keypoints.update(angles)
        return angles

    def _calculate_distance_features(self) -> Dict[str, float]:
        distances = {}
        for a_name, b_name in DISTANCE_PAIRS:
            if a_name in self.keypoints and b_name in self.keypoints:
                a = self.keypoints[a_name]
                b = self.keypoints[b_name]
                dist = FeaturesAnalyzer._calculate_distance(a, b)
                distances[f"{a_name}_{b_name}_distance"] = dist
        return distances
        
    @staticmethod
    def _calculate_angle(a: Dict[str, float], b: Dict[str, float], c: Dict[str, float]) -> float:
        a = np.array([a['x'], a['y']])
        b = np.array([b['x'], b['y']])
        c = np.array([c['x'], c['y']])
        radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
        angle = np.abs(radians * 180.0 / np.pi)
        if angle > 180.0:
            angle = 360 - angle
        return float(f"{angle:.3f}")

    @staticmethod
    def _calculate_distance(a: Dict[str, float], b: Dict[str, float]) -> float:
        a = np.array([a['x'], a['y']])
        b = np.array([b['x'], b['y']])
        dist = np.linalg.norm(a - b)
        # Scale the distance by image dimensions (640x480) to get pixel distance
        result = dist * np.sqrt(640**2 + 480**2)
        return float(f"{result:.3f}")
    
    @staticmethod
    def _extract_keypoints(image_process_result):
        keypoints = {}
        for idx, landmark in enumerate(image_process_result.pose_landmarks.landmark):
            if idx in POSE_LANDMARKS:
                name = POSE_LANDMARKS[idx]
                keypoints[name] = {
                    'x': landmark.x,
                    'y': landmark.y,
                    'z': landmark.z
                }
        return keypoints