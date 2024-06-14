'use client'
import React, { useEffect } from 'react'
import WebsiteScreen from '@/lib/components/WebsiteScreen'
import VideoFilter from './components/VideoFilter';


export default function Home() {


  return (
    <WebsiteScreen className={'flex'}>
      <div>Hello world!</div>
      <VideoFilter />
    </WebsiteScreen>
  )
}
