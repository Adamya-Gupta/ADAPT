import Image from "next/image";
import { Button } from "@/components/ui/button"
import { Modal } from "@/components/ui/Modal";

export default function Home() {
  return (
    <div className="">
      <main className="bg-blue-100">
        {/* Modal Section */}
        <section>
          <Modal/>
        </section>
        {/* Content Section */}
        <section>

        </section>
        hello world 
          <Button>Click me</Button>
      </main>
    </div>
  );
}
