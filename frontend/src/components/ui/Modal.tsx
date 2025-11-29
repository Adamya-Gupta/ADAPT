import { Button } from "@/components/ui/button"
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
  DialogTrigger,
} from "@/components/ui/dialog"
import AddContent from "../AddContent"


export function Modal() {
  return (
    <Dialog>
      <form>
        <DialogTrigger asChild>
          <Button variant="default" className="w-full bg-blue-600 px-2 py-1 text-white uppercase text-lg">Add content</Button>
        </DialogTrigger>
        <DialogContent className="sm:max-w-[425px]">
          <DialogHeader>
            <DialogTitle>Add new content</DialogTitle>
           
          </DialogHeader>
         <AddContent/>

        
        </DialogContent>
      </form>
    </Dialog>
  )
}
