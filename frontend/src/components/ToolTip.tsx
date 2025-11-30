import { Button } from "@/components/ui/button"
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "@/components/ui/tooltip"

export default function ToolTip({tool_tip_content,children}:{tool_tip_content:string,children:React.ReactNode}) {
  return (
    <Tooltip>
      <TooltipTrigger asChild>
        {children}
      </TooltipTrigger>
      <TooltipContent>
        <p>{tool_tip_content}</p>
      </TooltipContent>
    </Tooltip>
  )
}
