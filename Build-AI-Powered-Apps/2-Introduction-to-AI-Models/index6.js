// ES module syntax
import { get_encoding } from "tiktoken";

// common JS syntax
// const { get_encoding } = require("tiktoken");

const encoding = get_encoding("cl100k_base");

const tokens = encoding.encode(
  "hello world, this is the first test of tiktoken library."
);

console.log(tokens);
