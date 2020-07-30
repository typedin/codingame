import StringConvert from "../../src/StringConverter.js"
import Defibrilator from "../../src/defibrilator.js" 

describe('Defibrilator', () => {

  it('cannot be instanciate without entry', () => {
    expect(() => new Defibrilator(null, null)).toThrow("Valid entry array is expected");
  }); 

  it('cannot be instanciate with entry the wrong size', () => {
    const wrongSizeEntry = ['', '']
    expect(() => new Defibrilator(wrongSizeEntry, null)).toThrow(`Wrong length for entry array (expected 6, got 2)`);
  }); 

  it('cannot be instanciate without a formator', () => {
    const validArray = [1,2,3,4,5,6];
    expect(() => new Defibrilator(validArray, null)).toThrow("An instant of StringConvert is expected");
  }); 
});
