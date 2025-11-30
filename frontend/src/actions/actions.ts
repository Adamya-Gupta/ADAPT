'use server'
import { revalidatePath } from "next/cache"

export async function add_file(
    state:{status:string; message:string},
    formData:FormData) {
    const new_content = formData.get('add_content') as string;

    try{

        const response = await fetch('http://localhost:8000/contents/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({content:new_content,doc_type:"text"})
        })

        revalidatePath("/contents/")
        return {status:"success",message:"Content added successfully"}

    }
    catch(error){
        return {status:"error",message:"Failed to add content"}

    }
}