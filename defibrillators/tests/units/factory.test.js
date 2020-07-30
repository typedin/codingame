import User from "../../src/User.js"
import Defibrilator from "../../src/defibrilator.js"
import StringConverter from "../../src/StringConverter.js"
import Factory from "../../src/factory.js"

const lines = [
  "3,879483",
  "43,608177",
  "1",
  "1;Maison de la Prevention Sante;6 rue Maguelone 340000 Montpellier;;3,87952263361082;43,6071285339217",
];

describe('factory instanciation', function() {

  it('cannot be instanciate without lines', () => {
    expect(() => new Factory(null, new StringConverter)).toThrow("A valid line array must be provided")
  })

  it('cannot be instanciate without a formator', () => {
    expect(() => new Factory([], null)).toThrow("A valid formator must be provided")
  })
});

describe('factory objects', function() {
  
  it("creates a user", function(){
    const factory = new Factory(lines, new StringConverter());
    const user = factory.user();
    expect(user instanceof User).toBe(true)
  })

  it("creates an array of defibrilators", function(){
    const factory = new Factory(lines, new StringConverter());
    const defibrilators = factory.defibrilators()

    for (let defibrilator of defibrilators) {
      expect (defibrilator instanceof Defibrilator).toBe(true)
    }
  })
});
