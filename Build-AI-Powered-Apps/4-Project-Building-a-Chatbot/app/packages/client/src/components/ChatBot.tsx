import { FaArrowUp } from "react-icons/fa";
import { Button } from "./ui/button";
import { useForm } from "react-hook-form";

type FormData = {
  prompt: string;
};

const ChatBot = () => {
  const { register, handleSubmit, reset, formState } = useForm<FormData>({
    mode: "onChange",
  });

  const onSubmit = (data: FormData) => {
    console.log(data);
    reset();
  };

  const onKeyDown = (e: React.KeyboardEvent<HTMLFormElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(onSubmit)();
    }
  };

  return (
    <form
      onSubmit={handleSubmit(onSubmit)}
      onKeyDown={onKeyDown}
      className="flex flex-col gap-2 items-end border-2 p-4 rounded-3xl"
    >
      <textarea
        className="w-full border-0 focus:outline-0 resize-none"
        placeholder="Ask anything"
        maxLength={1000}
        {...register("prompt", {
          required: true,
          validate: (value) => value.trim().length > 0,
        })}
      />

      <Button
        disabled={!formState.isValid}
        className="rounded-full w-9 h-9 flex items-center justify-center border"
      >
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
    </form>
  );
};

export default ChatBot;
