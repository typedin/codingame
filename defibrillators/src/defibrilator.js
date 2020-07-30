import StringConvert from "../src/StringConverter.js"

export default class Defibrilator {

  constructor(entry, formator) {
    if(! Array.isArray(entry)) {
      throw new Error("Valid entry array is expected")
    }
    if(entry.length !== 6) {
      throw new Error(`Wrong length for entry array (expected 6, got ${entry.length})`)
    }
    this._entry = entry

    if(! (formator instanceof StringConvert)) {
      throw new Error("An instant of StringConvert is expected")
    }
    this._formator = formator
  }

  lon() {
    return this._formator.parse(this._entry[4])
  }

  lat() {
    return this._formator.parse(this._entry[5])
  }

  name() {
    return this._entry[1]
  }
}
