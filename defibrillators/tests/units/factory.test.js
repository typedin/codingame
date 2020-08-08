import User from "../../src/User.js"
import Defibrilator from "../../src/defibrilator.js"
import StringConverter from "../../src/StringConverter.js"
import Solution from "../../src/solution.js"

const lines = [
  "3,879483",
  "43,608177",
  "1",
  "1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217",
];

describe('solution instanciation', function() {

  it('cannot be instanciate without lines', () => {
    expect(() => new Solution(null, new StringConverter)).toThrow("A valid line array must be provided")
  })

  it('cannot be instanciate without a formator', () => {
    expect(() => new Solution([], null)).toThrow("A valid formator must be provided")
  })
});

describe('solution objects', function() {
  
  it("creates a user", function(){
    const solution = new Solution(lines, new StringConverter());
    const user = solution.user();
    expect(user instanceof User).toBe(true)
  })

  it("creates an array of defibrilators", function(){
    const solution = new Solution(lines, new StringConverter());
    const defibrilators = solution.defibrilators()

    for (let defibrilator of defibrilators) {
      expect (defibrilator instanceof Defibrilator).toBe(true)
    }
  })
});
