import User from "./User.js"
import Defibrilator from "./defibrilator.js"

export default class Algorithm {
  #user
  #defibrilators

  constructor(user, defibrilators) {
    if (! (user instanceof User)) {
      throw new Error("A valid user is required")
    }
    this.#user = user;

    if(! defibrilators.length) {
      throw new Error("An array of defibrilators is required")
    }
    defibrilators.forEach(function(defibrilator){
      if(! (defibrilator instanceof Defibrilator)) {
        throw new Error("An array of defibrilators is required")
      }
    })
    this.#defibrilators = defibrilators
  }

  static result(user, defibrilators) {
    return new Algorithm(user, defibrilators).getClosest()
  }

  getClosest() {
    const distances = [];
    let x, y, d;
    for(let i = 0 ; i < this.#defibrilators.length ; i++) {
      x = (this.#user.lon() - this.#defibrilators[i].lon()) * Math.cos((this.#defibrilators[i].lat() + this.#user.lat()) / 2)
      y = (this.#defibrilators[i].lat() - this.#user.lat())
      d = Math.sqrt((x*x) + (y*y))*6371

      distances.push({ 
        distance: d,
        defibrilator: this.#defibrilators[i]
      });
    }

    distances.sort(function(a, b) {
      return a.distance - b.distance
    }) 

    return distances[0].defibrilator.name();
  }
}
