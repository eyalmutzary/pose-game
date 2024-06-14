import '@/globals.css'
import type { ReactNode } from 'react'
import backgroundImage from '@/lib/assets/background.jpg'

interface Props {
  children?: ReactNode[] | ReactNode
  className?: string
}

export default function WebsiteScreen({ children, className }: Props) {
  return (
    <>
      <main 
      className={`overflow-auto ${className} bg-cover bg-no-repeat bg-top h-screen w-screen`}
      style={{ backgroundImage: `url(${backgroundImage.src})` }}
      >
        {children}
      </main>
    </>
  )
}
