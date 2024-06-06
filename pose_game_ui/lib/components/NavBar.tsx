import Link from 'next/link'
import Image from 'next/image'
import { PlusIcon } from '@heroicons/react/24/solid'
import { useCallback, useEffect, useRef, useState } from 'react'
import { BaseServerResponse } from '../types/ServerTypes'
import axios from 'axios'

const LinkClasses = 'hover:bg-base-200 px-2 py-1 rounded-md hover:link'

const NavBar = () => {

  // const getSchemaVersion = useCallback(async () => {
  //   try {
  //     const { data }: { data: BaseServerResponse<{schema_version: string}> } = await axios.get(
  //       APIRoutes.GET_TEST_SCHEMA_VERSION
  //     )
  //     setSchemaVersion(data?.data?.schema_version ?? 'Unknown version')
  //   } catch {
  //     console.error('Error fetching tests')
  //     setSchemaVersion('Unknown version')
  //   }
  // }, [])

  return (
    <nav className="sticky top-0 z-10 flex justify-between p-5 shadow-md bg-base-100">
      <div className="flex items-center">
        <Link href="/">
          <img src="https://dummyimage.com/600x400/808080/0011ff&text=Logo" alt="Logo" className="h-10" />
        </Link>
        <div className="divider divider-horizontal" />
        <h1 className="text-xl font-bold">Title</h1>
      </div>
      <div className="flex items-center space-x-10">
        {/* <Link className={LinkClasses} href="/">
          Link Example
        </Link> */}
        {/* <Link className="items-center btn btn-primary btn-outline" href="/create-test/meta">
          <PlusIcon className={'h-5'}/><span>Create Test</span>
        </Link> */}
      </div>
    </nav>
  )
}

export default NavBar
