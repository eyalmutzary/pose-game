import { useEffect, useState } from 'react'

const CountdownTimer = ({time}: {time: number}) => {
  const [seconds, setSeconds] = useState(time)

  useEffect(() => {
    if (seconds > 0) {
      const timerId = setTimeout(() => {
        setSeconds(seconds - 1)
      }, 1000)
      return () => clearTimeout(timerId)
    }
  }, [seconds])

  return <span>{seconds}</span>
}

export default CountdownTimer
