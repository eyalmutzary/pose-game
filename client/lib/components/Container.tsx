import React, { ReactNode } from 'react'
import styles from './Container.module.css'

type ContainerProps = {
  children: ReactNode
  className?: string
  onClick?: () => void
}

export const Container = ({ children, className, ...rest }: ContainerProps) => {
  return (
    <div
      className={`bg-yellowTheme border-orangeTheme ${styles.containerProps} ${className}`}
      {...rest}
    >
      {children}
    </div>
  )
}
export default Container
