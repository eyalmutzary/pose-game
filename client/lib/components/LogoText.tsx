import { ReactNode } from 'react'
import styles from './LogoText.module.css'

interface Props {
    children?: ReactNode[] | ReactNode
    className?: string
  }

const LogoText = ({ children, className }: Props) => {
  return (
    <span className={`font-bold font-secondary text-purpleTheme  ${styles.bigLogo} ${className}`}>
      {children}
    </span>
  )
}

export default LogoText
