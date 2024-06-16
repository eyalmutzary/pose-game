import React, { useRef, useEffect, useState } from 'react';
import Webcam from "react-webcam";
import axios from 'axios';

const VideoFilter = () => {
    const webcamRef = useRef(null);
    const [currentPose, setCurrentPose] = useState(null);
  
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
        // if (imageSrc) {
        //   try {
        //     const response = await axios.post('https://ubuvdip2130:8001/images/analyze', { image: imageSrc })
        //     // const data = await response.json();
        //     console.log(response.data);
        //     setCurrentPose(response.data.data ?? "None");
        //   } catch (error) {
        //     console.error('Error sending image:', error);
        //   }
        // }
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
              borderRadius: 2,
              // position: "absolute",
              // marginLeft: "auto",
              // marginRight: "auto",
              // left: 0,
              // right: 0,
              // textAlign: "center",
              // zindex: 1,
              // width: 640,
              // height: 480,
            }}
          />
        </header>
        <div>
          <h1 className={'bg-red-600 text-7xl'}>{currentPose}</h1>
        </div>
      </div>
    );
};

export default VideoFilter;