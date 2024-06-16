import Container from '@/lib/components/Container'
import PoseBox from './PoseBox'
import { useEffect, useState } from 'react'
import styles from './PoseSlider.module.css'

const PoseSlider = () => {
  const [boxes, setBoxes] = useState([])

  const createBox = (duration) => {
    setBoxes((prevBoxes) => [...prevBoxes, { id: Date.now(), duration }])
  }

  const removeBox = (id) => {
    setBoxes((prevBoxes) => prevBoxes.filter((box) => box.id !== id))
  }

  return (
    <Container className={`min-w-[80vw] flex relative overflow-hidden min-h-40`}>
      {boxes.map((box) => (
        <PoseBox key={box.id} id={box.id} duration={box.duration} removeBox={removeBox} />
      ))}
      <button onClick={() => createBox(5)}>Create 5s Box</button>
      <button onClick={() => createBox(10)}>Create 10s Box</button>
    </Container>
  )
}

export default PoseSlider
