import '@/globals.css'
import type { ReactNode } from 'react'
import NavBar from './NavBar'

interface Props {
  children?: ReactNode[] | ReactNode
  className?: string
}

export default function WebsiteScreen({ children, className }: Props) {
  return (
    <>
      <NavBar />
      <main className={`min-h-[calc(100vh-5.5rem)] overflow-auto ${className}`}>
        {children}
      </main>
    </>
  )
}
