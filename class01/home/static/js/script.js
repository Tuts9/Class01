// Animações para a página inicial
const textHome = document.querySelector('#text-home');
const imgHome = document.querySelector('#img-home');

function startAnimationHome(elem) {
  gsap.fromTo(elem,
    {
      opacity: 0,
      x: -250,
      ease: "power1.out",
    },
    {
      opacity: 1,
      x: 0,
      duration: 2,
    }
  );
}
startAnimationHome(textHome);
startAnimationHome(imgHome);

const sectionTwo = document.querySelector('#section2');
const titleTopic = document.querySelector('#title-topic');
const textTopic = document.querySelector('#text-topic');

function startAnimationText(elem) {
  gsap.to(elem, {
    opacity: 1,
    duration: 2,
    ease: "power1.out",
    scrollTrigger: {
      trigger: sectionTwo,
      start: "top 450px",
      end: "center 450px",
      scrub: true,
    },
  });
}
startAnimationText(titleTopic);
startAnimationText(textTopic);

const cards = document.querySelectorAll('.card')

ScrollTrigger.batch(cards, {
    onEnter: batch => gsap.to(batch,{
        autoAlpha: 1,
        stagger: 0.1
    }),
});

// Animações na página de tópicos

const titleTool = document.querySelector('#title-tool');
const imgTopic = document.querySelector('#img-topic');


function startAnimationTextTopic(elem) {
  gsap.fromTo(elem, {
    opacity: 0,
    y: -150,
    ease: "power1.out"
  }, {
    opacity: 1,
    y: 0,
    duration: 2,
    onComplete: () => {
      // document.querySelector('#title-tool').classList.add('text-blue-700');
      pass
    }
  });
}
startAnimationTextTopic(titleTool);

function startAnimationImg(elem) {
  gsap.fromTo(elem, {
    x: -500,
    opacity: 0,
    ease: 'power1.out'
  }, {
    x: 0,
    opacity: 1,
    duration: 1.7
  })
}

startAnimationImg(imgTopic);

//TODO: Terminar de configurar esta animação
const titleTools = document.querySelector('#title-tools');
const sectionTools = document.querySelector('#text-tools');

function startAnimationTitleTools(elem) {
  gsap.fromTo(elem, {
    opacity: 0,
    y: -150,
    ease: "power1.out"
  }, {
    opacity: 1,
    y: 0,
    duration: 2,
    scrollTrigger: {
      trigger: sectionTools,
      start: 'top bottom',
      end: 'center 70%',
      scrub: true
    }
  });
}

// startAnimationTitleTools(titleTools);


const cardTools = document.querySelectorAll('#card-tool');

cardTools.forEach(cardTool => {
  gsap.fromTo(cardTool, {
    x: -600,
    opacity: 0,
    ease: 'power1.out'
  }, {
    x: 0,
    opacity: 1,
    duration: 2,
    scrollTrigger: {
      trigger: cardTool, // <-- Use o elemento individual aqui
      start: 'top 80%',
      end: 'bottom 90%',
      scrub: true
    }
  });
});
