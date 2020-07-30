export default class User {

  #lon
  #lat

  constructor(lines, formator) {
    this.#lon = formator.parse(lines[0])
    this.#lat = formator.parse(lines[1])
  }

  lon() {
    return this.#lon
  }

  lat() {
    return this.#lat
  }
}
