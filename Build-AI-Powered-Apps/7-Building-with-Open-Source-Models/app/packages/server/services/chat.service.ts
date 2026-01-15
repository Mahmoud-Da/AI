import fs from "fs";
import path from "path";
import { llmClient } from "../llm/client";
import template from "../llm/prompts/chatbot.txt";
import { conversationRepository } from "../repositories/conversation.repository";

const parkInfoPath = path.join(
  __dirname,
  "..",
  "llm",
  "prompts",
  "wonderworld.md"
);
const parkInfo = fs.readFileSync(parkInfoPath, "utf8");
const instructions = template.replace("{{parkInfo}}", parkInfo);
interface ChatResponse {
  id: string;
  message: string;
}

export const chatService = {
  async sendMessage(
    prompt: string,
    conversationId: string
  ): Promise<ChatResponse> {
    const response = await llmClient.generateText({
      model: "gpt-5-mini",
      prompt,
      instructions,
      maxTokens: 1000,
      previousResponseId:
        conversationRepository.getLastResponseId(conversationId),
    });
    console.log(response);

    conversationRepository.setLastResponseId(conversationId, response.id);
    return {
      id: response.id,
      message: response.text,
    };
  },
};
