'use client'
import React, { useEffect, useState } from 'react'
import WebsiteScreen from '@/lib/components/WebsiteScreen'
import VideoFilter from './components/VideoFilter'
import Container from '@/lib/components/Container'
import PoseSlider from './components/PoseSlider'
import { Poses } from '@/lib/constants'
import { Button } from '@/lib/components/Button'
import CountdownTimer from '@/lib/components/CountdownTimer'

export type Box = {
  duration: number
  pose: Poses
}

const CREATE_BOX_INTERVAL = 4000

export default function Home() {
  const [boxes, setBoxes] = useState<{ [id: number]: Box }>({})
  const [score, setScore] = useState(0)
  const [currentPose, setCurrentPose] = useState(null)

  const gameLoop = () => {
    setInterval(() => {
      createBox(10)
    }, CREATE_BOX_INTERVAL)
  }

  useEffect(() => {
    gameLoop()
  }, [])

  useEffect(() => {
    // checks if the current pose in one of the boxes
    const boxIds = Object.keys(boxes)
    console.log('boxIds', boxIds)
    for (const id of boxIds) {
      if (boxes[Number(id)].pose === currentPose) {
        setScore((prevScore) => prevScore + 1)
        removeBox(Number(id))
        break
      }
    }
  }, [currentPose])

  const createBox = (duration: number): void => {
    const values = Object.values(Poses)
    const randomIndex = Math.floor(Math.random() * values.length)
    const randomValue = values[randomIndex]
    setBoxes((prevBoxes) => {
      const id = Date.now()
      // check if there is a box with a time of less than 1 second to avoid overlapping
      for (const other_id of Object.keys(prevBoxes)) {
        if (id - Number(other_id) < 500) {
          return prevBoxes
        }
      }

      return {
        ...prevBoxes,
        [id]: { duration, pose: randomValue },
      }
    })
  }

  const removeBox = (id: number): void => {
    setBoxes((prevBoxes) => {
      const newBoxes = { ...prevBoxes }
      delete newBoxes[id]
      return newBoxes
    })
  }

  return (
    <WebsiteScreen className={'flex flex-col items-center justify-center gap-6'}>
      <Container className="fixed px-3 py-2 text-xl cursor-pointer left-4 top-4">X</Container>
      <div className="flex items-end justify-between min-w-[80vw]">
        <Container className="p-2 text-xl">Score: {score}</Container>
        <Container>
          <VideoFilter setCurrentPose={setCurrentPose} />
        </Container>
        <Container className="p-2 text-xl">
          Time left: <CountdownTimer time={60} />
        </Container>
      </div>
      <PoseSlider boxes={boxes} removeBox={removeBox} />
    </WebsiteScreen>
  )
}
