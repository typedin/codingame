import ToDecimal from "../../src/StringConverter.js"
import { StringConverter } from "../../src/StringConverter.js"

describe('ToDecimal', function() {

  it("must implement the parse method", () => {
    class Invalid extends StringConverter {};

    expect(
      () => new Invalid().parse()
    ).toThrow("This function must be implemented")

  })

  it("must be provided with a string when parsing", () =>{
    expect(
      () => new ToDecimal().parse(null)
    ).toThrow("A string must be provided")
  })

  it("converts strings with comas to decimal", () => {
    expect(new ToDecimal().parse("3,879483")).toBe(3.879483)
  })
})

