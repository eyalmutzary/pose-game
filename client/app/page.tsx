'use client'
import React, { useEffect } from 'react'
import WebsiteScreen from '@/lib/components/WebsiteScreen'
import VideoFilter from './components/VideoFilter'
import Logo from './components/Logo'
import { Button } from '@/lib/components/Button'

export default function Home() {
  return (
    <WebsiteScreen className={'flex'}>
      <div className={'flex flex-col items-center justify-center h-full w-full gap-8'}>
        <Logo />
        <Button onClick={() => {}}>Start</Button>
        <Button onClick={() => {}}>Leaderboard</Button>
      </div>
    </WebsiteScreen>
  )
}
