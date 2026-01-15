import OpenAI from "openai";
import { InferenceClient } from "@huggingface/inference";
import summarizePrompt from "../llm/prompts/summarize-reviews.txt";

const inferenceClient = new InferenceClient(process.env.HF_TOKEN);

const openAIClient = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

export type GenerateTextOptions = {
  model?: string;
  prompt: string;
  instructions?: string;
  // NOTE GPT5-mini doesn`t have this attribute
  // temperature?: number;
  maxTokens?: number;
  previousResponseId?: string;
};

export type GenerateTextResult = {
  id: string;
  text: string;
};

export const llmClient = {
  async generateText(
    options: GenerateTextOptions
  ): Promise<GenerateTextResult> {
    const {
      model = "gpt-4.1",
      prompt,
      instructions,
      // temperature = 0.2,
      maxTokens = 300,
      previousResponseId,
    } = options;

    const response = await openAIClient.responses.create({
      model,
      input: prompt,
      instructions,
      // temperature,
      max_output_tokens: maxTokens,
      previous_response_id: previousResponseId,
    });

    return {
      id: response.id,
      text: response.output_text,
    };
  },

  // Using bart
  async summarize(text: string): Promise<string> {
    const output = await inferenceClient.summarization({
      model: "facebook/bart-large-cnn",
      inputs: text,
      provider: "hf-inference",
    });

    return output.summary_text;
  },

  // Using Llama-3
  async summarizeReviews(reviews: string) {
    const chatCompletion = await inferenceClient.chatCompletion({
      model: "meta-llama/Llama-3.1-8B-Instruct:novita",
      messages: [
        {
          role: "system",
          content: summarizePrompt,
        },
        {
          role: "user",
          content: reviews,
        },
      ],
    });
    return chatCompletion.choices[0]?.message.content || "";
  },
};
