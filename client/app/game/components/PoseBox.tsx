import { useEffect } from 'react'
import styles from './PoseBox.module.css'
import PoseImage from './PoseImage'
import { Poses } from '@/lib/constants'


interface PoseBoxProps {
  id: number;
  duration: number;
  removeBox: (id: number) => void;
  pose: Poses;
}

const PoseBox = ({ id, duration, removeBox, pose }: PoseBoxProps) => {
  useEffect(() => {
    const timeout = setTimeout(() => {
      removeBox(id)
    }, duration * 1000)

    return () => clearTimeout(timeout)
  }, [])

  return (
    <div
      style={{ animationDuration: `${duration}s` }}
      className={`${styles.box} flex items-center shadow-[0_2px_0px_2px_#000000] rounded bg-purpleTheme p-2 w-44 h-44`}
    >
      <PoseImage pose={pose} />
    </div>
  )
}

export default PoseBox
