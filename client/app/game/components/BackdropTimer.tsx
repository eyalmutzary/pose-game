import { useEffect, useState } from 'react'
import CountdownTimer from '@/lib/components/CountdownTimer'
import LogoText from '@/lib/components/LogoText'
import Backdrop from '@/lib/components/Backdrop'
// import Backdrop from '@/lib/components/Backdrop'

const BackdropTimer = ({time}: {time: number}) => {
  const [showBackdrop, setShowBackdrop] = useState(true)

  useEffect(() => {
    const timer = setTimeout(() => {
      setShowBackdrop(false)
    }, 3000) // Remove the component after 3 seconds (3000 milliseconds)

    return () => clearTimeout(timer) // Clean up the timer on component unmount
  }, [])

  if (!showBackdrop) {
    return null // Return null to remove the component from the DOM
  }

  return (
    <>
      <LogoText className={'fixed z-50 flex items-center justify-center text-[4.75em]'}>
        <CountdownTimer time={time} />
      </LogoText>
      <Backdrop />
    </>
  )
}

export default BackdropTimer
