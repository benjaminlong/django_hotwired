import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
    static targets = [ "name" ];

    jsAction() {
        console.log("Hello, Stimulus!", this.element);
        const element = this.nameTarget;
        const name = element.value;
        console.log(`Hello, ${name}!`);
    }
}
