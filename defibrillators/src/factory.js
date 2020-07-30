import User from "./User.js"
import Algorithm from "./algorithm.js"
import StringConvert from "./StringConverter.js"
import Defibrilator from "./defibrilator.js"

export default class Factory {
  
  #user
  #formator
  #lines = []
  #defibrilators = []

  constructor(lines, formator) {
    if(! Array.isArray(lines)) {
      throw new Error("A valid line array must be provided")
    }
    this.#lines = lines 

    if(! (formator instanceof StringConvert)) {
      throw new Error("A valid formator must be provided")
    }
    this.#formator = formator

    this.createUser()
    this.createDefibrilators()
  }
  
  createUser() {
    this.#user = new User(this.#lines.slice(0, 2), this.#formator)
  }

  user() {
    return this.#user
  }

  createDefibrilators() {
    this.#lines.slice(3).forEach(line => {
      this.#defibrilators.push(
        new Defibrilator(line.split(';'), this.#formator)
      )
    })
  }

  defibrilators() {
    return this.#defibrilators;
  }

  getClosest() {
    return Algorithm.result(this.#user, this.#defibrilators)
  }
}

