import Image from "next/image";
import { Button } from "@/components/ui/button"
import { Modal } from "@/components/ui/Modal";
import Filestable from "@/components/Filestable";

export default function Home() {
  return (
    <div className="">
      <main className="bg-blue-100 mt-8 mx-auto max-w-5xl">
        {/* Modal Section */}
        <section> 
          <Modal/>
        </section>
        {/* Content Section */}
        <section>
          <Filestable/>
        </section>
        
      </main>
    </div>
  );
}
