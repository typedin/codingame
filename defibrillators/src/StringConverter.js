export class StringConverter {
  parse() {
    throw Error("This function must be implemented")
  }
}

export default class ToDecimal extends StringConverter
{
  parse(aString) {
    if (typeof aString !== "string") {
      throw new Error("A string must be provided")
    }
    return parseFloat(aString.replace(',', '.'))
  }
}

