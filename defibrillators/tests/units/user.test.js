import User from "../../src/User.js"
import ToDecimal from "../../src/StringConverter.js"
import createArrayFromLines from "../../src/createArrayFromLines.js"

describe('user', function() {

  const fixturePath = "../tests/fixtures/case1.txt"
  const lines = [
    "3,879483",
    "43,608177"
  ];

  it("has a latitude and a longitude", () => {
    const user = new User(lines, new ToDecimal());
    expect(user.lon()).toBe(3.879483)
    expect(user.lat()).toBe(43.608177)
  })
})

