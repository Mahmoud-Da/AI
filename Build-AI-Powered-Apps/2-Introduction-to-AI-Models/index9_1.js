import OpenAI from "openai";

// Create OpenAI client
const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

// Normal request function
async function normalRequest() {
  const response = await client.responses.create({
    model: "gpt-4.1",
    input: "Write a short story about a robot.",
    temperature: 0.7,
    max_output_tokens: 100,
  });

  console.log("\n--- Normal Response ---\n");
  console.log(response.output_text);
}

// Streaming request function
async function streamingRequest() {
  const stream = await client.responses.create({
    model: "gpt-4.1",
    input: "Write a short story about a robot, streaming output.",
    temperature: 0.7,
    max_output_tokens: 200,
    stream: true,
  });

  console.log("\n--- Streaming Response ---\n");
  for await (const event of stream) {
    if (event.delta) {
      // Print token by token
      process.stdout.write(event.delta);
    }
  }
  console.log("\n"); // Add a newline at the end
}

// Run both examples
(async () => {
  await normalRequest();
  await streamingRequest();
})();
