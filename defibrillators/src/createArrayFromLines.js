const fs = require('fs');
const path = require('path');
const readline = require('readline');

export default async function createArrayFromLines(fixturePath) {
  const pathToFile = path.join(__dirname, fixturePath) 
  const fileStream = fs.createReadStream(pathToFile);
  const rl = readline.createInterface({
    input: fileStream,
    crlfDelay: Infinity
  });

  let lines = [];
  for await (const line of rl) {
    lines.push(line)
  }
  return lines
}

