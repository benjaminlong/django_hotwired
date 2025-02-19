import { Controller } from "@hotwired/stimulus"


export  default class extends Controller {
    static targets = ["card"];

    connect() {
        console.log("Connected to CardDeck Controller", this.cardTargets);
    }

    toggle_spread() {
        console.log("Spread card deck")
        this.element.classList.toggle("is-spread")
    }
}
