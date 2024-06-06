import Link from 'next/link'
import Image from 'next/image'
import logo from '@/public/mb_logo.svg'
import { PlusIcon } from '@heroicons/react/24/solid'
import { useCallback, useEffect, useRef, useState } from 'react'
import { BaseServerResponse } from '../types/ServerTypes'
import axios from 'axios'
import { APIRoutes } from '../constants'

const LinkClasses = 'hover:bg-base-200 px-2 py-1 rounded-md hover:link'

const NavBar = () => {
  const [schemaVersion, setSchemaVersion] = useState<string>('')

  useEffect(() => {
    getSchemaVersion()
  }, [])

  const getSchemaVersion = useCallback(async () => {
    try {
      const { data }: { data: BaseServerResponse<{schema_version: string}> } = await axios.get(
        APIRoutes.GET_TEST_SCHEMA_VERSION
      )
      setSchemaVersion(data?.data?.schema_version ?? 'Unknown version')
    } catch {
      console.error('Error fetching tests')
      setSchemaVersion('Unknown version')
    }
  }, [])

  return (
    <nav className="sticky top-0 z-10 flex justify-between p-5 shadow-md bg-base-100">
      <div className="flex items-center">
        <Link href="/">
        <Image src={logo} alt={'DV-Automation Test Creator'}/>
        </Link>
        <div className="divider divider-horizontal" />
        <h1 className="text-xl font-bold">DV - Test Builder &nbsp; {schemaVersion}</h1>
      </div>
      <div className="flex items-center space-x-10">
        <Link className={LinkClasses} href="/">
          All Tests
        </Link>
        <Link className={LinkClasses} href="/standard-params">
          Standard Params
        </Link>
        <Link className="items-center btn btn-primary btn-outline" href="/create-test/meta">
          <PlusIcon className={'h-5'}/><span>Create Test</span>
        </Link>
      </div>
    </nav>
  )
}

export default NavBar
