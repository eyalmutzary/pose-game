import Container from '@/lib/components/Container'
import Image from 'next/image'
import pose from '@/lib/assets/poses/high-bridge-output_image.png'
import { useEffect, useRef } from 'react'
import styles from './PoseBox.module.css'

const PoseBox = ({ id, duration, removeBox }) => {
  useEffect(() => {
    const timeout = setTimeout(() => {
      removeBox(id)
    }, duration * 1000)

    return () => clearTimeout(timeout)
  }, [id, duration, removeBox])

  return (
    <div
      style={{ animationDuration: `${duration}s` }}
      className={`${styles.box} flex items-center shadow-[0_2px_0px_2px_#000000] rounded bg-purpleTheme p-2 w-32 h-32`}
    >
      <Image src={pose} alt={'high-bridge'} />
    </div>
  )
}

export default PoseBox
