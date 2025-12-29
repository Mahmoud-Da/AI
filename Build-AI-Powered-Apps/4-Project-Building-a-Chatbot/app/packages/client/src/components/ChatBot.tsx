import axios from "axios";
import ReactMarkdown from "react-markdown";
import { useEffect, useRef, useState } from "react";
import { useForm } from "react-hook-form";
import { FaArrowUp } from "react-icons/fa";
import { Button } from "./ui/button";

type FormData = {
  prompt: string;
};

type ChatResponse = {
  message: string;
};

type Message = {
  content: string;
  role: "user" | "bot";
};

const ChatBot = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const lastMessageRef = useRef<HTMLDivElement | null>(null);
  const [isBotTyping, setIsBotTyping] = useState(false);
  const [error, setError] = useState<string>("");
  const conversationId = useRef<string>(crypto.randomUUID());

  const { register, handleSubmit, reset, formState } = useForm<FormData>({
    mode: "onChange",
  });

  useEffect(() => {
    lastMessageRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  const onSubmit = async ({ prompt }: FormData) => {
    try {
      setError("");
      setMessages((prev) => [...prev, { content: prompt, role: "user" }]);
      setIsBotTyping(true);
      reset({ prompt: "" });

      const { data } = await axios.post<ChatResponse>("/api/chat", {
        prompt,
        conversationId: conversationId.current,
      });

      setMessages((prev) => [...prev, { content: data.message, role: "bot" }]);
      setIsBotTyping(false);
    } catch (error) {
      console.error(error);
      setError("Something went wrong, please try again.");
    } finally {
      setIsBotTyping(false);
    }
  };

  const onKeyDown = (e: React.KeyboardEvent<HTMLFormElement>) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      handleSubmit(onSubmit)();
    }
  };

  const onCopyMessage = (e: React.ClipboardEvent<HTMLParagraphElement>) => {
    const selection = window.getSelection()?.toString().trim();
    if (selection) {
      e.preventDefault();
      e.clipboardData.setData("text/plain", selection);
    }
  };

  return (
    <div className="flex flex-col h-full">
      <div className="flex flex-col flex-1 gap-3 mb-10 overflow-y-auto">
        {messages.map((message, index) => (
          <div
            key={index}
            onCopy={onCopyMessage}
            ref={index === messages.length - 1 ? lastMessageRef : null}
            className={`
          px-3 py-1 rounded-xl
          ${
            message.role === "user"
              ? "bg-blue-600 text-white self-end"
              : "bg-gray-100 text-black self-start"
          }
        `}
          >
            <ReactMarkdown>{message.content}</ReactMarkdown>
          </div>
        ))}
        {isBotTyping && (
          <div className="self-start">
            <div className="flex gap-1 px-3 py-3 bg-gray-200 rounded-xl">
              <div className="w-2 h-2 rounded-full bg-gray-800 animate-pulse"></div>
              <div className="w-2 h-2 rounded-full bg-gray-800 animate-pulse [animation-delay:0.2s]"></div>
              <div className="w-2 h-2 rounded-full bg-gray-800 animate-pulse [animation-delay:0.4s]"></div>
            </div>
          </div>
        )}
        {error && <p className="text-red-500">{error}</p>}
      </div>
      <form
        onSubmit={handleSubmit(onSubmit)}
        onKeyDown={onKeyDown}
        className="flex flex-col gap-2 items-end border-2 p-4 rounded-3xl"
      >
        <textarea
          className="w-full border-0 focus:outline-0 resize-none"
          placeholder="Ask anything"
          maxLength={1000}
          autoFocus
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
    </div>
  );
};

export default ChatBot;
