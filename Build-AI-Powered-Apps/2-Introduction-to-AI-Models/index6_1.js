import { get_encoding } from "tiktoken";

// Initialize the tokenizer
const encoding = get_encoding("cl100k_base");

// Your text
const text = "hello world, this is the first test of tiktoken library.";

// Encode the text into token IDs
const tokenIds = encoding.encode(text);

// To track positions in original text
let currentIndex = 0;

console.log("Token breakdown:");

// Decode each token individually into string
tokenIds.forEach((id, idx) => {
  const tokenBytes = encoding.decode([id]); // returns Uint8Array
  const tokenText = new TextDecoder().decode(tokenBytes); // convert to string

  // Find start and end in original text
  const start = text.indexOf(tokenText, currentIndex);
  const end = start + tokenText.length;
  currentIndex = end;

  console.log(
    `Token ${
      idx + 1
    }: ID=${id}, Text="${tokenText}", Start=${start}, End=${end}`
  );
});

// Decode full text back to string
const fullTextBytes = encoding.decode(tokenIds);
const decodedText = new TextDecoder().decode(fullTextBytes);

console.log("\nDecoded full text:", decodedText);
