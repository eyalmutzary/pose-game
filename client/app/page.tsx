'use client'
import React, { useEffect } from 'react'
import WebsiteScreen from '@/lib/components/WebsiteScreen'
import axios from 'axios'

export default function Home() {

  const sendRequest = async () => {
    try {
        const response = await axios.get(`${process.env.NEXT_PUBLIC_SERVER_URL}/tests`);
        console.log(response.data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
  };

  useEffect(() => {
      sendRequest();
  }, []);

  return (
    <WebsiteScreen className={'flex'}>
      <div>Hello world!</div>
    </WebsiteScreen>
  )
}
