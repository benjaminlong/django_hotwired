import { Controller } from "@hotwired/stimulus"

export default class extends Controller {

    initialize() {
        this.duration = 750;
        this.easing = 'swing';
        this.offset = 0;
    }

    getElement(target) {
        const jQueryElement = Ember.$(target);
        if (!jQueryElement) {
            Ember.Logger.warn("element couldn't be found:", target);
            return;
        }

        return jQueryElement;
    }

    getVerticalCoord(target, offset = 0) {
        const  jQueryElement = this.getJQueryElement(target);
        return jQueryElement.offset().top + offset;
    }

    scrollTo(event, opts = {}) {
        // blong: I don't know why we had this scrollable.scrollTop... Might be bad
        // to remove it.
        // let scrollableTop = this.get('scrollable').scrollTop();
        let currentTarget = event.currentTarget;
        let body = document.querySelector('body');
        let {
            scrollToSelector,
            scrollToId,
            scrollToClassNames,
            scrollToName} = currentTarget.dataset;

        //let scrollableTop = 0;
        let destinationElement = null;
        if (scrollToSelector){
            destinationElement = document.querySelector(scrollToSelector);
        }
        if (scrollToId) {
            destinationElement = document.getElementById(scrollToId)
        } else if (scrollToClassNames) {
            destinationElement = document.getElementsByClassName(scrollToClassNames)
        } else if (scrollToName) {
            destinationElement = document.getElementsByName(scrollToName)
        }

        if (!destinationElement) {
            console.log("Can't find destination element with", currentTarget.dataset);
            return;
        }

        window.scrollTo(0, destinationElement.offsetTop);
        //let scrollableTop = 0;
        //let scrollTop = scrollableTop - body.offsetTop + destinationElement.offsetTop;
        //body.animate({scrollTop: scrollTop});
        //body.animate(
        //    {scrollTop: scrollableTop},
        //    ts.duration || this.get('duration'),
        //    opts.easing   || this.get('easing'),
        //    opts.complete
        //);

  }

}
