import User from "../../src/User.js"
import Algorithm from "../../src/algorithm.js"
import StringConverter from "../../src/StringConverter.js"

jest.mock("../../src/StringConverter.js")
jest.mock("../../src/User.js")

describe("algorithm instanciation", function(){
  beforeEach(() => {
    User.mockClear()
    StringConverter.mockClear()
  });
  it("must be provided a user", () => {
    expect(
      () => new Algorithm(null, [])
    ).toThrow("A valid user is required")
  })

  it("must be provided an array of defibrilators with a length", () => {
    expect(
      () => new Algorithm(new User, [])
    ).toThrow("An array of defibrilators is required")
  })

  it("must be provided an array of defibrilators", () => {
    expect(
      () => new Algorithm(new User, [{},{}])
    ).toThrow("An array of defibrilators is required")
  })
})

