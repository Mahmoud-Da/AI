import { FaArrowUp } from "react-icons/fa";
import { Button } from "./ui/button";
const ChatBot = () => {
  return (
    <div className="flex flex-col gap-2 items-end border-2 p-4 rounded-3xl">
      <textarea
        className="w-full border-0 focus:outline-0 resize-none"
        placeholder="Ask anything"
        maxLength={1000}
      />
      <Button className="rounded-full w-9 h-9 flex items-center justify-center border">
        <FaArrowUp />
        {/* another style */}
        {/* <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 448 512"
          className="w-4 h-4"
          fill="currentColor"
        >
          <path d="M438.6 233.4c12.5 12.5 12.5 32.8 0 45.3l-160 160c-12.5 12.5-32.8 12.5-45.3 0s-12.5-32.8 0-45.3L338.7 288H32c-17.7 0-32-14.3-32-32s14.3-32 32-32H338.7L233.4 118.6c-12.5-12.5-12.5-32.8 0-45.3s32.8-12.5 45.3 0l160 160z" />
        </svg> */}
      </Button>
    </div>
  );
};

export default ChatBot;
