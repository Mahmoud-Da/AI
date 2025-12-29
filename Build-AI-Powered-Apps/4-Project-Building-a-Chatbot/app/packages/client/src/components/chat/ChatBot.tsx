import axios from "axios";
import { useState } from "react";
import { useForm } from "react-hook-form";
import { FaArrowUp } from "react-icons/fa";
import type { Message } from "./ChatMessages";
import ChatMessages from "./ChatMessages";
import TypingIndicator from "./TypingIndicator";
import { Button } from "../ui/button";

type FormData = {
  prompt: string;
};

type ChatResponse = {
  message: string;
};

const ChatBot = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [isBotTyping, setIsBotTyping] = useState(false);
  const [error, setError] = useState("");
  const conversationId = crypto.randomUUID();

  const { register, handleSubmit, reset, formState } = useForm<FormData>({
    mode: "onChange",
  });

  const onSubmit = async ({ prompt }: FormData) => {
    try {
      setError("");
      setMessages((prev) => [...prev, { content: prompt, role: "user" }]);
      setIsBotTyping(true);
      reset({ prompt: "" });

      const { data } = await axios.post<ChatResponse>("/api/chat", {
        prompt,
        conversationId,
      });

      setMessages((prev) => [...prev, { content: data.message, role: "bot" }]);
    } catch {
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

  return (
    <div className="flex flex-col h-full">
      <div className="flex flex-col flex-1 gap-3 mb-10 overflow-y-auto">
        <ChatMessages messages={messages} />
        {isBotTyping && <TypingIndicator />}
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
        </Button>
      </form>
    </div>
  );
};

export default ChatBot;
