import '@/globals.css'
import type { Metadata } from 'next'
import type { ReactNode } from 'react'

export const metadata: Metadata = {
  title: 'Test Creator',
}

const RootLayout = ({ children }: { children: ReactNode })  => {
  return (
    <html data-theme="light">
      <body className="font-primary">{children}</body>
    </html>
  )
}

export default RootLayout
