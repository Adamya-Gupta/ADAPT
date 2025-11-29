import { SquareCheckBig, SquarePen, Trash2 } from "lucide-react";
import { SingleFile } from "../../types";

export default function Singledoc({filecontent}:{filecontent:SingleFile}) {
  return (
    <>
    <tr className="flex justify-between items-center border-b border-gray-500 px-2 py-2">
        <td>
            {filecontent.content}
        </td>
        <td className="flex gap-x-2">
            <SquareCheckBig />
            <SquarePen className="text-blue-500"/>
            <Trash2 className="text-red-500" />
        </td>
    </tr>
    </>
  )
}
