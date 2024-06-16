'use client'
import React, { useEffect } from 'react'
import WebsiteScreen from '@/lib/components/WebsiteScreen'
import Logo from './components/Logo'
import { Button } from '@/lib/components/Button'
import Link from 'next/link'

export default function Home() {
  return (
    <WebsiteScreen className={'flex'}>
      <div className={'flex flex-col items-center justify-center h-full w-full gap-8'}>
        <Logo />
        <Button onClick={() => {}}>
          <Link href="/game">
            Play
          </Link>
        </Button>
        <Button onClick={() => {}}>
          <Link href="/leaderboard">
            Leaderboard
          </Link>
        </Button>
      </div>
    </WebsiteScreen>
  )
}
