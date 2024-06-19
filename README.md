# Pose Rush

Pose Rush is an interactive game where players must mimic running postures displayed on the screen. The more accurately and quickly you mimic the postures, the more points you earn. As you accumulate points, the game's difficulty increases, adding to the challenge and excitement. Some postures are worth double points, so stay alert!

## Video Demo

### [Full gameplay](https://www.youtube.com/watch?v=QJji96QjGp4).

![](https://github.com/eyalmutzary/pose-game/blob/main/main_page.png)


## Features

- **Engaging Gameplay:** Mimic the running postures on the screen to score points.
- **Increasing Difficulty:** The game becomes more challenging as you earn more points.
- **Double Points:** Certain postures are worth double points, adding a strategic element to the game.
- **Advanced Pose Detection:** Utilizes computer vision and machine learning for accurate posture detection.

## Technologies Used

- **Computer Vision:** Utilizes the Mediapipe library to analyze body parts.
- **Machine Learning:** A random forest model classifies postures based on features such as angles (e.g., elbow angle), distances (e.g., wrist distances), and horizontal gaps.
- **UI/UX Design:** Designed using Figma ([link](https://www.figma.com/design/5Uv3KvVsthIiGs3kLwrhdx/Pose-Game?node-id=0-1&t=wZusfnSXqgL62XnC-1)).
- **Frontend:** Built with React (NextJS).
- **Backend:** FastAPI server processes images and returns detected postures.

## How It Works

1. **Pose Detection:** The Mediapipe library analyzes body parts from images.
2. **Feature Engineering:** Custom dataset creation with features like angles, distances, and gaps.
3. **Model Training:** A random forest model is trained to classify the postures.
4. **UI Design:** Figma was used to design the user interface.
5. **Server-Client Interaction:** 
   - The FastAPI server receives images and returns the detected postures.
   - The React (NextJS) client handles gameplay mechanics, displaying postures, and scoring.

## Installation Locally

To get started with Pose Rush, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/eyalmutzary/pose-game.git
    ```

2. Install the backend dependencies:
    ```bash
    cd server
    pip install -r requirements.txt
    ```

3. Install the frontend dependencies:
    ```bash
    cd ../client
    npm install
    ```

4. Run the backend server:
    ```bash
    cd ../server
    uvicorn main:app --reload
    ```

5. Run the frontend:
    ```bash
    cd ../client
    npm start
    ```

## Installation with Docker

To get started with Pose Rush, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/eyalmutzary/pose-game.git
    ```

2. Install the backend dependencies:
    ```bash
    cd docker
    docker-compose up --build
    ```
    

## Usage

- Open your web browser and navigate to `https://localhost:3000` to start playing Pose Rush.
- Notice: you need to have both client and server running on https. For client, add --experimental-https on package.json. For server, you should generate a local cetificate.
