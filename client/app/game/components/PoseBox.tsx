import { useEffect } from 'react'
import styles from './PoseBox.module.css'
import PoseImage from './PoseImage'
import { Poses } from '@/lib/constants'
import LogoText from '@/lib/components/LogoText'
import fireGif from '@/lib/assets/fire.gif'
import Image from 'next/image'

interface PoseBoxProps {
  id: number
  duration: number
  isSpecial: boolean
  isSuccessful: boolean
  removeBox: (id: number) => void
  pose: Poses
}

const PoseBox = ({ id, duration, isSpecial, isSuccessful, removeBox, pose }: PoseBoxProps) => {
  useEffect(() => {
    const timeout = setTimeout(() => {
      removeBox(id)
    }, duration * 1000)

    return () => clearTimeout(timeout)
  }, [])

  return (
    <div
      style={{ animationDuration: `${duration}s` }}
      className={`${styles.box} relative flex items-center shadow-[0_2px_0px_2px_#000000] rounded ${isSuccessful ? 'bg-greenTheme' : isSpecial ? 'bg-darkRedTheme' : 'bg-purpleTheme'} p-2 w-44 h-44 transition`}
    >
      <PoseImage pose={pose} />
      {isSpecial && (
        <>
          <Image src={fireGif} alt={'fire'} className={'absolute -bottom-[20%] -right-[30%] object-contain w-36'} priority/>
          <LogoText className="absolute bottom-0 left-[50%] -rotate-12 text-center text-[4em] !text-redTheme">
            X2
          </LogoText>
        </>
      )}
    </div>
  )
}

export default PoseBox
