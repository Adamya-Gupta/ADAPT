'use server'
import { revalidatePath } from "next/cache"

// Adding file 

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
            body:JSON.stringify({
                content:new_content,
                doc_type:"text",
                is_edited:false
            })
        })

        if (!response.ok) {
            return { status: "error", message: "Failed to add content" }
        }

        revalidatePath("/contents/")
        return {status:"success",message:"Content added successfully"}

    }
    catch(error){
        return {status:"error",message:"Failed to add content"}

    }
}

// Editing file

export async function edit_file(
    state:{status:string; message:string},
    {id, content, doc_type ,is_edited}: {id:number; content:string; doc_type:string; is_edited:boolean}) {
    

    try{

        const response = await fetch(`http://localhost:8000/contents/${id}`,{
            method:'PUT',
            headers:{
                'Content-Type':'application/json'
            },
            body:JSON.stringify({
                id:id ,
                content:content,
                doc_type:doc_type,
                is_edited:true
            })
        })

        if (!response.ok) {
            return { status: "error", message: `Server error: ${response.statusText}` }
        }

        revalidatePath("/contents/")
        return {status:"success",message:"Content edited successfully"}

    }
    catch(error){
        return {status:"error",message:"Failed to edit content"}
    }
}
