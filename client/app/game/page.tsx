'use client'
import React, { useEffect } from 'react'
import WebsiteScreen from '@/lib/components/WebsiteScreen'
import VideoFilter from './components/VideoFilter'
import Container from '@/lib/components/Container'
import PoseSlider from './components/PoseSlider'


export default function Home() {
  return (
    <WebsiteScreen className={'flex flex-col items-center justify-center gap-6'}>
        <Container>
            {/* <VideoFilter /> */}
        </Container>
        <PoseSlider />
    </WebsiteScreen>
  )
}
