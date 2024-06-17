'use client'
import React, { useEffect, useState } from 'react'
import WebsiteScreen from '@/lib/components/WebsiteScreen'
import VideoFilter from './components/VideoFilter'
import Container from '@/lib/components/Container'
import PoseSlider from './components/PoseSlider'
import { Poses } from '@/lib/constants'
import { Button } from '@/lib/components/Button'
import CountdownTimer from '@/lib/components/CountdownTimer'
import LogoText from '@/lib/components/LogoText'
import BackdropTimer from './components/BackdropTimer'
import Gameover from './components/Gameover'
import Link from 'next/link'

export type Box = {
  duration: number
  pose: Poses
  isSpecial: boolean
  isSuccessful: boolean
}

const CREATE_BOX_INTERVAL = 3000
const GAME_DURATION = 60
const PRE_GAME_COUNTDOWN = 3
const BOX_BASE_LIFETIME = 8
const MIN_BOX_LIFETIME = 4
const BASE_BOX_SCORE = 1
const SPECIAL_BOX_SCORE = 2
const SPECIAL_BOX_PROBABILITY = 0.8

export default function Home() {
  const [boxes, setBoxes] = useState<{ [id: number]: Box }>({})
  const [score, setScore] = useState(0)
  const [currentPose, setCurrentPose] = useState(null)
  const [isGameOver, setIsGameOver] = useState(false)

  const boxCreator = () => {
    const boxCreatorInterval = setInterval(() => {
      createBox()
    }, CREATE_BOX_INTERVAL)
    return boxCreatorInterval
  }

  useEffect(() => {
    const boxCreatorInterval = boxCreator()
    setTimeout(
      () => {
        setIsGameOver(true)
        clearInterval(boxCreatorInterval)
      },
      (GAME_DURATION + PRE_GAME_COUNTDOWN) * 1000
    )
  }, [])

  useEffect(() => {
    handleDidPose()
  }, [currentPose])

  const handleDidPose = () => {
    // checks if the current pose in one of the boxes
    // If so, deletes the box and update the points
    const boxIds = Object.keys(boxes)

    for (const id of boxIds) {
      if (boxes[Number(id)].pose === currentPose) {
        if (boxes[Number(id)].isSpecial) {
          setScore((prevScore) => prevScore + SPECIAL_BOX_SCORE)
        } else {
          setScore((prevScore) => prevScore + BASE_BOX_SCORE)
        }
        setSuccessfulBox(Number(id))
        break
      }
    }
  }

  const createBox = (): void => {
    const boxValues = defineRandomBox()
    setBoxes((prevBoxes) => {
      const id = Date.now()
      // check if there is a box with a time of less than 1 second to avoid overlapping (edge case)
      for (const other_id of Object.keys(prevBoxes)) {
        if (id - Number(other_id) < 500) {
          return prevBoxes
        }
      }

      return {
        ...prevBoxes,
        [id]: boxValues,
      }
    })
  }

  const defineRandomBox = (): Box => {
    const values = Object.values(Poses)
    const randomIndex = Math.floor(Math.random() * values.length)
    const randomPose = values[randomIndex]
    const isSpecial = Math.random() > (1-SPECIAL_BOX_PROBABILITY)
    if (isSpecial) {
      return { duration: MIN_BOX_LIFETIME, pose: randomPose, isSpecial: true, isSuccessful: false}
    }
    const duration = Math.max(
      BOX_BASE_LIFETIME - Math.floor(Math.random() * (score / 3)),
      MIN_BOX_LIFETIME
    )
    return { duration, pose: randomPose, isSpecial: false, isSuccessful: false }
  }

  const setSuccessfulBox = (id: number): void => {
    setBoxes((prevBoxes) => {
      const newBoxes = { ...prevBoxes }
      newBoxes[id].isSuccessful = true
      return newBoxes
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
    <WebsiteScreen className={'flex flex-col items-center justify-center gap-6 '}>
      <BackdropTimer time={PRE_GAME_COUNTDOWN} />
      <Container className="fixed z-50 px-3 py-2 text-xl cursor-pointer left-4 top-4">
        <Link href="/">X</Link>
      </Container>
      {!isGameOver && (
        <div className="flex items-end justify-between min-w-[80vw]">
          <Container className="p-2 text-xl">Score: {score}</Container>
          <Container className="w-[640px] h-[480px]">
            <VideoFilter setCurrentPose={setCurrentPose} />
          </Container>
          <Container className="p-2 text-xl">
            Time left: <CountdownTimer time={GAME_DURATION + PRE_GAME_COUNTDOWN} />
          </Container>
        </div>
      )}
      {!isGameOver && <PoseSlider boxes={boxes} removeBox={removeBox} />}
      {isGameOver && <Gameover score={score} />}
    </WebsiteScreen>
  )
}
