import { Controller } from "@hotwired/stimulus"

export default class extends Controller {
    static targets = [ "name" ];

    toggleModalFullscreenMenu() {
      let modal = document.getElementsByClassName('modal-fullscreen-menu')[0];
      if (modal.className.indexOf('is-active') === -1) {
          modal.classList.add('is-active');
      } else {
          modal.classList.remove('is-active');
      }
    }
}
