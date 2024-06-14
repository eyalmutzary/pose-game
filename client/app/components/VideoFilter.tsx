import React, { useRef, useEffect } from 'react';
import Webcam from "react-webcam";
import axios from 'axios';

const VideoFilter = () => {
    const webcamRef = useRef(null);
    const canvasRef = useRef(null);
  
    // Main function
    const runCoco = async () => {
      await detect();
      setInterval(async () => {
        await detect();
      }, 1000);
    };
  
    const detect = async () => {
      // Check data is available
      if (
        typeof webcamRef.current !== "undefined" &&
        webcamRef.current !== null &&
        webcamRef.current.video.readyState === 4
      ) {
        // Get Video Properties
        const video = webcamRef.current.video;
        const videoWidth = webcamRef.current.video.videoWidth;
        const videoHeight = webcamRef.current.video.videoHeight;
  
        // Set video width
        webcamRef.current.video.width = videoWidth;
        webcamRef.current.video.height = videoHeight;
        
        const imageSrc = webcamRef.current.getScreenshot();

        // Send the image to the server
        if (imageSrc) {
          try {
            const response = await axios.post('https://ubuvdip2130:8001/images/analyze', { image: imageSrc })
            // const data = await response.json();
            console.log(response.data);
          } catch (error) {
            console.error('Error sending image:', error);
          }
        }
        // Set canvas height and width
        // canvasRef.current.width = videoWidth;
        // canvasRef.current.height = videoHeight;
  
        // Make Detections
        // const obj = await net.detect(video);
  
        // Draw mesh
        // const ctx = canvasRef.current.getContext("2d");
        // drawRect(obj, ctx); 
      }
    };
  
    useEffect(()=>{runCoco()},[]);
  
    return (
      <div className="App">
        <header className="App-header">
          <Webcam
            ref={webcamRef}
            muted={true} 
            style={{
              position: "absolute",
              marginLeft: "auto",
              marginRight: "auto",
              left: 0,
              right: 0,
              textAlign: "center",
              zindex: 9,
              width: 640,
              height: 480,
            }}
          />
  
          <canvas
            ref={canvasRef}
            style={{
              position: "absolute",
              marginLeft: "auto",
              marginRight: "auto",
              left: 0,
              right: 0,
              textAlign: "center",
              zindex: 8,
              width: 640,
              height: 480,
            }}
          />
        </header>
      </div>
    );
};

export default VideoFilter;