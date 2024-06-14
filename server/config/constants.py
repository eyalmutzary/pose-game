from mediapipe.python.solutions.pose import PoseLandmark
from typing import Dict, List, Tuple
from mediapipe.python.solutions.pose import PoseLandmark

POSE_LANDMARKS: Dict[PoseLandmark, str] = {
    PoseLandmark.NOSE: "nose",
    PoseLandmark.LEFT_EAR: "left_ear",
    PoseLandmark.RIGHT_EAR: "right_ear",
    PoseLandmark.LEFT_SHOULDER: "left_shoulder",
    PoseLandmark.RIGHT_SHOULDER: "right_shoulder",
    PoseLandmark.LEFT_ELBOW: "left_elbow",
    PoseLandmark.RIGHT_ELBOW: "right_elbow",
    PoseLandmark.LEFT_WRIST: "left_wrist",
    PoseLandmark.RIGHT_WRIST: "right_wrist",
    PoseLandmark.LEFT_INDEX: "left_index",
    PoseLandmark.RIGHT_INDEX: "right_index",
    PoseLandmark.LEFT_HIP: "left_hip",
    PoseLandmark.RIGHT_HIP: "right_hip",
    PoseLandmark.LEFT_KNEE: "left_knee",
    PoseLandmark.RIGHT_KNEE: "right_knee",
    PoseLandmark.LEFT_ANKLE: "left_ankle",
    PoseLandmark.RIGHT_ANKLE: "right_ankle",
    PoseLandmark.LEFT_FOOT_INDEX: "left_foot_index",
    PoseLandmark.RIGHT_FOOT_INDEX: "right_foot_index",
}

# Define the joints we want to calculate angles for
ANGLE_JOINTS: List[Tuple[str, str, str]] = [
    ("left_hip", "left_shoulder", "left_elbow"),  # Left shoulder angle
    ("right_hip", "right_shoulder", "right_elbow"),  # Right shoulder angle
    ("left_shoulder", "left_elbow", "left_wrist"),  # Left elbow angle
    ("right_shoulder", "right_elbow", "right_wrist"),  # Right elbow angle
    ("left_hip", "left_knee", "left_ankle"),  # Left knee angle
    ("right_hip", "right_knee", "right_ankle"),  # Right knee angle
    ("left_shoulder", "left_hip", "left_knee"),  # Left hip angle
    ("right_shoulder", "right_hip", "right_knee"),  # Right hip angle
    ("left_index", "left_wrist", "left_elbow"),  # Left wrist angle
    ("right_index", "right_wrist", "right_elbow"),  # Right wrist angle
]

DISTANCE_PAIRS: List[Tuple[str, str]] = [
    ("left_wrist", "right_wrist"),  # Distance between wrists
    ("left_ankle", "right_ankle"),  # Distance between ankles
    ("left_shoulder", "right_shoulder"),  # Shoulder width
    ("left_hip", "right_hip"),  # Hip width
    ("left_knee", "right_knee"),  # Distance between knees
    ("left_elbow", "right_elbow"),  # Distance between elbows
    ("nose", "left_ankle"),  # Height (approximated)
    ("nose", "right_ankle"),  # Height (approximated)
    ("left_wrist", "left_ankle"),  # Left body length
    ("right_wrist", "right_ankle"),  # Right body length
    ("left_wrist", "left_hip"),  # Left upper body length
    ("right_wrist", "right_hip"),  # Right upper body length
    ("left_shoulder", "left_hip"),  # Left torso length
    ("right_shoulder", "right_hip"),  # Right torso length
]

GAPS_PAIRS: List[Tuple[str, str]] = [
    ("left_ear", "left_ankle"),
    ("right_ear", "right_ankle"),
    ("left_wrist", "left_ankle"),
    ("right_wrist", "right_ankle"),
    ("left_shoulder", "left_hip"),
    ("right_shoulder", "right_hip"),
    ("left_knee", "left_ankle"),
    ("right_knee", "right_ankle"),
]


FEATURE_ORDER: List[str] = [
    "left_shoulder_angle",
    "right_shoulder_angle",
    "left_elbow_angle",
    "right_elbow_angle",
    "left_knee_angle",
    "right_knee_angle",
    "left_hip_angle",
    "right_hip_angle",
    "left_wrist_angle",
    "right_wrist_angle",
    "left_wrist_right_wrist_distance",
    "left_ankle_right_ankle_distance",
    "left_shoulder_right_shoulder_distance",
    "left_hip_right_hip_distance",
    "left_knee_right_knee_distance",
    "left_elbow_right_elbow_distance",
    "nose_left_ankle_distance",
    "nose_right_ankle_distance",
    "left_wrist_left_ankle_distance",
    "right_wrist_right_ankle_distance",
    "left_wrist_left_hip_distance",
    "right_wrist_right_hip_distance",
    "left_shoulder_left_hip_distance",
    "right_shoulder_right_hip_distance",
    "left_ear_left_ankle_x_gap",
    "left_ear_left_ankle_y_gap",
    "right_ear_right_ankle_x_gap",
    "right_ear_right_ankle_y_gap",
    "left_wrist_left_ankle_x_gap",
    "left_wrist_left_ankle_y_gap",
    "right_wrist_right_ankle_x_gap",
    "right_wrist_right_ankle_y_gap",
    "left_shoulder_left_hip_x_gap",
    "left_shoulder_left_hip_y_gap",
    "right_shoulder_right_hip_x_gap",
    "right_shoulder_right_hip_y_gap",
    "left_knee_left_ankle_x_gap",
    "left_knee_left_ankle_y_gap",
    "right_knee_right_ankle_x_gap",
    "right_knee_right_ankle_y_gap",
]
