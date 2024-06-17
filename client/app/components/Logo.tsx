import React from 'react'
import styles from './Logo.module.css'
import LogoText from '@/lib/components/LogoText'

export const Logo = () => {
  return (
    <div>
      <div className="flex flex-col pb-4 text-center">
        <LogoText className={'text-[4.75em]'}>POSE</LogoText>
        <LogoText className={'text-[6em]'}>RUSH</LogoText>
      </div>
    <span className={`font-bold text-[1.75em] text-neutral-50 ${styles.smallLogo}`}>Sweat Your Way to Victory</span>
    </div>
  )
}

export default Logo
