import {Controller} from "@hotwired/stimulus";


function initTutorial(tutorialSwitch) {
  const tutorialDisplayed =
    localStorage.getItem("tutorialSwitch") !== null &&
    localStorage.getItem("tutorialSwitch");
  tutorialSwitch.checked = tutorialDisplayed;
  tutorialDisplayed
    ? document.body.setAttribute("data-tutorial", true)
    : document.body.removeAttribute("data-tutorial");
}

function resetTutorial(tutorialSwitch) {
  if (tutorialSwitch.checked) {
    document.body.setAttribute("data-tutorial", true);
    localStorage.setItem("tutorialSwitch", true);
  } else {
    document.body.removeAttribute("data-tutorial");
    localStorage.removeItem("tutorialSwitch");
  }
}

export default class extends Controller {
  static targets = [];

  connect() {
    const tutorialSwitch = document.getElementById("tutorialSwitch");
    console.log("Connected to Tutorial Mode Controller...", tutorialSwitch);
    if (tutorialSwitch) {
      initTutorial(tutorialSwitch);
      tutorialSwitch.addEventListener("change", () => {
        resetTutorial(tutorialSwitch);
      });
    }
  }
}
