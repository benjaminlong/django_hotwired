import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
  static targets = [ "source" ];

  test() {
    console.log('test');
    event.preventDefault();
  }

  copy(event) {
    event.preventDefault();
    this.sourceTarget.select();
    document.execCommand("copy");
    //console.log('HelloCopy');
    //document.getElementsByClassName('modal');
  }
}
