import React from 'react'
import styles from './Logo.module.css'

export const Logo = () => {
  return (
    <div>
      <div className="flex flex-col pb-4 text-center">
        <span className={`font-bold text-[6.875em] text-purpleTheme ${styles.bigLogo}`}>POSE</span>
        <span className={`font-bold text-[8em] text-purpleTheme ${styles.bigLogo}`}>RUSH</span>
      </div>
    <span className={`font-bold text-[1.75em] text-neutral-50 ${styles.smallLogo}`}>Sweat Your Way to Victory</span>
    </div>
  )
}

export default Logo
