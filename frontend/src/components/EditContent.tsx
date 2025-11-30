import React from 'react'

export default function AddContent(){
  return (
    <form className='flex flex-col justify-between items-center gap-x-4 w-full'>
        <input type='text' 
        placeholder='Edit content' 
        className='w-full'/>
        
        <button className='px-2 py-1 bg-blue-600 text-white rounded-md w-full mt-4'> Save </button>
    </form>
  )
}

