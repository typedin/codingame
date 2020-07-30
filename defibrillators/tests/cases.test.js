import createArrayFromLines from "../src/createArrayFromLines.js"
import StringConverter from "../src/StringConverter.js"
import Factory from "../src/factory.js"

describe("test cases", () => {
  let factory

  async function setUp(fixturePath) {
    factory = new Factory(await createArrayFromLines(fixturePath), new StringConverter);
  }

  it("returns Maison de la Prevention Sante for test 1", async () => {
    await setUp("../tests/fixtures/case1.txt")

    const result = factory.getClosest();

    expect(result).toBe("Maison de la Prevention Sante")
  })

  it("returns Cimetiere Saint-Etienne for test 2", async () => {
    await setUp("../tests/fixtures/case2.txt")

    const result = factory.getClosest();

    expect(result).toBe("Cimetiere Saint-Etienne")
  })

  it("returns CAF for test 3", async () => {
    await setUp("../tests/fixtures/case3.txt")

    const result = factory.getClosest();

    expect(result).toBe("Caisse Primaire d'Assurance Maladie")
  })

  it("returns Amphitheatre d'O for test 4", async () => {
    await setUp("../tests/fixtures/case4.txt")

    const result = factory.getClosest();

    expect(result).toBe("Amphitheatre d'O")
  })
})
